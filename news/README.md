The dataset is the `topic_doc_mean_n5000_k3477_seed_1.csv` downloaded from https://www.fredjo.com/files/NEWS_csv.zip and is mentioned in the paper titled "Learning Representations for Counterfactual Inference" by Fredrik D. Johansson, Uri Shalit, and David Sontag.


The variables are the following:

- treatment: The binary assigned intervention (0 or 1).
- y_factual: The observed simulated outcome for the assigned treatment.
- y_counterfactual: The unobserved, ground-truth outcome had the opposite treatment been assigned.
- mu0: The expected control response without added noise.
- mu1: The expected treatment response without added noise
- x_0 to x_3476: The latent topic features of the news articles.

Paper references:
Fredrik D. Johansson, Uri Shalit, & David Sontag. (2016). Learning Representations for Counterfactual Inference. In International Conference on Machine Learning (ICML).
