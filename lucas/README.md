# LUCAS0 Lung Cancer Sample Toy Dataset

## Overview

LUCAS0 is a synthetic benchmark dataset introduced in the *Causation and Prediction Challenge*. It was designed to evaluate feature selection, causal discovery, and predictive modeling methods under a known ground-truth data-generating process.

The dataset is generated from a predefined Bayesian network representing causal relationships between risk factors, symptoms, and lung cancer.

All variables are binary, and the full ground-truth graph structure is known.

The target variable is **Lung_Cancer**.

## Data Generating Process

The data are sampled from a directed acyclic graph (DAG) representing causal dependencies among variables.

Each node corresponds to a binary variable, and each edge represents a direct causal influence. The data are generated according to specified conditional probability tables (CPTs).

The generative model is a Markov process:

- Each variable depends only on its parents in the graph.
- Children are evaluated only after their parents.
- The joint distribution factorizes according to the DAG.

Both training and test sets are drawn from the same underlying distribution ("unmanipulated").

> Note: The conditional probabilities used for data generation are synthetic and have no biological interpretation.

## Conditional Probability Table used to generate this dataset
```
P(Anxiety=T)=0.64277
P(Peer Pressure=T)=0.32997
P(Smoking=T|Peer Pressure=F, Anxiety=F)=0.43118
P(Smoking=T|Peer Pressure=T, Anxiety=F)=0.74591
P(Smoking=T|Peer Pressure=F, Anxiety=T)=0.8686
P(Smoking=T|Peer Pressure=T, Anxiety=T)=0.91576
P(Yellow Fingers=T|Smoking=F)=0.23119
P(Yellow Fingers=T|Smoking=T)=0.95372
P(Genetics=T)=0.15953
P(Lung cancer=T|Genetics=F, Smoking=F)=0.23146
P(Lung cancer=T|Genetics=T, Smoking=F)=0.86996
P(Lung cancer=T|Genetics=F, Smoking=T)=0.83934
P(Lung cancer=T|Genetics=T, Smoking=T)=0.99351
P(Attention Disorder=T|Genetics=F)=0.28956
P(Attention Disorder=T|Genetics=T)=0.68706
P(Born an Even Day=T)=0.5
P(Allergy=T)=0.32841
P(Coughing=T|Allergy=F, Lung cancer=F)=0.1347
P(Coughing=T|Allergy=T, Lung cancer=F)=0.64592
P(Coughing=T|Allergy=F, Lung cancer=T)=0.7664
P(Coughing=T|Allergy=T, Lung cancer=T)=0.99947
P(Fatigue=T|Lung cancer=F, Coughing=F)=0.35212
P(Fatigue=T|Lung cancer=T, Coughing=F)=0.56514
P(Fatigue=T|Lung cancer=F, Coughing=T)=0.80016
P(Fatigue=T|Lung cancer=T, Coughing=T)=0.89589
P(Car Accident=T|Attention Disorder=F, Fatigue=F)=0.2274
P(Car Accident=T|Attention Disorder=T, Fatigue=F)=0.779
P(Car Accident=T|Attention Disorder=F, Fatigue=T)=0.78861
P(Car Accident=T|Attention Disorder=T, Fatigue=T)=0.97169
```

## Variables

The variables from left to right are as follows (11 is the target variable):

| Index | Variable |
|-------|----------|
| 0 | Smoking |
| 1 | Yellow_Fingers |
| 2 | Anxiety |
| 3 | Peer_Pressure |
| 4 | Genetics |
| 5 | Attention_Disorder |
| 6 | Born_an_Even_Day |
| 7 | Car_Accident |
| 8 | Fatigue |
| 9 | Allergy |
| 10 | Coughing |
| 11 | Lung_Cancer |

**Note:** all of these variable are binary variables where 1->True 0->False

## Dataset Files

| File Name | Description |
|--------------|------------|
| [data/lucas0.discrete.txt](data/lucas0.discrete.txt) | Training dataset sampled from the generative model |
| [ground.truth/lucas0.ground.truth.graph.txt](ground.truth/lucas0.ground.truth.graph.txt)  | Ground-truth DAG in DAggity format |
| [images/lucas0.lucas0.ground.truth.png](images/lucas0.lucas0.ground.truth.png) | Image of DAG from the main dataset |

## References

1. Guyon, Isabelle & Aliferis, Constantin & Cooper, Gregory & Elisseeff, André & Pellet, Jean-Philippe & Spirtes, Peter & Statnikov, Alexander. (2008).  
   *Design and Analysis of the Causation and Prediction Challenge.*  
   Journal of Machine Learning Research - Proceedings Track, 3, 1–33.

2. LUCAS Dataset Website:  
   [https://www.causality.inf.ethz.ch/data/LUCAS.html](https://www.causality.inf.ethz.ch/data/LUCAS.html)

## License

No explicit license information was provided by the original authors
for the LUCAS0 dataset.

This dataset is included here for research and benchmarking purposes
with attribution to the original source. The only modifications made
to the file are formatting changes.