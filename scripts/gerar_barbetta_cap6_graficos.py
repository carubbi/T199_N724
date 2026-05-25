from __future__ import annotations

import math
from pathlib import Path
from statistics import NormalDist

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "exs" / "und2" / "respostas" / "imgs"
N = NormalDist()


def normal_pdf(x: np.ndarray, mu: float = 0, sigma: float = 1) -> np.ndarray:
    return np.exp(-0.5 * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))


def phi(z: float) -> float:
    return N.cdf(z)


def binom_pmf(n: int, p: float) -> tuple[np.ndarray, np.ndarray]:
    xs = np.arange(n + 1)
    probs = np.array([math.comb(n, int(x)) * p**x * (1 - p) ** (n - x) for x in xs])
    return xs, probs


def poisson_pmf(lam: float, max_x: int) -> tuple[np.ndarray, np.ndarray]:
    xs = np.arange(max_x + 1)
    probs = np.array([math.exp(-lam) * lam**int(x) / math.factorial(int(x)) for x in xs])
    return xs, probs


def save(fig: plt.Figure, name: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT_DIR / name, dpi=180, bbox_inches="tight")
    plt.close(fig)


def base_ax(title: str, xlabel: str, ylabel: str):
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.25)
    return fig, ax


def plot_uniform(name: str, title: str, a: float, b: float, highlight: tuple[float, float] | None = None) -> None:
    xs = np.linspace(a - 0.15 * (b - a), b + 0.15 * (b - a), 400)
    density = np.where((xs >= a) & (xs <= b), 1 / (b - a), 0)
    fig, ax = base_ax(title, "x", "f(x)")
    ax.plot(xs, density, color="#1f77b4", linewidth=2)
    ax.fill_between(xs, 0, density, where=(xs >= a) & (xs <= b), color="#1f77b4", alpha=0.12)
    if highlight:
        lo, hi = highlight
        mask = (xs >= lo) & (xs <= hi)
        ax.fill_between(xs, 0, density, where=mask, color="#d62728", alpha=0.35, label="região do evento")
        ax.legend()
    ax.set_ylim(bottom=0)
    save(fig, name)


def plot_triangular(
    name: str,
    title: str,
    a: float,
    c: float,
    b: float,
    highlight: tuple[float, float] | None = None,
) -> None:
    xs = np.linspace(a, b, 500)
    density = np.where(xs <= c, (xs - a) / ((b - a) / 2) ** 2, (b - xs) / ((b - a) / 2) ** 2)
    if a == 20 and c == 22 and b == 24:
        density = np.where(xs <= c, (xs - 20) / 4, (24 - xs) / 4)
    fig, ax = base_ax(title, "x", "f(x)")
    ax.plot(xs, density, color="#1f77b4", linewidth=2)
    ax.fill_between(xs, 0, density, color="#1f77b4", alpha=0.12)
    if highlight:
        lo, hi = highlight
        mask = (xs >= lo) & (xs <= hi)
        ax.fill_between(xs, 0, density, where=mask, color="#d62728", alpha=0.35, label="região do evento")
        ax.legend()
    ax.set_ylim(bottom=0)
    save(fig, name)


def plot_exponential(
    name: str,
    title: str,
    lam: float,
    xmax: float,
    highlight: tuple[str, float | tuple[float, float]] | None = None,
) -> None:
    xs = np.linspace(0, xmax, 500)
    density = lam * np.exp(-lam * xs)
    fig, ax = base_ax(title, "t", "f(t)")
    ax.plot(xs, density, color="#1f77b4", linewidth=2)
    ax.fill_between(xs, 0, density, color="#1f77b4", alpha=0.10)
    if highlight:
        kind, value = highlight
        if kind == "right":
            mask = xs >= float(value)
        elif kind == "left":
            mask = xs <= float(value)
        else:
            lo, hi = value  # type: ignore[misc]
            mask = (xs >= lo) & (xs <= hi)
        ax.fill_between(xs, 0, density, where=mask, color="#d62728", alpha=0.35, label="região do evento")
        ax.legend()
    ax.set_ylim(bottom=0)
    save(fig, name)


