# data_processor.py
import logging
import pandas as pd

logger = logging.getLogger(__name__)

def remove_duplicates(df):
    """Remove duplicate rows."""
    before = df.copy()
    df = df.drop_duplicates()
    logger.debug(f"Removed {len(before) - len(df)} rows with duplicate data")
    return df


def handle_missing(df, axis="rows"):
    """Drop rows or columns containing missing values."""
    if axis == "rows":
        before = df.copy()
        df = df.dropna(axis=0)
        logger.debug(f"Removed {len(before) - len(df)} rows with missing data")

    if axis == "columns":
        before = df.copy()
        df = df.dropna(axis=1)
        logger.debug(f"Removed {before.shape[1] - df.shape[1]} columns with missing data")

    else:
        logger.error(f"Unsupported axis: {axis}"")
        raise ValueError(f"Unsupported axis: {axis}")
    return df


def remove_outliers(df, columns, method, threshold):
    """Remove outliers from the specified numeric columns."""
    pass


def process_data(df, config):
    """Apply the processing steps enabled in the configuration."""
    pass


def create_cleaning_report(df_before, df_after):
    """Return a dictionary summarizing the cleaning results."""
    pass
