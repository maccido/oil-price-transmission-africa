"""
ARDL and NARDL estimation helpers.
Author: Mohammed Tukur Saidu, PhD
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.ardl import ARDL, ardl_select_order
from statsmodels.stats.diagnostic import acorr_breusch_godfrey, het_breuschpagan
from statsmodels.stats.stattools import jarque_bera


def estimate_ardl(
    endog: pd.Series,
    exog: pd.DataFrame,
    maxlag: int = 6,
    trend: str = "c",
) -> ARDL:
    """
    Select optimal lag order and estimate ARDL model.
    """
    sel = ardl_select_order(
        endog, maxlag=maxlag, exog=exog, trend=trend, ic="aic", glob=True
    )
    return sel.model.fit()


def estimate_nardl(
    endog: pd.Series,
    brent_pos: pd.Series,
    brent_neg: pd.Series,
    controls: pd.DataFrame | None = None,
    maxlag: int = 6,
) -> ARDL:
    """
    Estimate NARDL by treating positive and negative partial sums as separate regressors.
    """
    exog = pd.concat([brent_pos, brent_neg], axis=1)
    if controls is not None:
        exog = pd.concat([exog, controls], axis=1)

    sel = ardl_select_order(
        endog, maxlag=maxlag, exog=exog, trend="c", ic="aic", glob=True
    )
    return sel.model.fit()


def bounds_test_summary(model: ARDL) -> dict:
    """
    Extract key cointegration diagnostics from an estimated ARDL.
    (Simplified version of Pesaran-Shin-Smith bounds test.)
    """
    # Note: Full critical-value tables require the bounds F-statistic.
    # Here we return the model F-stat and residual diagnostics as a practical proxy.
    return {
        "f_statistic": model.fvalue,
        "aic": model.aic,
        "bic": model.bic,
        "nobs": int(model.nobs),
    }


def residual_diagnostics(model) -> dict:
    """
    Standard post-estimation checks used in my published papers.
    """
    resid = model.resid
    bg = acorr_breusch_godfrey(model, nlags=4)
    bp = het_breuschpagan(resid, model.model.exog)
    jb = jarque_bera(resid)

    return {
        "Breusch-Godfrey_LM": bg[0],
        "Breusch-Godfrey_pval": bg[1],
        "Breusch-Pagan_LM": bp[0],
        "Breusch-Pagan_pval": bp[1],
        "Jarque-Bera": jb[0],
        "Jarque-Bera_pval": jb[1],
    }
