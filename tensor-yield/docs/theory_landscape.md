# Theory Landscape

## 1. The 2012 "Dual Curve" Era
* **Source:** *The Past, Present and Future of Curves* (2012).
* **Concept:** The paper introduces the "Curve Concept"—treating curves as managed model parameters rather than static functions.
* **Challenge:** Pricing OIS-discounted LIBOR swaps required a multi-stage bootstrap.
* **Architecture:** We strictly follow the definitions of **Calibration Target** and **Instrument Strategy** to decouple definition from construction.

## 2. The 2025 "RFR" Era
* **Shift:** Transition from LIBOR to Risk-Free Rates (SOFR/SONIA).
* **Impact:** The "spread" logic has simplified for standard swaps (Single Curve), but complexity has shifted to Term Rates.

## 3. The Neural / AAD Era
* **Technique:** Replacing numerical root-finding (Section 3.1) with **Adjoint Algorithmic Differentiation**.
* **Benefit:** Calculates risk sensitivities (Greeks) instantly.
