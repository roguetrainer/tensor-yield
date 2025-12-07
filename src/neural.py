import torch
import torch.nn as nn

class DifferentiableCurve(nn.Module):
    def __init__(self, times, initial_rates):
        super().__init__()
        self.times = torch.tensor(times, dtype=torch.float64)
        # Learnable parameters (The Zero Rates)
        self.rates = nn.Parameter(torch.tensor(initial_rates, dtype=torch.float64))

    def discount(self, t):
        # Simplified differentiable interpolation
        # In production: implement a torch.autograd.Function for exact linear interp on pillars
        return torch.exp(-self.rates.mean() * t)

def calibrate_neural(market_data):
    """
    Calibrates curve using Auto-Grad (AAD) rather than bumping.
    market_data: List of tuples (Maturity, Rate)
    """
    print("--- [Neural] Starting Gradient Descent Calibration ---")
    pillars = [m[0] for m in market_data]
    curve = DifferentiableCurve(pillars, [0.03]*len(pillars))
    
    # LBFGS is standard for 'clean' physics/math problems
    optimizer = torch.optim.LBFGS(curve.parameters(), lr=1)
    
    def closure():
        optimizer.zero_grad()
        loss = 0.0
        for T, rate in market_data:
            # Differentiable Par Swap Pricing Logic
            # Fixed Leg = rate * sum(dt * D(t)) ~ rate * T * D(T) [Simplified for demo]
            # Float Leg = 1 - D(T)
            df_end = curve.discount(T)
            # Minimize (Fixed - Float)^2
            loss += ((1.0 - df_end) - (rate * 1.0 * df_end))**2
        loss.backward()
        return loss
        
    optimizer.step(closure)
    return curve, curve.rates.grad
