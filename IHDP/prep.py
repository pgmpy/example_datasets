"""Extract the fixed IHDP covariates + treatment from a CEVAE/NPCI replication.

Downloads ihdp_npci_1.csv from the archived CEVAE repository:
https://github.com/AMLab-Amsterdam/CEVAE/tree/master/datasets/IHDP/csv

The source file is fetched on the fly rather than bundled in this repo
to avoid redistributing upstream data and the licensing complexity that
comes with it. The CEVAE repository is archived (read-only) since
July 2020, so the URL is stable.

Covariates and treatment are identical across all 1000 CEVAE/NPCI
replications (only the simulated outcome columns y_factual, y_cfactual,
mu0, mu1 vary), so extracting from replication #1 is sufficient and
representative of every other replication.

This file becomes permanent shared infrastructure once uploaded to the
pgmpy/example_datasets HuggingFace repo and loaded via _get_raw_data()
on every IHDPDataset instantiation, so the assertions below are meant
to catch a bad extraction (wrong source file, corrupted download,
upstream format change) before it ships, not just document intent.

Usage:
    python prep.py

Requirements:
    numpy, pandas
"""

import os
import ssl
import subprocess
import tempfile
import urllib.request

import numpy as np
import pandas as pd

CEVAE_URL = (
    "https://raw.githubusercontent.com/AMLab-Amsterdam/CEVAE/"
    "master/datasets/IHDP/csv/ihdp_npci_1.csv"
)
OUTPUT_PATH = "ihdp_covariates.csv"

# Download source file


def _download(url, dest):
    """Download ``url`` to ``dest``, working around common SSL issues."""
    # Try default SSL context first.
    try:
        urllib.request.urlretrieve(url, dest)
        return
    except urllib.error.URLError:
        pass

    # Try certifi certificates if available.
    try:
        import certifi

        ctx = ssl.create_default_context(cafile=certifi.where())
        opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
        with opener.open(url) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        return
    except (ImportError, urllib.error.URLError):
        pass

    # Last resort: fall back to curl (available on macOS/Linux).
    result = subprocess.run(["curl", "-fsSL", "-o", dest, url], capture_output=True)
    if result.returncode == 0:
        return

    raise RuntimeError(
        f"Could not download {url}. Tried urllib, certifi, and curl. "
        "Check your network connection and SSL certificates."
    )


print(f"Downloading {CEVAE_URL} ...")
tmp_fd, tmp_path = tempfile.mkstemp(suffix=".csv")
try:
    os.close(tmp_fd)
    _download(CEVAE_URL, tmp_path)
    print(f"Downloaded to temporary file: {tmp_path}")

    # Load and validate

    cols = ["treatment", "y_factual", "y_cfactual", "mu0", "mu1"] + [f"x{i}" for i in range(1, 26)]
    df = pd.read_csv(tmp_path, header=None, names=cols)
finally:
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)

    print("Cleaned up temporary file.")

print(f"Original shape: {df.shape}")
assert df.shape == (747, 30), f"Expected (747, 30), got {df.shape}"

# Extract covariates + treatment
covariates = df[["treatment"] + [f"x{i}" for i in range(1, 26)]]

print(f"Extracted shape: {covariates.shape}")
assert covariates.shape == (747, 26), f"Expected (747, 26), got {covariates.shape}"

n_treated = int(covariates["treatment"].sum())
n_control = len(covariates) - n_treated
print(f"Treated count: {n_treated}")
print(f"Control count: {n_control}")
assert (n_treated, n_control) == (139, 608), (
    f"Expected 139 treated / 608 control (the standard post-exclusion IHDP sample), got {n_treated} / {n_control}"
)

# x1-x6 (bw, b.head, preterm, birth.o, nnhealth, momage) are continuous
# and, per the upstream NPCI/CEVAE pipeline, already standardized. This
# is what lets the simulator skip re-standardizing on every load.
continuous_cols = [f"x{i}" for i in range(1, 7)]
means = covariates[continuous_cols].mean()
stds = covariates[continuous_cols].std()
assert np.allclose(means, 0, atol=1e-8), f"x1-x6 means not ~0:\n{means}"
assert np.allclose(stds, 1, atol=1e-6), f"x1-x6 stds not ~1:\n{stds}"
print("Continuous columns x1-x6 confirmed pre-standardized (mean~0, std=1).")

