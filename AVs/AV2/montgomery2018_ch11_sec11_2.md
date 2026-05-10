# Exercícios Montgomery 2018 - Capítulo 11, Seção 11.2

Fonte: `livros/Montgomery_2018.pdf`, Chapter 11 Exercises, subseção `Exercises for Section 11.2`, páginas internas do PDF 628 a 630.

Escopo extraído: exercícios `11.2.1` a `11.2.9`.

Observação: extração automática com limpeza leve de quebras de linha, hifenização e ligaturas. Conferir contra o PDF antes de usar como fonte final de avaliação.

### Exercício 11.2.1

Diabetes and obesity are serious health concerns in the United States and much of the developed world. Measuring the amount of body fat a person carries is one way to monitor weight control progress, but measuring it accurately involves either expensive X-ray equipment or a pool in which to dunk the subject. Instead body mass index (BMI) is often used as a proxy for body fat because it is easy to measure: BMI = mass(kg)/ (height(m))2 = 703 mass(lb)/(height(in))2. In a study of 250 men at Brigham Young University, both BMI and body fat were measured. Researchers found the following summary statistics:

| Quantity | Value |
| --- | ---: |
| `n` | 250 |
| `sum(x_i)` | 6322.28 |
| `sum(x_i^2)` | 162674.18 |
| `sum(y_i)` | 4757.90 |
| `sum(y_i^2)` | 107679.27 |
| `sum(x_i y_i)` | 125471.10 |

a. WP Calculate the least squares estimates of the slope and intercept. Graph the regression line.

b. WP Use the equation of the fitted line to predict what body fat would be observed, on average, for a man with a BMI of 30.

c. Suppose that the observed body fat of a man with a BMI of 25 is 25%. Find the residual for that observation.

d. Was the prediction for the BMI of 25 in part (c) an overestimate or underestimate? Explain briefly.

### Exercício 11.2.2

WP An article in Technometrics by S. C. Narula and J. F. Wellington [“Prediction, Linear Regression, and a Minimum Sum of Relative Errors” (1977, Vol. 19(2), pp. 185–190)] presents data on the selling price and annual taxes for 24 houses. The data are in the table that follows.

| Observation | Sale price / 1000 | Taxes / 1000 |
| ---: | ---: | ---: |
| 1 | 25.9 | 4.9176 |
| 2 | 29.5 | 5.0208 |
| 3 | 27.9 | 4.5429 |
| 4 | 25.9 | 4.5573 |
| 5 | 29.9 | 5.0597 |
| 6 | 29.9 | 3.8910 |
| 7 | 30.9 | 5.8980 |
| 8 | 28.9 | 5.6039 |
| 9 | 35.9 | 5.8282 |
| 10 | 31.5 | 5.3003 |
| 11 | 31.0 | 6.2712 |
| 12 | 30.9 | 5.9592 |
| 13 | 30.0 | 5.0500 |
| 14 | 36.9 | 8.2464 |
| 15 | 41.9 | 6.6969 |
| 16 | 40.5 | 7.7841 |
| 17 | 43.9 | 9.0384 |
| 18 | 37.5 | 5.9894 |
| 19 | 37.9 | 7.5422 |
| 20 | 44.5 | 8.7951 |
| 21 | 37.9 | 6.0831 |
| 22 | 38.9 | 8.3607 |
| 23 | 36.9 | 8.1400 |
| 24 | 45.8 | 9.1416 |

a. Assuming that a simple linear regression model is appropriate, obtain the least squares fit relating selling price to taxes paid. What is the estimate of sigma^2?

b. Find the mean selling price given that the taxes paid are x = 7.50.

c. Calculate the fitted value of y corresponding to x = 5.8980. Find the corresponding residual.

d. Calculate the fitted y_hat_i for each value of xi used to fit the model. Then construct a graph of y_hat_i versus the corresponding observed value yi and comment on what this plot would look like if the relationship between y and x was a deterministic (no random error) straight line. Does the plot actually obtained indicate that taxes paid is an effective regressor variable in predicting selling price?

### Exercício 11.2.3

WP An article in Concrete Research [“Near Surface Characteristics of Concrete: Intrinsic Permeability” (1989, Vol. 41, pp. 87–97)] presented data on compressive strength x and intrinsic permeability y of various concrete mixes and cures. Assume that the two variables are related according to the simple linear regression model. Summary quantities are:

