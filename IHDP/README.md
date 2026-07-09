# IHDP Covariates

This directory contains the fixed covariates and treatment assignment used by
pgmpy's IHDP semi-synthetic dataset simulator (`pgmpy.datasets.IHDPDataset`).

## Files

- `ihdp_covariates.csv` — covariate-only extract (747 rows × 26 columns:
  `treatment` + `x1` through `x25`).
- `prep.py` — script that downloads `ihdp_npci_1.csv` from the
  [CEVAE repository](https://github.com/AMLab-Amsterdam/CEVAE/tree/master/datasets/IHDP/csv),
  extracts the covariates, validates the expected shape/counts/coding,
  and writes `ihdp_covariates.csv`.
- `LICENSE` — provenance and licensing notice.

## Provenance

The extract is prepared from `ihdp_npci_1.csv` in the archived CEVAE
repository. The source file is **fetched at extraction time** by `prep.py`
(not bundled in this repo) to avoid redistributing upstream data.

The response-surface design follows the IHDP benchmark introduced by
Hill (2011) and the later CEVAE benchmark usage from Louizos et al. (2017).
The covariates and treatment assignment are fixed across the 1000
CEVAE/NPCI replications; only the simulated outcome columns vary.
Therefore pgmpy stores only the covariates and treatment needed to
generate outcomes inside `IHDPDataset`.

## Reproducing `ihdp_covariates.csv`

```bash
# Requires: numpy, pandas
python prep.py
```

The script downloads the source CSV, extracts covariates, runs validation
assertions, and writes `ihdp_covariates.csv`. The output is byte-identical
across runs given the same upstream file.

## Column details

- `x1`–`x6` (continuous): birth weight, head circumference, weeks preterm,
  birth order, neonatal health index, mother's age. Already standardized
  (mean ≈ 0, std ≈ 1) in the upstream CEVAE/NPCI file.
- `x7`–`x25` (binary/categorical): site and demographic indicators. All
  are `{0, 1}` except `x14` ("first" — firstborn), which is `{1, 2}` by
  upstream convention (matches EconML's coding).

## References

- Hill, J. L. (2011). Bayesian Nonparametric Modeling for Causal Inference.
  *Journal of Computational and Graphical Statistics*, 20(1), 217–240.
- Louizos, C., Shalit, U., Mooij, J. M., Sontag, D., Zemel, R., &
  Welling, M. (2017). Causal Effect Inference with Deep Latent-Variable
  Models. *NeurIPS*.
- Johansson, F., Shalit, U., & Sontag, D. (2016). Learning Representations
  for Counterfactual Inference. *ICML*.

## License

See [LICENSE](LICENSE) in this directory.
