# Angrist-Kreuger-CPS Dataset

This dataset is an extract of the CPS data containing 30,967 observations on men born 1944-53 from the 1979 and 1981-85 March CPS, matched to lottery number dummies for groups of 25 lottery numbers. There are 72 variables including all covariates. The raw files (`extract.dta` and `samplcps.do`) were replicated and processed into a ready-to-use tabular `.mixed.txt` format suitable for `pgmpy` consumption.

## Column Descriptions
The dataset contains 72 variables. Key columns include:
- `educ`: Years of education.
- `veteran`: Veteran status.
- `lnyrwage`, `annwage`: Logarithm of annual wage, and annual wage.
- `lnwkwage`, `wkwage`: Logarithm of weekly wage, and weekly wage.
- `yob45` through `yob53`: Year of birth dummy variables.
- `lot1b50` through `lot3b53`, and `lott1` through `lott13`: Lottery number dummies.
- `black`, `other`: Race demographic variables.
- `midatl`, `eastnth`, `westnth`, `city`: Regional and location indicator variables.
- `spsepres`, `yr81` to `yr85`, `ceiling`, `coarse1`, `coarse2`, `coarse3`, `recode`: Other covariates.

## References
**Source Citation:**
Angrist, J. D., & Krueger, A. B. (1995). Split-Sample Instrumental Variables Estimates of the Return to Schooling. Journal of Business & Economic Statistics, 13(2), 225-235.
Data extracted from the [Angrist Data Archive](https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive).
