# Tensor-Yield

**A comparative framework for Interest Rate Curve Calibration: From the Dual-Curve era (2012) to the RFR era (2025) and into Deep Learning.**

## Overview
This repository serves as a practical refresher for quantitative developers and risk managers. It implements the **Generic Calibration Framework** described in the public domain paper *The Past, Present and Future of Curves* (2012) and extends it to modern Deep Learning workflows.

## Structure
* **src/classic.py**: Implements the 2012 Dual-Curve bootstrap (OIS + LIBOR) using the "Calibration Target" and "Instrument Strategy" abstractions.
* **src/modern.py**: Adapts the architecture for 2025 Risk-Free Rates (SOFR/SONIA), focusing on OIS-centric construction.
* **src/neural.py**: A PyTorch-based differentiable curve engine using Adjoint Algorithmic Differentiation (AAD) for instant Greeks.

## Getting Started
1. Run `bash setup.sh` to install dependencies (QuantLib, PyTorch, etc).
2. Launch `jupyter notebook`.
3. Open `notebooks/1_Classic_Bootstrap.ipynb` to begin.

## Documentation
* **[Theory Landscape](docs/theory_landscape.md):** From LIBOR to SOFR.
* **[Implementation Notes](docs/implementation_notes.md):** Modern Python features (Dataclasses, AAD).
* **[Framework Choice](docs/tf_vs_pytorch.md):** TensorFlow vs PyTorch for AAD in Finance.
* **[Quantum Outlook](docs/quantum_outlook.md):** A brief on VQE, QAOA, and the future of pricing.

## Reference
* Gibbs, M., & Goyder, R. (2012). *The Past, Present and Future of Curves*. FINCAD.
