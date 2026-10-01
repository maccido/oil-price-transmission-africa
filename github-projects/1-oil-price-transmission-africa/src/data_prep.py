"""
Data preparation utilities for oil-price transmission analysis.
Author: Mohammed Tukur Saidu, PhD
"""

import pandas as pd
import numpy as np
from pathlib import Path

def load_and_prepare(data_path: str | Path) -> pd.DataFrame:
    """
    Load sample macro data and create the core variables used in ARDL/NARDL.
    
    Expected columns in CSV:
        date, brent, cpi_sa, cpi_ma, cpi_ci, reer_sa, reer_ma, reer_ci, ip_sa
    """
    df = pd.read_csv(data_path, parse_dates=["date"])
    df = df.set_index("date").sort_index()

    # Log transformations (standard in the literature)
    df["lbrent"] = np.log(df["brent"])
    df["lcpi_sa"] = np.log(df["cpi_sa"])
    df["lcpi_ma"] = np.log(df["cpi_ma"])
    df["lcpi_ci"] = np.log(df["cpi_ci"])
    df["lreer_sa"] = np.log(df["reer_sa"])
    df["lreer_ma"] = np.log(df["reer_ma"])
    df["lreer_ci"] = np.log(df["reer_ci"])

    # First differences
    for col in ["lbrent", "lcpi_sa", "lcpi_ma", "lcpi_ci",
                "lreer_sa", "lreer_ma", "lreer_ci"]:
        df[f"d_{col}"] = df[col].diff()

    # Positive and negative partial sums (NARDL)
    df["brent_pos"] = df["d_lbrent"].clip(lower=0).cumsum()
    df["brent_neg"] = df["d_lbrent"].clip(upper=0).cumsum()

    return df.dropna()


def create_sample_data(n_months: int = 288, seed: int = 42) -> pd.DataFrame:
    """
    Generate realistic sample monthly data (2000-01 to 2023-12)
    that mimics the statistical properties of the series used in the PhD thesis.
    """
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2000-01-01", periods=n_months, freq="MS")

    # Brent crude – random walk with drift + occasional spikes
    brent = 30 + np.cumsum(rng.normal(0.15, 2.5, n_months))
    brent = np.clip(brent, 15, 140)

    # CPI series (higher inflation environments)
    cpi_sa = 100 * np.exp(np.cumsum(rng.normal(0.004, 0.006, n_months)))
    cpi_ma = 100 * np.exp(np.cumsum(rng.normal(0.003, 0.005, n_months)))
    cpi_ci = 100 * np.exp(np.cumsum(rng.normal(0.005, 0.008, n_months)))

    # REER (mean-reverting around 100)
    reer_sa = 100 + np.cumsum(rng.normal(0, 1.2, n_months))
    reer_ma = 100 + np.cumsum(rng.normal(0, 1.0, n_months))
    reer_ci = 100 + np.cumsum(rng.normal(0, 1.5, n_months))

    # Industrial production (for control)
    ip_sa = 100 + np.cumsum(rng.normal(0.1, 1.8, n_months))

    df = pd.DataFrame({
        "date": dates,
        "brent": brent,
        "cpi_sa": cpi_sa,
        "cpi_ma": cpi_ma,
        "cpi_ci": cpi_ci,
        "reer_sa": reer_sa,
        "reer_ma": reer_ma,
        "reer_ci": reer_ci,
        "ip_sa": ip_sa,
    })
    return df
