# Empirical Modeling of Effective Porosity

This repository provides a universal power-law formula for estimating **effective porosity ($n_e$)** using **specific capacity ($q/s$)**.

## The Formula

The relationship is defined by the following equation:

$$n_e = 0.1508 \left( \frac{q}{s} \right)^{0.0826}$$

## Variable Definitions and Units

| Variable | Description | Units |
| :--- | :--- | :--- |
| $n_e$ | Effective Porosity | Dimensionless |
| $q/s$ | Specific Capacity | $m^2/day$ |
| $q$ | Well Discharge | $m^3/day$ |
| $s$ | Drawdown | $m$ |

> **Technical Note:** The constants ($0.1508$ and $0.0826$) are empirically derived. Well efficiency is inherently integrated into the specific capacity results ($q/s$) and requires no separate adjustment.

## Research Context
This work scales hydrodynamic parameters across varied lithologies (sedimentary, karstic, volcanic, and crystalline) and the seed for research was initiated while working on projects that culminated in the publication of **USGS Open-File Reports 96-328 and 94-134**, and later published in international journal papers.

---
**James Wilkinson, PhD, PG**

## How to Cite

If you use this data or the effective porosity formula in your research, please cite the following manuscript:

> Wilkinson, J. (2026). *Empirical Modeling of Effective Porosity and Groundwater Velocity using Specific Capacity.* [Hydrogeology Journal/In Prep].

**BibTeX:**
@article{wilkinson2026porosity,
  author = {Wilkinson, James},
  title = {Empirical Modeling of Effective Porosity and Groundwater Velocity using Specific Capacity},
  journal = {Hydrogeology Journal},
  year = {2026},
  note = {Data and formulas available at: [Link to your GitHub]}
}
