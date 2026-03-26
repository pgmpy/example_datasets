# Angrist-Krueger Quarter of Birth (1980 Census)

## Description

This dataset is extracted from the 1980 U.S. Census and was used by Joshua D. Angrist and
Alan B. Krueger in their seminal paper on instrumental variables estimation. It contains
individual-level data on earnings, education, and quarter of birth, which serves as an
instrument for estimating the causal effect of education on earnings.

## Source

Angrist, J. D., & Krueger, A. B. (1991). Does Compulsory School Attendance Affect Schooling
and Earnings? *The Quarterly Journal of Economics*, 106(4), 979–1014.
https://doi.org/10.2307/2937954

## Columns

| Column     | Description                                          |
|------------|------------------------------------------------------|
| `lwklywge` | Log weekly wage (natural log of weekly earnings)     |
| `educ`     | Years of completed education                         |
| `age`      | Age (in years) at the time of the 1980 Census        |
| `qob`      | Quarter of birth (1–4)                               |
| `pob`      | Place (state) of birth (FIPS state code)             |

## Files

- `data/angrist-krueger-qob.continuous.txt` — Tab-separated dataset with headers.

## License

CC0 1.0 Universal. See [LICENSE](LICENSE).