| Quantity | Value |
| --- | ---: |
| `n` | 14 |
| `sum(x_i)` | 43 |
| `sum(x_i^2)` | 157.42 |
| `sum(y_i)` | 572 |
| `sum(y_i^2)` | 23530 |
| `sum(x_i y_i)` | 1697.80 |

a. Calculate the least squares estimates of the slope and intercept. Estimate sigma^2. Graph the regression line.

b. Use the equation of the fitted line to predict what permeability would be observed when the compressive strength is x = 4.3.

c. Give a point estimate of the mean permeability when the compressive strength is x = 3.7.

d. Suppose that the observed value of permeability at x = 3.7 is y = 46.1. Calculate the value of the corresponding residual.

### Exercício 11.2.4

An article in the Journal of Sound and Vibration [“Measurement of Noise-Evoked Blood Pressure by Means of Averaging Method: Relation between Blood Pressure Rise and SPL” (1991, Vol. 151(3), pp. 383–394)] described a study investigating the relationship between noise exposure and hypertension. The following data are representative of those reported in the article.

| Observation | `x` sound pressure level (decibels) | `y` blood pressure rise (mmHg) |
| ---: | ---: | ---: |
| 1 | 60 | 1 |
| 2 | 63 | 0 |
| 3 | 65 | 1 |
| 4 | 70 | 2 |
| 5 | 70 | 5 |
| 6 | 70 | 1 |
| 7 | 80 | 4 |
| 8 | 90 | 6 |
| 9 | 80 | 2 |
| 10 | 80 | 3 |
| 11 | 85 | 5 |
| 12 | 89 | 4 |
| 13 | 90 | 6 |
| 14 | 90 | 8 |
| 15 | 90 | 4 |
| 16 | 90 | 5 |
| 17 | 94 | 7 |
| 18 | 100 | 9 |
| 19 | 100 | 7 |
| 20 | 100 | 6 |

a. Draw a scatter diagram of y (blood pressure rise in millimeters of mercury) versus x (sound pressure level in decibels). Does a simple linear regression model seem reasonable in this situation?

b. Fit the simple linear regression model using least squares. Find an estimate of sigma^2.

c. Find the predicted mean rise in blood pressure level associated with a sound pressure level of 85 decibels.

### Exercício 11.2.5

SS An article in the Tappi Journal (March 1986) presented data on green liquor Na2S concentration (in grams per liter) and paper machine production (in tons per day). The data (read from a graph) follow:

| Observation | `x` production (tons/day) | `y` green liquor Na2S concentration (g/L) |
| ---: | ---: | ---: |
| 1 | 825 | 40 |
| 2 | 830 | 42 |
| 3 | 890 | 49 |
| 4 | 895 | 46 |
| 5 | 890 | 44 |
| 6 | 910 | 48 |
| 7 | 915 | 46 |
| 8 | 960 | 43 |
| 9 | 990 | 53 |
| 10 | 1010 | 52 |
| 11 | 1012 | 54 |
| 12 | 1030 | 57 |
| 13 | 1050 | 58 |

a. Fit a simple linear regression model with y = green liquor Na2S concentration and x = production. Find an estimate of sigma^2. Draw a scatter diagram of the data and the resulting least squares fitted model.

b. Find the fitted value of y corresponding to x = 910 and the associated residual.

c. Find the mean green liquor Na2S concentration when the production rate is 950 tons per day.

### Exercício 11.2.6

WP VS An article in the Journal of Environmental Engineering (1989, Vol. 115(3), pp. 608–619) reported the results of a study on the occurrence of sodium and chloride in surface streams in central Rhode Island. The following data are chloride concentration y (in milligrams per liter) and roadway area in the watershed x (in percentage).

| Observation | `x` roadway area in watershed (%) | `y` chloride concentration (mg/L) |
| ---: | ---: | ---: |
| 1 | 0.19 | 4.4 |
| 2 | 0.15 | 6.6 |
| 3 | 0.57 | 9.7 |
| 4 | 0.70 | 10.6 |
| 5 | 0.67 | 10.8 |
| 6 | 0.63 | 10.9 |
| 7 | 0.47 | 11.8 |
| 8 | 0.70 | 12.1 |
| 9 | 0.60 | 14.3 |
| 10 | 0.78 | 14.7 |
| 11 | 0.81 | 15.0 |
| 12 | 0.78 | 17.3 |
| 13 | 0.69 | 19.2 |
| 14 | 1.30 | 23.1 |
| 15 | 1.05 | 27.4 |
| 16 | 1.06 | 27.7 |
| 17 | 1.74 | 31.8 |
| 18 | 1.62 | 39.5 |

