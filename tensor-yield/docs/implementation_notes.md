# Modern Implementation Patterns (2012 vs. 2025)

This repository does not just update the financial math; it updates the **software engineering** approach.

## 1. Data Classes (PEP 557)
* **The Old Way (2012):** To create a simple data container, you had to write a full class with `__init__` or use `namedtuple`.
* **The Tensor-Yield Way:** We use the `@dataclass` decorator. It automatically generates the boilerplate code, making the distinction between **Data** (Configuration) and **Logic** (Model) strictly enforced.

## 2. Type Hinting & Static Analysis (PEP 484)
* **The Old Way:** Python was historically treated as purely dynamic.
* **The Tensor-Yield Way:** We use explicit type hints throughout the framework.
```python
def calibrate(self, strategy: InstrumentStrategy) -> ql.RelinkableYieldTermStructureHandle:
```

## 3. Differentiable Programming (Auto-Grad)
* **The Old Way:** Calculating risk (Greeks) required **Finite Differences** ("Bumping"). To find the Delta of a curve to 50 inputs, you ran the calibration 51 times.
* **The Tensor-Yield Way:** By using **PyTorch**, the calibration logic becomes part of a **Computational Graph**.
```python
# src/neural.py
loss.backward() # Calculates gradients for ALL inputs in one pass
```
* **Why it matters:** This implements **Adjoint Algorithmic Differentiation (AAD)** automatically.

## 4. f-Strings (PEP 498)
* **The Old Way:** String formatting was often verbose (`"%s" % var`).
* **The Tensor-Yield Way:** We use f-strings for clean, inline logging.

## 5. Dependency Injection via Handles
* **The Concept:** The 2012 paper describes using a "Model" to manage dependencies.
* **The Implementation:** We utilize QuantLib's `RelinkableHandle`.
* **Why it matters:** This allows us to "promise" a curve (like OIS) to a dependent curve (like LIBOR) before the OIS curve is actually built.

## 6. Diagrams-as-Code (Mermaid)
* **The Old Way:** Static binary images.
* **The Tensor-Yield Way:** Text-based definitions in Markdown to render architecture diagrams dynamically.
