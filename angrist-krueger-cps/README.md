# Angrist-Krueger-CPS Dataset

This dataset is an extract of the CPS data containing 30,967 observations on men born 1944-53 from the 1979 and 1981-85 March CPS, matched to lottery number dummies for groups of 25 lottery numbers. There are 72 variables including all covariates. The raw files (`extract.dta` and `samplcps.do`) were replicated and processed into a ready-to-use tabular `.mixed.txt` format suitable for `pgmpy` consumption.

## Column Descriptions

The dataset contains 72 variables derived from CPS extracts used to estimate the causal return to schooling using Vietnam draft lottery instruments.

### Core Economic Variables
- educ: Years of completed education.
- annwage: Annual wage income.
- weeks: Number of weeks worked during the previous year.
- hrsly: Hours worked during the previous year.
- hrslw: Hours worked during the last week.
- wageflag: Indicator that wage information is valid/observed.

### Demographic Variables
- age: Age of the respondent.
- agesq: Age squared, used to model nonlinear age effects.
- age2: Alternative squared age variable used in some regressions.
- race: Race category from CPS.
- black: Dummy variable indicating Black respondents.
- other: Dummy variable for race other than White or Black.
- marital: Marital status indicator.
- spsepres: Indicator for spouse present in the household.

### Education Variables
- higratt: Highest grade attended.
- higrcomp: Highest grade completed.
- educ: Years of completed schooling.
- college: Indicator for college education.
- someco: Indicator for some college attendance.

### Labor Market Variables
- esr: Employment status recode.
- esrflag: Indicator for valid employment status data.
- class: Class of worker (private, government, self-employed, etc.).
- ind: Industry classification code.
- occ: Occupation classification code.
- vet: Veteran status indicator.
- veteran: Recoded veteran status variable.

### Geographic Variables
- state: State code.
- division: Census division classification.
- smsa: Indicator for residence in a Standard Metropolitan Statistical Area.
- metcode: Metropolitan area code.
- city: Indicator for residence in a central city.
- balsmsa: Balanced SMSA classification.

### Regional Indicator Variables
These variables represent U.S. census regions used as regression controls.

- neweng: New England region indicator.
- midatl: Mid-Atlantic region indicator.
- eastnth: East North Central region indicator.
- westnth: West North Central region indicator.
- sthatl: South Atlantic region indicator.
- eaststh: East South Central region indicator.
- weststh: West South Central region indicator.
- mount: Mountain region indicator.
- pacific: Pacific region indicator.

### Birth Year Variables
Dummy variables indicating the respondent’s year of birth.

- yob: Year of birth.
- yob44–yob53: Indicator variables for birth years 1944 through 1953.

### Survey Year Variables
Dummy variables identifying the CPS survey year.

- year: CPS survey year.
- yr81: Indicator for survey year 1981.
- yr82: Indicator for survey year 1982.
- yr83: Indicator for survey year 1983.
- yr84: Indicator for survey year 1984.
- yr85: Indicator for survey year 1985.

### Draft Lottery Instrument Variables
These variables represent grouped Vietnam draft lottery numbers used as instruments for education.

- lott1–lott13: Lottery number group indicator variables.

### Sampling and Administrative Variables
- marchwt: CPS March supplement sampling weight.
- recode: Observation identifier used in the replication dataset.

## Dataset Purpose

This dataset is used to estimate the causal effect of education on wages using instrumental variables derived from Vietnam draft lottery numbers. The lottery provides exogenous variation in schooling decisions among men born between 1944 and 1953.

## References
**Source Citation:**
Angrist, J. D., & Krueger, A. B. (1995). Split-Sample Instrumental Variables Estimates of the Return to Schooling. Journal of Business & Economic Statistics, 13(2), 225-235.
Data extracted from the [Angrist Data Archive](https://economics.mit.edu/people/faculty/josh-angrist/angrist-data-archive).
