# TensorFlow vs. PyTorch for AAD in Quantitative Finance

**Why does this repository use PyTorch?**

In the context of Quantitative Finance—specifically for Curve Calibration and Risk Management—the choice between TensorFlow and PyTorch often comes down to **usability** versus **deployment scale**. This document explains why `tensor-yield` defaults to PyTorch.

## 1. The Core Difference: Dynamic vs. Static Graphs

### PyTorch (Dynamic / Eager)
* **Philosophy:** "Define by Run". The computational graph is built on-the-fly as your Python code executes.
* **Quant Benefit:** Financial pricing logic often involves complex control flow (e.g., "if option is exercisable, do X, else Y"). In PyTorch, you write standard Python `if/else` loops, and the graph handles it automatically.
* **Debugging:** You can use standard Python debuggers (pdb) to step through your calibration loop line-by-line.

### TensorFlow (Static / Graph)
* **Philosophy:** "Define then Run". While TF 2.0 introduced Eager Execution, its performance benefits rely on compiling code into a static graph via `@tf.function`.
* **Quant Friction:** Converting complex Monte Carlo simulations or branching logic into efficient TF graphs often requires using `tf.cond` or `tf.while_loop`, which can feel un-Pythonic and harder to debug for researchers.

## 2. Adjoint Algorithmic Differentiation (AAD) API

### PyTorch `autograd`
Sensitivities (Greeks) are computed via the `.backward()` method. It feels magical but is tightly integrated into the tensor object itself.
```python
# PyTorch
x = torch.tensor(1.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad) # 2.0
```

### TensorFlow `GradientTape`
TF requires an explicit context manager to "watch" variables. This offers fine-grained control but adds verbosity to simple calibration scripts.
```python
# TensorFlow
x = tf.Variable(1.0)
with tf.GradientTape() as tape:
    y = x ** 2
grad = tape.gradient(y, x)
print(grad) # 2.0
```

## 3. Industry Adoption Trends (2025)

| Feature | PyTorch | TensorFlow |
| :--- | :--- | :--- |
| **Academic Research** | **Dominant.** Most papers on Deep Hedging, Volatility Calibration, and SDEs release code in PyTorch. | Decreasing presence in new financial publications. |
| **Production Serving** | Growing (TorchServe), but historically weaker. | **Strong.** TF Serving and TFLite are industry standards for deploying to mobile/edge. |
| **XVA / Risk Engines** | Preferred for rapid prototyping and "Quant-friendly" syntax. | Preferred for massive, static pipelines where latency is critical. |

## 4. Conclusion for `tensor-yield`
We chose **PyTorch** for this refresher because:
1.  It is easier for a "Rusty Quant" (someone coming from C++/Python 2.7) to read.
2.  It handles the iterative loops of curve bootstrapping intuitively.
3.  It aligns with the current state-of-the-art in Financial Machine Learning research.