a. Draw a scatter diagram of the data. Does a simple linear regression model seem appropriate here?

b. Fit the simple linear regression model using the method of least squares. Find an estimate of sigma^2.

c. Estimate the mean chloride concentration for a watershed that has 1% roadway area.

d. Find the fitted value corresponding to x = 0.47 and the associated residual.

### Exercício 11.2.7

WP GO Tutorial SS An article in the Journal of the American Ceramic Society [“Rapid Hot-Pressing of Ultrafine PSZ Powders” (1991, Vol. 74, pp. 1547–1553)] considered the microstructure of the ultrafine powder of partially stabilized zirconia as a function of temperature. The data follow:

| Observation | `x` temperature (graus C) | `y` porosity (%) |
| ---: | ---: | ---: |
| 1 | 1100 | 30.8 |
| 2 | 1200 | 19.2 |
| 3 | 1300 | 6.0 |
| 4 | 1100 | 13.5 |
| 5 | 1500 | 11.4 |
| 6 | 1200 | 7.7 |
| 7 | 1300 | 3.6 |

a. Fit the simple linear regression model using the method of least squares. Find an estimate of sigma^2.

b. Estimate the mean porosity for a temperature of 1400 graus C.

c. Find the fitted value corresponding to y = 11.4 and the associated residual.

d. Draw a scatter diagram of the data. Does a simple linear regression model seem appropriate here? Explain.

### Exercício 11.2.8

An article in Wood Science and Technology [“Creep in Chipboard, Part 3: Initial Assessment of the Influence of Moisture Content and Level of Stressing on Rate of Creep and Time to Failure” (1981, Vol. 15, pp. 125–144)] reported a study of the deflection (mm) of particleboard from stress levels of relative humidity. Assume that the two variables are related according to the simple linear regression model. The data follow:

| Observation | `x` stress level (%) | `y` deflection (mm) |
| ---: | ---: | ---: |
| 1 | 54 | 16.473 |
| 2 | 54 | 18.693 |
| 3 | 61 | 14.305 |
| 4 | 61 | 15.121 |
| 5 | 68 | 13.505 |
| 6 | 68 | 11.640 |
| 7 | 75 | 11.168 |
| 8 | 75 | 12.534 |
| 9 | 75 | 11.224 |

a. Calculate the least square estimates of the slope and intercept. What is the estimate of sigma^2? Graph the regression model and the data.

b. Find the estimate of the mean deflection if the stress level can be limited to 65%.

c. Estimate the change in the mean deflection associated with a 5% increment in stress level.

d. To decrease the mean deflection by one millimeter, how much increase in stress level must be generated?

e. Given that the stress level is 68%, find the fitted value of deflection and the corresponding residual.

### Exercício 11.2.9

WP An article in the Journal of the Environmental Engineering Division [“Least Squares Estimates of BOD Parameters” (1980, Vol. 106, pp. 1197–1202)] took a sample from the Holston River below Kingport, Tennessee, during August 1977. The biochemical oxygen demand (BOD) test is conducted over a period of time in days. The resulting data follow:

| Observation | `x` time (days) | `y` BOD (mg/liter) |
| ---: | ---: | ---: |
| 1 | 1 | 0.6 |
| 2 | 2 | 0.7 |
| 3 | 4 | 1.5 |
| 4 | 6 | 1.9 |
| 5 | 8 | 2.1 |
| 6 | 10 | 2.6 |
| 7 | 12 | 2.9 |
| 8 | 14 | 3.7 |
| 9 | 16 | 3.5 |
| 10 | 18 | 3.7 |
| 11 | 20 | 3.8 |

a. Assuming that a simple linear regression model is appropriate, fit the regression model relating BOD (y) to the time (x). What is the estimate of sigma^2?

b. What is the estimate of expected BOD level when the time is 15 days?

c. What change in mean BOD is expected when the time changes by 3 days?

d. Suppose that the time used is 6 days. Calculate the fitted value of y and the corresponding residual.

e. Calculate the fitted y_hat_i for each value of xi used to fit the model. Then construct a graph of y_hat_i versus the corresponding observed values yi and comment on what this plot would look like if the relationship between y and x was a deterministic (no random error) straight line. Does the plot actually obtained indicate that time is an effective regressor variable in predicting BOD?
