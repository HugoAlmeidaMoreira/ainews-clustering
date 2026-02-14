# Machine Learning - Complete Lecture Notes
*Combined from OCR outputs*

*Total lectures: 10*
---
## Table of Contents
1. [Introduction to Machine Learning](#01-introductionml)
2. [Associative analysis](#02-descriptivestatistics)
3. [Clustering (1/2)](#03a-clustering-part1)
4. [Clustering (2/2)](#03b-clustering-part2)
5. [Representation Learning](#04-representationlearning)
6. [Dimensionality reduction](#05-dimensionalityreduction)
7. [Outlier analysis](#06-outlieranalysis)
8. [Pattern Discovery: Introduction](#07a-patterndiscovery)
9. [Subspace clustering for pattern discovery](#07b-subspaceclustering-v2)
10. [Advanced Descriptive Modeling](#08-advancedpm-learningfromcomplexdata)

---

## Lecture 1: Introduction to Machine Learning

*Source: 01 IntroductionML*

---
# Introduction to Machine Learning

Descriptive versus predictive modeling

# Outline

- Intelligence and learning
- Descriptive vs predictive learning
- Machine Learning, Data Science and AI
- Supervised vs unsupervised learning
- Terminology
- Machine learning tasks

 

# Intelligence

- Rationality
- ability to act in a way that maximizes some utility function
- Curiosity
- ability to engage creative imaginative or inquisitive reasoning
- Adaptability $\Leftarrow$
- ability learn from experience
- make abstractions (patterning)
- deal with novelty and change

# Artificial Intelligence

## Qualities of intelligence?

- AI with a focus on learning from experience =&gt; machine/deep learning, reinforcement learning ...
- AI with a focus on rationality =&gt; planning, reasoning, optimization ...
- AI with a focus on curiosity =&gt; autonomous agents, affective computing, ...
- AI with a focus on social intelligence =&gt; human-agent interaction, social robots, multi-agent systems...

# AI and Data Science

- (machine) learning is a fundamental quality of (artificial) intelligence
- experience – data records – needed to learn intelligent agents!

- data science is the principled application of machine learning to solve data-rich problems
- at the core of many breakthroughs
- chatbots, smart assistants
- personalized recommenders
- self-driving vehicles
- intelligent care
- cybersecurity
- ...

# Systemic world view

- system
- set of elements organized with a shared purpose
- (open) surrounded and influenced by its environment
- described by its structure, purpose and functioning
- open systems evolve

- Universe → galaxy → solar system
→ Earth → societies → individuals
→ organs → cells → atoms

ENVIRONMENT

# Systemic world view

- Everything is systemic:
- biological systems
- ecological systems
- societal systems
- mechanical systems
- digital systems
- quantum systems
- hybrid systems
- astrophysical systems

“we contain, are, interact and move within systems”

Psychoanalyst: Know the influence of the surrounding systems in our life and be free!

- The behavior of all these systems can be monitored (e.g. sensorization, observation)

# Data everywhere!

Sensorization examples:

- biological systems
- physiological signals from biosensors, molecular signals using multi-omic high-throughput profiling
- health records (diagnostics, prescriptions, undertaken surgeries), exposomics, demographics
- ecological systems
- biodiversity, plant health, crop and livestock conditions, food nutrition, forestry and fishery surveillance monitored using remote vision (satellite, drones), physical sensors, acoustic sensors, citizen notifications
- societal systems
- social interactions via social networks, telecom and messaging apps
- commerce and finance via transaction records
- urban systems
- mobility from mobile phones, smart card validations, loop counters, privacy-preserving cameras
- water and energy supply via telemetry (flowrate, pressure, smart sensors)
- ... [homework: complete the list]

# From experience to learning

- Recall: learning as a fundamental quality of intelligence
- "learning is any process by which a system improves performance from experience" (Herbert Simon)

- Experience recorded as data observations acquired from:
- multiple systems of the same type
- e.g. multiple individuals (cohorts), vehicles, computers, regions, organizations
- single system instance under different conditions
- e.g. brain under different stimuli, crop under different weather, e-commerce along time

- Learn from the experience (records): multiple data observations... statistics!
- discover relevant associations (patterning)

 

# Statistical grounds

- Machine learning as...
- the rediscovery of multivariate **statistics** from observable data (samples)
- beyond descriptive and inferential statistics
- the rediscovery of **maths** (linear algebra, calculus...)

- Exercise: associate naïve Bayes, kNN and deep learning (DL) with the aforementioned fields
- solution: NB: statistics, kNN: algebra, DL: calculus

Sir William Petty, a 17th-century economist who used early statistical methods to analyse demographic data

# Descriptive vs predictive learning

- Major ends of pattern recognition (learning from experience):
- understanding system behavior (descriptive learning)
- data ⇒ information ⇒ knowledge
- unsupervised learning: learning in the absence of outcomes of interest
- supervised learning: outcomes of interest can be used to guide description
- supporting decisions (predictive learning)
- data and outcomes ⇒ decision support system
- supervised or semi-supervised learning
- semi-supervised when outcomes are only known for a subset of all observations

 

# When?

- Descriptive learning (e.g., finding associations, categories, anomalies, summaries, informative features, representations) when:
- human expertise does not exist (e.g. navigating on Mars, new cyberattacks)
- humans cannot explain their expertise (e.g. speech recognition)
- models must be customized (e.g. personalized medicine, user preferences)
- massive amounts of data (e.g. genomics, commerce, social media, web usage)

by Eric Eaton

# Learning stances

- classic AI
- e.g. heuristics to play chess, drive a car, recommend products, diagnose

- supervised learning
- e.g. experience from good chess players, drivers, liked recommendations, clinical histories for decision support

- unsupervised learning
- e.g. understand decisions, detect anomalies and behavioral patterns, summarize actions

"Machine Learning: field of study that gives computers the ability to learn without being explicitly programmed" Arthur Samuel (1959)

# Data Science and Machine Learning

- Machine Learning versus Data Science
- ML as the foundations, principles and algorithms to learn from available data
- grounded on statistical, algebraic, mathematical and algorithmic foundations
- Data science is the principled application of ML to solve specific data-rich problems
- in other words, ML is a means to data science
- data science has been termed as the art of discovering what we don't know from data

- Machine Learning versus Artificial Intelligence
- ML is a topic within the larger AI field
- AI topics: optimization, search/planning, knowledge systems, autonomous agents

# Coming to terms with terms

What about...
- Data-centric AI, Agentic AI
- Data Mining, Multivariate Data Analysis
- Business Intelligence

... and terminology choices...
- AI vs intelligent systems vs intelligent agents
- variable vs attribute vs feature
- observation vs instance vs object vs record vs data point

 

# Structured view on ML

## MELO DATA

feature data
text data
time series, event data
image, video data
heterogeneous data

## Learning

HOW approaches

## OUTPUT MODEL

predictive models (supervised)
descriptive models (unsupervised/supervised)
prescriptive models (reinforcement)

# Learning input-output functions

- Supervised learning
- with a teacher (that tells you the ground truth)
- learning from training data: pairs of inputs and outputs (labels, quantities, structures)

- Unsupervised learning
- without a teacher
- learning from training data without outputs (e.g. find associations, clusters/categories, anomalies)

- Reinforcement learning
- with a teacher (that highlights both good and bad outputs)
- learning rewards and penalties observed from sequence of decisions within a given environment

 

# Reinforcement learning?

- How can we have agents making decisions with little or no prior knowledge?
- trial-and-error (reinforcement learning)
+ learning from available observations
- In practice...
- conversational AI, e-mail bots, recommendations...
- adjusting predictors from ongoing pos or negative(!) feedback
- self-driving car in simulated environments
- rewards and penalties according to (un)desired risks
- optimization in industry (e.g., automation) and healthcare (e.g., therapeutics) based on ongoing pairs (protocol, outcome)

# Learning in practice

Recall: knowledge discovery from data (KDD) is a composition of steps:

- data acquisition and integration
- data preprocessing
- data cleaning (e.g. handling noise, duplicates, outliers, missings)
- data representation (e.g. extract features from complex data)
- data transformation (e.g. feature engineering, sampling, normalization, dimensionality reduction)
- data mining using machine learning
- postprocessing, explainability and knowledge acquisition from descriptive models or predictive models
- validate, consolidate and deploy discovered knowledge

# Terminology

## Multivariate data:

- set of **observations**, $X = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ (population)
- with values/**features** along a set of **variables**, $Y = \{y_1, \dots, y_m\}$
- **input variables** (explanatory) and optional output variables (**targets**), $Z = \{y_1, \dots, z_p\}$
- data **size** = number of observations, $|X| = n$
- data **dimensionality** = number of input variables, $|Y| = m$

# Learning from data

Learning from data: retrieving relevant patterns
- relations/patterns/abstractions ≡ associations of interest on specific observations and variables
- unexpectedly informative
- unexpectedly discriminative (of one or more targets)
- use these relations to learn descriptors, classifiers, regressors, multi-output predictors, forecasters...

# Feature space

A set of variables (dimensions) define a space

- multivariate observations are positioned in this space
- when variables are numeric:
- feature space ≡ vector space (e.g. Euclidean space)
- observation ≡ data point

$$
\mathbf {x} = \left\{x _ {1}, \dots , x _ {m} \right\} \in \mathbb {R} ^ {m}
$$

$$
\| \mathbf {a} - \mathbf {b} \| = \sqrt {\sum_ {i = 1} ^ {m} (a _ {i} - b _ {i}) ^ {2}}
$$

# Classification

Recall: given a set of labeled observations, $\{(x_1, z_1), \ldots, (x_n, z_n)\}$ where $z_n \in \Sigma$, a classifier $M$ is a mapping function between domain variables and a categoric variable, $M: X \to Z$

- **prediction**: given a new unlabeled observation $\mathbf{x}_{new}$, use $M$ to classify: $\hat{z}_{new} = M(x_{new})$
- **description**: inspect $M$ to acquire new knowledge

Binary classification:

Multi-class classification:

# Classification: salmon?

- width and lightness are discriminative variables
- generalization ability linked with:
- underfitting risks
- overfitting risks
- aim: find a balanced model capacity

TECNI

# Regression

- descriptive setting: given a set of observations, $\{(\mathbf{x}_1, z_1), \ldots, (\mathbf{x}_n, z_n)\}$ where $z_i \in \mathbb{R}$, describe the relation between a set of (explanatory) variables and a target numeric variable
- predictive setting: given a set of observations, $\{(\mathbf{x}_1,z_1),\ldots ,(\mathbf{x}_n,z_n)\}$ where $z_{i}\in \mathbb{R}$, learn a mapping, $M:X\to Z$, to estimate the outcome (quantity) of a new observation

# Multi-output prediction

- Most outputs are not described by a single feature
- generative AI (e.g. question-answer, image drawing, signal transform)
- many others (e.g. self-driving vehicles, tagging content)

- Multi-output predictors, $M: X \to Z$
- predictive setting (learn predictor $M$)
- descriptive setting (explain predictor $M$)

- Special cases: multi-label classification when $\mathbf{z} \in \Sigma^{p}$ and multi-output regression when $\mathbf{z} \in \mathbb{R}^{p}$

# Statistical modeling

## Associative analysis

### Description of system dynamics

- mixture models
- generative models (such as HMMs)

# Clustering

Given a set of data observations, $X = \{\mathbf{x}_1,\dots ,\mathbf{x}_n\}$, cluster analysis aims at grouping observations into clusters, $C_i \subseteq X$ with $i = 1..k$, according to their (dis)similarity:

- observations in the same cluster are more similar than those in different clusters

# Pattern mining

{symptomA, testB+} ⇒ condition1 [support=10%, confidence=80%, lift=1.4, p-value=1E-4]

Given a dataset, find local associations (aka patterns) satisfying:

- statistical significance criteria (min #observations to be unexpectedly frequent)
- discriminative power (qualitative targets) or correlation (numeric targets) criteria

# Outlier analysis

- Understand peculiar behaviors and isolate anomalous observations
- fraud, cyberattacks, personalized health risks, adverse events, deviant social behavior, vehicle failures...

# Representation learning

Describe data using a compact set of informative (unsupervised) and/or predictive (supervised) features

- dimensionality reduction: subset of features from multivariate observations with minimal info loss
- latent feature representations of complex signals (series, image, text data) using neural networks

# Example: biomedicine

- clinical trials (cohort studies), e.g. case-control populations
- observations generally correspond to:
- individuals
- input variables: health-related features (clinical records, multi-omics, exposomics)
- output variable: outcome annotations
- qualitative conditions (diagnostics, prognostics, prescriptions, traits)
- quantifiable phenotypes (impairments, molecular markers, risk, survivability, drug dosage)
- hospitals, tissue samples, undertaken procedures, healthcare professionals, drugs...
- ability to generalize from a population to new observations
- prevent overfitting (including non-relevant relations in the learned models)
- prevent underfitting (excluding relevant relations from the learned models)

# Example: biomedicine

- Statistical modeling: assess risk determinants, model health trajectories, test clinical hypotheses
- Clustering: group patients in accordance with biophysiological profile (e.g. stratified therapeutics)
- Pattern mining: discover meaningful associations to understand disease/therapeutic responses
- Outlier analysis: personalized care to particular needs (e.g. multimorbidity, rare diseases)
- Representation learning: encoders and saliency maps of medical signals/images/notes
- Generative modeling: comprehensive models of disease/treatment (e.g. health progression)
- Classification: how monitored inputs affect diagnostics/prognostics, therapeutic choices
- Regression: estimate risk, drug dosage or efficacy, quantifiable phenotypes

 

Rui Henriques

---

## Lecture 2: Associative analysis

*Source: 02 DescriptiveStatistics*

---
# Associative analysis

Univariate and bivariate statistics

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

 

# Classical statistics vs intelligence

- I have a **data-rich problem** at hands. What to do next?
- understanding and translating the problem into an appropriate task is the most critical step
- simple statistics vs intelligence? "do not use a cannon to kill a mosquito"

- Choose **classical statistics** when:
- the primary goal is **associative analysis**, **inference**, or **hypothesis testing**
- you need **confidence intervals**, $p$-values, **sample size** estimates, **uncertainty bounds**
- relationships in data are **simple** or **theoretically motivated**
- **assumptions** (linearity, normality, independence) are reasonable
- classical **feature extraction** is sufficient (e.g. sliding statistics from signals, spectrograms from images, term frequencies from text...)

# Classical statistics vs intelligence

- Choose **machine learning** when:
- the goal is **prediction** or **description** with the highest **efficacy** and generalization capacity
- system dynamics or relationships in data are highly **complex, noisy** or **unknown**
- data is **high-dimensional** with non-linear associations
- **feature extraction** is difficult or unclear

- Also recall: **learning** is just one of many forms of intelligence! Some problems better suited to:
- **rationality**: data-centric optimization, simulation, control, planning...
- **emotional intelligence**: data-grounded sensing, reasoning, expression of/under affective states...
- **social intelligence**: swarm intelligence for hard data-intensive tasks, agent communication...
- **hybrid**: combining forms of intelligence to solve challenging problems (e.g. self-driving cars)

- Follow classes to exercise and deepen this thinking with your project case studies!

 

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

# Univariate data analysis

- Irrespectively of the goal, **statistics** helps us understand data
- hearing our dataset is always the first important step!
- stances: univariate → bivariate → multivariate

- Random/aleatory variable
- function $X: \Omega \to \mathbb{E}$ from a sample space $\Omega$ to a measurable space $\mathbb{E}$
- e.g. height variable is a function that maps a person from a population $\Omega$ to a height in $\mathbb{R}^+$ ($\mathbb{E} = \mathbb{R}^+$)
- the observed height is referred as a measurement/feature
- from now one, we will refer a random variable simply as variable

- Univariate data analysis: single input variable
- comprises univariate data statistics or, in the presence of an output variable, bivariate data statistics

- Multivariate data analysis: multiple input variables
- multivariate order = number of input variables

# Variables

- Categorical (or qualitative) variables
- values are categories
- can either be nominal/symbolic or ordinal (e.g. {low, average, high})
- binary variables are variables with two categories (whether nominal or ordinal)
- variable cardinality = number of categories

- Numerical (or quantitative) variables
- values are quantities
- can be either be discrete (e.g. integers) or continuous (e.g. real values)

- Exercise: typify the following variables: gender, age, height

# Data profiling

- Data profiling ≡ data exploration (aka Exploratory Data Analysis)
- essential step to characterize data and guide subsequent data mining decisions

- Frequentist statistics
- categorical variables
- category frequencies
- category probabilities (probability mass function)
- numeric variables
- classic histograms: bin frequencies
- empirical probability distribution
- bin probabilities (probability mass function)
- probability density function (using for instance KDE)

# Data profiling: histograms

- The value range of a numeric variable can be divided into several bins
- bin size can strongly affect the frequency histogram
- revealing details when we lower bin size, yet at times a result of overfitting
- bin size also affects one's perception of the shape of distribution

# Data profiling

- Theoretical statistics
- summary statistics: mean and deviation statistics (Gaussian assumption)
- fitting theoretical distributions
- discrete numeric variables: fitting known probability mass functions
- continuous numeric variables fitting known probability density functions
- Empirical versus theoretical distributions
- empirical distribution are perfectly overfitted to observed data
- problematic for low data sample size, otherwise preferable
- Probability versus cumulative probability functions
- former is generally preferred (yet what about "age&lt;10"?)

# Data profiling: fitting theoretical distributions

- Theoretical pdfs: e.g. Uniform (left), Gaussian (center)

- How to fit?
- Kolmogorov-Sminor statistical test
https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html
- learn parameters that describe the variable

# Normal distribution

- many real-world variables are well-approximated to a Gaussian curve
- skewing is nevertheless pervasive, e.g. left skewing
- how to check if one variable satisfies the Gaussian assumption?
- use Kolmogorov-Smirnov test or, more suitably, Shapiro-Wilk test
- central limit theorem: 30 measurements often necessary to test this assumption
- interesting properties of the Normal curve:
- $\mu$–σ to $\mu$+σ contains about 68% of the measurements (μ: mean, σ: standard deviation)
- $\mu$–2σ to $\mu$+2σ contains ~95%, $\mu$–3σ to $\mu$+3σ: contains ~99.7%

# Univariate summary statistics

- sample size: number of data observations, $n$
- percentiles
- median, maximum and minimum (50, 100 and 0 percentiles respectively)
- 5, 10, 25 (first quantile), 75 (third quantile), 90, 95 are also informative

- center statistics
- arithmetic mean (average): $\bar{\mathbf{x}} = \frac{1}{n}\sum_{i=1}^{n}x_{i}$
- median: 50 percentile, e.g. median(1,1,2,3,4,5) = 2.5
- if n is even, the median can be found by interpolating them
- mode for categorical and discrete numeric values, e.g. mode(1,2,2,3,4,4,4) = 4

 

# Univariate summary statistics

- variability statistics
- standard deviation for numeric variables (square root of the variance)

$$
\sigma_{population} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \bar{\mathbf{X}})^2}, \quad \sigma_{sample} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{\mathbf{X}})^2}
$$

- population-based (divided by $n$) versus sample-based (divided by $n - 1$)
- sample is a conservative estimate (higher) since we do not observe the whole population
- example: $\{1,2,15\}$ measurements: $\mu = 6$, median $= 2$, $\sigma_{population} = 6.37$, $\sigma_{sample} = 7.81$

- entropy for categorical variables $H(\mathbf{x}) = -\sum_{x \in \mathbf{x}} p(x) \log p(x)$
- the higher entropy, the higher the variability
- example: $H(A,A,A,A) = 0$, $H(A,A,A,B) = 0.81$, $H(A,A,B,B) = 1$

 FORMÁCÃO AVANÇADA

# Univariate outliers

- Univariate outlier values = uncommon values
- unexpected measurements in accordance with a variable distribution
- can cause strong effects that can wreck our interpretation of data
- numeric example: mean and variance are based on averages, hence sensitive to outliers

- Challenge: detecting outliers requires judgment and depends on one's purpose

- Any heuristic?
- interquartile range (IQR) measures value expectations
- IQR is the difference between highest value in Q3 and lowest in Q2
- quartiles(1,1,2,3,5,5,6,100) = {(1,1),(2,3),(5,5),(6,100)}, IQR 5-3=2
- observations falling outside [Q1 - 1.5 × IQR, Q3 + 1.5 × IQR] seen as outliers
- deviations falling outside $\mu \pm 2\sigma$, $\mu \pm 3\sigma$ or other user-specific criteria

# Preprocessing procedures

- [discretization] numeric variables can be discretized into ordinal variables
- e.g. age categories of 0-10, 11-20, 21-30, 31-40...
- trade-off: loss of information versus utility for subsequent data analysis
- [normalization] numeric variables can be normalized
- comparability between variables with different domains E
- [aggregation] categoric variables with high cardinality can be aggregated
- 100 colors can be aggregated into coarser categories in accordance with hue
- [imputation] missing values can occur
- unobserved, error or noisy measurements
- missings can be imputed using variable expectations

 

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

 

# Bivariate data statistics

Considering pairwise input variables:
- check whether two variables are strongly associated
- e.g. two highly correlated numeric variables
- if strongly associated, variables may be redundant
- e.g. select the one with higher variability

Exercise: select non-redundant variables on the provided left example

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

 

# Discriminative power

## Class-conditional distributions

- given an input variable, the higher the dissimilarity between class-condition distributions: the higher the discriminative power
- exercise: consider the following data given by 9 numeric input variables and a binary class

- Is the left data easy or hard to classify using discriminants?

# Discriminative power

Using class-conditional distributions:

- discriminative rules can be inferred by identifying the more probable class per input value
- this classifier is termed univariate discriminant

# Correlation...

- Scatter diagrams can be used to visually assess correlation
- they further provide a first look at bivariate relations to see clusters, outliers, etc.

# Correlation...

Relationship between two quantitative variables

- correlation: degree to which two attributes are related (in [-1,1])
- the sign: nature of association (&gt;0 direct; &lt;0 inverse)
- the absolute value: strength of association
- unable to infer causal relationships

# Pearson correlation

- Linear correlation
- only suitable for numeric variables
- able to handle scales and shifts

|  Anxiety (y₁) | Test score (y₂)  |
| --- | --- |
|  10 | 2  |
|  8 | 3  |
|  2 | 9  |
|  1 | 7  |
|  5 | 6  |
|  6 | 5  |

$$
Pearson \mathbf{r} = \frac{cov(y_1, y_2)}{\sqrt{var(y_1)}\sqrt{var(y_2)}} = -0.94
$$

# Spearman rank

- Non-parametric coefficient
- works with rankings instead of absolute values
- How?
1. rank the values of $y_1$ and $y_2$
2. apply the Pearson correlation
- In the given example:
$$
r_s = PCC([5,6,1.5,3.5,3.5,7,1.5], [3,5.5,7,5.5,4,2,1]) = -0.17
$$
where $r_s$ is the magnitude of association

|  education level (y1) | income (y2) | rank y1 | rank y2  |
| --- | --- | --- | --- |
|  Preparatory | 25 | 5 | 3  |
|  Primary | 10 | 6 | 5.5  |
|  University | 8 | 1.5 | 7  |
|  Secondary | 10 | 3.5 | 5.5  |
|  Secondary | 15 | 3.5 | 4  |
|  Illiterate | 50 | 7 | 2  |
|  University | 60 | 1.5 | 1  |

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

 

# Hypothesis testing

- Evaluate evidence against a null hypothesis using sample data
- whether observed effects are likely due to chance vs statistically significant

- Hypothesis:
- null (H₀): no effect, no difference, or no association
- alternative (H₁): an effect, difference, or association exists

- Decision: given a predefined significance threshold (commonly α = 0.05)
- p ≤ α → Reject H₀ (evidence against the null)
- p &gt; α → Fail to reject H₀ (insufficient evidence)

- Example: test whether model M₁ is superior than M₂ using performance estimates:
- p = 1E-4 → reject no difference, i.e. statistically significant superiority given the collected estimates
- p = 0.1 → insufficient evidence

# Hypothesis testing

- You can test nearly anything...
- the fitting of theoretical distributions, outlier values, associations between variables
- and yes... correlations
- test: the population correlation ($\rho$) differs from zero ($H_0: \rho = 0$)
- low $p$-value indicate that the correlation is statistically significant
- high correlation coefficients can have low $p$-values
- low sample sizes, high variability create uncertainty
- similarly, small correlations can be statistically significant (interesting!)
- takeaway: always collect the $p$-value in addition to the coefficient!

- In a nutshell:
- testing offers ground to place decisions (e.g. statements in article should always be significant)
- yet do it with care: results depend on sample size and assumptions, evidence ≠ truth

 

# More on descriptive statistics…

For other ends:

- Testing **differences** between two samples
- differences of category proportions of categories
- differences means and variability
- Estimating **minimum data size** for a descriptive or predictive task based on its difficulty
- Inferring **uncertainty bounds** (e.g. confidence intervals)
- Assessing whether the **superiority** of a given method yields statistical significance
- ...

⇒ check the notebook on Descriptive Statistics!

 

# Putting all into practice…

Check the notebook on descriptive statistics to tackle the following challenges:

- describe the **jokes** dataset, including the distribution jokes' length and sentiment-based features
- what is the likelihood of a joke to have negative valence (polarity)?
- are the rating of jokes correlated with length- and sentiment-based features?
- is there a correlation between subjectivity and polarity features?
- does joke length significantly differ for positive, neutral and negative jokes?

- consider funny jokes to have rates above 6 (≥7).
- are hilarity (funny or not) and valence sign (positive, neutral, negative) associated?
- does joke subjectivity discriminate hilarity? And valence sign?

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

 

# Classical multivariate statistics

How to account for the associative aspects (dependencies) between multiple variables?

- **unsupervised setting**: we will delve into classical multivariate statistics throughout our module
- multi-wise associations between input variables
- they will be our baseline solutions to mine clusters, patterns, anomalies...
- **supervised setting**: recall the content of other DASH modules
- starting point: linear, ordinal, logistic regression for predictive tasks
- numeric, ordinal and nominal outputs, respectively
- way of assessing the relevance of each input variable given a set covariates (e.g. confounding factors)

 

# Classical multivariate statistics

Supervised settings are informative for descriptive ends

- pervasive in scientific practice
- linear, ordinal, logistic regression models are inherently **interpretable**

$$
\hat {z} = \beta_ {0} + \beta_ {1} x _ {1} + \dots + \beta_ {m} x _ {m} + \varepsilon
$$

- coefficients indicate change (in log-odds for logistic regression) in the target when holding other inputs constant
- coefficients can be tested to assess predictive significance
- low $p$-value under F-test for linear regression or likelihood ratios for logistic/ordinal regression
- challenges: linearity, independence and normality of errors... limited efficacy
- check $R^2$ on training observations to assess proportion of variance explained
- assess residue-based scores or classification-based scores on testing observations

 

# Outline

- Descriptive statistics vs machine learning
- Univariate statistics
- probability distributions and summary statistics
- preprocessing procedures
- Bivariate statistics
- Hypothesis testing
- Multivariate statistics

 

Rui Henriques

---

## Lecture 3: Clustering (1/2)

*Source: 03a Clustering Part1*

---
# Clustering (1/2)

Introduction to clustering

# Outline

- Introduction to clustering
- Multivariate similarity metrics
- Approaches
- hierarchical
- density-based
- From multivariate to complex data structures
- Evaluation
- intrinsic metrics
- extrinsic metrics

 

# Clustering

Cluster: group of observations

Cluster analysis: group observations into clusters according to their (dis)similarity: observations in the same cluster are more similar than those in different clusters

# Motivation

- Patients with a shared clinical condition: How to understand disease?
- cancer types, dementia progression, risk groups
- stratified diagnostics and therapeutics

- Customers: how to segment their profile for personalized marketing?
- Webpages, shopping products, media, documents: how to categorize them for recommendations?
- Genes, proteins and metabolites with different expression and concentration profile: how to understand their correlated behavior (biological functions)?
- Students, researchers, professors: how to improve science and education?

# Motivation

## ENDS
- Insight into the underlying structure/regularities of data
- Preprocessing step for other tasks
- Supporting prediction by stratifying populations (exercise: how?)
- Improving efficiency by using clusters as a proxy for observations
- Many others...

## Application DOMAINS
- Information retrieval: document and webpage clustering
- Marketing: customer groups according to profile and product-receptivity
- Insurance: policy holders with different average claim costs
- Medicine: risk groups, personalized medicine
- Biology: philogenetics, pathways, regulatory modules
- Others: city-planning, land use, seismic studies, atmospheric conditions

# Illustration

# Clustering modes

- Unsupervised (default)
- cluster observations without knowing their labels

- Semi-supervised
- cluster observations when:
- the labels of some observations may be known or
- pairs of observations are known to belong to the same cluster

- Supervised
- cluster observations when targets are considered, e.g.:
- label added as an additional input variable
- cluster class-conditional observations

# Clustering modes

- Deterministic versus probabilistic cluster stances
- **hard** solutions: each observation either belongs or not to a given cluster
- **soft** solutions: each observation has a probability (membership) of belonging to a given cluster
- fuzzy and model-based clustering
- Separation of clusters: **exclusive** versus **non-exclusive** (overlapping clusters)
- **Complete** versus **partial** (observations may not belong to any cluster)
- Uniform versus weighted
- variables can be weighted based on data semantics/domain knowledge
- observations can be weighted based on relevance criteria

 

# Motivation

Two major factors impact solutions: **distance** + **approach**

- **distance metrics** depend on the:
- variable domains
- numeric and ordinal (e.g. Euclidean)
- nominal (e.g. Hamming)
- non-iid attributes
- data structure: tabular, time series, image, spatiotemporal data, events...
- approach
- partitioning
- hierarchical
- density-based
- model-based

# Outline

- Introduction to clustering
- Multivariate similarity metrics
- Approaches
- hierarchical
- density-based
- From multivariate to complex data structures
- Evaluation
- intrinsic metrics
- extrinsic metrics

 

# Focal point: distances

- well-established distances can be applied yet...
...best distances are generally **customized** to the problem domain (background knowledge)

$$
\text{e.g. demographic dist}(ind_1, ind_2) = \frac{age_1 - age_2}{20} + 1[region_1 = region_2] \times 0.8 + 1[sex_1 = sex_2] \times 1.2 + \cdots
$$

- apply distance to produce pairwise **distance matrices** between observations (and/or clusters)
- similarity matrix = − distance matrix

|   | A | B | C | D | E | F  |
| --- | --- | --- | --- | --- | --- | --- |
|  A | 0 | 0.71 | 5.66 | 3.61 | 4.24 | 3.20  |
|  B | 0.71 | 0 | 4.95 | 2.92 | 3.54 | 2.50  |
|  C | 5.66 | 4.95 | 0 | 2.24 | 1.41 | 2.50  |
|  D | 3.61 | 2.92 | 2.24 | 0 | 1.00 | 0.50  |
|  E | 4.24 | 3.54 | 1.41 | 1.00 | 0 | 1.12  |
|  F | 3.20 | 2.50 | 2.50 | 0.50 | 1.12 | 0  |

# Clustering as a graph-based task

- Proximity between all data observations defines a weighted graph
- Nodes are the observations, edges capture their distances
- Clustering = breaking the graph into connected components
- Minimize the edge weight between clusters AND maximize the edge weight within clusters
- How? Incremental grouping using thresholds

|   | A | B | C | D | E  |
| --- | --- | --- | --- | --- | --- |
|  A | 0 | 1 | 2 | 2 | 3  |
|  B | 1 | 0 | 2 | 4 | 3  |
|  C | 2 | 2 | 0 | 1 | 5  |
|  D | 2 | 4 | 1 | 0 | 3  |
|  E | 3 | 3 | 5 | 3 | 0  |

# Distances and metrics

A distance function is a metric if the following conditions are met:

- non-negative
$$
d(x, y) \geq 0
$$

- distance to point itself is zero
$$
d(x, x) = 0
$$

- symmetry
$$
d(x, y) = d(y, x)
$$

- triangular inequality
$$
d(x, y) \leq d(x, z) + d(z, y)
$$

# Common distance metrics (numeric data)

## Minkowski distance

$$
d(i,j) = \sqrt[4]{\underbrace{|a_{i1} - a_{j1}|^q}_{1^{\text{st} \text{ dimension}}} + \underbrace{|a_{i2} - a_{j2}|^q}_{2^{\text{nd} \text{ dimension}}} + \dots + \underbrace{|a_{ip} - a_{jp}|^q}_{p^{\text{th} \text{ dimension}}}
$$

## Euclidean distance $(q = 2)$

$$
d(i,j) = \sqrt{ \left| a_{i1} - a_{j1} \right|^2 + \left| a_{i2} - a_{j2} \right|^2 + \dots + \left| a_{ip} - a_{jp} \right|^2 } \quad \text{(Note: } \text{where } \text{a}_{i1} = (a_{i1}, a_{i2}, \dots, a_{ip}) \text{ } \text{)}.
$$

## Manhattan distance $(q = 1)$

$$
d(i,j) = \left| a_{i1} - a_{j1} \right| + \left| a_{i2} - a_{j2} \right| + \dots + \left| a_{ip} - a_{jp} \right|
$$

# Common distance metrics

(numeric data)

2D example

$$
x _ {1} = (2, 8)
$$

$$
x _ {2} = (6, 3)
$$

Euclidean distance

$$
d (1, 2) = \sqrt {\left| 2 - 6 \right| ^ {2} + \left| 8 - 3 \right| ^ {2}} = \sqrt {4 1}
$$

Manhattan distance

$$
d (1, 2) = | 2 - 6 | + | 8 - 3 | = 9
$$

# Chebyshev distance
(numeric data)

- when $q \to \infty$, the metric highly penalizes maximum attribute errors
- useful if the worst case must be avoided:

$$
d_{\infty}(\mathbf{x}, \mathbf{y}) = \lim_{q \to \infty} \left( \sum_{i=1}^{n} |x_i - y_i|^q \right)^{1/q} = \max(|x_1 - y_1|, |x_2 - y_2|, \dots, |x_n - y_n|)
$$

Example:

$$
d_{\infty}((2,8), (6,3)) = \max(|2 - 6|, |8 - 3|) = \max(4,5) = 5
$$

# Correlation

- positive (negative): two variables vary in the same (opposite) way
- maximum value of 1 (-1) if X and Y are perfectly direct (inverse) correlated
- recall: Pearson and Spearman coefficients for numeric data
- how to handle categorical or mixed data?
- example: gene expression data clustering

$$
\begin{array}{l}
g1 = (1,2,3,4,5) \\
g2 = (100,200,300,400,500) \\
g3 = (5,4,3,2,1) \\
\end{array}
$$

Which genes are similar according to correlation coefficients?

# Hamming distance

(binary and categorical data)

- number of different attribute values
- distance of (1011101) and (1001001) is 2
- distance between (toned) and (roses) is 3

3-bit binary cube

100-&gt;011 has distance 3 (red path)
010-&gt;111 has distance 2 (blue path)

# Outline

- Introduction to clustering
- Multivariate similarity metrics
- Approaches
- hierarchical
- density-based
- From multivariate to complex data structures
- Evaluation
- intrinsic metrics
- extrinsic metrics

 

# Approaches

## Partitioning:
- Create partitions and iteratively update them (e.g. $k$-means, $k$-modes, $k$-medoids)

## Hierarchical:
- Create hierarchical decomposition of data points (e.g. Diana, Agnes)

## Density-based:
- Group points based on connectivity and density (e.g. DBSACN, DenClue)

## Model-based:
- Data are seen as a mixture of distributions (e.g. EM)

# Hierarchical clustering

FORMÁÇÃO AVANÇADA

# Hierarchical clustering

- Agglomerative (bottom-up)
- initialize each point as its own cluster
- iteratively merge clusters
- Divisive (top-down)
- initialize all data points into one cluster
- large clusters are successively divided

 

# Hierarchical clustering

The number of dendrograms with $n$ leafs $= (2n - 3)! / [(2^{(n - 2)}) (n - 2)!]$

|  Number of Leafs | Number of Possible Dendrograms  |
| --- | --- |
|  2 | 1  |
|  3 | 3  |
|  4 | 15  |
|  5 | 105  |
|  ... | ...  |
|  10 | 34,459,425  |

cannot test all possible trees
$\Rightarrow$ heuristic searches

# Cluster distance

- Single link: smallest distance between observations
- Complete link: largest distance between observations
- Average link: average distance between observations

$$
d(c_i, c_j) = \frac{1}{|c_i||c_j|} \sum_{x_i \in C_i} \sum_{x_j \in C_j} d(x_i, x_j)
$$

- Centroid link: distance between centroids
- Ward's distance: similarity based on the error increase when two clusters are merged (sum of squared distances of points to closest centroid)

# Cluster distance

- MIN (single link)
- MAX (complete link)
- Average link
- Centroid link
- Ward's method

similarity matrix

# Cluster distance

- MIN (single link)
- MAX (complete link)
- Average link
- Centroid link
- Ward's method

similarity matrix

# Cluster distance

- MIN (single link)
- MAX (complete link)
- Average link
- Centroid link
- Ward's method

similarity matrix

# Cluster distance

- MIN (single link)
- MAX (complete link)
- Average link
- Centroid link
- Ward's method

similarity matrix

# Cluster distance

- MIN (single link)
- MAX (complete link)
- Average link
- Centroid link
- Ward's method

similarity matrix

# Hierarchical clustering

- We begin with a distance matrix which contains the distances between every pair of objects in our database

$$
d(\text{} = 8
$$

$$
d(\text{} = 1
$$

|  0 | 8 | 8 | 7 | 7  |
| --- | --- | --- | --- | --- |
|   | 0 | 2 | 4 | 4  |
|   |  | 0 | 3 | 3  |
|   |  |  | 0 | 1  |
|   |  |  |  | 0  |

# Hierarchical clustering

Bottom-up (agglomerative): Starting with each point as a cluster, find best pair. Repeat until all clusters are fused

Consider all possible merges...

Choose the best

# Hierarchical clustering

Bottom-up (agglomerative): Starting with each point as a cluster, find best pair. Repeat until all clusters are fused

# Hierarchical clustering

Bottom-up (agglomerative)

Consider all possible merges...

Choose the best

Choose the best

Consider all possible merges...

Choose the best

Choose the best

Consider all possible merges...

Choose the best

CO
FORMAÇÃO ALGÃO

# MIN: strengths and limitations

- Can handle non-elliptical shapes

original points

clusters

- Overlapping clusters and noise

original points

clusters

C FORMAÇÃO

# MAX: strengths and limitations

- Less susceptible to noise and outliers

original points

clusters

- Tends to break large clusters
- Biased towards globular clusters

original points

clusters

# Hierarchical clustering: comparison

- problems MIN and MAX link can be minimized under average/centroid/Ward link
- strength: less susceptible to noise and outliers
- limitation: biases towards globular clusters

# DBSCAN (density-based clustering)

- clusters are defined as areas of higher density
- separation occurs in sparse areas
- isolated data points here seen as outliers
- advantages? limitations?

# DBSCAN (density-based clustering)

- parameters
- $\varepsilon$ maximum distance
- $p$ minimum neighbors

- algorithm
- for each point:
- cluster points with $p$
- neighbors at $&lt; \varepsilon$ distance

# Outline

- Introduction to clustering
- Multivariate similarity metrics
- Approaches
- hierarchical
- density-based
- From multivariate to complex data structures
- Evaluation
- intrinsic metrics
- extrinsic metrics

 

# Time series data

- Time series: sequence of values or symbols along time $\mathbf{s} = \langle \mathbf{x}_1, \ldots, \mathbf{x}_T \rangle$
- univariate or multivariate, $\mathbf{x}_j \in \mathbb{R}^m$ (or $\mathbf{x}_j \in \{Y_1 \ldots Y_m\}$), where $m$ is the multivariate order
- Time series data: $\{\mathbf{s}_1, \ldots, \mathbf{s}_n\}$ where $\mathbf{s}_i$ is a time series
- Time series are ubiquitous: monitoring biological, individual, organizational, geophysical, digital, mechanical, societal systems
- Movement, image and video as time series, text data as time series
- People measure things...
- their blood pressure
- the annual rainfall in New Zealand
- the value of their Yahoo stock
- the number of web hits per second
... and things change over time

# Time series clustering

Dynamic Time Warping Matching

Euclidean Matching

# Text document clustering

- Group related documents based on their content
- the similarity between every string pair is calculated as a basis for determining the clusters
- considering term vector spaces... cosine

- A similarity measure is required to calculate the similarity between two strings

approximate string matching

semantic similarity stem, feature extraction and lexical analysis

# GPS trajectory clustering

# Spatial clustering

# Image and video clustering

Image: Gansbeke et al.

Boxing

Clapping

Waving

Walking

Jogging

Running

# Representation learning (next class)

These and many other complex data structures may be encountered
- video, events, tensors, heterogeneous data structures...

Two major solutions
- dedicated distances or clustering approaches
- obtain (numeric) representations of these complex observations by extracting features
- features can be extracted using simple statistics
- e.g. extract centrality/variability/slope/max/min statistics on time series using sliding windows
- embeddings can be extracted using representation learning
- example: auto-encoder neural networks can be applied to deal with arbitrary complex inputs

# Outline

- Introduction to clustering
- Multivariate similarity metrics
- Approaches
- hierarchical
- density-based
- From multivariate to complex data structures
- Evaluation
- intrinsic metrics
- extrinsic metrics

 

# Evaluation: clustering quality

- 3 kinds of measures: external, internal and relative indexes
- External (supervised): extent to which cluster labels match true labels
- requires prior or expert knowledge
- Internal (unsupervised): goodness without external information
- how well they are separated (e.g. silhouette)
- should be independent from algorithm-specific functions (unbiased)
- Relative: compare different cluster analyses (different parameters/algorithms)

 

# Internal measures: cohesion and separation

Proximity graph-based approach to measure cohesion and separation

- Cohesion is the sum of the weight of all links within a cluster
- Separation is the sum of the weights between nodes in the cluster and nodes outside the cluster

cohesion

separation

# Internal measures: cohesion and separation

- Cohesion (e.g. sum of squared errors or sum of square within):
how closely related are points in a cluster
$$
SSE = SSW = \sum_{k=1}^{K} \sum_{x_i \in C_k} d(x_i, c_k)^2
$$

- Separation (e.g. sum of squares between clusters)
how distinct or well-separated a cluster is from other clusters
$$
SSB = BSS = \sum_{k} |c_k| d(c_k, \hat{x})^2
$$

- Total error (e.g. sum of squares): within and between errors
$$
TSS = SSB + SSE
$$
$$
TSS = \sum_{i}^{n} d(x_i, \hat{x})^2
$$

# Internal measures: cohesion and separation

SSB + SSE = constant

K=1 cluster:
$$
SSE = (1 - 3)^2 + (2 - 3)^2 + (4 - 3)^2 + (5 - 3)^2 = 10
$$
$$
SSB = 4 \times (3 - 3)^2 = 0
$$
$$
Total = 10 + 0 = 10
$$

K=2 clusters:
$$
SSE = (1 - 1.5)^2 + (2 - 1.5)^2 + (4 - 4.5)^2 + (5 - 4.5)^2 = 1
$$
$$
SSB = 2 \times (3 - 1.5)^2 + 2 \times (4.5 - 3)^2 = 9
$$
$$
Total = 1 + 9 = 10
$$

# Internal measures: cohesion

- For each observation, the error is the distance to the nearest cluster
- Square these errors (to penalize larger distances) and sum these errors

$$
SSE = \sum_{k=1}^{K} \sum_{x_i \in C_k} d(x_i, c_k)^2
$$

- Good to compare two clustering solutions or two clusters
- Can also be used to estimate the number of clusters

# Internal measures: cohesion

Challenge on finding optimal #clusters:
- an easy way to reduce SSE is to increase the #clusters
- solution: elbow method (next class)

# Internal measures: silhouette coefficient

- Combine ideas of both cohesion and separation
- Calculated for a specific object $\mathbf{x}_i$
- $a =$ average distance of $\mathbf{x}_i$ to the points in its cluster
- $b = \min$ (average distance of $\mathbf{x}_i$ to points in another cluster)
- the silhouette coefficient for a point is then given by

$$
s = 1 - a / b \quad \text{if } a &lt; b, \quad \text{(or } s = b / a - 1 \text{ if } a \geq b, \text{ not the usual case)}
$$

between $-1$ and $1$ (the closer to 1 the better)

- Silhouette of cluster and clustering solution: average of silhouettes

# Internal measures: silhouette coefficient

# Internal measures: similarity matrix

- Order the similarity matrix with respect to cluster labels and inspect visually

# Internal measures: similarity matrix

- Clusters in random data are not well-defined

# Recall: clustering evaluation

- 3 kinds of measures: external, internal and relative indexes
- External (supervised): extent to which cluster labels match true labels
- requires prior or expert knowledge
- Internal (unsupervised): goodness without external information
- how well they are separated (e.g. silhouette)
- should be independent from algorithm-specific functions (unbiased)
- Relative: compare different cluster analyses (different parameters/algorithms)

 

# External measures: purity

- $\Omega = \{\omega_1, \omega_2, \dots, \omega_K\}$ is the set of clusters
$C = \{c_1, c_2, \dots, c_J\}$ is the set of classes
- For each cluster $\omega_k$: find class $c_j$ with most objects in $\omega_k$, $n_{kj}$
- Sum all $n_{kj}$ and divide by total number of points

$$
\operatorname{purity}(\Omega, C) = \frac{1}{n} \sum_{k} \max_{j} |\omega_k \cap c_j|
$$

- **Problem**: biased ⇒ n clusters maximizes purity
- Alternatives: entropy of classes in clusters

# External measures: purity

cluster I

cluster II

cluster III

cluster I: purity = 1/6 (max(5, 1, 0)) = 5/6
cluster II: purity = 1/6 (max(1, 4, 1)) = 4/6
cluster III: purity = 1/5 (max(2, 0, 3)) = 3/5
solution: purity = 1/17 (5+4+3) = 12/17

# External measures: rand index

- Counts of object pairs

|  same class
different classes | same cluster | different clusters  |
| --- | --- | --- |
|   |  true positives (TP) | false negatives (FN)  |
|   |  false positives (FP) | true negatives (TN)  |

- Rand index  $\mathrm{RI} = \frac{TP + TN}{TP + FP + FN + TN}$

- Given a specific cluster (positive):
- precision = TP/(TP+FP)
- recall = TP/(TP+FN)
- F-measure = 2×precision×recall / (precision + recall)

# External measures: rand index

Rand index?

|  Number of object pairs | Same cluster | Different clusters  |
| --- | --- | --- |
|  Same class in ground truth | 20 | 24  |
|  Different classes in ground truth | 20 | 72  |

Rui Henriques

---

## Lecture 4: Clustering (2/2)

*Source: 03b Clustering Part2*

---
# Clustering (2/2)

Clustering: advanced aspects

# Outline

- Distances: advanced notes
- Clustering approaches
- $k$-means
- model-based (EM)
- deep learning
- Evaluation recap
- Advanced aspects

 

# Outline

- Distances: advanced notes
- Clustering approaches
- $k$-means
- model-based (EM)
- deep learning
- Evaluation recap
- Advanced aspects

 

# Recall: clustering

Cluster: group of observations

Cluster analysis: group observations into clusters according to their (dis)similarity: observations in the same cluster are more similar than those in different clusters

Main ingredients for clustering: distance + approach

# Clustering: distance and approach

Distance metrics depend on the:

- type of input variables:
- numeric distances, e.g. Euclidean, $d(\mathbf{a}, \mathbf{b}) = \sqrt{\sum_{j=1}^{m} (a_j - b_j)^2}$
- nominal distances, e.g. Hamming
- ordinal encodings, how?
- non-iid attributes, how?

- data structures
- (multivariate) time series
- image
- text
- others: spatiotemporal, events, relational...

# Categorical features

How do we represent categorical features in a multivariate space?

- Let us start with **binary variables** (e.g. gender)
- a binary feature can be mapped into one axis in a $m$-dimensional space where values are constrained to 0 or 1

- **Ordinal variables** (e.g. high-moderate-low)
- we can find a numeric encoding $f$ for an ordinal variable
- e.g. $f(high) = 5$, $f(moderate) = 1$, $f(low) = 0$
- in the absence of an encoding, one can assume equally spaced integers (e.g. 0, 1, 2...). Problems?

- Let us finally consider **nominal variables** with cardinality higher than 2 (e.g. Europe, Africa, America)
- challenge? As there is no order, we cannot position values along a single axis/dimension
- solution? Create $p$ axes for a nominal variable with cardinality $p$
- only one of the $p$ axes is active (1), while remaining are inactive (0)
- this operation is called **dummification**
- some machine learning methods depend on dummification

# Mixed data

- A data space can be composed by **non-iid numeric variables**
- i.i.d. stands for **independent** and **identically distributed**
- two numeric variables may be correlated, i.e. not independent
- two numeric variables may have distinct distributions (e.g. $U(0,100)$ and $N(3,5)$), i.e. non-identically distributed

- Observations can have numeric, nominal and ordinal features
- we informally term such data as **mixed data**
- examples?

# Distances for mixed data

- First concern: two non-identically distributed variables – e.g. $Y_{1} \sim U(0,1)$ and $Y_{2} \sim U(0,100)$
- Problem? In the given example, distances are most affected by variable $Y_{2}$
- yet why should this variable have higher weight than $Y_{1}$!
- Possible solution? Normalize variables
- in the given example, $Y_{2} \sim U'(0,1)$ using for instance min-max scaling
- Second concern: how to deal with simultaneous categoric and numeric variables?
- distance can be a composition: $d(\mathbf{x}_1, \mathbf{x}_2) = \alpha d_{\text{numeric}}(\mathbf{x}_1, \mathbf{x}_2) + \beta d_{\text{categoric}}(\mathbf{x}_1, \mathbf{x}_2)$ where $\alpha$ and $\beta$ are parameters that reveal the relevance of each component, generally $\alpha + \beta = 1$
- parameters can be fixed based on the number of variables or available domain knowledge

# Handling complex data structures

Two major paradigms

- dedicated distances for series/image/text/events (see previous class!)
- feature extraction to map complex data structures into tabular data
- manual extraction often incomplete and error-prone
- automated extraction susceptible to diverse idiosyncrasies
- examples: statistics on a sliding window for time series, structure–texture–color cues for images, term frequencies for text, geometric features for trajectories...
- problem: feature extraction and subsequent engineering entail 90% of overall ML effort!
- solution: learn representations
- "A good representation is one that makes subsequent learning task easier" Goodfellow et al. 2016 (including clustering!)

 

# Numeric encodings of complex data

- A good representation is:
- compact (minimal)
- explanatory (sufficient)
- disentangled (independent factors)
- informative (make subsequent problem solving easier)

- How to learn numeric representations from complex data?
- neural networks $\Rightarrow$ check our class on representation learning!

- Implications?
- classic distances can be applied
- yet given the above properties: cosine distance recommended

# Distances vs correlation

- Consider the scenario where you have three documents (observations): $d_{1}, d_{2}$ and $d_{3}$
- each document is characterized by the frequency of terms in the text (features)
- Now consider we enter a query $q$ to retrieve documents similar to $q$
- Euclidean distance is... a bad idea as it is large for vectors of different lengths
- the Euclidean distance between $q$ and $d_{2}$ is large even though the distribution of terms in the query $q$ and $d_{2}$ are very similar

# Vector norm

The normalization of an observation, should not be mislead with variable normalization

- variable normalization guarantees that the measurements of a given variable yield statistical properties of interest, e.g. [0,1] or N(0,1)

# From angles to cosines

- the following two notions are equivalent:
- distance of the angle between two vectors
- similarity of the cosine between two vectors
- cosine is a monotonically decreasing function for the interval $[0^{\circ}, 180^{\circ}]$

# Cosine similarity

$$
\cos (\mathbf {x} _ {1}, \mathbf {x} _ {2}) = \frac {\mathbf {x} _ {1} \cdot \mathbf {x} _ {2}}{\| \mathbf {x} _ {1} \| \| \mathbf {x} _ {2} \|} = \frac {\sum_ {i} x _ {1 i} x _ {2 i}}{\sqrt {\sum_ {i} x _ {1 i} {} ^ {2}} \sqrt {\sum_ {i} x _ {2 i} {} ^ {2}}}
$$

- $x_{1i}$ is the feature from variable $y_{i}$ in observation $\mathbf{x}_{1}$
- $\| \mathbf{x}_1\|$ and $\| \mathbf{x}_2\|$ are 2-norm lengths of vectors $\mathbf{x}_1$ and $\mathbf{x}_2$
- $\cos (\mathbf{x}_1,\mathbf{x}_2)$ is the (cosine) similarity of $\mathbf{x}_1$ and $\mathbf{x}_2$

RICH

For length-normalized vectors, cosine similarity is simply the dot product (or scalar product):

$$
\cos (\mathbf {x} _ {1}, \mathbf {x} _ {2}) = \mathbf {x} _ {1} \cdot \mathbf {x} _ {2} = \sum_ {i = 1} ^ {m} x _ {1 i} x _ {2 i}
$$

# Cosine similarity

Euclidean distance

$$
l _ {2} \left(\mathbf {x} _ {1}, \mathbf {x} _ {2}\right) = \sqrt {\left| 2 - 6 \right| ^ {2} + \left| 8 - 3 \right| ^ {2}} = \sqrt {4 1}
$$

Manhattan distance

$$
l _ {1} \left(\mathbf {x} _ {1}, \mathbf {x} _ {2}\right) = | 2 - 6 | + | 8 - 3 | = 9
$$

Cosine similarity

$$
\cos (\mathbf {x} _ {1}, \mathbf {x} _ {2}) = \frac {\mathbf {x} _ {1} \cdot \mathbf {x} _ {2}}{\| \mathbf {x} _ {1} \| \| \mathbf {x} _ {2} \|} = \frac {2 \times 6 + 8 \times 3}{\sqrt {2 ^ {2} + 8 ^ {2}} \sqrt {6 ^ {2} + 3 ^ {2}}} = 0.65
$$

# Distances in clustering

- Distances (or similarities) applied between:
- two observations $d(\mathbf{x}_i, \mathbf{x}_j)$
- one observation and a cluster $d(\mathbf{x}_i, \mathbf{c}_j)$
- two clusters $d(\mathbf{c}_i, \mathbf{c}_j)$

- **Cluster**: $\mathbf{c}_j = \{\mathbf{x} \mid d(\mathbf{x}, \mathbf{c}_j) = \min_i d(\mathbf{x}, \mathbf{c}_i)\}$

- **Centroid** of a cluster as its mass center: $\bar{\mathbf{c}}_j$ (e.g., mean/mode value per real/categorical variable)

- Squared **error** of clustering solution: $E = \sum_{k=1}^{K} \sum_{\mathbf{x} \in \mathbf{c}_k} d(\mathbf{x}, \bar{\mathbf{c}}_k)^2$

# Outline

- Distances: advanced notes
- Clustering approaches
- $k$-means
- model-based (EM)
- deep learning
- Evaluation recap
- Advanced aspects

 

# Approaches

## Partitioning $\Leftarrow$
- Create partitions and iteratively update them (e.g. $k$-means, $k$-modes, $k$-medoids)

## Hierarchical
- Create hierarchical decomposition of data points

## Density-based
- Group points based on connectivity and density functions

## Model-based $\Leftarrow$
- Data are seen as a mixture of distributions (e.g. EM)

## Deep learning $\Leftarrow$
- End-to-end neural networks for high-efficacy clustering

 

# Partitioning algorithms

Given $k$ clusters:

1. partition observations into $k$ non-empty subsets
2. compute the centroid $c_{j}$ of each subset
- centroid is the center of mass: e.g. mean or median centers
3. reassign each observation to the cluster with the nearest centroid
4. goto step 2, stop when:
i) assignment does not change, ii) $|E^{new} - E^{old}| &lt; \varepsilon$, or iii) max iterations is reached

## Variants

- centroid calculus
- selection of the initial seeds
- adjustments for **batches** of observations (instead of all) for very large datasets

# $k$-means

# k-medoids

- numeric data: centroid as the mean or median
- categoric data: centroid as the mode – $k$-modes [Huang'98]
- frequency-based procedure to update modes of clusters
- mixed data: centroid combining mean and modes ($k$-prototype)
- $k$-medoids: the most centrally located observation in a cluster is the centroid
- observation with minimum average distance to all observations in the cluster
- What is the algorithm most robust to outliers: $k$-means or $k$-medoids?

# $k$-means: challenges

- Efficiency: $O(tkn)$ $n = \# \text{observation}$, $k = \# \text{clusters}$, $t = \# \text{iterations}$, usually $k, t \ll n$
- Problems
- dependent on initialization
- sensitive to outliers
- sensitive noisy data
- noise can substantially distort centroids
- not suitable to discover clusters with non-convex shapes
- deal only with clusters with spherical symmetrical point distribution
- need to specify $k$, the number of clusters, in advance
- convergence?

 

# Limitations of $k$-means

Different sizes

Different densities

# Limitations of $k$-means

Non-globular shapes

Original Points

K-means (2 Clusters)

Fixed number of clusters

Original Points

K-means Clusters

# Overcoming $k$-means limitations

# Model-based vs partitioning approaches

- $k$-means algorithm performs a **hard assignment** of data points to clusters, in which each data point is associated uniquely with one cluster
- in $k$-means the shape of the cluster is described by Euclidean distance function
- Model-based clustering makes a **soft assignment** based on the posterior probabilities
- Expectation Maximization (EM) is the paradigmatic algorithm

k-Means Clustering

EM Clustering

# EM: example

# EM: principles

- Fix the number of clusters, assume each cluster follows a specific distribution
- multivariate Gaussian mixture for numeric variables
- frequentist view for discrete variables
- joint probabilities under independence assumption for mixed data

- EM algorithm
- Iterate between two steps until convergence
- Expectation step: assign observations to clusters
- Maximation step: update the model parameters (adjust distributions)

# EM and soft clustering

- each observation has a likelihood of being generate by every cluster, $p(\mathbf{x}|c)$
- can be assigned to the cluster with higher likelihood, $\argmax_c p(c|\mathbf{x})$
- can be assigned to more than one cluster (if both satisfy minimum likelihood) or none
- tackles major problems of density-based approaches (e.g. DBSCAN cannot partition data below)

# Deep learning approaches

- Check our presentation on representation learning to recover the foundations!
- Two major paradigms

1. learn good representations from data (whether simple or complex data structures) using deep learning followed by classic clustering stances (e.g. $k$-means)

- addresses data idiosyncrasies (e.g., non-iid variables)

2. apply emerging end-to-end deep learning pipelines for clustering

# Outline

- Distances: advanced notes
- Clustering approaches
- $k$-means
- model-based (EM)
- deep learning
- Evaluation recap
- Advanced aspects

 

# Recall: clustering evaluation

- 3 kinds of measures: external, internal and relative indexes
- External (supervised): extent to which cluster labels match true labels
- requires prior or expert knowledge
- Internal (unsupervised): goodness without external information
- how well they are separated (e.g. silhouette)
- should be independent from algorithm-specific functions (unbiased)
- Relative: compare different cluster analyses (different parameters/algorithms)

 

# Statistical significance

- Why? need to robustly interpret measure
- if our measure of evaluation has the value, 10, is that good, fair, or poor? ⇒ p-value

- How? Compare the values of an index that result from a randomized dataset against the index values from the target cluster analysis
- If the value of the index is unlikely, then results are significant

- To test superiority between two clustering solutions, simpler statistical tests can be considered

- Interesting fact: the more "atypical" a clustering result is, the more likely it represents valid structure in the data

 

# Statistical significance

- Compare SSE of 0.005 against SSE of clusters in 500 sets of random data points of size 100 (histogram)

# Statistical significance

- Are correlations of -0.92 and -0.58 statistically significant?
- Histogram shows correlation on randomized data with K-means

Corr = -0.9235

Corr = -0.5810

# Outline

- Distances: advanced notes
- Clustering approaches
- $k$-means
- model-based (EM)
- deep learning
- Evaluation recap
- Advanced aspects

 

# Recall: clustering modes

- memberships: **hard** (observation belongs to a single cluster) versus **soft** (each observation has a probability of belonging to each cluster – e.g. fuzzy, model-based clustering)
- supervision
- **unsupervised** (default): cluster observations without knowing their outcome variable
- **semi-supervised**: cluster observations when labels of some observations may be known or pairs of observations are known to belong to the same cluster
- “supervised”: cluster observations in the presence of variables of interest (e.g. targets as inputs, class-conditional clustering)
- separation of clusters: **exclusive** versus **non-exclusive** (overlapping clusters)
- **complete** versus **partial** (cluster some objects)
- uniform versus **weighted attributes** or observations

# Visualizing clustering solutions

Key principles for knowledge discovery (to be mastered during our course!)

- Compute the variables that are better separated by the clusters
- add a cluster's column to the dataset and run ANOVA (f-classif in sklearn) to assess the discriminative power of each input variable (use p-values to rank them by importance)
- Retrieve the centroids
- Compute the cluster-conditional distributions for the most important features
- Retrieve observation memberships/distances to each cluster/centroid
- Visualize clustering solutions in a 2D or 3D space
- select specific features of interest (importance or domain knowledge)
- project the original m-dimensional space into a 2D or 3D space using uMAP, PCA, tSNE

 

# Visualizing clustering solutions

Key principles for knowledge discovery (to be mastered during our course!)

- Retrieve the **centroids** and/or **medoids**
- Compute the **cluster-conditional distributions** for the most relevant variables

$y_{7}$   $y_{12}$

··· ···

- Retrieve **observation memberships/distances** to each cluster/centroid

# Visualizing clustering solutions

Key principles for knowledge discovery (to be mastered during our course!)

- Most informative variables? The ones that were better separated by the clusters
- add a column with clusters to the dataset
- run ANOVA (f-classif in sklearn) to assess the discriminative power of each input variable
- use p-values to rank variables by importance

- Visualize clustering solutions in a 2D or 3D space
- select specific features of interest (importance or domain knowledge)
- project the original m-dimensional space into a 2D or 3D space using uMAP, PCA, tSNE

# Importance of seeding initial centroids

# Importance of seeding initial centroids

- If there are $k$ real clusters...
- ... chance of selecting one centroid from each cluster is small when $k$ is large
- e.g. if $k = 10$, then probability = $10! / 10^10 = 0.00036$

- **Difficulty**: sometimes centroids readjust in 'right' way, sometimes don't

- **Solution**
- multiple runs (helps, but probability is not on your side)
- hierarchical clustering to determine initial centroids
- select more than $k$ initial centroids and then select among these initial centroids (select most widely separated)
- postprocessing

 

# Number of clusters?

How many clusters?

Six Clusters

Two Clusters

Four Clusters

# Number of clusters?

k = 1: cohesion (SSE) is 873.0

k = 2: cohesion (SSE) is 173.1

k = 3: cohesion (SSE) is 133.6

# Number of clusters?

## Knee/elbow method:
- plot the SSE for different $k$
- find the elbow. Example: abrupt changes (k=2) are highly suggestive of two clusters in the data

## Other methods
- plot metrics less sensitive to the #clusters (e.g., silhouette)
- find the k with maximum value or higher neighborhood average centered on k

# Pre- and post-processing

## Pre-processing
- normalize data
- data reduction and transformation
- remove outliers

## Post-processing
- eliminate small clusters that may represent outliers
- split 'loose' clusters (clusters with relatively high SSE)
- merge clusters that are 'close' (clusters with relatively low SSE)
- these steps can be integrated within the clustering process

 

# Requirements

- clustering quality
- ability to deal with different data types
- attribute: numeric, nominal, ordinal and mixtures
- structure: vectors, events, time series, etc.
- dimensionality
- ability to deal with noise, missings and outliers
- discovery of clusters with arbitrary shape
- actionability
- efficiency/scalability
- interpretability and usability
- parameter-free (unfixed number of clusters)
- clustering in the presence of domain knowledge and user-specified constraints

# How data characteristics affect clustering?

- sparseness
- variable domain
- data structure
- data distribution
- size and dimensionality
- noise and outliers

Rui Henriques

---

## Lecture 5: Representation Learning

*Source: 04 RepresentationLearning*

---
# Representation Learning

Representations of Complex Data Structures using Deep Learning

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

 

# Representation Learning

- Good features essential for successful descriptive and predictive tasks
- feature extraction and engineering estimated to entail 90% of the overall ML effort
- principle: instead of learning $f: X \to Y$, learn a representation $g: X \to Z$, then learn the predictor/descriptor $f: Z \to Y$ on top of it

- "A good representation is one that makes a subsequent learning task easier"
— Deep Learning, Goodfellow et al. 2016

# Representation Learning

However... feature extraction is now always trivial

- manual extraction is laborious, often incomplete and prone to errors (e.g., features derived from EEG visual inspection)
- automated extraction pipelines not always good to handle complex data
- statistics on a sliding window for time series, structure-texture-color cues for images, term frequencies for text, geometric features for trajectories...
- ... are often uninformative and susceptible to diverse idiosyncrasies

# Representation Learning

- Core premises
- observed data is a causal result of underlying factors
- variation in these factors explain the variation in the data
- Example: objects, rotation, lightning, etc. are underlying factors of images

- Why learning representations?
- feature extraction from complex data structures (e.g., text, time series, image, events)
- less dependence on feature engineering and domain knowledge
- easy application of machine learning (controlled dimensionality, feature independence)
- improved descriptive and predictive capacity
- others: denoising, summarization, visualization...

 

# Good representations

What makes a good representation? Good representations are:

1. compact (minimal)
2. explanatory (sufficient)
3. disentangled (independent factors)
4. interpretable
5. informative (make subsequent problem solving easier)

by Isola, Freeman, Torralba

# Good representations

- Smoothness: if $x_1 \approx x_2$, then $g(x_1) \approx g(x_2)$
- the most basic prior
- similarity in the representation (somehow) reflects similarity of raw data

- Invariances/equivariance/coherence:
small semantic changes should result in similar representations. Invariance is domain-specific:
- image representations should be invariant under transformations like rotations, color jitter...
- time series representations can be invariant to temporal shifts, rescales...

- Less supervision: unsupervised / semi-supervised / self-supervised representations
- representations should capture raw content (easily lost when focusing on specific targets)
- one representation may be used for multiple end goals

 

# Good representations

- Multiple explanatory factors
- recover different factors so it is useful for many tasks
- Disentangled explanatory factors
- each dimension of the representation should capture a separate/meaningful aspect of the data
- Hierarchical explanatory factors
- some underlying factors are more abstract than others and could be further defined in terms of less abstract ones
- Loose factor dependencies
- factors should be related through simple, linear dependencies
- leverage interpretability (e.g., physics) and support subsequent learning
- Sparsity: for any observation $x$, only some factors are
- relevant $\Rightarrow$ most dimensions of $g(x)$ should be zero, or
- invariant to small variations of $x$

# Good representations

These properties can be easily tested

- smoothness: reconstruction capacity
- given $\mathbf{z} = g(\mathbf{x})$, recover $\hat{\mathbf{x}} = g1(\mathbf{z})$ and assess $\|\hat{\mathbf{x}} - \mathbf{x}\|$
- invariance: inject non-relevant changes, $\mathbf{x}'$, and assess $\|\mathbf{z}' - \mathbf{z}\|$
- disentanglement: low dependencies in $Z$ (recall descriptive statistics from previous class)
- sparsity: average #zeros per representation, $\{z_1, \ldots, z_n\}$
- learning utility: predictive scores (accuracy, F1, errors...) and descriptive scores (clustering quality...)
- compactness: #features
- ...

# Numeric representations

- Goal: capture underlying explanatory factors attending to their specific constraints
- coverage, invariance, hierarchy, disentanglement, diversity, sparsity, smoothness...
- Clue: numeric representations may offer interesting properties!
- Still: some hard trade-offs
- attaining coverage (preserving as much input information) together with nice properties (e.g., feature independence, sparsity, invariance)
- It seems a hard task! How to?

compressed image code

# Autoencoders

- How then? A classic approach is to learn an autoencoder

# Autoencoders

- How then? A classic approach is to learn an autoencoder:
- learn an encoder $g: X \to Z$ and the corresponding $(g^{-1})$ decoder $d: Z \to X$
- the goal is to reconstruct the input, i.e. $\mathbf{x} \approx d(g(\mathbf{x}))$
- we can learn the encoder and decoder functions from data by minimizing a loss
- reconstruction loss, $Loss(\mathbf{x}) = Loss(\mathbf{x}, d(g(\mathbf{x})))$
using, for instance, the mean squared error (MSE) on numeric features

- Yet... How to learn encoder-decoder functions without previous knowledge?
- Neural networks!
- and indeed... neural representations can attain some of the nice properties!

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

 

# Neurons...

- Central unit of our brain: neuron
- Computational peer: perceptron (node)
- given an input signal: set of features
$$
\mathbf{x} = (x_1, \dots, x_m)
$$
- returns an output quantity: weighted sum
$$
z = w_0 + \sum_{i=1}^{m} w_i x_i
$$
(linear function of input features)
- Learning a perceptron $f: X \to Z \ldots$
- iteratively adjusting the parameters (weights)
$$
\mathbf{w} = (w_1, \dots, w_m)
$$
from pairs $\{(\mathbf{x}_1, z_1), \dots, (\mathbf{x}_n, z_n)\}$

# Neural networks

- Yet... most real-world predictive and descriptive problems not well described by linear functions
- And indeed... our brain is a complex connectome
- $10^{40}$ neurons
- $10^{4-5}$ connections per neuron
- necessary for neuroplasticity: learning and memory
- In maths, we can compose **linear** functions, $f(x)$ and $h(x)$, to form a **non-linear** function, $c(f(x), h(x))$ for modeling more complex behavior
- How to compose neurons (nodes)?
- the composition can be **organized** in **layers**
- the outputs of each node in one layer feeds the input of the nodes in the next layer

# Non-linear models

Multiple layers of cascade linear units still produce only linear functions

$$
z_{out} = \sum w \left(\sum w x_i\right)
$$

- Solution?

$$
z_{out} = f \left(\sum w f \left(\sum w x_i\right)\right)
$$

# Activation functions

A large part of the expressiveness of networks are driven by the $f$ functions, termed **activations**

Sigmoid

$$
\sigma(x) = \frac{1}{1 + e^{-x}}
$$

tanh

$$
\tanh(x)
$$

ReLU

$$
\max(0, x)
$$

Leaky ReLU

$$
\max(0.1x, x)
$$

Maxout

$$
\max(w_1^T x + b_1, w_2^T x + b_2)
$$

ELU

$$
\left\{ \begin{array}{ll}
x &amp; x \geq 0 \\
\alpha(e^x - 1) &amp; x &lt; 0
\end{array} \right.
$$

# Exercise moment

Consider the following multilayer perceptron:

- trained on pairs (document, graded relevance)
- inputs: frequencies of specific terms in a document
- output: how likely a document covers natural catastrophes
- all biases as zero ($w_0 = 0$) and rectifier (ReLU) activation on the hidden and output nodes where $ReLU(x) = \max(0, x)$

Exercise: score document $\mathbf{x}$ knowing the frequencies of sun, fire and rain are 1, 0 and 2, i.e. $\mathbf{x} = (1,0,2)$

Solution: a simple propagation step is necessary

$$
\begin{array}{l}
\hat{z} = 0.5 \times h_1 + 0.1 \times h_2 - 0.2 \times h_3 \\
= 0.5 \times (\max(0, 0.9 \times 1) + \max(0, 0.8 \times 0) + \max(0, 0.1 \times 4)) + 0.1 \times (\dots) - 0.2 \times (\dots) = 0.7
\end{array}
$$

# Neural networks for predictive tasks

- The previous neural networks can be used for:
- single-output regression (estimate quantity)
- binary classification (output above a given threshold $\theta$)

- Neural networks can have multiple output nodes:
- each output is a category in multi-class classification (e.g., document categorization, digit recognition)
- the output category is the node with highest value
- multiple-output prediction, i.e. multiple targets (e.g., autonomous driving – speed and direction)

# Expressive boundaries

- Non-linear (often non-convex) predictors
- expressive *hyperboundaries* in classification problems (*left*)
- expressive *hypersurfaces* in regression problems (*right*)

# Learning neural networks

## Goal

- given a training set of input-output pairs $(\mathbf{x}_i, \mathbf{z}_i)$, learn the parameters $\theta$ of the network
- the parameters are essentially the weights from all layers

## How?

- finding the weights that minimize a loss between the real and estimated outputs
- a common loss is the squared error $L(\hat{\mathbf{z}}, \mathbf{z}) = \|\hat{\mathbf{z}} - \mathbf{z}\|^2$
- gradients are used to adjust weights in a direction that decreases the loss
- the adjusting process is often termed gradient descent (GD) or backpropagation
- randomly initialize weights and iteratively adjust throughout epochs using batches of pairs
- the learning rate $\eta$ and batch size controls the intensity and stability of weight updates

 

# Neural processing layers as transformations

- A layer $[p]$ can be seen as a non-linear mapping, transforming the input signal $\mathbf{x}^{[p - 1]}$ into a new signal $\mathbf{x}^{[p]}$

$$
\mathbf {x} ^ {[ p ]} = \phi (\mathbf {W} ^ {[ p ]} \mathbf {x} ^ {[ p - 1 ]} + \mathbf {b} ^ {[ p ]})
$$

# From single to multiple hidden layers

Multi-layer learning process to extract rich features (good data representations)

- image: pixels → edges → textures → motifs → parts → objects
- text: character → word → word group → clause → sentence → story

by Param Vir Singh

# Deep Learning

- DL is a ML subfield dedicated to the learning of models with a high number of parameters
- paradigmatic case: neural networks (deep in reference to the #layers and/or #parameters)
- Mathematically: shallow NNs (few layers, high #nodes per layer) should be as good as deeper NNs
- the fact that deep NNs work better is empirical: better convergence and computational scalability
- Advantages of deep NNs
- outperform other ML techniques in many tasks
- expressivity to learn from high-dimensional data (including image, text, signal)
- effective end-to-end learning system (can bypass the need for explicit feature extraction)
- Challenges of deep NNs: larger amounts of data required, prone to overfitting (regularization necessary)

# Hyperparameterization

- How many layers? Some of the mentioned hyperparameters:
- #layers, #neurons per layer, activations
- loss function, learning rate, batch size
- others: layering (more to come!), regularization (e.g. penalty, dropout rate), momentum, decay...

- The hyperparametric choices define the **architecture** of the neural network

- So many choices ☹ How do we select the best hyperparameters?
- **manual** optimization (rely on *intuition* yet discouraged as DL is not rocket science)
- **automatic** optimization can be exhaustive (grid searches) or approximate (default option)
- many good packages available for effective approximate optimization (e.g. optuna)

# Convergence: early stopping

- We can keep optimizing the network weights...
... until the network perfectly overfits the training data, hampering the ability to generalize to unseen data

- One possible solution? Early stopping
- stop convergence before MLP overfits data
- how?
- optimize weights with training data, yet assess the loss on a validation set
- stop learning when the validation error increases along few iterations (evidence of overfitting)

- Deep networks? Still provide a max number of epochs!

# NNs for Representation Learning

- Two major schools for obtaining a numeric representation (termed embedding):

supervised

unsupervised

- Hybrid variants: network with supervised and unsupervised paths

# Supervised data representations

- The first school seems a natural choice...
- extracts features in a latent space (hidden layer) with inherent predictive value for a selected task

- Problems
- discriminative yet not necessarily descriptive
- unable to represent/reconstruct input
- no guarantees of smoothness, invariance
- biased towards the target predictive task

- Solutions
- multi-task learning stances
- extend the number of outputs to capture multiple tasks
- features become less biased and more informative towards varying ends
- unsupervised learning stances ⇒ next!

 

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

 

# Unsupervised vs supervised stances

- Recall the two major paradigms for data representation

supervised

unsupervised

by Isola, Freeman, Torralba

# Autoencoders

Recall: autoencoders as **unsupervised** approaches to representation learning

- goal: learn a compact representation (embedding) to reconstruct input, i.e. $\mathbf{x} \approx d(g(\mathbf{x}))$
- learn the parameters of the encoder $g: X \to Z$ and decoder $d: Z \to X$ minimizing a reconstruction loss such as $\| \hat{\mathbf{x}} - \mathbf{x} \|^2$ where $\hat{\mathbf{x}} = d(g(\mathbf{x}))$

arg $\min_{\mathcal{F}} \mathbb{E}_{\mathbf{X}}[||\mathcal{F}(\mathbf{X}) - \mathbf{X}||]$

# Autoencoders

- Learning an **autoencoder** ≡ learning a network that learns to predict the input in the output
- Beyond representation...
- compression
- visualization (in lower spaces)
- manifold learning
- denoising

# Explainability

- Meaning of the embedding features
- saliency maps in the original/raw inputs (check our Explainability class)
- Inverting representations (all versus subset of factors)

[81 20 84 64 58 39 17 54 72 15]

# Hybrid architectures

- Downside of purely unsupervised approaches
- focus on reconstruction may not ensure that the extracted features yield the sufficient predictive power to effectively handle predictive tasks
- Solution: combining supervision and unsupervision
- single encoder
- two decoders
- a dedicated path for the predictive task, other for reconstruction
- loss with two components as well
- parameters of decoders updated simultaneously or alternatively

# Multi-task learning

Going beyond two dedicate paths...

- as many paths as relevant predictive/descriptive tasks
- ensure representations are more expressive
- generalizable for multiple downstream ends

## Examples:

- on time series: forecasting, anomaly detection, imputation (reconstructing incomplete observations)
- on text: tagging, syntactic parsing, sentiment analysis, text classification, translation

 

# Self-supervision

In the absence of annotations (unsupervised settings), self-supervision can be pursued to emulate predictive tasks

- masking parts of data for reconstruction (e.g. word masking is at the basis of LLMs such as ChatGPT)

A supervised alternative for coloring tasks:

# Contrastive learning

- Learn embeddings by comparing inputs rather than solely relying on reconstruction or prediction
- Form pairs of inputs and train models by
- pulling representations of similar (positive) examples closer together
- pushing representations of dissimilar (negative) examples farther

by Isola, Freeman, Torralba

# Multi-level embeddings

- Challenge: high-dimensional embeddings (e.g. thousands of dimensions for text) hamper tasks, such as retrieval and clustering, where you want to quickly find neighbors (closest records, images, signals, documents, webpages) for a given input (e.g., web search)
- Solution: learn multiple representations by training autoencoders with varying bottleneck sizes

- small-sized embeddings used to find the nearest neighbor candidates (e.g., top 200) using cosine similarity
- optimal-sized embedding of candidates to obtain a final ranking (e.g., ordered top 10)

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

# From MLPs to other neural architectures

MLPs originally proposed for the analysis of simple multivariate data, however...

- fully-connected layers are computationally expensive for high-dimensional data
- given $p$ units in the 1st layer: $m \times p$ parameters (high $m$, $p$ in same magnitude) for this single layer
- other data structures are described by features with unique dependencies...

- image and video: features are spatiotemporally correlated! Spatial dependencies
- (multivariate) time series: features change along time! Temporal dependencies
- text and speech: terms are situated (syntactical and semantical context)! Sequential dependencies

- we need to go beyond classic fully-connected layering...

- convolutional layering (CNNs) for signal and image data
- recurrent layering (RNNs) for time series data
- self-attention layering for language data

# CNNs, RNNs, self-attention

- convolutions and recurrence replace full connections with different forms of locality
- self-attention rely on flexible positional encodings (not requiring processing in any fixed order)

https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html

# Computer vision tasks

- Computer vision has been a focal area of interest for ML
- Illustrative tasks: localization, object detection, instance segmentation

Classification
CAT

Classification + Localization
CAT

Object Detection
CAT, DOG, DUCK

Instance Segmentation
CAT, DOG, DUCK

Picture from: Li, Karpathy, Johnson – Understanding and Visualizing CNNs

# Convolutional NNs

Hidden units are connected to local receptive fields (spatial dependencies)

- much lower number of parameters than fully-connected layers!
- inspired by neurophysiological experiments [Hubel &amp; Wiesel 1962]
- convolution and pooling operations form the basis of CNNs

by eCognition

# Convolutional autoencoders

Convolutions can be applied in autoencoder architectures to create image representations

- embedding size and layering should be sufficiently expressive to handle vision challenges...

# Recurrent NNs

- How to learn from time series data or video data?
- CNNs can be used for these ends: 1D CNNs for time series, 3D CNNs for video data
- however, the locality of convolution operations often neglect long-term temporal dependencies
- Recurrent NNs offer a possible way out
- recurrent connections: a single unit to process features from one variable along time
- memory of the previous inputs stored in the internal state to capture temporal associations
- Long Short-Term Memory (LSTM) networks are a RNN variant with enhanced internal state
- well-prepared to model long-term temporal dependencies
- Trade-off: RNNs are more sensitive to the vanishing gradient problem than CNNs, hence less stable

# Recurrent NNs

RNNs traditionally applied over time series data... yet applications can go well beyond...

# Recurrent autoencoders

... and, yes, recurrent layering can be also considered for autoencoders
- find numeric representations of (multivariate) time series

Hybrid layering: combines different types of transformations

# Large Language Models

- Deep neural networks used for general-purpose language understanding and generation
- LLMs they embody the data representation principle!
- expressive embeddings for high-efficacy downstream tasks
- key given the diversity of downstream applications...

# Large Language Models

Central principles:
- word embeddings
- positional embeddings
- self-supervision
- self-attention
- pre-training + fine-tuning

https://www.baeldung.com/cs/large-language-models

# LLMs: text encodings

Apply a dedicated NN to map words into numeric vectors capturing:

- semantic similarity
- syntactic similarity

Create a complementary numeric vector per word with its positional encoding

- aims at capturing relative positions of a word in text (e.g. "Mary loves John" ≈ "John is loved by Mary")

# LLMs: self-supervision

The sequence of word (and positional) embeddings in a text concatenated into a numeric tensor
- this tensor can be a text representation by itself, yet is high-dimensional and lacks expressivity
- padding/transforms entailed to ensure the tensor has uniform shape for texts with varying length

The tensor feeds a neural network with the aim of learning an expressive embedding
- autoencoders are rare since as text reconstruction is generally insufficient to capture text semantics
- supervised neural architectures are alternatively applied using a key principle

- self-supervision
- create fictitious predictive tasks to learn embeddings
- common: targets derived from unlabeled text by masking words to allow supervision
- predictive task: classify the masked words (e.g., arbitrarily positioned word, next word)

# LLMs: attention-based architecture

Architectural elements of an LLM

- attention: enhance parts of the signal while diminishing other parts
- self-attention: weighting the relevance of terms/tokens (from their embedding) to predict the masked term
- central component: attention-based transformer (right)
- encoder layer encodes which parts of the input are relevant to each other
- decoder takes all encodings to generate an output sequence
- encoder-only (whole text modeling) and decoder-only (word prediction) variants are also common
- an LLM is a stacking of multiple transformer components with skip connections for multi-domain learning capacity

# LLMs: pre-training and fine-tuning

- LLM are commonly **pre-trained** on different datasets and different tasks
- going beyond single corpus and word prediction (e.g., semantic similarity between paired text)
- the parameters of the first layers (i.e. transformers) are updated for the alternating tasks

- Pre-training followed by **fine tuning**
- to orient the LLM for specific tasks and/or more closely related data
- two major strategies
- retrain all network (heavy)
- retrain last layers only (preserve embeddings/intermediate signals)

Fine-tuning - Updating The Output Layers

Fine-tuning - Updating All Layers

https://www.baeldung.com/cs/large-language-models

Evolutionary Tree

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

# Multimodal Representations

- Learning representations from heterogeneous data structures
- combining features, text, vision, time series, events, trajectories, multiple omics...

- Classic stance:
- extract features from each mode separately
- classic statistics and/or unimodal data representations
- concatenate the representations (larger numeric vector with mode-dedicated sections)

- Problems:
- informative features capturing cross-modal synergies are neglected
- many of earlier representation principles no longer satisfied (e.g., succinctness, disentanglement)
- dependencies between representations of each mode
- what if one modality is not available for some training or testing observations?

- Solution: multimodal autoencoders and shared multi-task learning

iit

# Multimodal Representations

Multimodal LLMs are well-known class
- embeddings for coupled vision, audio, and text observations
- captioning

http://cs.stanford.edu/people/karpathy/deepimagesent

"two young girls are playing with lego toy."

"boy is doing backflip on wakeboard."

"construction worker in orange safety vest is working on road."

"man in black shirt is playing guitar."

- text-to-image generation
- "teddy bear swimming at the Olympics"
- "cute corgi lives inside sushi house"
- "sloth holding treasure with bright golden light"

by Sahara et al. 2022

# How deep?

A portrait photo of a kangaroo wearing an orange hoodie with blue sunglasses standing on the grass in front of the Sydney Opera House holding a sign on the chest that says Welcome Friends! by Yu et al. 2022

# Multimodal representations

- Different strategies to learn multimodal representations, including:

- joint representation (simplest version)
- modality concatenation (early fusion)
- unsupervised or supervised
- similarity-based methods (e.g., cosine)

- coordinated representations
- constraints on structure (e.g., orthogonality, sparseness)

# Joint representations

- Shared representations (joint embedding) capture cross-modal synergies
- efficiency: lower dimensionality than the sum of individual representations
- expressivity: higher efficacy for downstream tasks
- Each modality can be pre-trained (using modality-specific autoencoders) before adding the shared layer

# Joint representations

- At training time:
- all modalities can be inputted
- a subset of modalities can be removed for some data instances
- regarded as a form of regularization (dropout) that helps the training
- At testing time: if only some modalities are available, the remaining are generated

# Outline

- Data Representations
- Neural Networks
- Unsupervised and Self-supervised Stances
- Handling Complex Data Structures
- Multimodal Data Representations

 

Rui Henriques

---

## Lecture 6: Dimensionality reduction

*Source: 05 DimensionalityReduction*

---
# Dimensionality reduction

Feature selection, principal component analysis, discriminant analysis

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

 

# Motivation

- At a first glimpse, increasing the number of variables should improve learning...
- In practice, including more variables can degrade performance (i.e. **curse of dimensionality**)
- challenges: learning complexity and generalization difficulty (over/underfitting)
- common definition of **high-dimensionality**: $|Y| \gg |X|$ (i.e. $m \gg n$)
- The number of training observations required increases **exponentially** with dimensionality
- How then can we learn in high-dimensional data spaces with a limited number of observations?
- dimensionality reduction

 FORMÁCÃO AVANÇADA

# Data domains with high-dimensionality

- text and web content data (left)
- social behavioral data
- biological data
- genetic variants (millions per individual)
- gene expression (&gt;20k genes)
- molecular concentrations (metabolites, proteins...)
- healthcare data (clinical records)
- consumer data
- signal, audio, image and video data

# Challenges

High-dimensional data analysis:
- learning complexity: large data space
- generalization difficulty (insufficient observations)
- overfitting risk
- underfitting risk
- how to evaluate these risks?
- behavior for varying data size
- compare training and testing error
- variability of errors across testing folds
- bias and variance components of error

# Generalization: overfitting and underfitting risks

## Overfitting
- unability to discard non-informative and/or non-discriminative data

## Underfitting
- exclusion of informative or discriminative data from the learning

# Global and local learning

## "Global" learning

- descriptors (e.g., clusters) and predictors (e.g., discriminants)
- all features considered, often equally relevant in joint probabilistic stances (e.g. naïve Bayes)
- Problem? overfitting
- what if only a few variables are relevant?

## "Local" learning

- descriptors (patterns) and predictors (e.g. decision trees, kNN)
- few combined features or observations as long as they are informative or discriminative
- Problem? underfitting
- many potentially relevant features or observations neglected

# Dimensionality reduction

Some goals of dimensionality reduction:

- Guide supervised learning (focus on discriminative regions)
- Guide unsupervised learning (focus on informative regions)
- Visualization (project high-dim data into interpretable low-dim data)
- Data compression (efficient storage and retrieval)
- Noise removal (denoising data)
- Speed-up learning
- Describe the underlying properties of data
- Guarantee simplicity and comprehensibility of mined results
- Map multimedia data (image and signal data) into feature-based data
- Support matrix operations (inverse, rank determination, approximation)...

# How?

1. Feature selection
2. Feature extraction/transformation
- principal component analysis
- linear discriminant analysis
- representation learning
3. Sparse kernels and regularization in parametric models to exclude non-relevant parameters
- neural networks, support vector machines, discriminant analysis...
4. Subspace selection to jointly select variables and observations
- pattern mining, decision trees and random forests
- associative classifiers and decision tables

# Dimensionality reduction

- Project the $m$-dimensional observations into a $k$-dimensional space $(k \ll m)$
- preserve most of relevant information or structure from data
- Solve the learning problem in low dimensions
- Two major approaches
- feature selection
- choosing a subset of all features
$$
[y_1, y_2, \dots, y_m] \rightarrow [y_{i1}, y_{i2}, \dots, y_{ik}]
$$
- feature extraction
- creating new features by combining existing ones
$$
[y_1, y_2, \dots, y_m] \rightarrow [d_1, d_2, \dots, d_k] \quad \text{using} \quad f([y_{i1}, y_{i2}, \dots, y_{im}])
$$

 FORMÁCÃO AVANÇADA

# Outline

- Dimensionality reduction: why and how
- Feature selection: recall
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Feature selection

- Optimal subset of features according to an objective function
- differs from feature extraction where output features are (non-)linear combinations of original features

- Objective criteria
- unsupervised setting: variables with higher variability and entropy
- supervised setting: maximize discrimination/correlation with target variable

- Perspectives
- subset search vs. feature ranking
- models: filter vs. wrapper

# Feature ranking

- Weighting each individual feature according to objective criteria (e.g. information gain)

- Sort and select top-ranked features: a) threshold, b) $k$-top, or c) percentile
- Disadvantages
- hard to determine threshold or $k$
- unable to consider correlation between features
- Advantages
- efficient $O(m)$ no need to test combination of features (subset optimality)

 FORMÁCÃO AVANÇADA

# Measures for feature ranking

Goodness of a feature/feature subset:
- information measures
- correlation/association measures
- distance measures
- accuracy measures

# Information measures in classification

- $\chi^2$ test (chi2 in Python)
- robust for input categorical variables
- two values: $\chi^2$ statistic (higher the better), $p$-value

```python
iris = datasets.load_iris()
X, y = iris.data, iris.target
chi2, pval = chi2(X, y)
[ 10.81782088 3.59449902 116.16984746 67.24482759 ]
[ 4.47651e-03 1.6575e-01 5.943443e-26 2.50017e-15 ]
```

- ANOVA test (f_classif in Python)
- robust for numeric input variables
- also valid for categorical input with numerical output
- two values: F-value statistic (higher the better), $p$-value

# Information measures in regression

- correlation for numeric input variables:
- Pearson and Spearman (see previous lectures)
- $F$-statistic (higher the better) and accompanying $p$-value

- mutual information or ANOVA for categorical input variables

- want to abstract the type of input variables? use f_regression from sklearn

# Information measures in description

- as a **filter**: measure feature importance and select top-$k$ features or above threshold
- **unsupervised** setting: **high entropy**
- supervised setting: **next slides**
- as a **wrapper**: assess learning performance with varying subsets of features
- simple: measure feature importance and test descriptors on top-$k$ features with varying $k$
- advanced: assess descriptors with different subsets of variables (irrespectively of top-$k$)
- how to assess descriptors?
- e.g. clustering quality – any problem when considering silhouette?

 

# Feature selection: filter vs. wrapper

## Filter model
- independent from the learning algorithm
- efficient and no learning biases
- rely on general characteristics of data

## Wrapper model
- evaluated on a given descriptor/predictor
- descriptive utility or predictive accuracy as a goodness measure
- better yet dependent on the learning approach
- more computationally expensive

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Feature extraction

- Feature extraction used to
- extract relevant features from complex data to handle structural complexity
- extract domain-specific features of interest
- e.g. PQRST statistics from ECG signal
- extract domain-independent statistics of interest
- e.g. spectral statistics from time series and images
- learn latent features using neural networks (data representation)

- learn transformations that explain simple multivariate data with reduced dimensionality

# Feature extraction

Feature extraction used to

- extract relevant features from complex data to handle structural complexity
- learn transformations that explain simple multivariate data with reduced dimensionality: TODAY!
- classical approaches aim at finding a linear transformation
- Why? simple to compute and analytically tractable
- Goal: reduction that preserves as much information in data as possible
- paradigmatic case: Principal Component Analysis (PCA)
- simple extensions available
- non-linear transformations (kernel trick)
- accommodate discriminative power in supervised settings
- Goal: reduction that best separates the data
- paradigmatic case: Linear Discriminant Analysis (LDA)

# Algebra ground for PCA

Axes of greater variance given by eigenvectors of covariance matrix

# Algebra ground

- A covariance matrix measures the tendency of two variables to vary in the same direction
- positive (negative) covariance denote positive (inverse) correlation
- nevertheless magnitude of values not easily interpretable
- when normalizing covariance by their variances we obtain linear correlation in $[-1,1]$
- covariance matrix is symmetric and positive-definite

- Remember
- sample covariance: $n - 1$ in the denominator (Bessel's correction)

$$
cov(y_1, y_2) = \frac{\sum_{i=1}^{n} (a_{1i} - \overline{y_1}) \cdot (a_{2i} - \overline{y_2})}{n - 1}
$$

- whole population: $n$ is the denominator

$$
cov(y_1, y_2) = \frac{\sum_{i=1}^{n} (a_{1i} - \overline{y_1}) \cdot (a_{2i} - \overline{y_2})}{n}
$$

 FORMÁCÃO AVANÇADA

# Algebra ground

- Covariance matrix, given $m$ attributes, $y_1, \ldots, y_m$

$$
C^{m \times m} = (c_{ij} | \mathrm{i}, \mathrm{j} = 1.. \mathrm{m}), \text{ where } c_{ij} = \operatorname{cov}(y_i, y_j)
$$

|   | Hours(H) | Mark(M)  |
| --- | --- | --- |
|  Data | 9 | 39  |
|   |  15 | 56  |
|   |  25 | 93  |
|   |  14 | 61  |
|   |  10 | 50  |
|   |  18 | 75  |
|   |  0 | 32  |
|   |  16 | 85  |
|   |  5 | 42  |
|   |  19 | 70  |
|   |  16 | 66  |
|   |  20 | 80  |
|  Totals | 167 | 749  |
|  Averages | 13.92 | 62.42  |

$$
\begin{array}{l}
C^{m \times m} = \left( \begin{array}{cc} \operatorname{cov}(H, H) &amp; \operatorname{cov}(H, M) \\ \operatorname{cov}(M, H) &amp; \operatorname{cov}(M, M) \end{array} \right) \\
= \left( \begin{array}{cc} \operatorname{var}(H) &amp; 104.5 \\ 104.5 &amp; \operatorname{var}(M) \end{array} \right) \\
= \left( \begin{array}{cc} 47.7 &amp; 104.5 \\ 104.5 &amp; 370 \end{array} \right)
\end{array}
$$

# Algebra ground

- The covariance matrix of the data points defines the ellipses of equiprobability on the right

# Eigenvalues and eigenvectors

- Let $C$ be a $m \times m$ covariance matrix
- Vectors $\mathbf{v}$ having same direction as $C\mathbf{v}$ are called **eigenvectors**
- eigenvectors define the linear composition of attributes
- In the equation $\boxed{C\mathbf{v} = \lambda\mathbf{v}}$, $\lambda$ is called an **eigenvalue** of $C$
- Example:
$$
\begin{pmatrix} 2 &amp; 3 \\ 2 &amp; 1 \end{pmatrix} \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 12 \\ 8 \end{pmatrix} = 4 \begin{pmatrix} 3 \\ 2 \end{pmatrix}
$$
$$
\mathbf{v} = [3\ 2]^T \text{ and } \lambda = 4
$$
meaning that data is described by $y_{new} = 3y_1 + 2y_2$

 FORMÁCÃO AVANÇADA

# Eigenvalues and eigenvectors

- $A\mathbf{v} = \lambda \mathbf{v} \Leftrightarrow (A - \lambda I)\mathbf{v} = 0$
- Given $A$, how to calculate $\mathbf{v}$ and $\lambda$:
- determine roots to $\det(A - \lambda I) = 0$, roots are eigenvalues $\lambda$
- solve $(A - \lambda I)\mathbf{v} = 0$ for each $\lambda$ to obtain eigenvectors $\mathbf{v}$

|  y_{1} | y_{2}  |
| --- | --- |
|  -5.1 | 9.25  |
|  14.9 | 20.25  |
|  5.9 | 33.25  |
|  5.9 | -30.75  |
|  ... | ...  |
|  -9.1 | -10.75  |
|  -9.1 | -21.75  |
|  5.9 | 19.25  |

$$
C = \begin{pmatrix} 2 &amp; 0.8 \\ 0.8 &amp; 0.6 \end{pmatrix}
$$

Eigenvectors and eigenvalues:
$\mathbf{v}_1 = [0.91, 0.41], \lambda_1 = 2.36$
$\mathbf{v}_2 = [-0.41, 0.91], \lambda_2 = 0.23$

$$
\mathbf{x}_i = \begin{pmatrix} 0.91 &amp; 0.41 \end{pmatrix} \begin{pmatrix} a_{i1} \\ a_{i2} \end{pmatrix}
$$

|  y_{new}  |
| --- |
|  -0.8  |
|  21.9  |
|  19  |
|  -7.2  |
|  ...  |
|  -12.7  |
|  -17.2  |
|  13.3  |

# Dimensionality reduction

- Map data with $m$ variables into $k$ variables (such that $k &lt; m$) without significant loss

- Residual variation: information in A not retained in A'
- Trade-off: dimensionality $(k)$ and interpretability versus information loss

# Linear transformations

## Intuition:
- find the axis that shows the greatest variation
- project all points into this axis

## How:
- move origin to the center of the dataset
- find the eigenvectors and eigenvalues of the data covariance matrix
- the eigenvectors define the new data space

# Singular value decomposition (SVD)

$1^{\text{st}}$ singular vector: direction of maximal variance
$\lambda_{1}$: how much data variance is explained by $1^{\text{st}}$ vector
$2^{\text{nd}}$ singular vector: direction of maximal variance, after removing projection of $1^{\text{st}}$ vector
$\lambda_{2}$: how much data variance is explained by the $2^{\text{nd}}$ vector

...

$k^{\text{th}}$ singular vector ...

(until unexplained variance below threshold)

# Principal component analysis (PCA)

- PCA is SVD done on centered data
- singular vector/value = eigenvector/value
- First component (PC1): highest eigenvalue (direction with greatest variation)
- Second component (PC2): direction with maximum variation orthogonal to PC1

# Component selection

- The variance in the direction of the $k^{\text{th}}$ eigenvector is given by the eigenvalue $\lambda_{k}$
- Singular values can be used to estimate how many components to keep
- **Rule of thumb**: keep enough to explain 85% of the variation

$$
\frac {\sum_ {j = 1} ^ {k} \lambda_ {j}}{\sum_ {j = 1} ^ {m} \lambda_ {j}} \approx 0.85
$$

if $k = m$, we preserve 100% of the original variation

- depending on the reduced dimensionality and learning needs: 90%, 95%, 98% also common
- **Karhunen-Loeve (KL)** transform is PCA without subsequent removal of components
- no information loss

 

# Principal component analysis

- PCA projects data along the directions where the data varies most
- directions are determined by the eigenvectors with the largest eigenvalues
- reduction can imply information loss, yet PCA preserves as much information as possible

- Components (summary variables)
- linear combinations of the original variables
- uncorrelated with each other
- the largest eigenvalues are called **principal components**
- the eigenvalue is the magnitude of eigenvector, defining the direction's variance
- in general: only few components needed to capture most data variability

 

# Principal component analysis

- Revising how
1. Subtract mean of each variable
2. Compute the covariance matrix $m \times m$ (scatter of data)
3. Compute eigenvalues, $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_m$, and eigenvectors, $v_1, v_2, \ldots, v_m$
4. Keep the large $k$ eigenvalues ($k \leq m$) and construct the transformed space
5. Transform the dataset $D \to D'$

- Exercise: apply PCA on the following dataset

# PCA: Example

## 1. Centering data

|  y_{1} | y_{2}  |
| --- | --- |
|  2.5 | 2.4  |
|  0.5 | 0.7  |
|  2.2 | 2.9  |
|  1.9 | 2.2  |
|  3.1 | 3.0  |
|  2.3 | 2.7  |
|  2 | 1.6  |
|  1 | 1.1  |
|  1.5 | 1.6  |
|  1.1 | 0.9  |
|  mean 1.81 | 1.91  |
|  y_{1} | y_{2}  |
| --- | --- |
|  .69 | .49  |
|  -1.31 | -1.21  |
|  .39 | .99  |
|  .09 | .29  |
|  1.29 | 1.09  |
|  .49 | .79  |
|  .19 | -.31  |
|  -.81 | -.81  |
|  -.31 | -.31  |
|  -.71 | -1.01  |
|  mean 0 | 0  |

# PCA example

2. Calculate the covariance matrix:

$$
cov = \left( \begin{array}{cc} y_1 &amp; y_2 \\ .616555556 &amp; .615444444 \\ .615444444 &amp; .716555556 \end{array} \right) y_1
$$

3. Calculate its (unit) eigenvectors and eigenvalues

$$
eigenvalues = \left( \begin{array}{c} .0490833989 \\ 1.28402771 \end{array} \right) \qquad eigenvectors = \left( \begin{array}{cc} -.735178656 &amp; -.677873399 \\ .677873399 &amp; -.735178656 \end{array} \right)
$$

4. Order eigenvectors by eigenvalue, highest to lowest and select top $p$

$$
\mathbf{v}_1 = \left( \begin{array}{cc} -.6779 \\ -.7352 \end{array} \right) \quad \lambda_1 = 1.284 \qquad \mathbf{v}_2 = \left( \begin{array}{c} -.7352 \\ .6779 \end{array} \right) \quad \lambda_2 = .0491
$$

... and construct the transformed feature vector

$$
FeatureVector(k = 2) = \left( \begin{array}{cc} -.6779 &amp; -.7352 \\ -.7352 &amp; .6779 \end{array} \right) \quad FeatureVector(k = 1) = \left( \begin{array}{c} -.6779 \\ -.7352 \end{array} \right)
$$

# PCA example

## 5. Derive the new data set

TransformedData = RowFeatureVector × RowDataAdjust

$$
DataAdjusted = \left( \begin{array}{cccccccccc}
.69 &amp; -1.31 &amp; .39 &amp; .09 &amp; 1.29 &amp; .49 &amp; .19 &amp; -.81 &amp; -.31 &amp; -.71 \\
.49 &amp; -1.21 &amp; .99 &amp; .29 &amp; 1.09 &amp; .79 &amp; -.31 &amp; -.81 &amp; -.31 &amp; -1.01
\end{array} \right)
$$

$$
FeatureVector(p = 2)^T = \left( \begin{array}{cc}
-.6779 &amp; -.7352 \\
-.7352 &amp; .6779
\end{array} \right)
$$

$$
FeatureVector(p = 1)^T = (-.6779 \quad -.7352)
$$

TransformedData $(p=2)$

|  c_{1} | c_{2}  |
| --- | --- |
|  -.827970186 | -.175115307  |
|  1.77758033 | .142857227  |
|  -.992197494 | .384374989  |
|  -.274210416 | .130417207  |
|  -1.67580142 | -.209498461  |
|  -.912949103 | .175282444  |
|  .0991094375 | -.349824698  |
|  1.14457216 | .0464172582  |
|  .438046137 | .0177646297  |
|  1.22382056 | -.162675287  |

TransformedData $(p=1) =$

|  c_{1}  |
| --- |
|  -.827970186  |
|  1.77758033  |
|  -.992197494  |
|  -.274210416  |
|  -1.67580142  |
|  -.912949103  |
|  .0991094375  |
|  1.14457216  |
|  .438046137  |
|  1.22382056  |

# PCA example

Original data

Data transformed with  $k = 2$  eigenvectors

Data transformed with  $k = 1$  eigenvector

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Compression

- Goal: compress data without information loss
- Why? Remember...
- description
- compactness, interpretability, simplicity
- transforms can be used to explain relevant information (variable dependencies)
- how? Assess which variables are contributing more to each component
- remember a component is a linear composition of variables
- guide prediction on the compressed data space
- denoising data
- efficient data storage, retrieval, learning

 

# Recovering original data

- The original vectors can be reconstructed using its principal components
- Given the reduced data space, how to retrieve/decompress old data?

DataRecovered = (FeatureVector × TransformedData) + OriginalMean

```vba
we did: TransformedData = FeatureVector^T × DataAdjust^T
so we can do: DataAdjust^T = (FeatureVector^T)^{-1} × TransformedData
(orthogonal property) = FeatureVector × TransformedData
and: DataRecovered = DataAdjust + OriginalMean
```

# Reconstruction: example

FeatureVector $(p = 2)^T = \begin{pmatrix} -.6779 &amp; -.7352 \\ -.7352 &amp; .6779 \end{pmatrix}$

FeatureVector $(p = 1)^T = (-.6779 - .7352)$

|  y_{1} | y_{2} | c_{1} | c_{2}  |
| --- | --- | --- | --- |
|  2.5 | 2.4 | -.827970186 | -.175115307  |
|  0.5 | 0.7 | 1.77758033 | .142857227  |
|  2.2 | 2.9 | -.992197494 | .384374989  |
|  1.9 | 2.2 | -.274210416 | .130417207  |
|  3.1 | 3.0 | -1.67580142 | -.209498461  |
|  2.3 | 2.7 | -.912949103 | .175282444  |
|  2 | 1.6 | .0991094375 | -.349824698  |
|  1 | 1.1 | 1.14457216 | .0464172582  |
|  1.5 | 1.6 | .438046137 | .0177646297  |
|  1.1 | 0.9 | 1.22382056 | -.162675287  |

using both components

|  y_{1}' | y_{2}' | y'_{1} | y'_{2}  |
| --- | --- | --- | --- |
|  0.69 | 0.49 | 2.5 | 2.4  |
|  -1.31 | -1.21 | 0.5 | 0.7  |
|  0.39 | 0.99 | 2.2 | 2.9  |
|  0.09 | 0.29 | 1.9 | 2.2  |
|  1.29 | 1.09 | 3.1 | 3  |
|  0.49 | 0.79 | 2.3 | 2.7  |
|  0.19 | -0.31 | 2 | 1.6  |
|  -0.81 | -0.81 | 1 | 1.1  |
|  -0.31 | -0.31 | 1.5 | 1.6  |
|  -0.71 | -1.01 | 1.1 | 0.9  |

after uncentering

DataRecovered = (FeatureVector x TransformedData) + OriginalMean

# Reconstruction error

- PCA minimizes the reconstruction error:  $\| \mathbf{x} - \hat{\mathbf{x}}\|$
- It can be shown that the reconstruction error is:  $\text{error} = 1/2 \sum_{i=k+1}^{m} \lambda_i$

- using 2 components: recovery error = 0 (from previous slide)
- using 1 component

|  y'₁ | y'_₂ | y'_1 | y'_2  |
| --- | --- | --- | --- |
|  0.56 | 0.61 | 2.4 | 2.5  |
|  -1.20 | -1.31 | 0.6 | 0.6  |
|  0.67 | 0.73 | 2.5 | 2.6  |
|  0.19 | 0.20 | 2.0 | 2.1  |
|  1.14 | 1.23 | 2.9 | 3.1  |
|  0.62 | 0.67 | 2.4 | 2.6  |
|  -0.07 | -0.07 | 1.7 | 1.8  |
|  -0.78 | -0.84 | 1.0 | 1.1  |
|  -0.30 | -0.32 | 1.5 | 1.6  |
|  -0.83 | -0.90 | 1.0 | 1.0  |

$$
\text{error} = 0.245 = \frac{0.49}{2} = \frac{\lambda}{2}
$$

$$
\text{DataRecovered} = (\text{FeatureVector}(p=1) \times \text{TransformedData}) + \text{OriginalMean}
$$

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Nonlinearities using kernels

Linear projections will not detect this pattern

# Nonlinear PCA using kernels

- Traditional PCA applies linear transformation (ineffective for nonlinear data)
- Solution: apply nonlinear transformation to potentially higher-dimensional spaces

$$
\varphi \colon \mathbf {x} \to \varphi (\mathbf {x})
$$

- how? apply the kernel trick: PCA rewritten in terms of dot product

$$
K (\mathbf {x} _ {i}, \mathbf {x} _ {j}) = \varphi (\mathbf {x} _ {i}) \bullet \varphi (\mathbf {x} _ {j})
$$

- Example

$$
\varphi \colon (a _ {i 1}, a _ {i 2}, a _ {i 3}) \to (a _ {i 1}, \sqrt {a _ {i 2} a _ {i 3}}, a _ {i 1} ^ {2} a _ {i 3})
$$

simplified: transform $A = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ accordingly and apply PCA

$$
\mathbf {x} _ {i} = (2, 4, 1) \rightarrow (2, 2, 4)
$$

# Dimensionality reduction techniques

## Linear transformations
- Eigenvalue analysis: SVD, PCA and KL: $O(nm^2)$ time
- FastMap: approximate searches in $O(nm)$ time (optimal searches also in $O(nm^2)$ time)
- Multi-dimensional scaling: $O(nm^2)$ time
- Random projections: $O(nm)$ time

## Non-linear transformations
- Kernel SVD/PCA
- Locally linear embedding (LLE)
- Laplacian eigenmaps (LEM)
- Semidefinite embedding (SDE)

# Linear discriminant analysis (LDA)

- Challenges of PCA in supervised settings?
- Reduction does not consider impact on the ability to discriminate output variables
- Goal: data transformation guaranteeing class separation
- Principle: pick a new dimension that
- maximize separation between projected classes
- minimize variance of observations within each class
- Solution: LDA
- eigenvectors based on between-class and within-class covariance matrices

good projection: separates classes well

# Linear discriminant analysis (LDA)

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Subspace selection

- Minimize overfitting: remove uninformative regions (focus on informative/discriminative patterns only)
- Minimize underfitting: mine all relevant regions

# Subspace selection

- Addresses limitations of feature selection/extraction
- single space → multiple compact spaces
- goodness criteria computed from all observations → goodness verified on a subset of observations

- Yet limited applicability
- pattern mining and biclustering
- associative classification
- pattern-centric visualization

 

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Evaluation of low-dimensional spaces

- Direct metrics
- match scores against a reference set features/subspaces (only suitable for artificial data or data with prior knowledge)

- Indirect evaluation
- Learning on the original versus reduced data space (e.g., predictive accuracy, goodness of resulting clusters)
- before-and-after comparison
- comparison using different learning algorithms
- Reconstruction error
- Learning curves

 

# Evaluation of low-dimensional spaces

- learning curves

- before-and-after fitness using clustering

# Outline

- Dimensionality reduction: why and how
- Feature selection
- Linear transformations
- algebra ground
- principal component analysis
- compression and reconstruction
- non-linear kernels
- linear discriminant analysis
- Subspace selection
- Evaluation
- Data reduction

# Data reduction

Dimensionality reduction is one of the multiple forms of data reduction
- data reduction similarly considered to aid learning and time-memory efficiency

## Other data reduction strategies:

- domain reduction: reduce data representation
- binning/discretization of real-valued attributes, e.g. continuous variable onto ranges
- cardinality reduction of nominal and ordinal attributes: aggregating categories
- data size reduction (subsampling): reduce the number of instances
1. simple random subsample (SRS): randomly remove observations (either without or with replacement)
2. balanced sample: remove observations guaranteeing that the reduced data satisfies a predefined criterion (e.g. balanced number of classes)

 

# Data reduction

## Subsampling (continue)

3. stratified sample: observations are divided into mutually disjointed parts, called strata, and removal (SRS) is done at each stratum
4. data clustering
- clustering the data and use centroids instead of the actual data
5. data condensation
- obtain minimal data set for correctly classifying all original observations
- emerges from the fact that naive sampling (random or stratified sampling) is not suitable to learn from noisy data (dependent on algorithms)
6. data squashing
- compress ("squash") data in such a way that a statistical analysis carried out on the compressed or original data yields the same outcome

 

Rui Henriques

---

## Lecture 7: Outlier analysis

*Source: 06 OutlierAnalysis*

---
# Outlier analysis

Unsupervised and supervised stances

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

 

# Outlier analysis: applications

- Fraud detection: credit card, telecom, criminal activity in e-commerce
- Cybersecurity and intrusion detection (anti-viruses and network firewalls)
- Customized marketing: high/low income buying habits
- Healthcare: unusual responses to various drugs, rare diseases
- Analysis of performance statistics (e.g. professional athletes)
- Adverse weather and seismic prediction
- Financial applications: loan approval, stock tracking
- ...

# What is an outlier?

- Outlier $\equiv$ anomaly $\equiv$ exception $\approx$ novelty
- outlier analysis $\equiv$ deviant behavior analysis $\equiv$ anomaly analysis $\equiv$ exception analysis $\approx$ novelty analysis

- Outlier: observation that deviates significantly from the normal observations as if it was generated by a different mechanism
- e.g. unusual credit card purchase, Michael Jordon...
- global outlier: observations inconsistent with rest of the dataset
- local outlier: observations inconsistent with their neighborhoods

- Outliers differ from noise data
- noise is random error or variance in the measured variables
- outlier analysis should be able to discard noise

# Types of outliers (1/2)

- Global outlier (or point anomaly)
- observation that significantly deviates from the rest of the data (e.g. intrusion)
- issue: find an appropriate measurement of deviation

- Contextual outlier (or conditional outlier)
- observation that significantly deviates from a given context
- e.g. 30°C in Urbana outlier depending on whether is summer or winter?
- variables divided into two groups
- contextual variables: define the context (e.g. time, location)
- behavioral variables: define the features for outlier evaluation (e.g. temperature)
- generalization of local outliers—deviation from its local area
- issue: define or formulate meaningful context

 

# Types of outliers (2/2)

## Collective Outliers

- a subset of observations that collectively significantly deviate from the whole data (even when each observation is not outlier)
- e.g. risk groups with rare/infrequent genetic variants
- issues
- consider both individual and group behavior
- need suitable distances

## Final considerations

- a dataset may have multiple types of outlier
- one observation may belong to more than one type of outlier

# Challenges

- Separating normal observations from outliers
- hard to enumerate all possible normal behaviours
- border between normal and outlier objects is often a gray area

- Application-specific
- distance metric or statistical assumptions are application-dependent (e.g. clinic data and small deviations, marketing and larger fluctuations)

- Handling noise
- noise may distort the normal objects

- Understandability
- explanatory detection
- degree of outlier: likelihood of being generated by a normal mechanism

 

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

# Outlier analysis

- Our core premises
- data is preprocessed (e.g., minimum artifacts/missings, numerical encodings of ordinals)
- access to good representations of (complex) data ⇒ check representation learning class
- controlled dimensionality of observations ⇒ check statistics and dim. reduction classes

- Two ways of categorizing outlier detection approaches:
- whether labeled examples of outliers are given
- supervised, semi-supervised vs. unsupervised methods
- whether assumptions/knowledge w.r.t. data are available
- statistical, proximity-based, and clustering-based methods vs. deep learning

 

# Outlier analysis: supervised methods

## Supervised outlier detection

- outlier detection as a **classification** task
- observations validated by domain experts (e.g., fraud clearance) for training and testing
- given an observation, the probability of the outlier class can be seen as a score
- **single-class prediction** task
- model normal (outlier) observations and report those not matching the model

## Challenges

- imbalanced classes (outliers are rare)
- ensure that the applied learning approach can handle imbalance (e.g. avoid kNN, favor neural networks with weighted observations or trees/ensembles)
- catch as many outliers as possible
- **sensitivity**/recall more important than accuracy
- $F_{\beta}$-measure with higher $\beta$ values

# Outlier analysis: unsupervised methods

## Unsupervised outlier detection

- observations "clustered" into groups, each with unique properties
- outlier is far away from any group of normal objects
- e.g. intrusion or virus detection, normal activities are diverse

- Weakness
- unsupervised methods may have high false positive rate but still miss many real outliers (supervised often more effective)
- cannot detect collective outliers effectively

- How? find clusters, then outliers are isolated observations and small clusters
- problem 1: hard to distinguish noise from outliers
- problem 2: costly (clustering all data when only few are outliers)

# Outlier analysis: semi-supervised methods

## Semi-supervised outlier detection

- Number of annotated observations is often small
- annotations could be on outliers only, normal observations only, or both

- How? Semi-supervised learning
1. if some **normal observations** are annotated
- use labeled examples and the nearby unlabeled observations to train a model for normal observations; those not fitting the model are seen as outliers
2. if some **outliers** are annotated (may not cover all possible outliers well)
- get help from models for normal observations learned from unsupervised methods

 

# Outlier analysis: statistical methods

- Statistical methods ≡ model-based methods (i.e. parametric)
- assume normal data follows some statistical distribution (stochastic model)
- observations not following the model seen as outliers
- example: Gaussian distribution to model normal data
- estimate probability of an observation fitting the distribution if low unlikely to be generated and thus an outlier
- Challenge: effectiveness depends on whether statistical assumption holds in real data

# Outlier analysis: proximity methods

- Observation is an outlier if nearest neighbors are far away
- proximity significantly deviates from the proximity of most observations
- Two major approaches: **distance-based** and **density-based**
- example: proximity of an object using 3 nearest neighbors
- **Challenge**: effectiveness highly depends on the distance metric
- in some applications, distances cannot be obtained easily
- difficulty in finding collective outliers

# Outlier analysis: clustering methods

- Principle
- normal data belong to large and dense clusters
- outliers belong to small or sparse clusters
- example: outliers form a tiny cluster (right)
- How? Clustering-based outlier detection methods
- many forms (e.g. DBSCAN)
- Challenge: clustering can be expensive

# Outlier analysis: deep learning methods

- Principle
- train an autoencoder using neural networks
- recall the aim: reconstruct an observation using a bottleneck architecture (relevant for denoising, representation... and detecting outliers!)
- normal observations should be easy reconstructed
- outlier observations have unexpected patterning and thus higher reconstruction error

- Challenge: high NN capacity can expressively model deviant behavior (low reconstruction error)

 

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

# Statistical-based detection (distribution-based)

- assumes that normal data is generated by a distribution with parameters $\theta$
- the probability density function $f(\mathbf{x}|\theta)$ gives the probability of observation $\mathbf{x}$ being generated by the distribution: the smaller, the more likely $\mathbf{x}$ is an outlier
- e.g. univariate outliers in $\{24.0, 28.9, 28.9, 29.0, 29.1, 29.1, 29.2, 29.2, 29.3, 29.4\}$ assuming $\mu + 3\sigma$?
- multivariate case?
- multivariate Gaussian
- naïve Bayes assumption

 FORMÁCÃO AVANÇADA

# Statistical-based detection (histogram-based)

- Model of normal data without a priori distribution
- example (figure)
- a transaction with amount $7,500 is an outlier, since only 0.2% transactions are &gt;$5,000

- Challenge: fix bin size
- too small → normal objects in rare bins, false positive
- too big → outliers in some frequent bins, false negative

Amount per transaction

# Statistical-based detection (depth-based)

## How
- search for outliers at data borders
- observations in convex hull layers
- outliers are observations on outer layers

- Observations with depth ≤ k are outliers
- Basic assumption
- outliers are located at the border of the data space
- normal observations in the center of the data space

## Discussion
- similar to statistical approaches (k=1 distributions) but without a priori distribution
- convex hull computation is usually only efficient in small dimensional spaces (e.g. 3D)
- can be extended for outlier likelihood: depth as scoring value

# Statistical-based approaches

Learn model fitting data, and identify objects in low probability regions

- Two categories
- parametric: distribution-based
- non-parametric: histogram-based and depth-based

- Strengths
- common and effective: many data distributions are well-approximated

- Weakness
- distribution-based: assume the distribution is known
- histogram/depth-based: overfitting to available data

 

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

 

# Proximity-based approaches

- Intuition: observations that are far away from the others are outliers
- Assumption: the proximity of an outlier deviates significantly from that of most of the others in the data set
- Two types of proximity-based outlier detection methods
- distance-based outlier detection:
an observation is an outlier if its neighborhood does not have enough other observations
- density-based outlier detection:
an observation is an outlier if its density is relatively lower than that of its neighbors

 

# Distance-based approaches

- An observation $\mathbf{x}$ in a dataset $X$ is a $(p, d)$-outlier if at least a fraction $p$ of observations in $X$ are $\geq$ distant $d$ from $\mathbf{x}$
- An observation $\mathbf{x}$ in a dataset is a $(k, d)$-outlier if no more than $k$ points in the dataset are at a distance $d$ or less from $\mathbf{x}$
- Distance of the $k^{\text{th}}$ nearest neighbor of $\mathbf{x}$ can be used as an outlier score
- Efficient computation:
- for any observation $\mathbf{x}_i$, calculate its distance to other observations
- if $k = pn$ observations are within $r$ distance, terminate the inner loop: $\mathbf{x}_i$ is normal, otherwise a $(p,d)$-outlier

 

# Density-based approaches

- Local outliers: outliers comparing to their local neighborhoods, instead of the global data distribution
- $o_1$ and $o_2$ are local outliers to $C_1$
- $o_3$ is a global outlier, but $o_4$ is not an outlier
- distance-based clustering insufficient here

- Intuition (density-based outlier detection): the density around an outlier observation is significantly different from the density around its neighbors
- Method: use the relative density of an object against its neighbors
- $k$-distance: distance between observation and its $k$-th NN
- $k$-distance neighborhood: consider the distribution of distance to the $k$ neighbors

# Density-based approaches

Approaches essentially differ in how to estimate density
- density is simply measured by the inverse of the kNN distance
- examples
- local outlier factor (LOF)
- LOF ≈ 1: observation is in a cluster (homogeneous density around the point and its neighbors)
- LOF &gt;&gt; 1: point is an outlier
- connectivity-based outlier factor (COF)
- motivation: in regions of low density, it may be hard to detect outliers
- how: treat "low density" and "isolation" differently (take the ε-neighborhood instead of kNN)
- test multiple resolutions (varying ε)

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

 

# Clustering approaches

- Observation is an outlier:
- not belong to any cluster
- density-based clustering method such as DBSCAN
- far from its closest cluster
- partitioning-based clustering such as k-means
- for each observation, assign an outlier score based on its distance from its closest center
- if dist/averageDist is large, likely an outlier
- belongs to a small or sparse cluster

# Clustering approaches

- (cont.) small or sparse clusters
- FindCBLOF: find clusters, sort them in decreasing size, compute statistic to detect significantly size differences
- Pros and cons of clustering-based approaches
- strengths
- work for many types of data (clusters regarded as summaries)
- not requiring any labeled data
- efficiency in detecting outliers once the cluster are obtained
- weakness
- effectiveness highly depends on the clustering method
- clustering can be costly

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

# Deep Learning approaches

Recall: autoencoders for reconstructing inputs, i.e. $\mathbf{x} \approx d(g(\mathbf{x}))$

- goal: learn the parameters of the encoder $g\colon X \to Z$ and decoder $d\colon Z \to X$ minimizing a reconstruction loss such as $\| \hat{\mathbf{x}} - \mathbf{x} \|^2$ where $\hat{\mathbf{x}} = d(g(\mathbf{x}))$
- premise: deviant behaviors are harder to reconstruct
- principle: reconstruction loss as a proxy for outlier likelihood

- Pros: inherent ability to handle complex data without an explicit data representation step
- dense, recurrent, convolutional, transformer-based layering for multivariate, temporal, spatial, text content

- Cons: expressivity needs to be controlled (e.g. ensuring compact bottleneck) to avoid high capacity to reconstruct outliers

# Outline

- Motivation
- Learning paradigms
- Statistical approaches
- Proximity-based approaches
- Clustering approaches
- Deep learning approaches
- Other approaches

# Supervised approach: one-class model

- Idea: in the presence of labeled data, train a classification model that can distinguish "normal" data from outliers
- Problem: training set is typically heavily biased (normal observations far exceeds outliers)
- Possible solution: one-class model
- learn classifier to describe only the normal class.
- learn the decision boundary of the normal class (e.g. using SVM)
- observations that do not belong to the normal class (not within the decision boundary) declared as outliers
- Advantage: detect new outliers that may not appear close to any outlier in training data
- Extension: Normal objects may belong to multiple classes

 

# Supervised approach: multi-task learning

## Hybrid neural networks

- combining supervision and unsupervision (autoencoders)
- single encoder
- two decoders
- dedicated path for the supervised outlier detection task, other for reconstruction
- parameters of decoders updated simultaneously or alternatively
- going beyond two dedicate paths... exploring synergies with other (un)supervised tasks

# Semi-supervised approaches

## How

- semi-supervised classification (e.g. pseudo-labeling)
- semi-supervised clustering (e.g. membership constraints)
- any object that does not fall into the model for $C$ (such as $a$) is considered an outlier as well

## Pros and cons

- strengths: efficient, effective
- bottlenecks:
- quality heavily depends on the availability and quality of train data
- difficult to obtain representative and high-quality training data

- objects with label "normal"
- objects with label "outlier"
- objects without label

 

# Outlier analysis in high-dimensional data

## Challenges
- distance between observations becomes heavily dominated by noise
- data in high-dimensional spaces are often sparse
- interpretation of outliers: detecting outliers without saying why they are outliers is not very useful in high-dim data due to many involved features

## Solutions
- use more robust distance functions and find full-dimensional outliers
- find outliers in projections of the original feature space: dimensionality reduction works only when in lower-dimensional spaces normal instances can still be distinguished from outliers
- PCA: components with low variance preferred since normal observations are likely close to each other and outliers often deviate from majority
- use supervised reduction whenever possible

 

# Outlier analysis in high-dimensional data

- HilOut: distance-based detection, yet uses ranks instead of absolute distances
- subspaces: find outliers in multiple lower dimensional subspaces: easy to interpret
- ABOD: angle-based outlier degree
- angles are more stable than distances in high dimensional spaces
- observation is outlier if most others are located in similar directions

# Outlier analysis on temporal data

Simple extension of traditional outlier detection techniques:

- learn good representations of time series data and apply previous techniques
- apply time series clustering and remove
- observations untagged by density-based clustering approaches
- observations belonging to very small clusters or clusters with loose silhouette
- model time series distributions (centroid or class-conditional "prototype" time series) and test expectations (how well a time series is described by the distribution)

Please note that novelty detection in a single time series (left image) differs from novelty detection in time series data (above)

# Summary

- Outlier analysis aims to detect observations deviating from expectations
- outliers either inconsistent with the rest data (global) or neighbors (local)
- outliers can deviate in a given context, and appear in a group (collective)

- Given labeled examples, outlier analysis can be solved using **classification** with imbalanced classes (supervised) or guided by **semi-supervised** clustering

- **Statistical** approaches assume data is generated by a distribution to test the likelihood of an observation to be generated by the approximated distribution

- In **proximity-based** approaches, outliers have distant nearest neighbors or a density differs from the density around neighbors

- Small, compact **clusters** or unclustered observations also seen as outliers

- **Deep learning** offer expressive measures of unexpected behaviors from **reconstruction loss**

- Variants of outlier analysis for temporal data and high-dimensional data

Rui Henriques

---

## Lecture 8: Pattern Discovery: Introduction

*Source: 07a PatternDiscovery*

---
# Pattern Discovery: Introduction

Classic stances on pattern and association rule mining

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive and negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Patterns everywhere!

Frequently Bought Together
This item: Face tape™ foundation
$40.00

+ Liquid Touch Foundation Brush
$27.00

+ Breezy cream blush &amp; bronzer palette
$35.00

# Pattern Recognition

- Patterns are local relationships in data, often yielding informative and predictive power
- statistical regularities: correlations, trends, discriminative associations...
- structural relationships: sequences, hierarchies, spatiotemporal layouts (e.g. word order in text, shapes in images)...
- latent representations: hidden features that efficiently summarize content...
- Locality in reference to the extent of the content space (e.g., subset of features, time, text, space)
- Pattern recognition underlies all learning tasks by humans and machines
- prediction: patterning used for driving? Image classification? Question answering?
- description: patterning used for clustering behaviors? Describing series? Detecting outliers?

 

# Pattern Recognition

- Why patterns matter:
- artificial agents do not understand meaning directly
- patterns offer a way to minimize (descriptive or predictive) error on observed data
- good generalization capacity if those patterns also hold in unseen data
- useful patterns (signals) → generalize
- spurious patterns (noise) → overfitting

- Patterns seem to be everything and nothing!
- indeed pattern recognition became a proxy name to machine learning

Classification

Clustering

# Pattern Discovery

- Patterns form the ground for knowledge acquisition
- yet, to this end, we need to be able to access and interpret them
- problem: many patterns in ML are not clearly defined or easily interpretable (e.g. latent patterning in neural networks)

- Two paradigms: recognition of implicit versus explicit patterns
- for descriptive ends: we want to move toward explicit patterns
- well-defined and human-understandable (easy to inspect and validate)
- e.g. if-then rules in decision trees, handcrafted features (e.g. "knee angle &gt; θ"), ...
- Pattern discovery: subfield of ML dedicated to the retrieval of (explicit) patterns

 

# Pattern Discovery

- From now on: **patterns** as local relationships in data that are both *explicit* and *relevant*
- What makes a pattern **relevant**?
- statistical significance (# spurious)
- actionability (ability to be used to guide decisions in a given domain)
- non-triviality and novelty (can expand existing knowledge)
- informative power (e.g. summarization capacity) and/or predictive power
- non-redundancy (with other patterns in voluminous solutions)
- Pattern mining: discovery of all relevant patterns in a given dataset

 

# Patterns everywhere!

- Different data structures ⇒ different patterns
- multivariate patterns: co-occurring features, e.g. (age &gt; 50 ∨ BMI &gt; 35) ∧ drug = A
- transactional patterns: itemsets, e.g. {milk, bananas}
- vision patterns: edges, textures, shapes, object parts
- language patterns: syntactic structures, semantic associations, phrase usage
- temporal patterns: trends, motifs, cycles, anomalies
- and more...
- graph patterns: subgraphs, e.g. social communities
- relational patterns: associations spanning multiple tables, e.g. buys(y, x) ∧ retailer(z, y)
- spatiotemporal patterns, multi-event patterns...

# Why mining patterns?

- Acquiring knowledge from non-trivial and actionable patterns
- classic: basket analysis, cross-marketing, web navigation, DNA sequence analysis, catalog design, sales campaign...
- Patterns further form the foundation for many essential data mining tasks
- multivariate association and causality analysis
- feature extraction from complex data
- e.g. patterns in media, spatiotemporal, stream data as features
- prediction: associative classifiers and regressors
- clustering: pattern-based clustering (e.g. shapelet-based clustering)
- semantic data compression (e.g. fascicles)

 

# Applications

- social networks: communities of individuals with shared interests, correlated activity and/or coherent intercommunication; content aggregation from comments and tags
- text data: group content-related documents to support searches, suggestions and tagging
- e-commerce: browsing and shopping patterns
- financial/trading: profitability patterns for buy/hold/sell trading points
- collaborative filtering: groups of users with similar preference patterns
- omics data: functional processes and pathways
- physiological data: patient groups with coherent stimuli- or disease-conditional responses
- clinical data: risk profiles from health records
- biological networks: modules of correlated genes, proteins or metabolites

 

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive and negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Origins... basket analysis

- Some of the origins of pattern mining resort back to market basket analysis...
- A transactional database is a set of transactions
- each transaction (basket) is a set of items
- Patterns often given by:
- frequent itemsets, i.e. co-occurring items in a number or percentage of transactions
- association rules, i.e. items that discriminate occurrence of other items
- Accordingly, frequent itemset mining (FIM) and association rule mining (ARM) aim at finding all those patterns

|  ID | Items  |
| --- | --- |
|  1 | {Bread, Milk}  |
|  2 | {Bread, Diapers, Beer, Eggs}  |
|  3 | {Milk, Diapers, Beer, Cola}  |
|  4 | {Bread, Milk, Diapers, Beer}  |
|  5 | {Bread, Milk, Diapers, Cola}  |
|  ... | ...  |

{Diapers, Beer} Example of a frequent itemset
{Diapers} → {Beer} Example of an association rule

… extended to multivariate data

Patterns given by:

- value expectations on a subset of variables
- the pattern coverage is the set of observations satisfying those expectation
- the pattern defines a subspace
- association rules, i.e. values on some variables that discriminate the values on other variables
- supervised setting: input features in the antecedent and outcomes in the consequent
- unsupervised setting: free associations between input features

# Frequent vs relevant patterns

- Considering the itemset {water, potatoes}
- Can it be considered frequent if its support is 5%? 20% 50%?
- What about the itemset {diapers, flowers}?

- Challenge: impossible to define a single support threshold as item probabilities highly vary!
- same challenge in multivariate data (e.g. brown skin and blue eyes)
- implication: frequency is not good proxy for relevance
- e.g. the pattern "dog bites human" is as frequent as "human bites dog" on a given dataset, yet the latest is much less expected so surely more important!

- Replace frequency by statistical significance

 

# Statistically significant patterns

- Considering a transactional database of 1000 baskets
- the probability of a user buying water is 30% and buying potatoes is 10% (probabilities directly estimated from the database)
- what is the null joint probability of buying $\varphi = \{\text{water, potatoes}\}$?
Under independence assumption:
$$
p_{\text{null}}(\varphi) = p_{\text{null}}(\text{water} \cap \text{potatoes}) = p(\text{water}) \times p(\text{potatoes}) = 0.3 \times 0.1 = 0.03
$$

- Assuming that we observe 35 baskets in the database with water and potatoes: Is $\{\text{water, potatoes}\}$ statistically significant?
- to answer this, we need to test "Given $N = 1000$, what is the probability of at least $n = 35$ users buying water and potatoes knowing $p_{\text{null}} = 0.03$?"

# Statistically significant patterns

- Given $N = 1000$, what is the probability of observing at least $n = 35$ users buying water and potatoes with $p = 0.03$?

- can be answered by computing the tail of a Binomial, i.e. $p(n &gt; 35 \mid n \sim \text{Binomial}(N, p))$
- $p(n \geq 35) = 0.15$, as 0.15 is above reference significance levels (0.05 or 0.01) for statistical tests, we can say that is not unexpectedly low and therefore not relevant
- if $n = 50$, then $p(n \geq 50) = 2.37E-4$, hence {water, potatoes} is relevant in such dataset

- Summary: joint probability and binomial testing to assess relevance

- How? scipy in python, excel...
- 1 – cumulative Binomial with $n$, $N$ and $p$ parameters (also known as survival function)

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Rare and negative patterns

- Why to solely pursue unexpectedly frequent patterns (aka positive patterns)?
- As we moved from clusters to anomalies...
... we can move from unexpectedly frequent to unexpectedly infrequent patterns

- Rare patterns
- very low support but interesting (e.g. buying diamond)

- Negative pattern
- patterns that are unexpectedly rare (instead of frequent)
- example: buying Ford Expedition (SUV car) and Toyota Prius (hybrid car) together is unlikely since Ford Expedition and Toyota Prius are negatively correlated
- rare/infrequent negative patterns can even be more interesting than frequent ones!

# Negative patterns

- Support-based definition
- If patterns $P1$ and $P2$ are both frequent or significant, yet rarely occur together, i.e., $\sup(P1 \cup P2) \ll \sup(P1) \times \sup(P2)$
- then $P1$ and $P2$ are negatively correlated
- Example: a store sells needles $A$ and $B$, with $p(A) = p(B) = 0.5$
- assuming only one transaction contained both $A$ and $B$
- when there is a total of 200 observations, $\sup(A) \times \sup(B) = 0.25$ and $\sup(A \cup B) = \frac{1}{200} = 0.005 &lt; \sup(A) \times \sup(B)$
- Other definitions available, e.g. Kulzynski-based definition
- If patterns $P1$ and $P2$ are frequent, yet $(P(P1|P2) + P(P2|P1))/2 &lt; \epsilon$, then $P1$ and $P2$ are negatively correlated

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Association rules

- Recall the concept of an association rule, $R: A \Rightarrow B$
- where $A$ is the antecedent (set of features) and $B$ is the consequent (set of features or outcomes)
- if $B$ is an outcome of interest, $R$ is also termed discriminative pattern

- Considering the following transactional database
- $\varphi = \{\text{Socks}, \text{Tie}\}$ is an itemset with coverage $\{T1, T2\}$, support 0.5, and $p$-value (Binomial test with $n=2$, $N=4$ and null probability $p(\varphi) = \frac{3}{4} \times \frac{3}{4} = 0.56$) of 0.4, hence not unexpectedly frequent
- What about Socks $\Rightarrow$ Tie? Is it relevant?

|  T1 | Shoes,Socks,Tie  |
| --- | --- |
|  T2 | Shoes,Socks,Tie,Belt,Shirt  |
|  T3 | Shoes,Tie  |
|  T4 | Shoes,Socks,Belt  |

# Association rules in multivariate data

Association have been further classified into different categories:

- Boolean association rule
$$
\text{Keyboard} \Rightarrow \text{Mouse} [\sup=6\%, \text{conf}=70\%]
$$
- the choice in transactional, sequential and categorical multivariate data

- Quantitative association rule
$$
\text{Age} \in [26,30] \Rightarrow \text{Cars} \in \{1,2\} [\sup=3\%, \text{conf}=36\%]
$$
- the choice in numeric data

- Hybrid association rules
$$
\text{Age} \in [26,30] \land \text{Keyboard} \Rightarrow \text{Mouse} \in \{1,2\}
$$
- the choice in mixed multivariate data, transactions with numeric outcomes, etc.

# Association rules are already familiar…

- Recall: **decision trees** for prediction
- each path from root to leaf is an association rule
- **classification** (classes on leaves) and **regression** (quantities on leaves)

# Association rules are already familiar…

|  Name | Hair | Height | Weight | Lotion | Result  |
| --- | --- | --- | --- | --- | --- |
|  Sarah | blonde | average | light | no | sunburned (positive)  |
|  Dana | blonde | tall | average | yes | none (negative)  |
|  Alex | brown | short | average | yes | none  |
|  Annie | blonde | short | average | no | sunburned  |
|  Emily | red | average | heavy | no | sunburned  |
|  Pete | brown | tall | heavy | no | none  |
|  John | brown | average | heavy | no | none  |
|  Katie | blonde | short | light | yes | none  |

If the person's hair is blonde and the person uses lotion then nothing happens

If a person's hair color is blonde and the person uses no lotion then the person turns red

If the person's hair color is red then the person turns red

If the person's hair color is brown then nothing happens

# Relevant association rules

- Any given association rule, e.g. $A \Rightarrow B$, can be further characterized by its:
- **support**, fraction of observations that satisfy the rule, i.e. $\sup(A \Rightarrow B) = \sup(A \cap B)$
- **confidence**, fraction of observations with the antecedent in which the consequent is also satisfied, i.e.

$$
\mathrm{confidence}(A \Rightarrow B) = P(B|A) = \frac{P(A \cap B)}{P(A)} = \frac{\mathrm{support}(A \Rightarrow B)}{\mathrm{support}(A)}
$$

- Recovering R: $\{\mathrm{Socks}\} \Rightarrow \{\mathrm{Tie}\}$
- support of R is 50% (2/4)
- confidence of R is 66.67% (2/3)
- are the observed support and confidence high enough? Is the rule relevant?

|  T1 | Shoes, **Socks, Tie**  |
| --- | --- |
|  T2 | Shoes, **Socks, Tie**, Belt, Shirt  |
|  T3 | Shoes, Tie  |
|  T4 | Shoes, Socks, Belt  |

# Relevant association rules

- Example: among 5000 students
- 3000 play basketball
- 3750 eat cereal
- 2000 both play basketball and eat cereal

- play basketball ⇒ eat cereal [sup=40%, conf=66.7%]
- Misleading! Overall percentage of students eating cereal is 75%, higher than 66.7%
- play basketball ⇒ not eat cereal [sup=20%, conf=33.3%]
- Far more accurate! Although lower support and confidence!

- How to more accurately measure a rule's relevance?

|   | basketball | not basketball  |
| --- | --- | --- |
|  cereal | 2000 | 1750  |
|  not cereal | 1000 | 250  |

# Interestingness: lift

- Lift measures the discriminative power (also known as surprise) of the rule

$$
lift(A \Rightarrow B) = \frac{P(B|A)}{P(B)} = \frac{P(A \cap B)}{P(A) \times P(B)}
$$

- in contrast with confidence, takes into account the probability of the consequent
- in fact, $\operatorname{lift}(A \Rightarrow B) = \frac{\operatorname{conf}(A \Rightarrow B)}{P(B)}$

- lift &lt; 1: A and B negatively correlated, if the value is less than 1
- the higher, the greater the relevance of the rule

- lift &gt; 1: A and B are positively correlated

- lift = 1: A and B are independent, $P(A \cap B) = P(A)P(B)$

# Interestingness

- Classic pattern mining methods define simplistic thresholds:
- FIM aims at finding all patterns satisfying a minimum support threshold
- ARM aims at finding all rules satisfying a minimum support and confidence
- rules satisfying both thresholds are called **strong**

- Modern pattern mining methods further consider:
- statistical significance criteria
- e.g. p-value&lt;0.1 under binomial test from null data model)
- interestingness criteria, e.g. lift&gt;1.3...

|  X | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Y | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0  |
|  Z | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1  |
|  Rule | Support | Lift  |
| --- | --- | --- |
|  X⇒Y | 25% | 2  |
|  X⇒Z | 37.50% | 0.9  |
|  Y⇒Z | 12.50% | 0.57  |

# Interestingness

- many other possibilities...
- DISA is a Python package that implements most of them:

https://github.com/JupitersMight/DISA

|  symbol | measure | range | formula  |
| --- | --- | --- | --- |
|  φ | φ-coefficient | -1...1 | P(A,B)-P(A)P(B)  |
|  Q | Yule's Q | -1...1 | √P(A)P(B)(1-P(A))(1-P(B))P(A,B)P(A,B)-P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  Y | Yule's Y | -1...1 | √P(A,B)P(A,B)-√P(A,B)P(A,B)√P(A,B)P(A,B)+√P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  k | Cohen's | -1...1 | P(A,B)+P(A,B)-P(A)P(B)-P(A)P(B)1-P(A)P(B)-P(A)P(B)  |
|  PS | Piatetsky-Shapiro's | -0.25...0.25 | P(A,B)-P(A)P(B)  |
|  F | Certainty factor | -1...1 | max(P(B|A)-P(B), P(A|B)-P(A))1-P(B), P(A|B)-P(A))  |
|  AV | added value | -0.5...1 | max(P(B|A)-P(B), P(A|B)-P(A))  |
|  K | Klosgen's Q | -0.33...0.38 | √P(A,B)max(P(B|A)-P(B), P(A|B)-P(A))ΣjmaxkP(Aj,Bk)+ΣkmaxjP(Aj,Bk)-maxjP(Aj)-maxkP(Bk)ΣjΣjP(Aj,Bj)log P(Aj,Bj)max(P(Aj,Bj)min(-ΣjP(Aj)log P(Aj)log P(Aj)-maxjP(Aj))  |
|  g | Goodman-kruskal's | 0...1 | ∑jΣjP(Aj,Bj)log P(Aj)-maxjP(Aj)max(P(Aj,Bj)min(-ΣjP(Aj)log P(Aj)log P(Aj)-maxjP(Aj))  |
|  M | Mutual Information | 0...1 | max(P(A|P(B|A)+P(A|B)-P(A|B)+P(A|B)-P(A|B)+P(A|B))  |
|  J | J-Measure | 0...1 | max(P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)-P(A|B)  |
|  G | Gini index | 0...1 | max(P(A|P(B|A)+P(A|B)-P(A|B)+P(A|B)-P(A|B)-P(A|B))  |
|  s | support | 0...1 | P(A,B)  |
|  c | confidence | 0...1 | max(P(B|A), P(A|B))  |
|  L | Laplace | 0...1 | max(NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)+1/NP(A,B)  |
|  IS | Cosine | 0...1 | √P(A,B)  |
|  γ | coherence(Jaccard) | 0...1 | √P(A,B)P(A)P(B)-P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  α | all_confidence | 0...1 | max(P(A|P(B), P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))  |
|  o | odds ratio | 0...∞ | P(A,B)P(A)P(B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  V | Conviction | 0.5...∞ | max(P(A|P(B), P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))P(A|P(B))  |
|  λ | lift | 0...∞ | P(A,B)P(A)P(B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A,B)P(A)  |
|  S | Collective strength | 0...∞ | ∑i(P(A,i)-Ei)2Ei  |

#

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Pattern mining challenges

- There is usually a massive number of patterns on real-life databases
- thousands or hundreds of thousands!
- How to handle large pattern sets?
- pursuing condensed representations
- returning dissimilar patterns only
- filtering less relevant patterns
- outputting top patterns only
- using background knowledge to guide the mining process
- focusing the process according to user expectations and available knowledge

# Condensed patterns

- A long pattern contains a combinatorial high number of subpatterns
- Example: $\varphi = \{yi_{1,\dots}, yi_{100}\}$ contains $\binom{100}{2} + \binom{100}{3} + \cdots + \binom{100}{99} = 1.27 \times 10^{30}$ sub-patterns!

- Solution:
- Mine closed patterns or maximal patterns only
- A pattern $P1$ is **maximal** if $P1$ is frequent and there exists no frequent super-pattern $P2 \supset P1$
- A pattern $P1$ is **closed** if $P1$ is frequent and there exists no super-pattern $P2 \supset P1$, with the same support as $P1$

# Condensed patterns: maximal and closed

- Given a pattern $\varphi$
- a subspace with a smaller pattern, $|\varphi(B1)| &lt; |\varphi(B3)|$, generally has more supporting observations (vertical shape)
- a subspace with a larger pattern, $|\varphi(B3)| &gt; |\varphi(B2)|$, generally has lower coverage (horizontal shape)

- In the right example:
- Closed patterns? B1 and B3
- Maximal patterns? B3

- Closed representations is a lossless compression of patterns
- default representation when pattern mining

- Maximal pattern representations can cause the loss of relevant patterns
- vertical shaped patterns are generally neglected in preference towards horizontal ones

# Other patterns

- Top **k** patterns
- compact pattern solution w.r.t. significance, interestingness, dissimilarity (redundancy-aware)
- Generative pattern-based models
- concise graphical models that explain a set of patterns
- Contrast patterns from two datasets
- pattern-centric highlighting of differences
- Noisy (fault-tolerant) patterns
- supporting observations accommodate a parameterizable number or percentage of errors
- Mining truly interesting patterns:
- incorporating (domain-driven) measures of actionability, surprise, novelty...
- Mining emerging patterns:
- considering recency weighting in stream or temporal data

 

# Efficient pattern mining

- Exhaustive discovery of patterns is a highly computational heavy task
- Principle to boost efficiency: downward closure property
- any subset of a frequent pattern is also frequent
- if {beer, diaper, nuts} is frequent, so is {beer, diaper}
- i.e., transactions with {beer, diaper, nuts} also contain {beer, diaper}
- Three major approaches mining approaches (details in Appendix)
- Apriori family (Agrawal and Srikant)
- FP-growth family (Han, Pei &amp; Yin)
- Vertical family (Charm and Zaki)

# Association rule mining

- Association rules can be exhaustively generated from the found patterns with PM approaches
- efficiently combine disjoint patterns on the antecedent/consequent
- efficiently test interestingness criteria
- Upper bounds to the pattern length in the consequent can be imposed
- What if we have outcomes of interest?
- patterns can be found within each outcome-conditional dataset
- yet one pattern can be statistically significant for multiple outcomes
- solution: post-test the discriminative power of each rule $P \Rightarrow$ outcome (e.g. lift)
- straightforward PM extension to impose variables of interest to appear in the consequent

# Colossal patterns

- Colossal patterns are lengthy patterns
- generally yield higher importance than small patterns
- Many real-world tasks need mining colossal patterns
- high-dimensional data domains (biomedicine, text/media, social networks...)
- Problem: a subpattern of a frequent pattern is frequent, data with lengthy patterns have an explosive set of patterns 😊
- the downward property of classical approaches is insufficient
- whether we use breadth-first search (e.g. Apriori) or depth-first search (e.g. FPgrowth)
- closed/maximal patterns partially alleviate, yet not solve
- still need to find scattered large patterns

 

# Pattern fusion

- Philosophy: jump out of the swamp of mid-sized patterns and quickly reach colossal patterns
- mid-sized patterns are called **core patterns**
- a colossal pattern is composed by multiple **core patterns** and a few **small-sized patterns**

- Pattern Fusion is an approach to this end using tree structures
- traverses the tree in a bounded-breadth way, only expands a bounded-size candidate pool
- only a fixed number of patterns are used as starting nodes — avoiding the exponential search space
- identifies "shortcuts" whenever possible (e.g. agglomeration of patterns in the pool)
- pattern fusion shortcuts will direct the search down the tree much more rapidly towards the colossal patterns

 

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Quantitative and multi-level associations

- Major problems of classic pattern mining?
- unable to deal with **numeric data**
- solution: discretization
- problems?
- discretization is susceptible to item-boundary problems
- loss of expressivity
- unable to handle with the **multi-level** and **multi-dimensional** structure of data
- e.g. different types of potatoes, different milk brands – generalize or specialize?

- Handling these problems
- **biclustering** (next class!) and **quantitative associations**
- multi-level and multi-dimensional associations

 

# Quantitative associations

- Simplistic preprocessing strategies
- static discretization based on predefined concept hierarchies (manual)
- dynamic discretization
- based on variable distribution (simple)
- such that the confidence or compactness of the rules mined is maximized (advanced)
- one-dimensional clustering: distance-based association
- Under these strategies, classic pattern mining is applied on the found numeric ranges
- problems of discretization?
- what about non-constant patterns?
- to be covered in the next class

 

# Quantitative associations

- Two major forms of association rules:
- categorical ⇒ quantitative rules or quantitative ⇒ quantitative rules
- e.g. education in [14-18] (yrs) ⇒ mean wage = $11.64/h

- Finding extraordinary and therefore interesting phenomena, e.g.
$$
\text{sex} = \text{female} \Rightarrow \text{wage: mean} = \$7 \text{ (overall mean} = \$9\text{)}
$$

- LHS: a subset of the population
- RHS: an extraordinary behavior of this subset

- The rule is accepted if a statistical test (e.g. Z-test) confirms inference with high confidence

- Subrule: highlights the extraordinary behavior of a pop. subset of the super rule, e.g.
$$
(\text{sex} = \text{female}) \wedge (\text{south} = \text{yes}) \Rightarrow \text{mean wage} = \$6.3/h
$$

- Open problem: efficient methods for LHS containing two or more quantitative attributes

# Multi-level associations

- Items in transactional databases or categories in multivariate data often form hierarchies
- Flexible support settings: items at the lower level are expected to have lower support

- some rules may be redundant due to "ancestor" relationships between items. Example
- milk ⇒ wheat bread [support = 8%, confidence = 70%]
- fat milk ⇒ wheat bread [support = 2%, confidence = 72%]

- we say the first rule is an ancestor of the second rule
- a rule is redundant if its support is close to the "expected" value based on rule's ancestor

# Multi-dimensional associations

- Single-dimensional rules:
- buys(X, milk) ⇒ buys(X, bread)
- Multi-dimensional rules: ≥2 dimensions or predicates
- Inter-dimension association rules (no repeated predicates)
- age(X, [19,25]) ∧ occupation(X, student) ⇒ buys(X, coke)
- Hybrid-dimension association rules (repeated predicates)
- age(X, [19,25]) ∧ buys(X, popcorn) ⇒ buys(X, coke)
- How to? Data cube approaches

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Constrained pattern mining

- Finding all the patterns in a database autonomously? Unrealistic!
- the patterns could be too many but not focused
- what makes a truly interesting pattern?

- Available domain knowledge can be used to guide the pattern discovery
- ideally we can formalize background knowledge using constraints

- A constraint is a predicate in the data space
- Given a dataset and a set of constraints $C$, the problem of **constrained pattern mining** is the discovery of all relevant patterns satisfying $C$
- Simplistic examples:
- metric constraints, e.g. lift $&gt; \theta$
- value/item constraints, e.g. specific features to be included/excluded from patterns

 

# Constrained pattern mining

## Meta-rule constraints

- partially instantiated predicates and constants, example:
- $P1(x,Y) \land P2(x,W) \Rightarrow \mathrm{buys}(x,iPad)$
- pattern satisfying this constraint: $age(x, [15,25]) \land job(x, student) \Rightarrow \mathrm{buys}(x, iPad)$
- How? push constants deeply when possible into the mining process

## Other constraints:

- knowledge type constraint: known classification, association, etc.
- query constraint: e.g. "find product pairs sold together in stores in Chicago"
- dimension/level constraint: in relevance to region, price, brand, customer category

## Recall: data mining should be an interactive process

- user directs what to be mined using a data mining query language

# Constrained pattern mining

- Domain-driven constraints:
- user flexibility: provides constraints on what to be mined
- system optimization: explores such constraints for efficient mining. How? Below

- Pattern space pruning constraints
- anti-monotonic: if constraint $c$ is violated, its further mining can be terminated
- monotonic: if $c$ is satisfied, no need to check $c$ again
- succinct: $c$ must be satisfied, so one can start with the data sets satisfying $c$
- convertible: $c$ can be mapped into (anti-)monotonic $c$ when values are properly ordered

- Data space pruning constraints
- data succinct: data space can be pruned at the initial pattern mining process
- data anti-monotonic: if an observation does not satisfy $c$, it can be pruned

 

# Outline

- Pattern discovery
- Statistically significant patterns
- Positive vs negative patterns
- Association rules
- Efficient pattern mining
- Quantitative and multi-level patterns
- Knowledge incorporation
- Final remarks

 

# Remarks

- Until here... we have tapped into patterns in multivariate and transactional data structures
- Two notes of care
- check if pattern discovery offers a way to answer your problem
- remember that pattern discovery is primarily used for **descriptive ends** ⇒ check next slide
- although it can be used for **predictive ends** ⇒ check next class (associative learning)
- methods can be hard to scale for high-dimensional data with extensive feature dependencies
- practical principles to boost the search
- reduce dimensionality
- handle redundant variables (remove, combine...)
- remove highly frequent categories
- when discretizing data opt for qcut (equal frequency) over cut (equal width)
- ...

 

# Remarks

Check if explicit patterns are the best solution to our problem! An illustrative example:

- Recommendation problems span our daily lives: shopping, media, webpage, document suggestions ... and pattern discovery can be used to retrieved frequently co-accessed, co-bought, co-liked items 😊
- Yet... not all recommendation tasks need to be answered using pattern discovery
- we need to separate description (knowledge acquisition) from prediction
- user-specific recommendations can be answered using predictive tasks
- predict a set of outputs from a set of input features that characterize user behavior
- each output corresponds to a measure interest (binary/numeric) of a user on a given item
- items/outputs are then ranked based on the estimated interest to deliver recommendations
- what about recommendations not custom to single users (e.g. market shelf display, privacy-aware web navigation rules...)? Yes, patterns offer here important rules and descriptive insights!
- Yet our preferences change over time, so...

 

# Complex data structures

- Moving beyond multivariate and transactional data...
- Recall: different data structures ⇒ different patterns
- temporal patterns: trends, motifs, cycles, anomalies
- vision patterns: edges, textures, shapes, object parts
- language patterns: syntactic structures, semantic associations, phrase usage
- graph patterns: subgraphs, e.g. social communities
- relational patterns: associations spanning multiple tables, e.g. buys(y, x) ∧ retailer(z, y)
- spatiotemporal patterns: flocks, trajectories, colocation
- multi-event patterns: episodes, dependency graphs

Details in our next class!

# Complex data: a snippet

A snippet view on patterns in temporal data structures where **frequency** can be considered...

- **across** time series observations
- sequential pattern mining (frequent orders)
- biclustering (univariate time series data)
- triclustering (multivariate time series data)
- temporal association rules

- **within** a single time series
- motif discovery
- predictive rule mining A ⇒ Δt B

once antecedent is observed, consequent expected within interval Δt

Rui Henriques

# APPENDIX

# Apriori

- Principle: if a pattern is infrequent, its superset is infrequent (should not be generated)
- Method: iteratively increase (k+1)-length candidate patterns from k-length frequent patterns

database

|  Tid | Items  |
| --- | --- |
|  10 | A, C, D  |
|  20 | B, C, E  |
|  30 | A, B, C, E  |
|  40 | B, E  |

# Improving Apriori

- Challenges
- multiple scans of transaction database
- huge number of candidates
- workload of support counting for candidates

- Improving Apriori: general ideas
- reduce passes of transaction database scans
- shrink number of candidates
- facilitate support counting of candidates
- implementation available for relational databases using object-relational extensions
- distribution and parallelization

# FP-Growth

- Bottlenecks of Apriori
- multiple database scans are costly
- long patterns generate lots of candidates
- recall $\varphi = \{y_{i1}, y_{i100}\}$ contains $1.27 \times 10^{30}$ patterns
- Can we avoid candidate generation?
- Yes! using Frequent Pattern (FP) tree structure (avoid further data scans) and pattern-conditional trees to efficiently grow patterns
- FP-Growth approach
- for each frequent itemset, construct its conditional pattern-base and FP-tree
- repeat the process on each newly created conditional FP-tree

 

# FP-Growth

|  TID | Items bought | (ordered) frequent items  |
| --- | --- | --- |
|  100 | {f, a, c, d, g, i, m, p} | {f, c, a, m, p}  |
|  200 | {a, b, c, f, l, m, o} | {f, c, a, b, m}  |
|  300 | {b, f, h, j, o, w} | {f, b}  |
|  400 | {b, c, k, s, p} | {c, b, p}  |
|  500 | {a, f, c, e, l, p, m, n} | {f, c, a, m, p}  |

- divide-and-conquer
- decompose the mining task according to the frequent patterns obtained so far
- leads to focused search of smaller databases
- no candidate generation, no candidate test
- no repeated scans of entire database
- compressed database: FP-tree structure
- efficient counting operations on the FP-tree

# Vertical approaches

- Problem: high-dimensionality
- Apriori and FP-Growth are computationally heavy for spaces with thousands of variables

- Solutions:
- scalability extensions
- vertical partitioning of the dataset, followed by efficient pattern fusion
- parallelization of operations
- vertical pattern mining approaches (e.g. ECLAT) – flip/transpose the view:
- items and categoric features have a list of observation IDs
- pattern growth by intersecting observation IDs (instead of large sets of items)

 

# Mining maximal patterns

- 1st scan: find frequent items
- A, B, C, D, E
- 2nd scan: find support for
- AB, AC, AD, AE, ABCDE
- BC, BD, BE, BCDE ← candidate max-patterns
- CD, CE, DE, CDE

|  ID | items  |
| --- | --- |
|  10 | A,B,C,D,E  |
|  20 | B,C,D,E,  |
|  30 | A,C,D,F  |

- Since BCDE is a max-pattern, no need to check BCD, BDE, CDE in later scan
- Principles combined in Apriori and FP-Growth approaches

# Mining closed patterns (CLOSET)

- Recall: closed representations are lossless
- useful to remove subspaces contained in large ones
- relevant for large patterns and spaces with high homogeneity
- List of all frequent items in support ascending order, e.g. $d$-$a$-$f$-$e$-$c$
- Divide search space
- patterns having $d$
- patterns having $d$ but no $a$, etc.
- Find frequent closed pattern recursively
- every transaction having $d$ has $cfa$, hence $cfad$ is a closed pattern

min support =2

|  ID | items  |
| --- | --- |
|  10 | a, c, d, e, f  |
|  20 | a, b, e  |
|  30 | c, e, f  |
|  40 | a, c, d, f  |
|  50 | c, e, f  |

---

## Lecture 9: Subspace clustering for pattern discovery

*Source: 07b SubspaceClustering v2*

---
# Subspace clustering for pattern discovery

# Outline

- Subspace clustering
- Biclustering
- coherence
- quality
- structure
- evaluation
- searches
- Triclustering
- Deep learning
- Appendix

 

# Why subspace clustering?

- Find patterns on real-valued data
- classic pattern mining (e.g. FIM, ARM) suffer from discretization drawbacks
- Find less-trivial patterns with non-constant homogeneity
- classic pattern mining is only able to find constant patterns (i.e. simple repetitions)
- Other applications
- well-established role in predictive tasks using discriminative patterns
- dimensionality reduction by reducing data into a set of informative or/and discriminative subspaces
- imputation of missings taking into consideration a subspace's homogeneity
- ...

 

# Motivation

|  2 2 2
2 2 3
2 ? 2 | Constant overall with noise and missing  |
| --- | --- |
|  1 3 2
1 3 2
1 3 2 | Constant across rows  |
|  +0 +2 +1
1 3 2
4 6 5
3 4 4 | Additive on columns  |
|  2x
-1x
1x | 2 -6 4
-1 3 -2
1 -3 2  |
|  Multiplicative with symmetries on rows | Multiplicative with constant overall  |
|  1 1 3
1 3 2
1 2 2 | 2 3 1
1 3 0
3 4 2  |
|  Order preserving across rows  |   |

# Motivation

- GLOBAL stance: clustering
- Group observations correlated according to values of all variables
- Problem?
- High-dimensional data: hundreds to thousands of variables
Similarity on all variables can be misleading if strong correlation occurs only on a subset
x1 = 0.2 0.1 0.2 0.1 0.4 0.7 0.4 0.3
x2 = 0.1 0.3 0.1 0.2 0.4 0.7 0.4 0.2
x3 = 0.3 0.1 0.2 0.3 0.4 0.7 0.4 0.1
Dissimilar? What about this coherent pattern

- Solution? LOCAL stance: subspace clustering
- Group observations correlated on a subset of all variables (subspace)
- Non-exhaustive and overlapping groups of observations

 

# Definition

- Subspace clustering can be applied to different data structures, including:
- [biclustering] simple multivariate data
- [n-way subspace clustering] tensor data (e.g. **triclustering** for three-way data)

- Given a dataset, $D$, with a set of observations $X = \{\mathbf{x}_1, \ldots, \mathbf{x}_N\}$, a set of variables $Y = \{y_1, \ldots, y_M\}$, and elements $a_{ij} \in R$ relating observation $x_i$ and variable $y_j$:
- A bicluster $B = (I, J)$ defines a pattern in $D$, where $I = (\mathbf{x}_{i_1}, \ldots, \mathbf{x}_{i_n}) \subset X$ is a subset of observations (pattern support) and $J = (y_{j_1}, \ldots, y_{j_m}) \subset Y$ is a subset of variables (subspace)
- The biclustering task aims to identify a set of biclusters $\mathbf{B} = \{B_1, \ldots, Bs\}$ such that each bicluster $B_k = (I_k, J_k)$ satisfies specific criteria of homogeneity and statistical significance

# Applications: social domains

- Social networks
- communities of individuals with shared interests or correlated activity (X=Y=individuals)
- aggregation of contents (X) based on correlated accessors' profile, comments and tags (Y)
- Text data: group content-related documents to support searches, suggestions and tagging (X=documents, Y=features)
- (e-)commerce: browsing patterns (X=users, Y=webpage accesses)
- Education: performance analysis (X=students/professors, Y=topics/features)
- Financial/trading: subsets of indicators producing similar profitability for subsets of trading points (X=buy and sell signals, Y=stock market ratios)
- Collaborative filtering data: groups of users with similar rating patterns and behavior on a subset of available actions (X=users, Y=items/actions)

 

# Applications: biomedicine

- Omic data: functional processes and pathways (X=genes/proteins/metabolites, Y=conditions)
- Physiological data: coherent sliding features on a subset of stimuli-elicited responses; groups of patients with shared local patterns (X=signals, Y=features)
- Clinical data: health trends and risk profiles from health records; individuals with similar treatments, diagnoses and tests (X=individuals, Y=clinical features)
- Genomic mutations: correlated mutations (Y) for specific populations (X)
- Biological networks: modules of genes, proteins or metabolites (X=Y=biological entities) with cohesive local interaction using adjacency matrices

 

# Motivation

Consider **gene expression** data analysis (where $X =$ samples/individuals and $Y =$ genes)

- **clustering** groups samples or genes $\Rightarrow$ limited relevance! **Why?**
- only a small set of the genes participates in a cellular process of interest
- an interesting cellular process is active only in a subset of the conditions
- a single gene may participate in multiple pathways that may or not be coactive under all conditions

- **biclustering** groups genes that show similar activity patterns under a subset of samples =&gt; **current way of extracting new knowledge**
- SARS-CoV-2 knowledge advances on regulatory responses and vaccines
- breakthroughs on cancer mechanisms and therapies

# Outline

- Subspace clustering
- Biclustering
- coherence
- quality
- structure
- evaluation
- searches
- Triclustering
- Deep learning
- Appendix

 

# Homogeneity

- Let us recall: the **biclustering task** aims to identify a set of biclusters such that each bicluster satisfies specific criteria of...

- **homogeneity**: patterns of interest
- the placed homogeneity determines the **structure** (positioning), **coherence** (correlation) and **quality** (noise tolerance) of biclusters

- **statistical significance**: non-spurious patterns,
i.e. biclusters should not occur by chance (unexpectedly frequent)
- non-significant bicluster discovered: false positive
- significant bicluster not discovered: false negative

 

# Coherence

- The allowed form of correlation is termed coherence assumption

# Coherence

- Homogeneity commonly guaranteed through a merit function
- e.g. the variance of the values in a subspace

Low variance can be used to find biclusters with constant values

# Constant model

- Constant values
- overall (low-variance)
$$
a_{ij} = c + \eta_{ij}
$$
- on variables
$$
a_{ij} = c_j + \eta_{ij}
$$
where...
- $c_j$ is a constant
- $\eta_{ij}$ the noise factor
- $a_{IJ}$ average $(I,J)$
- $a_{IJ}$ average $(I,\{yj\})$

|  1.2 | 0.5 | 0.3 | 1.3  |
| --- | --- | --- | --- |
|  1.3 | 0.5 | 0.1 | 1.2  |
|  1.2 | 0.6 | 0.6 | 1.1  |
|  1.1 | 1.3 | 0.8 | 1.2  |
|  1.2 | 0.5 | 0.3 | 1.3  |
| --- | --- | --- | --- |
|  1.3 | 0.5 | 0.1 | 1.2  |
|  1.2 | 0.6 | 0.6 | 1.1  |
|  1.1 | 1.3 | 0.8 | 1.2  |
|  1.2 | 0.5 | 0.3 | 1.3  |
| --- | --- | --- | --- |
|  1.3 | 0.5 | 0.1 | 1.2  |
|  1.2 | 0.6 | 0.6 | 1.1  |
|  1.1 | 1.3 | 0.8 | 1.2  |

# Additive model

$$
a_{ij} = c_j + \gamma_i + \eta_{ij}
$$

$$
\gamma_1 = +0
$$

$$
\gamma_2 = +3
$$

$$
\gamma_3 = +2
$$

$$
c_1 = 1 \quad c_2 = 3 \quad c_3 = 2
$$

|  1 | 3 | 2 | 5  |
| --- | --- | --- | --- |
|  4 | 6 | 5 | 1  |
|  3 | 5 | 4 | 2  |
|  4 | 1 | 2 | 3  |

- $c_j$ is the value of variable $y_j$
- $\gamma_i$ is the adjustment for observation $x_i$

- bicluster **pattern** $\phi_B$ is the expected values in the absence of adjustments $\gamma_i$ and noise factors $\eta_{ij}$
- e.g. $\phi_B = \{c_1 = 1, c_2 = 3, c_3 = 2\}$

# Additive model

## Why?

- medical field: handle individual differences, different stages of disease progression
- biological field: responsiveness of genes, experimental differences
- social field: individual differences regarding activity

# Multiplicative model

- Similar to the additive model:
- on observations
$$
a_{ij} = c_j \gamma_i + \eta_{ij}
$$
- on variables
$$
a_{ij} = c_i \gamma_j + \eta_{ij}
$$

|  $\gamma_1 = 2$  |
| --- |
|  $\gamma_2 = -1$  |
|  $\gamma_3 = 1$  |
|  $c_1 = 1$ | $c_2 = -3$ | $c_3 = 2$  |
| --- | --- | --- |
|  2 | -6 | 4  |
|  2 | 3 | 2  |
|  1 | 2 | 2  |
|  4 | 1 | 2  |

- $c_j$ (or $c_i$) is the value of variable $y_j$ (or observation $x_i$)
- $\gamma_i$ (or $\gamma_j$) is the adjustment for observation $x_i$ (or variable $y_j$)

# Order-preserving model

- A bicluster following an order-preserving model is (I, J) where the values on each observation in I across the J variables are ordered according the same permutation $\pi$

|   | y_{1} | y_{2} | y_{3} | y_{4}  |
| --- | --- | --- | --- | --- |
|  x_{1} | 19 | 12 | 6 | 14  |
|  x_{2} | 10 | 7 | 13 | 9  |
|  x_{3} | 11 | 6 | 17 | 8  |
|  x_{4} | 13 | 4 | 1 | 11  |

$$
\begin{array}{l}
\pi = y_1 \geq y_4 \geq y_2 \\
B = (\{x_1, x_2, x_3, x_4\}, \{y_1, y_2, y_4\})
\end{array}
$$

## Why?

- More flexible and noise robust
- Focus on orderings instead of absolute values (preferences, difficulties)

# Symmetries

- Symmetries can be accommodated on observations: $a_{ij} \times k_i$ where $k_i \in \{1, -1\}$
- e.g. activation and repression regulatory patterns

level of expression
a. Constant (with symmetries)
conditions

level of expression
b. Multiplicative (with symmetries)
conditions

# Plaid model

The plaid assumption considers the cumulative effect of the contributions from multiple bicusters on areas where their observations and variables overlap

Why? Synergistic behaviors (e.g. social networking, comorbidity effects, multi-purpose genes)

# Merit functions

- Variance of values ⇒ constant overall
- Mean square residue, $H \Rightarrow$ additive
$$
r(a_{ij}) = a_{ij} - aiJ - a_{Ij} + aIJ \text{ (residue of an element in an additive subspace)}
$$
$$
H(I,J) = \frac{1}{|I||J|} \sum_{i \in I, j \in J} r(a_{ij})^2 \text{ (measure of additive coherence)}
$$

- Pearson correlation ⇒ additive/multiplicative
- Cosine measure ⇒ order-preserving

Many others...

 

# Coherence strength

- Let $\bar{A}$ be the amplitude of the range of values in a matrix $A$
- Given $A$, the **coherence strength** is a range $\delta \in [0, \bar{A}]$, such that $a_{ij} = c_j + \gamma_i + \eta_{ij}$ (or other) and $\eta_{ij} \in [-\delta/2, \delta/2]$
- e.g. $a_{13} = 1.4$, $a_{23} = 1.8$ and $a_{33} = 1.6$ can be seen as constant column if $\delta = 0.4$
- Increasing coherence strength
- more tolerance to noise
- larger biclusters
- Decreasing coherence strength?
- How to fix coherence strength?

# Quality

The quality of a set of biclusters is defined by the type and amount of accommodated noise

- amount of noisy elements: e.g. 30% of noisy elements
- type of noise: e.g. consider only small deviations from $[\eta_{ij} - \delta /2,\eta_{ij} + \delta /2]$

|  2. 2. 2. 2.  |
| --- |
|  2. 4. 2. 2.  |
|  2. 2. 2. 2.  |
|  2. 2. 0. 2.  |

12.5% of noisy elements

|  2. 2. 2. 2.  |
| --- |
|  2. 1.8 2. 1.7  |
|  2.4 2. 2. 2.  |
|  2. 2. 2.3 2.  |

25% of slight deviations from $[\eta_{ij} - \delta /2,\eta_{ij} + \delta /2]$

# Structure

- Number of biclusters
- Size and shape
- Positioning constraints:
- Exhaustive: rows and/or columns
- Exclusive: rows and/or columns
- Non-overlapping
- Others: tree, hierarchical structures

Flexible structure:
- non-fixed number of biclusters
- no constraints on size, shape and positioning

# Structures

- Exclusive on rows (left), columns (middle), or both (right)

- Exhaustive on rows (left), columns (middle), or both (right)

# Structures

- Hierarchical

- Others
- coclustering structure/checkboard
- diagonal, L, square shape

# Flexible structures

- Arbitrarily positioned (possibly overlapping) biclusters

- Biclustering solutions with flexible positioning can be associated with redundant patterns
- searches should further include dissimilarity criteria
(e.g. merging biclusters with high overlapping at mining or postprocessing time)

# Statistical significance

Is a bicluster unexpected?

- e.g. Is a bicluster defined by 2 observations and 2 variables in large dataset interesting? Or does it occur by chance?
- Solution: assess statistical significance
- randomize data several times and compute the ratio of datasets where we are able to find a similar bicluster
- approximate data distributions and perform a statistical test
- the null hypothesis is that the bicluster does not occur by chance
- we can statistically test its support using binomial test similarly as we did for itemsets
- Assessment can be considered during the biclustering search
- Refresh memory: False positive bicluster? False negative bicluster?

 

# Evaluation metrics

## Challenges

- no ground truth to evaluate biclusters observed in real data
- metrics only able to assess a single homogeneity criteria
- evaluation metrics used within the biclustering searches – problem?

## Options

- synthetic data (knowledge of true/hidden biclusters)
- objective metrics: accuracy, precision, completeness
- real data (no knowledge of true biclusters)
- subjective metrics: domain-driven relevance scores

 

# Evaluation metrics

Synthetic data (objective metrics)

H is the set of true biclusters and B is the set of found biclusters

- Clustering metrics on one dimension (X and Y separately)
- silhouette, recall and precision – problems?

- Jaccard-based match scores (MS) to assess the similarity of $B$ and $H$
- $MS(B,H)$ extent to which found biclusters match hidden biclusters
- $MS(H,B)$ reflects how well hidden biclusters are recovered

$$
MS(\mathcal{B}, \mathcal{H}) = \frac{1}{|\mathcal{B}|} \Sigma_{(I_1, J_1) \in \mathcal{B}} \max_{(I_2, J_2) \in \mathcal{H}} \frac{|I_1 \cap I_2|}{|I_1 \cup I_2|}
$$

- Fabia consensus is sensitive to the number of biclusters in both sets

$$
FC(\mathcal{B}, \mathcal{H}) = \frac{1}{|\mathcal{S}_1|} \Sigma_{((I_1, J_1) \in \mathcal{S}_1, (I_2, J_2) \in \mathcal{S}_2) \in MP} \frac{|I_1 \cap I_2| \times |J_1 \cap J_2|}{|I_1| \times |J_1| + |I_2| \times |J_2| - |I_1 \cap I_2| \times |J_1 \cap J_2|}
$$

# Evaluation metrics

## Real data (subjective metrics)

- **statistical significance**: unexpected occurrence probability
- **domain relevance**: unexpected probability of participating in studied process
- domain and statistical significance correlated but not always in agreement!

- HOW to assess domain relevance of bicluster $(I, J)$?
- source of annotations: knowledge bases (e.g. GO) and literature data (e.g. PubMED)
- statistically test I and J against well-established annotations
- hypergeometric tests to compute enrichment p-values against an annotation database
- intuition: most of entries in I (or J) sharing annotations in a database suggests relevance

 

# Approaches

- Number of biclusters at a time
- discover one bicluster at a time and then mask it
- discover a set of biclusters at a time

- Optimality
- exhaustive and (quasi-)exhaustive searches
- e.g. find heavy subgraphs in bipartite graphs mapped from data
- heavy! Place restrictions on structure, coherence and quality
- approximate searches (next slide)

 

# Approaches

- Greedy iterative searches
- iteratively add/remove rows and columns to maximize a merit function
- e.g. CC minimize mean square residue (MSR) until reaching MSR &lt; δ
- Row and column clustering combination (e.g. CTWC, ITWC)
- apply clustering on rows and columns separately
- use an iterative procedure to combine the two clustering results
- Divide and conquer searches
- break the matrix into submatrices (e.g. find best row or column split)
- continue the biclustering process on the new submatrices
- Distribution parameter identification (e.g. plaid)
- use mixture to describe biclustering solution and learn its parameters (maximize likelihood)

 

# Outline

- Subspace clustering
- Biclustering
- coherence
- quality
- structure
- evaluation
- searches
- Triclustering
- Deep learning
- Appendix

 

# Time series biclustering

- Until here: biclustering as relevant pattern discovery task for multivariate data, yet...
- applicability to (univariate) time series data is equally pervasive
- a bicluster is defined by a subset of **observations** and **time points**
- contiguity is generally assumed across time points (convex temporal pattern)
- temporal misalignments between observations can be further accommodated
- e.g. individuals at different stages of a disease

- Illustrative method: CCC identifies patterns in linear complexity time using suffix trees
- eCCC extension can further allow temporal misalignments and noise

 

# Time series biclustering: CCC algorithm

Time series data

# Triclustering

- How to move from univariate to multivariate time series (MTS) data?
- multivariate data is defined by a set of observations, variables and time points

- Solution: triclustering
- a tricluster is a subset of observations, variables and time points with good:
- homogeneity, e.g. well established temporal pattern on a subset of variables
- statistical significance, e.g. unexpected high #observations supporting the pattern

Full-clustering on attributes

Full-clustering on observations

Partial-clustering (all attributes)

Partial-clustering (all observations)

Triclustering

# Triclustering

Triclusters with low variance and cumulative effects on overlapping regions

Tricluster with constant pattern on observations and contexts

Tricluster with low mean square residue

# Triclustering

- Applications
- computational biology: regulation (genes × conditions × time), protein–protein interaction (proteins × interaction × conditions), drug response profiling (cell lines × drugs × dosages)
- recommender systems: dynamic preference modeling (users × items × time/location/device)
- NLP: topic discovery (documents × terms × time/language), sentiment analysis with context
- social networks: community detection with context, role discovery in dynamic networks
- time series: segmentation (sensors × signals × time windows), EEG analysis, climate monitoring
- vision: video analysis (objects × features × frames), activity recognition, multimodal systems
- business: sales patterns (products × stores × time), fraud detection, basket analysis with season
- healthcare: patient stratification (patients × variables × time), treatment outcome, epidemiology

- Challenge: extend previous concepts on biclustering after reading the survey by Henriques et al. (2017)

# Outline

- Subspace clustering
- Biclustering
- coherence
- quality
- structure
- evaluation
- searches
- Triclustering
- Deep learning
- Appendix

 

# Patterns and deep learning?

Until now: focus placed on explicit pattern discovery (classic and subspace clustering)

What about deep learning? Multi-layer learning process to extract rich implicit patterns

- image: pixels → edges → textures → motifs → parts → objects
- text: character → word → word group → clause → sentence → story

by Param Vir Singh

# Patterns and deep learning?

- Hidden unit ≈ latent pattern
- high-weight connections ≈ frequent features
- activations per observation ≈ pattern support

- Recall the following properties of a good representation
- **disentangled** explanatory factors
- each unit should capture a separate, meaningful aspect of the data
- **loose factor dependencies**
- **sparsity**: for any observation x, only some factors are relevant

# Patterns and deep learning?

- Handling complex neural networks?
- multimodal architectures
- extension to shared spaces: latent patterns embody relationships across data modalities
- transformer-based architectures
- attention weights ≈ pattern importance
- attention heads ≈ distinct patterns

- Core problem: neural networks only able to generate implicit patterns
- limited pattern deidentification
- limited post-hoc explainability on the deidentified patterns

 

Rui Henriques

# Appendix

# BicPAMS: constant biclusters (using frequent itemset mining)

# Maximal biclusters
(≡ closed frequent itemsets)

# BicPAMS: noise-tolerant biclusters (using association rules)

# Handling missings

# BicPAMS: additive models
(based on shifting factors)

# BicPAMS: order-preserving models (with sequential pattern mining)

# Summary

- Subspace clustering is key to find **non-trivial patterns** on **real-valued data**
- unsupervised exploration of **high-dimensional data** (focus on subspaces)
- Subspace clusters satisfy specific criteria of homogeneity and statistical significance
- **Merit functions** determine the homogeneity (patterns of interest)
- condition the structure, coherence and quality (noise tolerance) of patterns
- **Statistically significant** patterns are unexpected (low $p$-value)
- **Coherence** defines the underlying assumption (constant, additive, order-preserving...) and strength
- The **structure** is determined by the number, shape and positioning of patterns
- Subspace clustering **searches** can be classified in exhaustive, greedy, and parametric

---

## Lecture 10: Advanced Descriptive Modeling

*Source: 08 AdvancedPM LearningFromComplexData*

---
# Advanced Descriptive Modeling

Learning from Complex Data Structures

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Temporal data structures

- Some examples...

A numeric time series is a time series with numerical values for each time point.

Sensor data

Discretization

A symbolic time series is a time series with nominal values for each point.

ABCBDADBBCBAAABBCBDBABDABA

DNA sequences

A symbolic interval sequence has overlapping intervals with nominal values.

Sign language

An itemset sequence is a time sequence with sets of nominal values assigned to each time point.

Shopping baskets for same customer

A symbolic time sequence has nominal values with possible duplicate time points

Events from machine service logs

# Time series

- Time series: sequence of values or symbols along time $\mathbf{x} = <x_1, ...,="" x_t="">$
- univariate or multivariate, $x_j \in \mathbb{R}^m$ (or $x_j \in \{Y_1 \dots Y_m\}$), where $m$ is the multivariate order
- Time series data: $\{\mathbf{x}_1, \ldots, \mathbf{x}_n\}$ where $\mathbf{x}_i$ is a time series
- People measure things...
- their blood pressure
- the annual rainfall in New Zealand
- the value of their Yahoo stock
- the number of web hits per second
... and things change over time

time series occur in near every public, scientific and businesses domain

</x_1,>

# Time series

- Time series are ubiquotous: monitoring biological, individual, organizational, geophysical, digital, mechanical, societal systems
- Movement, image and video as time series
- Text data as time series

# Image data as time series

# Video data as time series

# Sequence data

Examples:
- website navigation
- shopping behaviour
- DNA (univariate symbolic sequence)

Focused on **orders** instead of **time points**

Recall: transactional data structures
- market basket analysis at the level of the basket
- What if I want to mine sequences of baskets per user?
- Answer: **itemset sequence** data, a type of sequence data

# Event data

Event: timestamped occurrence
- non-variate, univariate (typed event), multivariate (e.g. high and low blood pressure)

Event sequence: set of events

Event data: set of observations, each being an event sequence

Examples:
- health records
- social interactions
- machine logs
- musical melodies
- headline events

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Temporal data mining

Describe: understand the past and present
- decomposition into essential elements: trend, seasonalities, spectral components, noise
- causality analysis, temporal rules
- motifs and other patterns of interest

Predict the future and unseen features
- anticipate events of interest
- classify and regress time series for system diagnostics and prognostics
- forecast time series

Exercise: major needs in corporate domains?
- mining user behavior, KPIs, stock prices, demand, imports, supply, GDP...

 

# Temporal data mining

Temporal data mining (TDM) tasks include:
- temporal data clustering
- temporal data classification, regression
- temporal data modelling (e.g., explanatory equations and mixtures)
- temporal data transformation (e.g., frequency domain representations)
- temporal data reduction/compression (e.g., variants of PCA for series)
- temporal pattern mining, associative analysis
- temporal data outlier/anomaly detection
- temporal data visualization
- temporal data forecasting

TDM can be further characterized by the:
- target temporal data structure
- presence/absence of temporal semantics (domain knowledge)

# Learning from temporal data

Five major options

1. traditional descriptors/predictors
- first: map temporal data into multivariate data
- retrieve statistics along time: centrality, variance, regression coefficients, percentiles...
- retrieve statistics along time windows (rolling mean and rolling variance) and discard temporal dependence between the statistics produced for each window
- learn embeddings: data representations using neural networks
- second: apply multivariate methods (clustering, pattern mining, NBs, DTs, RFs, SVMs, NNs, etc.)

2. distance-based descriptors/predictors
3. associative descriptors/predictors
4. deep descriptors/predictors
5. prompt-engineered LLM descriptors/predictors

 

# Learning from temporal data: traditional

Temporal data can be mapped into numeric vectors (embeddings) to subsequently apply classic ML

- embeddings are latent feature representations with minimal information loss
- recall the paradigmatic unsupervised case: autoencoders (AE)
- principle: preserve as much information in a compact vector by maximizing reconstruction ability
- enhanced expressivity when considering multi-task self-supervision: check our early class!
- the neural architecture should be able to capture temporal dependencies:
- recurrent layering (e.g., LSTMs), convolutional layering, transformer layering...
- classic ML descriptors and predictors (prepared to learn from tabular data)

# Learning from temporal data: distance-based

- Approaches that rely on distances between two observations
- The simplest regressor/classifier is lazy learning
- train: use temporal distances to detect the nearest neighbors
- test: use them to estimate targets

# Learning from temporal data: distance-based

- Temporal data clustering based on distances between observations and centroids:
- partition-based clustering (k-medoids)
- agglomerative clustering
- density-based clustering

- replace simple tabular distances (e.g. Minkowski) for distances able to accommodate temporal misalignments (e.g. elastic distances such as DTW for time series)

# Learning from temporal data: distance-based

- Centroid of a cluster of temporal observations (e.g., time series) referred as barycenter

- Partitioning-based methods
- means not adequate as centroid if time series are misaligned
- solution: medoids (prototype time series minimizing DTW) or barycenter-driven $k$-means (e.g. tslearn package)

# Elastic time series distances

Fixed Time Axis

"Warped" Time Axis

# Learning from temporal data: associative

## Rule-based predictor

- **TRAIN**: given observations with temporal information
- find temporal patterns
- use the found temporal patterns to produce association rules **pattern ⇒ class**
- rule interestingness criteria reveal the discriminative power of the rule
- *lift* is a good proxy when data is imbalanced

- **TEST**: given a new observation
- find the closest patterns from the produced rules
- label the time series using the rules' consequents (voting stage)
- mode from either all matched rules or top-$k$ closest rules
- weight matched rules by their relevance and discriminative power

 

# Learning from temporal data: associative

## Pattern-centric predictor

- **TRAIN**: given the time series data
- discover temporal patterns and create a tabular dataset with a feature per pattern
- fill the tabular dataset in accordance with one of the following options:
1. **boolean dataset**: whether a time series $x_i$ has or not a given pattern $y_j$
2. **real-valued dataset**: how well a time series $x_i$ contains a given pattern $y_j$
- apply classic classifiers to learn a model using this tabular dataset

- **TEST**: given a new time series
- produce the feature-vector: test if the testing time series has the given patterns (boolean) or how well captures the patterns (real-valued)
- apply the trained classifier to on the feature-vector to return a label

 

# Learning from temporal data: associative

Euclidean ([8,1,1], [2,7,5]) = 9.38

Transformation

Pattern 1

$$
y _ {3} = 2; y _ {4} = 7; y _ {5} = 5
$$

$$
\text{lift} = \frac {\frac {2}{6}}{\frac {3}{6} \times \frac {2}{6}} = 2
$$

- Under this mapping: clustering solutions and high-order patterns can be as well pursued

# Learning from temporal data: deep

Dedicate layering: recurrent (e.g. LSTMs), convolutional (1D or 2D depending on whether data is univariate or multivariate), temporal convolutions, transformer-based...

- Descriptive: learn NNs to denoise (autoenconding observations), extract features, impute...
- Precitive: end-to-end supervised learning
- TRAIN: learn expressive functions that map time-rich inputs and corresponding targets
- TEST: apply the function on testing observations and return the estimates

 

# Learning from temporal data: deep

Classic time-aware models can be deep (many parameters): although less used, remain relevant

## Dynamic Bayesian networks

## Hidden Markov models

- Descriptive: describe system dynamics from time series or sequence data
- check "generative modeling of repositories of health records"
- Predictive:
- TRAIN: learn an automaton per class based on the observed time series for each class
- TEST: given a testing time series, see how each of the automaton better describes it and output the automaton's class as the result

# Learning from temporal data: LLM prompting

- Given a data-rich prompting...
can LLMs be used to extract features, learn descriptions and place predictions data?

- The answer largely depends on task complexity: use LLMs with great caution
- poor performance on hard, specialized tasks and even in some simple ones (e.g., attention to info in the text prompt may override the attached structured data)
- pros
- flexible, fast, task-adaptive without retraining
- works with missing, noisy, or heterogeneous data
- cons
- limited numerical precision and temporal grounding
- weak guarantees on predictive accuracy
- sensitive to prompt design and assumptions

# Learning from temporal data: LLM prompting

Yet an option as LLMs hold unique "analytical" capacities from:

- large-scale multi-task pretraining
- learn cross-domain regularities transferable to different tasks (e.g. descriptive, predictive, inferential), enabling generalization beyond task-specific models
- store latent abstractions of patterns, relationships, and dependencies

- universal sequence modeling
- trained to model sequences, allowing them to process text, code, time series (as serialized inputs) and other (time-rich) data structures
- inherent capacity to handle variable-length and irregular inputs

- in-context learning
- can infer task structure directly from prompts (zero-shot)
- can be guided by few-shot examples without the need for parameter updates (fine tuning)

# Learning from temporal data: LLM prompting

LLM "analytical" capacities:

- Compositional Reasoning for chain descriptive-predictive subtasks in complex data analysis pipelines
- Flexible Input-Output Mapping with prompting allowing for custom input and output formats
- Prior Knowledge Integration from learnt domain heuristics and background associative patterns
- Robustness to Imperfect Data (tolerance to missing, noisy, inconsistent inputs) from contextual inference
- Task Unification via Language by reformulating data-driven tasks as a "predict the next token" task
- Prompt-Controlled Inductive Bias by imposing temporal-causality assumptions and constraints on reasoning and outputs, effectively steering the model toward task-specific behavior

The promise: the increasing LLMs size and context from multi-modal and multi-stage analyses can push LLMs to answer complex, specialized descriptive and predictive tasks

 

# Learning from temporal data: LLM prompting

- Prompting principles for descriptive tasks
- explicitly define temporal scope (time window, granularity)
- ask for trend-aware descriptions (seasonality, peaks, regime shifts)
- use structured outputs (tables, bullet summaries, timelines)
- on inferential tasks, encourage step-by-step temporal reasoning
- request explicit feature identification (lags, growth rates, volatility)
- compare multiple time windows or regimes

- Best suited for
- exploratory analysis, hypothesis generation, feature engineering support
- reporting, data quality assessment, model interpretability

 

# Learning from temporal data: LLM prompting

- Some multimodal LLMs indeed trained on temporal data...

- Prompting principles for predictive tasks
- clearly specify the prediction horizon and assumptions
- constrain outputs to probabilistic or scenario-based estimates
- explicitly ask to separate data-driven inference from speculation

- Example: Given the historical data, forecast the next 7 time steps, disclosing uncertainty drivers.
- Best suited for short-term forecast assistance, scenario analysis, decisions under uncertainty

 

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Sequential pattern mining

- A sequence is an ordered list of events, denoted $&lt; e_1 e_2 \ldots e_l &gt;$
- an event can be univariate, multivariate or an itemset

- Given two sequences $\alpha = &lt; a_1 a_2 \ldots an &gt;$ and $\beta = &lt; b_1 b_2 \ldots bm &gt;$
- $\alpha$ is called a **subsequence** of $\beta$, denoted as $\alpha \subseteq \beta$, if there exist integers $1 \leq j_1 &lt; j_2 &lt; \ldots &lt; j_n \leq m$ such that $a_1 \subseteq bj_1, a_2 \subseteq bj_2, \ldots, an \subseteq b_{jn}$
- $\beta$ is a **supersequence** of $\alpha$
- e.g. $&lt; a(bc)dc &gt;$ is a **subsequence** of $&lt; a(abc)(ac)d(cf) &gt;$

- A sequence database is a set of (itemset) sequences
- A sequential pattern is an association capturing relevant **precedences** and **co-occurrences** in a sequence database

# Sequential pattern mining (SPM)

- Given a set of sequences and support threshold, SPM tasks aims at finding all frequent subsequences
- example: considering a min support of 2:  $&lt;(\text{ab})c&gt;$  is a sequential pattern
- challenges?

|  SID | sequence  |
| --- | --- |
|  10 | <a(abc)(ac)d(cf)>  |
|  20 | <(ad)c(bc)(ae)>  |
|  30 | <(ef)(ab)(df)cb>  |
|  40 | <eg(af)cbc>  |

- Extend the definition to further guarantee:
- statistical significance of sequential patterns (unexpectedly high frequency)
- ability to incorporate various kinds of user-specific constraints to focus on novel, actionable and non-trivial patterns

 

# Sequential pattern mining (SPM)

- SPM is computationally complex! Approaches:
- candidate generation: Apriori-like (e.g. GSP method)
- pattern growth using suffix trees (e.g. PrefixSpan)

- Voluminous solutions?
- exact same principles as in classic pattern mining: filtering, condensed pattern representations, dissimilarity

- Statistical significance
- exact same binomial statistical test as in simple patterns on the pattern support
- null model based on Markov assumption
- e.g. $p_{null}(&lt; adc &gt;) = p(a)p(&lt; ad &gt; |a)p(&lt; dc &gt; |d)$ where the probabilities are based on the frequentist view (ratio of observations)
- using previous table $p_{null}(&lt; adc &gt;) = 1 \times \frac{2}{4} / 1 \times \frac{3}{4} / \frac{3}{4} = \frac{2}{4}$

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Recall: learning from time series data

Clustering

Classification

Normal

Ischemia

Motif Discovery

Rule discovery

Query by content

# Pattern mining in time series

Frequency...

- across time series observations
- sequential pattern mining (frequent orders and precedences in symbolic series data)
- biclustering (univariate time series data)
- triclustering (multivariate time series data)
- temporal association rules
- within single time series
- motif discovery
- predictive rule mining $A \Rightarrow \Delta t B$
once antecedent is observed, consequent expected within interval $\Delta t$

# Time series biclustering

- Recall: **biclustering** aims at discovering patterns in simple multivariate data such that each pattern satisfies specific criteria of *homogeneity* and *statistical significance*
- can further include *dissimilarity* and, given variables of interest, *predictive power*

- Biclustering is also used to retrieve patterns from *univariate time series*
- a *bicluster* is a subset of *observations* with coherent values on a subset of *time points*
- *contiguity* is generally assumed across time points (convex temporal pattern)
- *temporal misalignments* between observations can be further accommodated (e.g. patients at different disease stages)

"Late"
Biclusters
same pattern
potential delay

# Triclustering

- How to discover patterns in multivariate time series (MTS) data?
- MTS data: each observation is described by a set of variables measured along time
- Option: triclustering
- a **tricluster** is a subset of observations, variables and time points with good:
- homogeneity, e.g. well established temporal pattern on a subset of variables
- statistical significance, e.g. unexpected high #observations supporting the pattern

Full-clustering on attributes

Full-clustering on observations

Partial-clustering (all attributes)

Partial-clustering (all observations)

Triclustering

# Motif discovery

- To exhaustively find all motifs: combinatorially explosive number of distances to compute
- the obvious brute force search algorithm is just too slow!
- one solution: symbolize the time series and apply efficient intersections on a sliding basis

# Signals... any care?

- Signals collected from sensors show unique complexities
- Time series representations essential to:
- Reveal the **internal structure** of the signal
- decompose signal into a set of meaningful components

- Alternatives to deep learning? Yes...
- describe *raw signal* as a finite *composition of well-known abstractions*
- spectral analysis
- **Fourier** transform for biosensors (e.g. brain waves from EEG)
- **Wavelet** transform in telemetry (e.g. appliances on from utility consumption sensors)

# Fourier and Wavelet analysis

Signal
Constituent sinusoids of different frequencies

Signal
Constituent wavelets of different scales and positions

# Case: EEG analysis

- Given a raw electroencephalographic signal:
- multivariate time series with $p$ order (corresponding to #electrodes)
- nearly impossible to interpret in raw form
- spectral analysis to decompose signal into activity levels (waves)
- gamma (40-100Hz): cognition, info processing, learning
- beta (12-40Hz): conscious focus, memory, problem solving
- alpha (8-12Hz): transition between focus and relaxation
- theta (4-8Hz): emotional connection, relaxation
- delta (0-4Hz): healing, restorative/deep sleep

- Use **triclustering** or (multivariate) **motif discovery** to find patterns on the frequency representation of the raw signals
- e.g. decreased alpha-to-gamma activity in the frontal lobe and increased high activity in the occipital lobe is a statistically significant pattern and discriminative of schizophrenia

# Time series representations

- Goal: identify the structural elements of a time series
- automatically extract explanatory components of a time series using abstractions
- e.g. embeddings, spectral components...
- useful to tackle inherent idiosyncrasies of time series data analysis
- high dimensionality, noise and variability
- promote ability to measure distances between time series

- Two large families
- numeric representations: $\mathbf{x}_i \in \mathbb{R}^n \rightarrow \mathbf{x}_i \in \mathbb{R}^p$
- symbolic representations: $\mathbf{x}_i \in \mathbb{R}^n \rightarrow \mathbf{x}_i \in \Sigma^p$

# Symbolic time series data

- Time series can be mapped into symbolic sequences (SAX, codebooks)
- Many research contributions from:
- bioinformatics (efficient analysis of DNA and protein sequences)
- information retrieval (efficient analysis of text data)
- Mining symbolic time series data is indeed similar to real-valued data:
- distance-based clustering, classification and regression
- distance metrics on strings, e.g. edit distance, Jaro-Winkler, Levenshtein
- associative clustering, classification and regression
- symbolic temporal patterns (instead of continuous motifs, patterns)

 

# Symbolic Aggregate approXimation (SAX)

paradigmatic approach to convert/symbolize time series using piecewise aggregation followed by discretization

# Time series bitmaps

- SAX benefits...
- finding motifs
- visualizing massive time series
- clustering streaming time series
- kolmogorov complexity data mining
- classification and indexing

- These ends are grounded bitmap analysis:

|  a | b  |
| --- | --- |
|  c | d  |
|  aa | ab | ba | bb  |
| --- | --- | --- | --- |
|  ac | ad | bc | bd  |
|  ca | cb | da | db  |
|  cc | cd | dc | dd  |

accbabcbdcabdcabcdbcdcadbaacb...

# Clustering and anomalies

bitmaps similar (normal behavior)

# Classification using bitmaps

# Patterns in symbolic time series data

## Examples

- symbolic motifs in a single series
- substring patterns (B → C → B)
- sequence of symbols
- extensions to allow gaps
- regular expression patterns (B → ¬C → A | B)
- extension to allow gaps (via wildcards), negations, repetitions, etc.

Exercise: are the given patterns sufficient to describe web usage behavior? Any addition?

# Patterns in multivariate time series

Example: pattern mining on multivariate time series
- tone mining: discretization, segmentation
- chord mining: variation of itemset mining
- phrase mining: variation of partial order mining

 FORMAÇÃO AVANC

duration

coincidence

partial order

# Patterns in multivariate time series

- Tones represent duration with intervals
- Chords represent coincidence of tones
- Phrases represent partial order of chords

Chords

Phrase

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Learning from event data

- Clustering with dedicated distances between events sets
- Clustering, classification and regression
- traditional learners using neural embeddings or statistics from event sets
- distances between event sets
- discriminative patterns in event data (next slides): associative models
- Distances between event sets:
- map events into sequence data by focusing on orders
- map events into sparse time series
- map events into itemset sequence data using time windows
... and use distance functions for these temporal data structures

 

# Frequent episodes

- Episode is an arrangement of events
- serial episode: F appears after E
- parallel episode: A appears with B in any order
- hybrid serial-parallel episode: no total order

- Two formulations:
- frequent episodes along a single sequence
- similarities with motif discovery?
- frequent episodes on a dataset of sequences
- similarities with sequential pattern mining?

# Frequent episodes

- Given a sliding windows, the frequency of an episode $P$: fraction of windows where $P$ appears
- Apriori-style search, given maximum window length:
- find frequent events (e.g., A, B, C)
- generate candidate episodes (e.g., AB, AC, BC), counting frequencies
- find next-level episodes
- Efficient counts:
- no need to count all arrangements when sliding (updates)
- WINEPI search further uses automata and hierarchies

# Interval series data

- A time sequence is a multi set of time points
- A pair of time points defines a time interval
- Two intervals overlap if there is at least one time point that lies within both intervals
- An interval series is a set of non overlapping time intervals
- Representation of event data when events have duration
- Interval series different than feature intervals [min v, max v]

|  before | A | B  |
| --- | --- | --- |
|  meets |  | B  |
|  overlaps |  | B  |
|  starts | B |   |
|  during | B |   |
|  finishes | B |   |
|  equals | B |   |

# Interval series data

- Duration: persistence of an event along time points
- Order: sequential occurrence of time points or intervals
- Concurrency: closeness of two or more events in time
- Coincidence: intersection of intervals
- Synchronicity: synchronous occurrence of two events
- Periodicity: repetition of the same event with a nearly constant period

# Mining interval series data

In time series data
- focus on orders or concurrency

In interval series data:
- focus on order, concurrency, synchronicity

# Mining interval series data

- Clustering using dedicated distances for interval series
- Classification and regression
- traditional learners using statistics from interval series
- distance-based learners with distances on interval series
- associative learners using interval patterns
- Deep representations using dedicated neural architectures
- Prompting engineering
- Note: there are variants not only prepared for time intervals but feature intervals
- e.g. daily variation of temperature (min-max) along a year
- correctly interpret dependencies between pairs of features defining an interval

 

# Patterns in interval series data

Apriori-style [Hoeppner 2001]

- combine two $k$-patterns with common $k - 1$ prefix

- use transitivity of interval relations to prune candidates
- B {contains, ended by, overlaps, meets, before} C
- pruned relations: {after, met by, overlapped by, started by}

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Spatiotemporal data

- Urban data: mobility, emergency services, utility supply systems
- Social data: georeferenced activity (messaging, photos)
- Deep space data
- Location-based search data, navigation data (trajectories)
- Brain activity: functional connectivity, synchronization
- Biological data: organ and tissue properties
- Image and video data: moving objects
- Geophysical data (Earth science): atmospheric, ecosystem and seismic activity
- Forensic data (crime mapping)
- Economic (national or world-wide) data

# Spatiotemporal data

- Epidemiology data (geography of health)
- Example: patterning of viral spread?
Changes in transmissibility over space and time?
- E-commerce and marketing data
- What happens if a new store is added?
- predicting consumer spatial behaviors
- delineating trade areas
- analyzing market performance
- How sales divert geographically? Trends?
- changes in population, ethic-mix, and transportation network impact choices and communication with customers

# Spatiotemporal data structures

- georeferenced observations
- tabular data with spatial attributes
- e.g. location of individuals, geographies, stores, etc.
- geolocalized time series data
- e.g. telemetry data: measurements at a specific location

- timestamped georeferences
- trajectory / moving object data
- e.g. city mobility, vehicle monitoring, deep space objects
- geolocalized event data
- e.g. location of payments, health records, shopping baskets, activities of interest

- continuous/interpolated spatial data (e.g. geophysical maps)

# Spatiotemporal data mining

The process of discovering useful, non-trivial patterns from spatiotemporal data to support decisions
- spatiotemporal data prediction and clustering
- spatiotemporal outlier discovery (discontinuities, unexpected events/trends)
- spatiotemporal pattern mining

What's NOT spatial data mining
- querying (storing and indexing) spatial data
- ex. retrieve current traffic on the shortest path from Boston to Houston
- testing simple hypotheses (also referred as primary data analysis)
- ex. female chimpanzee territories are smaller than male territories
- SDM ≡ secondary data analysis: generate multiple plausible hypotheses
- uninteresting or obvious patterns in spatial data
- ex. rainfall in Minneapolis correlated with rainfall in St. Paul (10 miles apart)

# Spatiotemporal data mining

- input: spatiotemporal data structures and their properties
- output: patterns, predictors, clusters, outliers...
- learning (input→output): statistical foundations and algorithms
- descriptive learning: pattern mining, clustering and outlier analysis
- predictive learning: classification, regression and trend analysis
- Location helps bring rich contexts to learning
- physical: e.g., rainfall, temperature, and wind
- demographical: e.g., age group, gender, and income type
- problem-specific: e.g. distance to highway or water

# Input: spatiotemporal data relationships

- relationships on **non-spatial data**
- arithmetic: order, correlation, etc.
- temporal: duration, order, concurrency, coincidence, periodicity

- relationships on **spatial data**
- set-oriented: union, intersection, membership, etc.
- topological: meet, within, overlap, etc.
- directional: North, NE, left, behind, etc.
- metric: distance, area, perimeter, etc.
- dynamic: update, create, destroy, etc.
- granularity-based
- shape-based and visibility

|  Granularity | Elevation example | Road example  |
| --- | --- | --- |
|  Local | Elevation | On road?  |
|  Focal | Slope | Adjacent to road?  |
|  Zonal | Highest elevation in a zone | Distance to nearest road  |

# Learning: spatial autocorrelation

- Classical data mining
- observations assumed to be independent
- cross-correlation measures
- Spatiotemporal data mining
- observations are not independent
- nearby observations tend to be more similar than distant observations
- spatial autocorrelation
- spatial heterogeneity

# Learning: spatial splicing

- Spatial heterogeneity: global model might be inconsistent with regional models

global model

regional models

- Learning different models for different spatial regions (and time periods)
- slicing input data can improve the effectiveness of SDM
- slicing output models: e.g. association rule with support map

# Spatiotemporal data mining: approaches

- Option 1: map spatial data into multivariate data
- observations with spatial variables
- consider latitude, longitude, elevation, radius as numeric variables
- whenever possible adapt distances to guarantee sensitivity to such variables
- e.g. $d$(location(customer), location(store))
- cluster geographies (nominal/ordinal variables)
- when an observation is a time series: combine time series statistics with spatial features
- trajectory data: statistics on trajectory
- georeferenced event data: statistics (spatiotemporal distribution)
- continuous spatiotemporal data: e.g. Wavelet and spectral features after spatial slicing
- Do not forget: neural embeddings and LLM prompt-based features as alternative representations

 

# Spatiotemporal data mining: approaches

- Option 2: use spatial-sensitive distances
Distanced-based learners – e.g. kNN, clustering and biclustering – over:
- observations with spatial attributes
- Euclidean, walking, driving, contiguity distance between two locations
- weighted attributes: relevance of spatial component (versus remaining)
- when an observation is a time series: combine time series distance with spatial distance
- trajectory data
- dedicated distances between two trajectories
- georeferenced event data
- distance between sets of spatial events (e.g. differences between spatiotemporal distributions)
- continuous spatiotemporal data:
- matrix distances (local or global) able to accommodate misalignments

 

# Spatial clustering

- Different types
- clustering observations with spatial information (e.g., georeferenced vectors and series)
- clustering trajectories...
- Similarity measures
- distances combining non-spatial and spatial attributes
- topological: neighborhood EM (NEM) for joint partitioning feature space and space
- Interest measures
- spatial proximity
- cartographic generalization
- unusual density
- consistent feature-space (nearest neighbors in same cluster)
- Challenges
- temporal data (changing locations of an observation)
- spatial constraints in algorithmic design

# Spatial clustering

## Variants:
- clustering geographies (maps) ensuring spatial contiguity
- weighted clustering on space and feature-space

Inputs:
Complete Spatial Random (CSR),
Cluster, Decluster

Classical spatial clustering

Data is of Complete Spatial Randomness

Effective spatial clustering

# Spatial outlier analysis

## Types of outliers
- global outlier versus spatial outlier (contextual/local)
- georeferenced data: outliers are observations with deviant behavior and location (referred as multi-attribute spatial outliers)
- continuous spatial data: outliers are regions with unexpected values/events

## Approaches
- quantitative outlier detection: scatter plot, and z-score
- graph-based outlier detection: variogram, Moran scatter plot

## Challenges
- adequate spatial statistical tests
- collective spatial outlier detection

 

# Spatial outlier analysis

- Traditional
- quantitative tests (scatter spatial plots)
- graphical tests (e.g. variogram)
- Deficiency of traditional tests
- outliers can negatively impact nearby points
- outliers may be ignored
- Solution
- replace the features of the detected outlier with the median of its neighbors' values

Expected Outliers: S1, S2, S3
Outliers by traditional approaches: E1, E2, S1

# Spatiotemporal data mining: approaches

## Option 3: rely on spatiotemporal patterns

- discover spatiotemporal patterns
- option 3.1: learn predictive rules
- discriminative rules spatiotemporal pattern ⇒ label/value
- temporal rule spatiotemporal pattern ⇒ [t] spatiotemporal
- option 3.2: infer a multivariate dataset observations x patterns
- binary or real-valued defining the likelihood of pattern belonging to observation
- use the dataset to:
- to group observations (clustering)
- to learn classification and regression models
- to find high-order patterns

 

# Spatiotemporal patterns

FPAR-Hi ⇒ NPP-Hi

(sup=5.9%, conf=55.7%)
grassland/shrubland areas

- Newly emerging diseases o Re-emerging diseases

Emerging patterns and spatiotemporal associations
- urban dynamics
- consumer/user habits
- public health (e.g. infectious diseases)
- homeland defense

emerging road traffic
congestions in the city

# Spatiotemporal patterns

Open field with thousands of possibilities
- flock patterns on trajectory data
- moving patterns from evolving spatial clusters
- colocation patterns from event data
- patterns whose cause and consequence do not happen colocated or at the same time
- spatial distance or temporal delay for the consequence to show up

... less-trivial (yet relevant) applications
- ecology (e.g. migration, relocation patterns)
- games (e.g. game tactics)

# Spatiotemporal data mining: approaches

## Option 4: dedicated approaches

- spatial slicing over classical approaches to turn learning sensitive to space
- guarantee sensitivity to spatiotemporal dynamics
- annotate events or group observations in accordance with spatial partitions
- examples: Bayesian classifiers with probabilities conditional to class and location, tree-based classifiers with info gain also dependent on location
- grouping criteria:
- circles centered at reference features
- gridded cells
- min-cut partitions
- Voronoi diagrams
- dedicated learning algorithms to solve new tasks (e.g., location prediction)

 

# Location-aware prediction

## Location-aware regression

- spatial autoregressive model (SAR)
- linear Regression  $z = A\beta + \varepsilon$
- spatial Regression  $z = \rho Wy + A\beta + \varepsilon$
- models spatial autocorrelation using  $W$  (continuity matrix)
- geographically weighted regression (GWR)

## Location-aware classification

- logistic SAR and GWR (similarly as classic logistic regression)
- Markov random fields (Bayesian view of the neighborhood region)

ROC Curve for testing data comparing linear and spatial regression (spatial is better)

# Spatiotemporal data mining: approaches

## Option 5: deep learning

- spatial locality via convolutional layers
- time dependency (short/long-range) using recurrence, convolutions or attention
- hierarchical layering for multi-scale spatial and temporal representations
- graph neural networks to represent non-Euclidean spatial structures
- modular combination of spatial and temporal neural components into a unified architecture
- parameter sharing in space and time to improve generalization
- spatiotemporal factorization to reduce complexity

## Option 6: LLM prompting

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Motivation

- Disperse/distributed data in private and public organizational settings often consolidated using **multi-dimensional data structures** (also known as data warehouses)
- Most real-world organizational data stored follows a **relational data structure**

- Business
- Turism
- Commerce
- Banking
- Education
- Transport
- Healthcare
- Public administration

- This poses a **key question**: how to mine multi-dimensional and relational data?

# What is a data warehouse?

- Data warehouse
- database maintained separately from the organization's operational database(s) for consolidated, historical data analysis and decision making
- Data warehouse composition:
- dimension tables: such as item, supplier, location or time
- fact table: contains measures and keys to each related dimension table
- Why a separate data warehouse?
- databases: tuned for OLTP (access methods, indexing, concurrency, recovery)
- warehouses: tuned for OLAP (complex queries, consolidation)
- missing data: operational DBs do not typically maintain all historical data
- data consolidation: aggregation, summarization of heterogeneous data
- data quality: reconciliation of sources with inconsistent data representations, codes, formats

 

# Multi-dimension: facts and dimensions

# Mining multi-dimensional data

Example: electronic health records

- Health-record as a central fact table (high multiplicity of measures) linked to multiple dimensions (date, patient, payer, provider, prescription, location)

- Mapping multi-dimensional data ⇒ event sequences
- aggregation dimension (patient) and date dimension to compose repository of events (patient, fact-measure, value, timestamp)

- Learning from event sequences: recall the multiple options! For instance:
1. Discover event patterns (e.g. frequent arrangements)
2. Learn predictive models (e.g. associative classification)

# Learning from multi-dimensional data

- Equals learning from tensors extracted from a fact table
- If the tensor is three-dimensional (cube)
- triclustering
- generative modeling (HMMs, DBNs)
- multivariate time series data analysis
- pattern and motif discovery
- classification and regression
- temporal network data analysis
- If the tensor has $k &gt; 3$ dimensions (hypercube)
- $k$-way subspace clustering
- tensor decomposition
- mapping to more adequate (temporal) data structures
- multi-dimensional space transformations
- denormalization + dimensionality reduction

# Example: MD sequential patterns

- Multi-dimensional (MD) sequential pattern mining as an illustrative case: integrates multi-dimensional analysis and sequential pattern mining
- Recap: sequential pattern mining to find frequent subsequences

|  10 | <a(abc)(ac)d(cf)>  |
| --- | --- |
|  20 | <(ad)c(bc)(ae)>  |
|  30 | <(ef)(ab)(df)cb>  |
|  40 | <eg(af)cbc>  |

<a(bc)dc> is a subsequence of <a(abc)(ac)d(cf)>

Given support threshold  $\theta = 2$ ,

$&lt;(\mathrm{ab})c&gt;$  is a sequential pattern

- MD sequence database: combine dimensional information to the itemset sequence produced from the fact entries of a given object (split dimension)

- example: if  $\theta = 2$ ,  $P = (\text{group} = *, \text{city} = \text{Chicago}, \text{age} = *, \text{qeq} = &lt;\text{bf}&gt;)$  is a MD pattern

|  cid | Cust_grp | City | Age_grp | sequence  |
| --- | --- | --- | --- | --- |
|  10 | Business | Boston | Middle | <(bd)cba>  |
|  20 | Professional | Chicago | Young | <(bf)(ce)(fg)>  |
|  30 | Business | Chicago | Middle | <(ah)abf>  |
|  40 | Education | New York | Retired | <(be)(ce)>  |

</a(abc)(ac)d(cf)></a(bc)dc>

# Example: MD sequential patterns

Mining MD-patterns – e.g. (*,Chicago,*)
- first project seq. databases – e.g. &lt;(bf)(ce)(fg)&gt; and &lt;(ah)abf&gt; for (*,Chicago,*)
- find seq. patterns in projected database – e.g. P=(*,Chicago,*,<bf>)

|  cid | Cust_grp | City | Age_grp | sequence  |
| --- | --- | --- | --- | --- |
|  10 | Business | Boston | Middle | <(bd)cba>  |
|  20 | Professional | Chicago | Young | <(bf)(ce)(fg)>  |
|  30 | Business | Chicago | Middle | <(ah)abf>  |
|  40 | Education | New York | Retired | <(be)(ce)>  |

(cust-grp,city,age-grp)

|  cid | MD-extension of sequences  |
| --- | --- |
|  10 | <(Business,Boston,Middle)(bd)cba>  |
|  20 | <(Professional,Chicago,Young)(bf)(ce)(fg)>  |
|  30 | <(Business,Chicago,Middle)(ah)abf>  |
|  40 | <(Education,New York,Retired)(be)(ce)>  |

</bf>

# Relational data structures

How to mine relational databases?

- naïve solution: bringing all information to a single table
- e.g. customer table where we combine as much info as possible
- problems:
- redundancies
- feature dependence
- how to deal with the multiplicity of orders per customer?
- one line per ‘order’ → analysis results will be about orders, not customers!

|  ID | Name | First Name | ... | Response | Delivery mode | Payment mode | Store size | Store type | Location  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  3478 | Smith | John | ... | Y | regular | cash | small | franchis | city  |
|  3478 | Smith | John | ... | Y | express | check | small | franchis | city  |
|  ... | ... | ... | ... | ... | ... | ... | ... | ... | ...  |

# Relational data mining

## Relational data mining (RDM)
- analysis of data distributed in multiple relations

Multiple paradigms: classic, deep learning, prompt-based...
... yet many RDM principles come from inductive logic programming (ILP)
- ILP concerned with finding patterns expressed as logic programs
- initially: data modelling/description/synthesis
- in recent years: whole spectrum of data mining tasks
- ILP successes in commercial settings and scientific fields such as:
- chemistry/biology (toxicology, nuclear magnetic resonance spectra)
- traffic accident data
- survey data in medicine
- ecological biodegradation rates

 

# Example: relational patterns

- Relational patterns involve multiple relations from a relational database
- Typically stated in a more expressive language
- relational classification rules
- relational regression trees
- relational association rules

```txt
IF Customer(C1,N1,FN1,Str1,City1,Zip1,Sex1,SoSt1,In1,Age1,Resp1)
AND order(C1,O1,S1,Deliv1, Pay1)
AND Pay1 = credit_card AND In1 ≥ 108000
THEN Resp1 = Yes
```

- Relation in a relational database: predicate in predicate logic
- Relational pattern can be expressed in a subset of first-order logic

```txt
good_customer(C1) ←
customer(C1, N1, FN1, Str1, City1, Zip1, Sex1, SoSt1, In1, Age1, Resp1) ∧
order(C1, O1, S1, Deliv1, credit_card) ∧ In1 ≥ 108000
```

# Example: relational association rules

|  LIKES  |   |
| --- | --- |
|  KID | OBJECT  |
|  Joni | ice-cream  |
|  Joni | dolphin  |
|  Elliot | piglet  |
|  Elliot | gnu  |
|  Elliot | lion  |
|  HAS  |   |
| --- | --- |
|  KID | OBJECT  |
|  Joni | ice-cream  |
|  Joni | piglet  |
|  Elliot | ice-cream  |
|  PREFERS  |   |   |   |
| --- | --- | --- | --- |
|  KID | OBJECT | TO  |   |
|  Joni | ice-cream | pudding  |   |
|  Joni | pudding | raisins  |   |
|  Joni | giraffe | gnu  |   |
|  Elliot | lion | ice-cream  |   |
|  Elliot | piglet | dolphin  |   |

likes(KID, A), has(KID, B) → prefers(KID, A, B) (70%, 98%)

**WARMR**: iteratively generate candidate $k$-atomsets from $(k-1)$-atomsets until no more large atomsets are found

likes(KID, piglet), likes(KID, ice-cream) atomset

# Example: relational association rules (ILP)

is_a(X, large_town), intersects(X,R), is_a(R, road), adjacent_to(X,W), is_a(W, water)

is_a(X, large_town), intersects(X,R), is_a(R, road), is_a(W, water) → adjacent_to(X,W) [62%, 86%]

# Outline

- Learning from temporal data
- temporal data structures
- five learning families
- sequential pattern mining
- time series pattern mining
- event pattern mining
- Learning from spatiotemporal data
- Learning from multi-dimensional and relational data

 

# Many other data structures…

- image, text, multimodal... to be explored in DL and LLM DASH modules
- yet we overlook a pervasive one... network data (graphs)
- most real-world systems can be represented as static or dynamic graphs
- chemical compound structures
- biological networks
- cities (multimodal transportation networks)
- social networks (messaging, content interaction)
- ecosystems
- ...
- the large network science community is dedicated to study systems as graphs
- and you guessed it right: strong intersection with data science

# Example: graph pattern mining

- The five learning approaches can be as well considered when learning from graphs
- Yet for now... a sneak peek to a pattern-centric stance
- Pattern discovery in graphs follows similar principles as we saw for time series
- graph dataset: find frequent subgraphs
- single large graph observation: find frequent components
- We can as well query graphs: find all graphs containing a given query
- All the studied pattern metrics (lift, support, significance) are key here

# Example: graph pattern mining

- Bioinformatics: gene networks, protein interactions, metabolic pathways
- Software engineering: program execution flow analysis
- Web graphs, XML structures, semantic web, information networks
- Social networks, web communities, tweets, computer networks
- Chem-informatics: mining chemical compound structures
- Across domains, for different ends:
- knowledge acquisition
- at the core of graph indexing and graph similarity search
- building blocks for graph prediction, clustering, compression, comparison, correlation

# Summary

- Temporal data are ubiquitous: measuring bio, individual, organizational and societal systems
- Application domains include the analysis of log data, medical records, user behavior, shapes, musical sheets, sensor data, text, Twitter, speech, user actions
- Mining temporal data commonly rely on one of four major paradigms:
- feature extraction followed by classic algorithms
- distance-based approaches with elastic distances (e.g. DTW)
- pattern mining following by associative analysis
- generative models (e.g. temporal neural networks)
- Symbolic and spectral representations (e.g. SAX, Fourier and Wavelet transforms) offer relevant abstractions to handle the idiosyncrasies of signal data
- Pattern mining in temporal data
- sequential pattern mining in sequence data
- biclustering, triclustering and motif discovery in (multivariate) time series data
- discovery of episodes, partial orders and event arragments over event sequences

 

# Summary

- Spatiotemporal data is pervasive: urban, social, healthcare, geophysical, deep space
- Learning from spatiotemporal structures: observation is a feature-vector, time series, trajectory
- observations are not independent (dependent): spatial auto-correlation and heterogeneity
- tasks: spatiotemporal pattern mining, outlier analysis, prediction, clustering
- Principles can be placed to learn from spatiotemporal data
- spatial slicing to learn spatial-aware descriptive and predictive models
- spatial-aware distances to weight non-spatial and spatial attributes
- discovery of spatiotemporal patterns (co-locations, associations, emerging patterns, flocks)
- Real data structures in public and private orgs are relational or multi-dimensional
- Mining relational and multi-dimensional data focused on a table (fact) of interest
- apply subspace clustering, generative modelling, multivariate time series analysis and tensor
- map into more adequate (temporal) data structures for the sequent application of classic TDM
- Relational data mining (RDM) dedicated to analyse data in multiple relations using ILP principles

 

Rui Henriques

---
