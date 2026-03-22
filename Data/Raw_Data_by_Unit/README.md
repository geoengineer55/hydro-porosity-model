# Data Dictionary: Raw Hydrogeologic Unit Data

This directory contains the original field measurements for 609 well records, categorized by lithology. These data form the basis for the specific capacity ($q/s$) analysis and the subsequent application of the power-law formula for effective porosity ($n_e$).

---

## Column Definitions

| Column Header | Description | Units |
| :--- | :--- | :--- |
| **ID** | Unique identifier for each well record (1–609). | Integer |
| **Yield_m3_day** | Pumping rate or discharge during the well test. | $m^3/day$ |
| **Drawdown_m** | Total drop in water level measured in the well. | Meters ($m$) |
| **Spec_Cap_m2_day** | Specific Capacity ($q/s$), calculated as Yield / Drawdown. | $m^2/day$ |
| **Lithology** | Primary geologic unit identified from driller's logs. | Code |

---

## Lithology Codes

* **SG**: Sand and Gravel (Unconsolidated)
* **TG**: Gravel (Coarse unconsolidated)
* **TS**: Sandstone (Consolidated sedimentary)
* **OR**: Volcanic rocks (Crystalline/extrusive)
* **UF**: Fine-grained sediments (Silt/Clay-rich)
* **C1 / C2**: Confining Units (Low-permeability boundaries)
* **Mixed**: Wells intersecting multiple units or with ambiguous driller notes.

---

## Reference Formula
The data in these files are intended for use with the empirical power-law relation:
$$n_e = 0.1508(q/s)^{0.0826}$$
