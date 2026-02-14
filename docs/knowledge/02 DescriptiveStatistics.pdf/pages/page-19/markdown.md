# Bivariate data statistics

Consider the **predictive power** one input variable for one output variable

- for categorical outputs: we want to assess the **discriminative power** of the input variable
- for numeric outputs: we want to assess the **correlation** with the input variable
- the higher the correlation, the higher the relevance of the input variable to describe the targets

How?

- if both input-output variables are numeric
- linear correlation given by **Pearson** correlation coefficient (PCC)
- rank-based correlation given by **Spearman** or Kendall tau prioritizes ranks instead of magnitude
- if one variable is ordinal and other numeric or ordinal: **Spearman** or Kendall tau are suggested
- if one variable is nominal and other numeric: **analysis of variance** (ANOVA) or non-parametric peer
- if both variables are categorical: $\chi^2$ or information gain

TÉCNICO+ FORMACÃO AVANÇADA