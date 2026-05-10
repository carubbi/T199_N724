#!/usr/bin/env python3
"""Gera XML Moodle/AVA a partir das provas Markdown da AV2."""

from __future__ import annotations

import argparse
import html
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


LETTERS = ("A", "B", "C", "D", "E")


@dataclass
class Alternative:
    letter: str
    text: str
    feedback: str
    correct: bool


@dataclass
class Question:
    number: int
    stem: str
    general_feedback: str
    alternatives: list[Alternative]


@dataclass
class Problem:
    number: int
    title: str
    description_md: str
    questions: list[Question]


def normalize_latex(md: str) -> str:
    md = re.sub(r"\$\$(.*?)\$\$", lambda m: "\\[\n" + m.group(1).strip() + "\n\\]", md, flags=re.S)
    md = re.sub(r"(?<!\\)\$(.+?)(?<!\\)\$", lambda m: r"\(" + m.group(1).strip() + r"\)", md)
    return md


def inline_html(text: str) -> str:
    text = normalize_latex(text)
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*__([^_]+)__\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"__\*\*([^*]+)\*\*__", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", text)
    return text


def table_to_html(lines: list[str]) -> str:
    rows = []
    align_index = None
    for index, line in enumerate(lines):
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            align_index = index
            continue
        rows.append((index, cells))

    if not rows:
        return ""

    header = rows[0][1] if align_index == 1 else None
    body_rows = rows[1:] if header else rows
    out = ['<table border="1" cellspacing="0" cellpadding="6">']
    if header:
        out.append("<thead><tr>")
        out.extend(f"<th>{inline_html(cell)}</th>" for cell in header)
        out.append("</tr></thead>")
    out.append("<tbody>")
    for _, cells in body_rows:
        out.append("<tr>")
        out.extend(f"<td>{inline_html(cell)}</td>" for cell in cells)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def markdown_to_html(md: str) -> str:
    lines = md.strip().splitlines()
    out: list[str] = []
    paragraph: list[str] = []
    bullet_items: list[str] = []
    table_lines: list[str] = []
    display_math: list[str] | None = None

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            out.append(f"<p>{inline_html(' '.join(paragraph).strip())}</p>")
            paragraph = []

    def flush_bullets() -> None:
        nonlocal bullet_items
        if bullet_items:
            out.append("<ul>")
            out.extend(f"<li>{inline_html(item)}</li>" for item in bullet_items)
            out.append("</ul>")
            bullet_items = []

    def flush_table() -> None:
        nonlocal table_lines
        if table_lines:
            out.append(table_to_html(table_lines))
            table_lines = []

    for raw_line in lines:
        line = raw_line.rstrip()

        if display_math is not None:
            if line.strip() == "$$":
                math_body = "\n".join(display_math).strip()
                out.append(f"<p>\\[\n{html.escape(math_body, quote=False)}\n\\]</p>")
                display_math = None
            else:
                display_math.append(line)
            continue

        if line.strip() == "$$":
            flush_paragraph()
            flush_bullets()
            flush_table()
            display_math = []
            continue

        if not line.strip():
            flush_paragraph()
            flush_bullets()
            flush_table()
            continue

        if line.startswith("|"):
            flush_paragraph()
            flush_bullets()
            table_lines.append(line)
            continue

        if table_lines:
            flush_table()

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            flush_bullets()
            level = min(len(heading.group(1)) + 1, 6)
            out.append(f"<h{level}>{inline_html(heading.group(2))}</h{level}>")
            continue

        bullet = re.match(r"^-\s+(.+)$", line)
        if bullet:
            flush_paragraph()
            bullet_items.append(bullet.group(1))
            continue

        if bullet_items:
            flush_bullets()

        paragraph.append(line.strip())

    if display_math is not None:
        raise ValueError("Bloco LaTeX aberto sem fechamento com $$")
    flush_paragraph()
    flush_bullets()
    flush_table()
    return "".join(out)


def split_sections(md: str) -> tuple[str, list[Problem], dict[int, str]]:
    before_gabarito, _, gabarito_md = md.partition("## Gabarito")
    formulas_match = re.search(r"^## Fórmulas\s*$", before_gabarito, flags=re.M)
    problem1_match = re.search(r"^## Problema 1\b.*$", before_gabarito, flags=re.M)
    if not formulas_match or not problem1_match:
        raise ValueError("Não foi possível localizar '## Fórmulas' e '## Problema 1'")

    formulas_md = before_gabarito[formulas_match.start() : problem1_match.start()].strip()
    problems_md = before_gabarito[problem1_match.start() :].strip()

    problem_matches = list(re.finditer(r"^## Problema\s+(\d+)\s*-\s*(.+)$", problems_md, flags=re.M))
    if len(problem_matches) != 3:
        raise ValueError(f"Esperados 3 problemas, encontrados {len(problem_matches)}")

    gabarito = parse_gabarito(gabarito_md)
    problems: list[Problem] = []
    for idx, match in enumerate(problem_matches):
        start = match.start()
        end = problem_matches[idx + 1].start() if idx + 1 < len(problem_matches) else len(problems_md)
        block = problems_md[start:end].strip()
        number = int(match.group(1))
        title = f"Problema {number} - {match.group(2).strip()}"
        question_match = re.search(r"^### Questão\s+\d+\s+\(0,5 ponto\)\s*$", block, flags=re.M)
        if not question_match:
            raise ValueError(f"Problema {number} sem questões")
        description_md = block[: question_match.start()].strip()
        questions_md = block[question_match.start() :].strip()
        questions = parse_questions(questions_md, gabarito)
        problems.append(Problem(number, title, description_md, questions))

    return formulas_md, problems, gabarito


