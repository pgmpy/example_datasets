# Lalonde Job Training Dataset

## Overview

This dataset originates from a randomized job-training experiment designed to estimate the causal effect of a workforce development program on participants' future earnings.

A group of disadvantaged workers applied for the training program. Among eligible applicants:

- Some were randomly assigned to receive training (treated group)
- Others were randomly assigned not to receive training (control group)

Because assignment was randomized, the treated and control groups are highly comparable. Their covariate distributions strongly overlap, allowing for credible causal inference.

The experimental comparison provides a ground-truth estimate of the treatment effect on earnings.

## Observational Comparison Groups

In addition to the experimental data, the dataset includes two non-experimental comparison groups:

- CPS (Current Population Survey)
- PSID (Panel Study of Income Dynamics)

These datasets are drawn from general population surveys and are not part of the original randomized experiment.

They are used to replace the experimental control group in order to simulate an observational setting, where:

- The treated group comes from the experimental sample
- The control group comes from a different population

This setup introduces:

- Covariate imbalance
- Potential selection bias
- Reduced overlap

These observational variants are commonly used to evaluate the robustness of causal inference methods.

## Structure of the dataset

Each row represents an individual applicant from the job-training program.

| Variable (Left to Right)| Description                                      | Type        |
|--------------|--------------------------------------------------|------------|
| training    | Training indicator (1 = training, 0 = control)  | Categorical     |
| age          | Age in years                                     | Discrete |
| education    | Years of education                               | Discrete |
| black        | 1 if Black, 0 otherwise                          | Categorical     |
| hispanic     | 1 if Hispanic, 0 otherwise                       | Categorical     |
| married      | 1 if married, 0 otherwise                        | Categorical     |
| no_degree     | 1 if no high school degree, 0 otherwise          | Categorical     |
| re74         | Earnings in 1974                                 | Continuous |
| re75         | Earnings in 1975                                 | Continuous |
| re78         | Earnings in 1978 (primary outcome)               | Continuous |


## Dataset Files

| Dataset Name              | File Name                | Description                                      | Number of Samples |
|---------------------------|--------------------------|--------------------------------------------------|-------------------|
| lalonde/treated  | [nswre74_treated.txt](data/nswre74_treated.txt)    | Randomized treated group (Dehejia-Wahha Sample) | 185               |
| lalonde/control  | [nswre74_control.txt](data/nswre74_control.txt)      | Randomized control group (Dehejia-Wahha Sample) | 260               |
| lalonde/cps               | [cps_controls.txt](data/cps_controls.txt)          | Non-experimental CPS comparison group            | 15,992               |
| lalonde/cps2              | [cps2_controls.txt](data/cps2_controls.txt)          | Non-experimental CPS comparison group            | 2,369               |
| lalonde/cps3              | [cps3_controls.txt](data/cps3_controls.txt)         | Non-experimental CPS comparison group            | 429               |
| lalonde/psid              | [psid_controls.txt](data/psid_controls.txt)        | Non-experimental PSID comparison group           | 2,490               |
| lalonde/psid2             | [psid2_controls.txt](data/psid2_controls.txt)         | Non-experimental PSID comparison group           | 253               |
| lalonde/psid3             | [psid3_controls.txt](data/psid3_controls.txt)         | Non-experimental PSID comparison group           | 128               |

NOTE: Only changes from the file done is to standardization based on data format in this repo. 

## References

1. [National Supported Work (NSW) Data – NBER](https://users.nber.org/~rdehejia/nswdata2.html)

2. Rajeev Dehejia and Sadek Wahba, "Causal Effects in Non-Experimental Studies: Reevaluating the Evaluation of Training Programs," Journal of the American Statistical Association, Vol. 94, No. 448 (December 1999), pp. 1053-1062. 

3. Rajeev Dehejia and Sadek Wahba, "Propensity Score Matching Methods for Non-Experimental Causal Studies," Review of Economics and Statistics, Vol. 84, (February 2002), pp. 151-161.

4. Robert Lalonde, "Evaluating the Econometric Evaluations of Training Programs," American Economic Review, Vol. 76 (1986), pp. 604-620. 

## License

This dataset is distributed under the Creative Commons
Attribution-NonCommercial 2.0 Generic (CC BY-NC 2.0) license.
It is redistributed in this repository strictly for research and
benchmarking purposes.

See the [LICENSE](LICENSE) file for the full license text.