# x7-x25 are binary/categorical site & demographic indicators. All are
# {0,1} except x14 ("first" = firstborn indicator), which is {1,2} in
# the canonical CEVAE/NPCI data — not a bug: EconML's own port carries
# an explicit comment doing the equivalent {0,1}->{1,2} shift for this
# same variable, so this is the literature-standard coding, kept as-is.
strictly_binary_cols = [f"x{i}" for i in range(7, 26) if i != 14]
for col in strictly_binary_cols:
    uniques = set(covariates[col].unique().tolist())
    assert uniques <= {0, 1}, f"{col} is not binary, found values: {uniques}"
assert set(covariates["x14"].unique().tolist()) == {1, 2}, (
    "x14 ('first') expected to be {1,2}-coded (matches EconML's convention "
    "for this variable) — got a different value set, upstream file may "
    "have changed."
)
print("Columns x7-x25 confirmed binary (0/1), except x14 ('first') which is {1,2} by design.")

covariates.to_csv(OUTPUT_PATH, index=False)
print(f"Saved {OUTPUT_PATH}")

# Covariate identity reference (documentation only -- x1..x25 stay as the
# actual column names; see rationale below the dict).
#
# Verified empirically, not assumed from documentation: cross-referenced
# against EconML's independently-maintained raw covariate file
# (econml/data/ihdp/sim.csv, github.com/microsoft/EconML), which has real
# column names. Confirmed by reconstruction, not just plausible ordering:
#   1. Applied the same treated-nonwhite-mother exclusion to EconML's raw
#      985-row file -> 747 rows, 139 treated / 608 control (exact match)
#   2. Row-by-row treatment assignment: 100% match after exclusion, which
#      only happens if row order is identical between the two independently
#      sourced files (a random misalignment would give ~70% agreement, not
#      100%, given the 139/747 treated base rate)
#   3. x7-x25 (all binary/site indicators except x14): bit-for-bit exact
#      match against EconML's named columns, in this order
#   4. x14 ("first"): exact match once EconML's raw {0,1} value has 1
#      added -> {1,2} -- confirming this is genuinely how the variable is
#      coded upstream, not a data error introduced anywhere in this pipeline
#   5. x1-x6 (continuous): exact match, residuals at floating-point
#      precision (1e-9 to 1e-15), once EconML's raw values are standardized
#      using this file's own 747-row mean and std(ddof=1)
#
# Every one of treatment + x1..x25 reconstructs exactly under this mapping.
#
# Not renamed to these names in the actual output: every paper and package
# that reports IHDP results (NPCI, EconML, CEVAE, ...) refers to these
# covariates as x1-x25, and IHDPDataset's DAG/test/cross-validation code
# is built around that convention. This dict is for anyone who needs to
# know what a given xN actually is.

COVARIATE_INFO = {
    "x1": ("bw", "continuous", "Birth weight (grams)"),
    "x2": ("b.head", "continuous", "Head circumference at birth"),
    "x3": ("preterm", "continuous", "Weeks preterm"),
    "x4": ("birth.o", "continuous", "Birth order"),
    "x5": ("nnhealth", "continuous", "Neonatal health index"),
    "x6": ("momage", "continuous", "Mother's age"),
    "x7": ("sex", "binary", "Infant sex"),
    "x8": ("twin", "binary", "Twin birth"),
    "x9": ("b.marr", "binary", "Mother married at birth"),
    "x10": ("mom.lths", "binary", "Mother's education: less than high school"),
    "x11": ("mom.hs", "binary", "Mother's education: high school"),
    "x12": ("mom.scoll", "binary", "Mother's education: some college"),
    "x13": ("cig", "binary", "Smoked cigarettes during pregnancy"),
    "x14": ("first", "{1,2} -- not 0/1, see note above", "Firstborn"),
    "x15": ("booze", "binary", "Drank alcohol during pregnancy"),
    "x16": ("drugs", "binary", "Used drugs during pregnancy"),
    "x17": ("work.dur", "binary", "Worked during pregnancy"),
    "x18": ("prenatal", "binary", "Received prenatal care"),
    "x19": ("site1", "binary", "Trial site indicator"),
    "x20": ("site2", "binary", "Trial site indicator"),
    "x21": ("site3", "binary", "Trial site indicator"),
    "x22": ("site4", "binary", "Trial site indicator"),
    "x23": ("site5", "binary", "Trial site indicator"),
    "x24": ("site6", "binary", "Trial site indicator"),
    "x25": ("site7", "binary", "Trial site indicator"),
}
