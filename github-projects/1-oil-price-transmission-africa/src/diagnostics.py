"""
Diagnostic and visualization helpers.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_series(df: pd.DataFrame, cols: list[str], title: str = "", save_path: str | None = None):
    """Multi-panel time-series plot."""
    n = len(cols)
    fig, axes = plt.subplots(n, 1, figsize=(12, 2.8 * n), sharex=True)
    if n == 1:
        axes = [axes]
    for ax, col in zip(axes, cols):
        ax.plot(df.index, df[col], color="#1f77b4", linewidth=1.2)
        ax.set_ylabel(col)
        ax.grid(True, alpha=0.3)
    axes[0].set_title(title, fontsize=13, fontweight="bold")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_partial_sums(df: pd.DataFrame, save_path: str | None = None):
    """Visualize positive / negative oil-price decompositions."""
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(df.index, df["brent_pos"], label="Positive partial sum", color="#2ca02c")
    ax.plot(df.index, df["brent_neg"], label="Negative partial sum", color="#d62728")
    ax.set_title("Oil-Price Partial Sum Decomposition (NARDL)", fontweight="bold")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def cusum_plot(model, save_path: str | None = None):
    """
    Simple recursive residual CUSUM-style plot for stability illustration.
    (Full recursive residuals require recursive estimation; this is a practical proxy.)
    """
    resid = model.resid
    cusum = np.cumsum(resid) / np.std(resid)
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(cusum, color="#1f77b4")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.set_title("CUSUM of Recursive Residuals (illustrative)", fontweight="bold")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
