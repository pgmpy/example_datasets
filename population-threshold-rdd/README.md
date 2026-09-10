# Population Threshold RDD (Italy)

Municipality-year sample for regression discontinuity designs that use legal
population cutoffs, from Eggers, Freier, Grembi, and Nannicini (AJPS 2018).
This file is the Italian `ipd` table from `pop_devs_three_countries_v5.RData`
in the replication archive. Each row is one municipality-year compared to a
nearby population threshold.

## Source

Grembi, Veronica; Freier, Ronny; Eggers, Andrew C.; Nannicini, Tommaso, 2017,
"Replication Data for: Regression Discontinuity Designs Based on Population
Thresholds: Pitfalls and Solutions", Harvard Dataverse, V1.
https://doi.org/10.7910/DVN/PGXO5O

Eggers, Andrew C., Ronny Freier, Veronica Grembi, and Tommaso Nannicini. 2018.
"Regression Discontinuity Designs Based on Population Thresholds: Pitfalls and
Solutions." *American Journal of Political Science* 62 (1): 210-229.
https://doi.org/10.1111/ajps.12332

Original archive: `replication_materials_submitted_20170403.zip`
MD5 `df3c2bd36a9f5fcd9d1e86d5b8e31f66`

## License

CC0 1.0 Universal. See [LICENSE](LICENSE).

## Checksums

- Original Dataverse zip MD5: `df3c2bd36a9f5fcd9d1e86d5b8e31f66`
- Packaged file SHA256: `608e33e1907f573e991d206ea72827b7b65c674f514d3a5f37ae754ba1430846`
- Packaged file: `data/population-threshold-rdd.italy.mixed.txt`

## Columns

| Column | Description |
|---|---|
| `id` | Municipality identifier (`n_istat`) |
| `year` | Census year |
| `pop` | Census population (running variable in levels) |
| `cut` | Population threshold |
| `pop_dev` | `pop - cut` (RDD running variable; treated if >= 0) |
| `lpop_dev` | Lagged running variable |
| `lead_pop` | Lead census population |
| `placebo` | 1 if this cutoff is a placebo threshold |
| `salary` | 1 if mayor wage changes at this cutoff |
| `council` | 1 if council size changes at this cutoff |
| `small_threshold` | 1 if the cutoff is a small threshold |
| `region_code` | ISTAT region code |
| `macro_area` | North / Center / South |
| `sea` | 1 if the municipality is on the shore |
| `nonprof_ass` | Nonprofit organizations per capita (provincial, 2001) |
| `donation` | Blood bags per 100 inhabitants (1995) |
| `pop_more_54` | Share of residents older than 54 |
| `pop_less_20` | Share of residents younger than 20 |
| `vacation_homes_91` | Vacation homes as a share of residential buildings, 1991 |

Missing values are encoded as `NA`.
