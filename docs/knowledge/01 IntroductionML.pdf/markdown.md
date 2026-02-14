TÉCNICO+ FORMAÇÃO AVANÇADA

# Introduction to Machine Learning

Descriptive versus predictive modeling

DASH: Data Science e Análise Não Supervisionada

Rui Henriques, rmch@tecnico.ulisboa.pt

Instituto Superior Técnico, Universidade de Lisboa

# Outline

- Intelligence and learning
- Descriptive vs predictive learning
- Machine Learning, Data Science and AI
- Supervised vs unsupervised learning
- Terminology
- Machine learning tasks

TÉCNICO+ FORMACÃO AVANÇADA

# Intelligence

- Rationality
- ability to act in a way that maximizes some utility function
- Curiosity
- ability to engage creative imaginative or inquisitive reasoning
- Adaptability $\Leftarrow$
- ability learn from experience
- make abstractions (patterning)
- deal with novelty and change

3

TÉCNICO+

FORMAÇÃO AVANÇADA

# Artificial Intelligence

## Qualities of intelligence?

- AI with a focus on learning from experience =&gt; machine/deep learning, reinforcement learning ...
- AI with a focus on rationality =&gt; planning, reasoning, optimization ...
- AI with a focus on curiosity =&gt; autonomous agents, affective computing, ...
- AI with a focus on social intelligence =&gt; human-agent interaction, social robots, multi-agent systems...

