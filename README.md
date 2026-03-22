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
This work scales hydrodynamic parameters across varied lithologies (karstic, volcanic, and crystalline) and builds upon methodologies documented in **USGS Open-File Reports 96-328 and 94-134**.

---
**James Wilkinson, PhD, PG**
