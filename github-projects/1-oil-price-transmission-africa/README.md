# Oil-Price Transmission, Exchange-Rate Pass-Through & Inflation Dynamics in Emerging Africa

**Author:** Mohammed Tukur Saidu, PhD  
**ORCID:** [0000-0003-0250-1311](https://orcid.org/0000-0003-0250-1311)  
**Google Scholar:** [Profile](https://scholar.google.com/citations?user=RWRqtmsAAAAJ)  
**Contact:** maccido@gmail.com | [LinkedIn](https://www.linkedin.com/in/mohammed-tukur-saidu-7458a858)

---

## Overview

This repository implements the core econometric framework used in my peer-reviewed research on oil-price transmission mechanisms in South Africa, Morocco, Côte d’Ivoire and the broader WAEMU region. It demonstrates:

- Symmetric and asymmetric ARDL / NARDL models  
- Exchange-rate pass-through and inflation dynamics  
- Robustness checks (CUSUM, CUSUMSQ, structural-break tests)  
- Scenario & sensitivity analysis  
- Reproducible Python workflow (with optional R companion)

The analysis mirrors the modelling approach in my publications in *Energy Reports*, *OPEC Energy Review* and *International Journal of Energy Economics and Policy*.

## Research Question

How do oil-price shocks transmit to consumer prices and real effective exchange rates in net oil-importing and exporting emerging African economies, and is the transmission asymmetric?

## Key Features

| Component | Implementation |
|-----------|----------------|
| Data | Monthly series (2000–2023) for Brent crude, REER, CPI, industrial production |
| Models | ARDL, NARDL (Shin et al. 2014), bounds testing |
| Diagnostics | Serial correlation, heteroskedasticity, normality, stability |
| Visualization | Impulse-response style cumulative multipliers, partial-sum decompositions |
| Output | Publication-ready tables & figures |

## Repository Structure

```
1-oil-price-transmission-africa/
├── data/
│   └── sample_macro_africa.csv          # Simulated / public-domain aligned series
├── notebooks/
│   └── 01_ardl_nardl_analysis.ipynb     # Main analysis notebook
├── src/
│   ├── data_prep.py
│   ├── ardl_models.py
│   └── diagnostics.py
├── results/
│   ├── tables/
│   └── figures/
├── requirements.txt
└── README.md
```

## Quick Start

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/oil-price-transmission-africa.git
cd oil-price-transmission-africa

# Environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run analysis
jupyter notebook notebooks/01_ardl_nardl_analysis.ipynb
```

## Methodology Snapshot

1. **Unit-root testing** – ADF, PP, KPSS (mixed I(0)/I(1) series required for ARDL).  
2. **Bounds testing** – Pesaran, Shin & Smith (2001) for cointegration.  
3. **ARDL / NARDL estimation** – Optimal lag selection via AIC/SIC.  
4. **Asymmetry testing** – Wald tests on positive vs negative partial sums.  
5. **Dynamic multipliers** – Cumulative response of inflation / REER to oil-price shocks.  
6. **Robustness** – Alternative proxies, sub-sample stability, CUSUM/CUSUMSQ.

## Citation

If you use this code or adapt the modelling pipeline, please cite:

> Saidu, M. T. (2021). *Impact of Oil Price Change on Economic Growth, Real Effective Exchange Rate and Inflation in South Africa, Morocco and Côte d’Ivoire*. PhD Dissertation, Universiti Putra Malaysia.

and any relevant peer-reviewed articles listed on my Google Scholar / ORCID profiles.

## License

MIT License – free for academic and non-commercial research use. Commercial applications require prior written permission.

## Contact & Collaboration

Open to research collaboration, peer review, and applied policy work on energy-macro linkages in Sub-Saharan Africa and emerging markets.  
Email: maccido@gmail.com | maccido@fuez.edu.ng