def plot_exponential_survival(name: str, title: str, lam: float, xmax: float, mark: float | None = None) -> None:
    xs = np.linspace(0, xmax, 500)
    fig, ax = base_ax(title, "t", "probabilidade")
    ax.plot(xs, 1 - np.exp(-lam * xs), label="F(t)=P(T<t)", color="#1f77b4", linewidth=2)
    ax.plot(xs, np.exp(-lam * xs), label="P(T>t)", color="#ff7f0e", linewidth=2)
    if mark is not None:
        ax.axvline(mark, color="#d62728", linestyle="--", linewidth=1.6)
    ax.set_ylim(0, 1.02)
    ax.legend()
    save(fig, name)


def plot_normal(
    name: str,
    title: str,
    mu: float,
    sigma: float,
    highlight: tuple[float | None, float | None] | None = None,
) -> None:
    xs = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 800)
    density = normal_pdf(xs, mu, sigma)
    fig, ax = base_ax(title, "x", "f(x)")
    ax.plot(xs, density, color="#1f77b4", linewidth=2)
    ax.fill_between(xs, 0, density, color="#1f77b4", alpha=0.08)
    ax.axvline(mu, color="#444444", linestyle="--", linewidth=1.2, label="média")
    if highlight:
        lo, hi = highlight
        mask = np.ones_like(xs, dtype=bool)
        if lo is not None:
            mask &= xs >= lo
            ax.axvline(lo, color="#d62728", linestyle=":", linewidth=1)
        if hi is not None:
            mask &= xs <= hi
            ax.axvline(hi, color="#d62728", linestyle=":", linewidth=1)
        ax.fill_between(xs, 0, density, where=mask, color="#d62728", alpha=0.35, label="região do evento")
    ax.set_ylim(bottom=0)
    ax.legend()
    save(fig, name)


def plot_two_normals(name: str, title: str) -> None:
    xs = np.linspace(0, 16, 800)
    fig, ax = base_ax(title, "anos", "densidade")
    ax.plot(xs, normal_pdf(xs, 6, 2.3), label="M1: média 6, desvio 2,3", color="#1f77b4", linewidth=2)
    ax.plot(xs, normal_pdf(xs, 8, 2.8), label="M2: média 8, desvio 2,8", color="#ff7f0e", linewidth=2)
    ax.axvline(2, color="#1f77b4", linestyle=":", linewidth=1.3)
    ax.axvline(3, color="#ff7f0e", linestyle=":", linewidth=1.3)
    ax.fill_between(xs, 0, normal_pdf(xs, 6, 2.3), where=xs <= 2, color="#1f77b4", alpha=0.20)
    ax.fill_between(xs, 0, normal_pdf(xs, 8, 2.8), where=xs <= 3, color="#ff7f0e", alpha=0.20)
    ax.legend()
    save(fig, name)


def plot_binomial(
    name: str,
    title: str,
    n: int,
    p: float,
    highlight: tuple[str, int],
    normal_overlay: bool = False,
) -> None:
    xs, probs = binom_pmf(n, p)
    fig, ax = base_ax(title, "x", "p(x)")
    if n > 60:
        width = 0.9
    else:
        width = 0.75
    colors = np.full(len(xs), "#8fb9dd", dtype=object)
    kind, k = highlight
    if kind == "ge":
        colors[xs >= k] = "#d62728"
    elif kind == "gt":
        colors[xs > k] = "#d62728"
    elif kind == "eq":
        colors[xs == k] = "#d62728"
    ax.bar(xs, probs, width=width, color=colors, edgecolor="white")
    if normal_overlay:
        mu = n * p
        sigma = math.sqrt(n * p * (1 - p))
        xline = np.linspace(max(0, mu - 4 * sigma), min(n, mu + 4 * sigma), 500)
        ax.plot(xline, normal_pdf(xline, mu, sigma), color="#111111", linewidth=2, label="normal aproximada")
        ax.legend()
    save(fig, name)