def parse_gabarito(md: str) -> dict[int, str]:
    gabarito: dict[int, str] = {}
    for line in md.splitlines():
        match = re.match(r"^\|\s*(\d+)\s*\|\s*([A-E])\s*\|", line.strip())
        if match:
            gabarito[int(match.group(1))] = match.group(2)
    if len(gabarito) != 14:
        raise ValueError(f"Gabarito deve conter 14 entradas; contém {len(gabarito)}")
    return gabarito


def parse_questions(md: str, gabarito: dict[int, str]) -> list[Question]:
    matches = list(re.finditer(r"^### Questão\s+(\d+)\s+\(0,5 ponto\)\s*$", md, flags=re.M))
    questions: list[Question] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md)
        number = int(match.group(1))
        block = md[start:end].strip()
        questions.append(parse_question(number, block, gabarito[number]))
    return questions


def parse_question(number: int, block: str, correct_letter: str) -> Question:
    before_feedback, sep, feedback_block = block.partition("**Feedback Geral**")
    if not sep:
        raise ValueError(f"Questão {number} sem Feedback Geral")
    general_feedback_md, sep, specific_block = feedback_block.partition("**Feedback Específico**")
    if not sep:
        raise ValueError(f"Questão {number} sem Feedback Específico")

    alt_matches = list(re.finditer(r"^([A-E])\.\s+(.+)$", before_feedback, flags=re.M))
    if len(alt_matches) != 5:
        raise ValueError(f"Questão {number} deve ter 5 alternativas; tem {len(alt_matches)}")

    stem = before_feedback[: alt_matches[0].start()].strip()
    alt_texts: dict[str, str] = {}
    for idx, match in enumerate(alt_matches):
        end = alt_matches[idx + 1].start() if idx + 1 < len(alt_matches) else len(before_feedback)
        text = match.group(2) + before_feedback[match.end() : end]
        alt_texts[match.group(1)] = text.strip()

    feedbacks = parse_specific_feedback(number, specific_block)
    alternatives = [
        Alternative(
            letter=letter,
            text=alt_texts[letter],
            feedback=feedbacks[letter],
            correct=(letter == correct_letter),
        )
        for letter in LETTERS
    ]
    return Question(number, stem, general_feedback_md.strip(), alternatives)


def parse_specific_feedback(number: int, block: str) -> dict[str, str]:
    matches = list(re.finditer(r"^-\s+([A-E])\.\s+(.+)$", block.strip(), flags=re.M))
    if len(matches) != 5:
        raise ValueError(f"Questão {number} deve ter feedback específico A-E; tem {len(matches)}")
    feedbacks: dict[str, str] = {}
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(block.strip())
        text = match.group(2) + block.strip()[match.end() : end]
        feedbacks[match.group(1)] = text.strip()
    return feedbacks


def add_text(parent: ET.Element, tag: str, text: str | None = None, **attrs: str) -> ET.Element:
    child = ET.SubElement(parent, tag, attrs)
    if text is not None:
        child.text = text
    return child


def add_text_container(parent: ET.Element, tag: str, text: str, **attrs: str) -> ET.Element:
    container = add_text(parent, tag, **attrs)
    add_text(container, "text", text)
    return container


def add_common_question_tags(question_el: ET.Element, grade: str, penalty: str) -> None:
    add_text(question_el, "defaultgrade", grade)
    add_text(question_el, "penalty", penalty)
    add_text(question_el, "hidden", "0")
    ET.SubElement(question_el, "idnumber")


def add_description(root: ET.Element, name: str, html_text: str) -> None:
    q = ET.SubElement(root, "question", {"type": "description"})
    add_text_container(q, "name", name)
    add_text_container(q, "questiontext", html_text, format="html")
    add_text_container(q, "generalfeedback", "", format="html")
    add_common_question_tags(q, "0.0000000", "0.0000000")


