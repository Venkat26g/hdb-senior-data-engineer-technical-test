"""
Project configuration.

This module centralizes all project paths and constants used across the ETL pipeline.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Project Paths
# -----------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"
CLEANED_DIR = DATA_DIR / "cleaned"
TRANSFORMED_DIR = DATA_DIR / "transformed"
FAILED_DIR = DATA_DIR / "failed"
HASHED_DIR = DATA_DIR / "hashed"

DOCS_DIR = PROJECT_ROOT / "docs"
NOTEBOOK_DIR = PROJECT_ROOT / "notebooks"
TEST_DIR = PROJECT_ROOT / "tests"

LOG_DIR = PROJECT_ROOT / "logs"

# -----------------------------------------------------------------------------
# Create folders if they don't exist
# -----------------------------------------------------------------------------

DIRECTORIES = [
    RAW_DIR,
    CLEANED_DIR,
    TRANSFORMED_DIR,
    FAILED_DIR,
    HASHED_DIR,
    DOCS_DIR,
    LOG_DIR
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Input Files
# -----------------------------------------------------------------------------

INPUT_FILES = [
    "ResaleFlatPricesBasedonApprovalDate2000Feb2012.csv",
    "resale-flat-prices-based-on-registration-date-from-jan-2012-to-dec-2014.csv",
    "resale-flat-prices-based-on-registration-date-from-jan-2015-to-dec-2016.csv",
]

# -----------------------------------------------------------------------------
# Output Files
# -----------------------------------------------------------------------------

MASTER_DATASET = CLEANED_DIR / "master_dataset.csv"

FAILED_DATASET = FAILED_DIR / "failed_records.csv"

TRANSFORMED_DATASET = TRANSFORMED_DIR / "transformed_dataset.csv"

HASHED_DATASET = HASHED_DIR / "hashed_dataset.csv"

PROFILE_REPORT = DOCS_DIR / "data_profile_report.csv"

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------

LOG_FILE = LOG_DIR / "etl_pipeline.log"

# -----------------------------------------------------------------------------
# Lease Configuration
# -----------------------------------------------------------------------------

LEASE_DURATION = 99

# -----------------------------------------------------------------------------
# Hashing
# -----------------------------------------------------------------------------

HASH_ALGORITHM = "sha256"