def plot_poisson_normal(name: str, title: str, lam: float, cutoff: float) -> None:
    max_x = max(int(lam + 5 * math.sqrt(lam)), int(cutoff + 10))
    xs, probs = poisson_pmf(lam, max_x)
    fig, ax = base_ax(title, "x", "probabilidade")
    colors = np.where(xs > cutoff, "#d62728", "#8fb9dd")
    ax.bar(xs, probs, width=0.85, color=colors, edgecolor="white", label="Poisson")
    xline = np.linspace(max(0, lam - 4 * math.sqrt(lam)), lam + 4 * math.sqrt(lam), 500)
    ax.plot(xline, normal_pdf(xline, lam, math.sqrt(lam)), color="#111111", linewidth=2, label="normal aproximada")
    ax.legend()
    save(fig, name)


def plot_ex_07_memoryless() -> None:
    lam = 1
    xs = np.linspace(0, 6, 500)
    fig, ax = base_ax("Ex. 7 - Falta de memória da exponencial", "tempo", "P(T>t)")
    ax.plot(xs, np.exp(-lam * xs), color="#1f77b4", linewidth=2, label="P(T>t)")
    s, t = 2, 1.5
    ax.axvline(s, color="#ff7f0e", linestyle="--", label="s")
    ax.axvline(s + t, color="#d62728", linestyle="--", label="s+t")
    ax.annotate("após s, a curva restante mantém a mesma forma", xy=(s, math.exp(-s)), xytext=(2.4, 0.55), arrowprops={"arrowstyle": "->"})
    ax.set_ylim(0, 1.02)
    ax.legend()
    save(fig, "barbetta_cap6_ex_07_falta_memoria.png")