def add_multichoice(root: ET.Element, prefix: str, question: Question) -> None:
    q = ET.SubElement(root, "question", {"type": "multichoice"})
    number = f"{question.number:02d}"
    add_text_container(q, "name", f"{prefix} Q{number}")
    question_html = f"<h3>Questão {question.number}</h3>{markdown_to_html(question.stem)}"
    add_text_container(q, "questiontext", question_html, format="html")
    feedback_html = f"<h3>Feedback Geral</h3>{markdown_to_html(question.general_feedback)}"
    add_text_container(q, "generalfeedback", feedback_html, format="html")
    add_common_question_tags(q, "0.5000000", "0.3333333")
    add_text(q, "single", "true")
    add_text(q, "shuffleanswers", "true")
    add_text(q, "answernumbering", "abc")
    add_text(q, "showstandardinstruction", "0")
    add_text_container(q, "correctfeedback", "Resposta correta.", format="html")
    add_text_container(q, "partiallycorrectfeedback", "", format="html")
    add_text_container(q, "incorrectfeedback", "Resposta incorreta.", format="html")

    for alt in question.alternatives:
        answer = ET.SubElement(q, "answer", {"fraction": "100" if alt.correct else "0", "format": "html"})
        add_text(answer, "text", markdown_to_html(alt.text))
        add_text_container(answer, "feedback", markdown_to_html(alt.feedback), format="html")


def validate_model(problems: list[Problem], gabarito: dict[int, str]) -> None:
    all_questions = [question for problem in problems for question in problem.questions]
    if len(all_questions) != 14:
        raise ValueError(f"Esperadas 14 questões; encontradas {len(all_questions)}")
    if sorted(q.number for q in all_questions) != list(range(1, 15)):
        raise ValueError("Numeração das questões não vai de 1 a 14")
    for question in all_questions:
        if len(question.alternatives) != 5:
            raise ValueError(f"Questão {question.number} não tem 5 alternativas")
        if sum(1 for alt in question.alternatives if alt.correct) != 1:
            raise ValueError(f"Questão {question.number} não tem exatamente uma correta")
        if not question.general_feedback:
            raise ValueError(f"Questão {question.number} sem feedback geral")
        for alt in question.alternatives:
            if not alt.feedback:
                raise ValueError(f"Questão {question.number}, alternativa {alt.letter}, sem feedback")
    if set(gabarito) != set(range(1, 15)):
        raise ValueError("Gabarito não contém exatamente as questões 1 a 14")


def validate_xml(xml_path: Path) -> None:
    tree = ET.parse(xml_path)
    root = tree.getroot()
    descriptions = root.findall("./question[@type='description']")
    multichoice = root.findall("./question[@type='multichoice']")
    if len(descriptions) != 4:
        raise ValueError(f"XML deve ter 4 descriptions; tem {len(descriptions)}")
    if len(multichoice) != 14:
        raise ValueError(f"XML deve ter 14 multichoice; tem {len(multichoice)}")
    for q in multichoice:
        answers = q.findall("answer")
        if len(answers) != 5:
            raise ValueError(f"{q.findtext('name/text')} não tem 5 alternativas")
        if sum(1 for answer in answers if answer.attrib.get("fraction") == "100") != 1:
            raise ValueError(f"{q.findtext('name/text')} não tem exatamente uma fração 100")
        for answer in answers:
            text = answer.findtext("text") or ""
            if re.match(r"^\s*<p>[A-E]\.", text):
                raise ValueError(f"{q.findtext('name/text')} contém prefixo fixo de alternativa")
        if q.findtext("defaultgrade") != "0.5000000":
            raise ValueError(f"{q.findtext('name/text')} com pontuação incorreta")
        if q.findtext("shuffleanswers") != "true":
            raise ValueError(f"{q.findtext('name/text')} sem embaralhamento de alternativas")


def build_xml(input_path: Path, output_path: Path, prefix: str, category: str) -> None:
    md = input_path.read_text(encoding="utf-8")
    formulas_md, problems, gabarito = split_sections(md)
    validate_model(problems, gabarito)

    root = ET.Element("quiz")
    category_question = ET.SubElement(root, "question", {"type": "category"})
    category_el = ET.SubElement(category_question, "category")
    add_text(category_el, "text", category)

    formulas_html = "<h2>Fórmulas da AV2</h2>" + markdown_to_html(
        re.sub(r"^## Fórmulas\s*", "", formulas_md).strip()
    )
    add_description(root, "00 - Fórmulas", formulas_html)

    expected_counts = {1: 5, 2: 4, 3: 5}
    for problem in problems:
        if len(problem.questions) != expected_counts[problem.number]:
            raise ValueError(
                f"Problema {problem.number} deveria ter {expected_counts[problem.number]} questões; "
                f"tem {len(problem.questions)}"
            )
        add_description(root, f"0{problem.number} - Problema {problem.number}", markdown_to_html(problem.description_md))
        for question in problem.questions:
            add_multichoice(root, prefix, question)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    validate_xml(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera XML Moodle/AVA da AV2.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--category", default="$course$/AV2")
    args = parser.parse_args()

    try:
        build_xml(args.input, args.output, args.prefix, args.category)
    except Exception as exc:  # noqa: BLE001
        print(f"Erro: {exc}", file=sys.stderr)
        return 1
    print(f"XML gerado e validado: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