![img-0.jpeg](img-0.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

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

![img-1.jpeg](img-1.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

# Systemic world view

- system
- set of elements organized with a shared purpose
- (open) surrounded and influenced by its environment
- described by its structure, purpose and functioning
- open systems evolve

- Universe → galaxy → solar system
→ Earth → societies → individuals
→ organs → cells → atoms

![img-2.jpeg](img-2.jpeg)
ENVIRONMENT

![img-3.jpeg](img-3.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+ FORMACÃO AVANÇADA

# Statistical grounds

- Machine learning as...
- the rediscovery of multivariate **statistics** from observable data (samples)
- beyond descriptive and inferential statistics
- the rediscovery of **maths** (linear algebra, calculus...)

- Exercise: associate naïve Bayes, kNN and deep learning (DL) with the aforementioned fields
- solution: NB: statistics, kNN: algebra, DL: calculus

![img-4.jpeg](img-4.jpeg)

Sir William Petty, a 17th-century economist who used early statistical methods to analyse demographic data

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+ FORMACÃO AVANÇADA

# When?

- Descriptive learning (e.g., finding associations, categories, anomalies, summaries, informative features, representations) when:
- human expertise does not exist (e.g. navigating on Mars, new cyberattacks)
- humans cannot explain their expertise (e.g. speech recognition)
- models must be customized (e.g. personalized medicine, user preferences)
- massive amounts of data (e.g. genomics, commerce, social media, web usage)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)

![img-8.jpeg](img-8.jpeg)
by Eric Eaton

TÉCNICO+
FORMAÇÃO AVANÇADA

# Learning stances

- classic AI
- e.g. heuristics to play chess, drive a car, recommend products, diagnose

- supervised learning
- e.g. experience from good chess players, drivers, liked recommendations, clinical histories for decision support

- unsupervised learning
- e.g. understand decisions, detect anomalies and behavioral patterns, summarize actions

![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

![img-11.jpeg](img-11.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+ FORMAÇÃO AVANÇADA

# Coming to terms with terms

What about...
- Data-centric AI, Agentic AI
- Data Mining, Multivariate Data Analysis
- Business Intelligence

... and terminology choices...
- AI vs intelligent systems vs intelligent agents
- variable vs attribute vs feature
- observation vs instance vs object vs record vs data point

TÉCNICO+ FORMACÃO AVANÇADA

# Structured view on ML

16

TÉCNICO+

FORMAÇÃO AVANÇADA

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

TÉCNICO+ FORMACÃO AVANÇADA

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

![img-12.jpeg](img-12.jpeg)

![img-13.jpeg](img-13.jpeg)

TÉCNICO+

FORMAÇÃO AVANÇADA

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

![img-14.jpeg](img-14.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

# Terminology

![img-15.jpeg](img-15.jpeg)

## Multivariate data:

- set of **observations**, $X = \{\mathbf{x}_1, \dots, \mathbf{x}_n\}$ (population)
- with values/**features** along a set of **variables**, $Y = \{y_1, \dots, y_m\}$
- **input variables** (explanatory) and optional output variables (**targets**), $Z = \{y_1, \dots, z_p\}$
- data **size** = number of observations, $|X| = n$
- data **dimensionality** = number of input variables, $|Y| = m$

TÉCNICO+
FORMAÇÃO AVANÇADA

# Learning from data

![img-16.jpeg](img-16.jpeg)

Learning from data: retrieving relevant patterns
- relations/patterns/abstractions ≡ associations of interest on specific observations and variables
- unexpectedly informative
- unexpectedly discriminative (of one or more targets)
- use these relations to learn descriptors, classifiers, regressors, multi-output predictors, forecasters...

TÉCNICO+
FORMAÇÃO AVANÇADA
21

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

![img-17.jpeg](img-17.jpeg)

TÉCNICO+

FORMAÇÃO AVANÇADA

# Classification

Recall: given a set of labeled observations, $\{(x_1, z_1), \ldots, (x_n, z_n)\}$ where $z_n \in \Sigma$, a classifier $M$ is a mapping function between domain variables and a categoric variable, $M: X \to Z$

- **prediction**: given a new unlabeled observation $\mathbf{x}_{new}$, use $M$ to classify: $\hat{z}_{new} = M(x_{new})$
- **description**: inspect $M$ to acquire new knowledge

![img-18.jpeg](img-18.jpeg)
Binary classification:

![img-19.jpeg](img-19.jpeg)
Multi-class classification:

TÉCNICO+

FORMAÇÃO AVANÇADA

# Classification: salmon?

![img-20.jpeg](img-20.jpeg)

- width and lightness are discriminative variables
- generalization ability linked with:
- underfitting risks
- overfitting risks
- aim: find a balanced model capacity

![img-21.jpeg](img-21.jpeg)

![img-22.jpeg](img-22.jpeg)

24

TECNICO+

FORMAÇÃO AVANÇADA

# Regression

- descriptive setting: given a set of observations, $\{(\mathbf{x}_1, z_1), \ldots, (\mathbf{x}_n, z_n)\}$ where $z_i \in \mathbb{R}$, describe the relation between a set of (explanatory) variables and a target numeric variable
- predictive setting: given a set of observations, $\{(\mathbf{x}_1,z_1),\ldots ,(\mathbf{x}_n,z_n)\}$ where $z_{i}\in \mathbb{R}$, learn a mapping, $M:X\to Z$, to estimate the outcome (quantity) of a new observation

![img-23.jpeg](img-23.jpeg)

TÉCNICO+

FORMAÇÃO AVANÇADA

# Multi-output prediction

- Most outputs are not described by a single feature
- generative AI (e.g. question-answer, image drawing, signal transform)
- many others (e.g. self-driving vehicles, tagging content)

- Multi-output predictors, $M: X \to Z$
- predictive setting (learn predictor $M$)
- descriptive setting (explain predictor $M$)

- Special cases: multi-label classification when $\mathbf{z} \in \Sigma^{p}$ and multi-output regression when $\mathbf{z} \in \mathbb{R}^{p}$

![img-24.jpeg](img-24.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

# Statistical modeling

## Associative analysis

### Description of system dynamics

- mixture models
- generative models (such as HMMs)

![img-25.jpeg](img-25.jpeg)

![img-26.jpeg](img-26.jpeg)

![img-27.jpeg](img-27.jpeg)

TÉCNICO+

FORMAÇÃO AVANÇADA

# Clustering

Given a set of data observations, $X = \{\mathbf{x}_1,\dots ,\mathbf{x}_n\}$, cluster analysis aims at grouping observations into clusters, $C_i \subseteq X$ with $i = 1..k$, according to their (dis)similarity:

- observations in the same cluster are more similar than those in different clusters

![img-28.jpeg](img-28.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

# Pattern mining

![img-29.jpeg](img-29.jpeg)

{symptomA, testB+} ⇒ condition1 [support=10%, confidence=80%, lift=1.4, p-value=1E-4]

Given a dataset, find local associations (aka patterns) satisfying:

- statistical significance criteria (min #observations to be unexpectedly frequent)
- discriminative power (qualitative targets) or correlation (numeric targets) criteria

TÉCNICO+
FORMAÇÃO AVANÇADA

# Outlier analysis

- Understand peculiar behaviors and isolate anomalous observations
- fraud, cyberattacks, personalized health risks, adverse events, deviant social behavior, vehicle failures...

![img-30.jpeg](img-30.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

# Representation learning

Describe data using a compact set of informative (unsupervised) and/or predictive (supervised) features

- dimensionality reduction: subset of features from multivariate observations with minimal info loss
- latent feature representations of complex signals (series, image, text data) using neural networks

![img-31.jpeg](img-31.jpeg)

TÉCNICO+
FORMAÇÃO AVANÇADA

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

TÉCNICO+
FORMAÇÃO AVANÇADA

# Example: biomedicine

- Statistical modeling: assess risk determinants, model health trajectories, test clinical hypotheses
- Clustering: group patients in accordance with biophysiological profile (e.g. stratified therapeutics)
- Pattern mining: discover meaningful associations to understand disease/therapeutic responses
- Outlier analysis: personalized care to particular needs (e.g. multimorbidity, rare diseases)
- Representation learning: encoders and saliency maps of medical signals/images/notes
- Generative modeling: comprehensive models of disease/treatment (e.g. health progression)
- Classification: how monitored inputs affect diagnostics/prognostics, therapeutic choices
- Regression: estimate risk, drug dosage or efficacy, quantifiable phenotypes

TÉCNICO+ FORMACÃO AVANÇADA

Thank you!

Rui Henriques
rmch@tecnico.ulisboa.pt