def main() -> None:
    # Exemplos resolvidos.
    plot_uniform("barbetta_cap6_exemplo_6_1_ponteiro_discretizacao.png", "Exemplo 6.1 - Probabilidades como áreas", 0, 360, (90, 180))
    plot_uniform("barbetta_cap6_exemplo_6_2_uniforme_angulo.png", "Exemplo 6.2 - Ângulo uniforme em [0,360)", 0, 360, (90, 180))
    plot_exponential("barbetta_cap6_exemplo_6_3_exponencial_tempo_resposta.png", "Exemplo 6.3 - Tempo de resposta exponencial", 2, 4, ("right", 3))
    plot_normal("barbetta_cap6_exemplo_6_4_normal_padrao.png", "Exemplo 6.4 - Normal padrão", 0, 1, (-0.42, 0.42))
    plot_normal("barbetta_cap6_exemplo_6_5_valor_critico_95.png", "Exemplo 6.5 - Área central de 95%", 0, 1, (-1.96, 1.96))
    plot_normal("barbetta_cap6_exemplo_6_6_absorcao_agua.png", "Exemplo 6.6 - Absorção de água", 2.5, 0.6, (2, 3.5))
    plot_binomial("barbetta_cap6_exemplo_6_7_aproximacao_binomial.png", "Exemplo 6.7 - Binomial aproximada pela normal", 1000, 0.1, ("gt", 120), True)
    plot_binomial("barbetta_cap6_exemplo_6_8_correcao_continuidade.png", "Exemplo 6.8 - Correção de continuidade", 10, 0.5, ("eq", 4), True)

    # Exercícios propostos.
    plot_uniform("barbetta_cap6_ex_01_uniforme_0_1.png", "Ex. 1 - Uniforme em [0,1]", 0, 1, (0.25, 0.75))
    plot_uniform("barbetta_cap6_ex_02_uniforme_20_24.png", "Ex. 2 - Tempo uniforme em [20,24]", 20, 24, (23, 24))
    plot_triangular("barbetta_cap6_ex_03_triangular_20_24.png", "Ex. 3 - Densidade triangular em [20,24]", 20, 22, 24, (23, 24))
    plot_exponential_survival("barbetta_cap6_ex_04_acumulada_exponencial.png", "Ex. 4 - F(x)=1-e^{-x}", 1, 6)
    plot_triangular("barbetta_cap6_ex_05_triangular_0_2.png", "Ex. 5 - Densidade por partes em [0,2]", 0, 1, 2, (1 / 3, 1.5))
    plot_exponential("barbetta_cap6_ex_06_vida_transistor.png", "Ex. 6 - Vida de transistor", 1 / 500, 2200, ("interval", (300, 1000)))
    plot_ex_07_memoryless()
    plot_normal("barbetta_cap6_ex_08_normal_padrao.png", "Ex. 8 - Normal padrão", 0, 1, (-1, 1))
    plot_normal("barbetta_cap6_ex_09_tempo_algoritmo.png", "Ex. 9 - Tempo de resposta", 23, 4, (20, 30))
    plot_normal("barbetta_cap6_ex_10_peso_bruto.png", "Ex. 10 - Peso bruto", 1000, math.sqrt(116), (980, 1020))
    plot_binomial("barbetta_cap6_ex_11_binomial_normal.png", "Ex. 11 - Defeituosos em 100 itens", 100, 0.1, ("gt", 12), True)
    plot_poisson_normal("barbetta_cap6_ex_12_poisson_normal.png", "Ex. 12 - Solicitações em 10 minutos", 70, 80)
    plot_exponential("barbetta_cap6_ex_13_falha_equipamento.png", "Ex. 13 - Tempo até falha", 0.75, 5, ("right", 1))
    plot_exponential("barbetta_cap6_ex_14_falha_antes_media.png", "Ex. 14 - Falha antes de 10.000 h", 1 / 10000, 40000, ("left", 10000))
    plot_exponential_survival("barbetta_cap6_ex_15_quantil_exponencial.png", "Ex. 15 - Tempo para 25% de falhas", 1 / 10000, 40000, -10000 * math.log(0.75))
    plot_exponential("barbetta_cap6_ex_16_distancia_defeito.png", "Ex. 16 - Distância até próximo defeito", 1 / 100, 350, ("right", 120))
    plot_normal("barbetta_cap6_ex_17_temperatura_pasteurizador.png", "Ex. 17 - Temperatura do pasteurizador", 75.4, 2.2, (None, 70))
    plot_normal("barbetta_cap6_ex_18_tempo_tarefa.png", "Ex. 18 - Tempo de execução", 320, 7, (310, 330))
    plot_binomial("barbetta_cap6_ex_19_aprovacao_palpite.png", "Ex. 19 - Aprovação por palpite", 10, 0.25, ("ge", 5), False)
    plot_poisson_normal("barbetta_cap6_ex_20_requisicoes_banco.png", "Ex. 20 - Requisições por minuto", 100, 120)
    plot_exponential_survival("barbetta_cap6_ex_21_primeira_conexao.png", "Ex. 21 - Tempo até primeira conexão", 5, 1, -math.log(0.1) / 5)
    plot_normal("barbetta_cap6_ex_22_diametro_pontos.png", "Ex. 22 - Diâmetro dos pontos", 4, 0.19, (3.7, 4.3))
    plot_normal("barbetta_cap6_ex_23_resistencia_cimento.png", "Ex. 23 - Resistência do cimento", 5800, 180, (None, 5600))
    plot_two_normals("barbetta_cap6_ex_24_monitores.png", "Ex. 24 - Durabilidade dos monitores")

    print(f"Geradas {len(list(OUT_DIR.glob('barbetta_cap6_*.png')))} imagens em {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
