import QuantLib as ql
from .framework import CalibrationTarget, InstrumentStrategy

class ClassicModel:
    """
    The 'Model' that manages the dependency tree of pricing parameters.
    See Section 4.1 'Model' in the 2012 paper.
    """
    def __init__(self, calc_date):
        ql.Settings.instance().evaluationDate = calc_date
        self._handles = {} 

    def get_handle(self, curve_name):
        if curve_name not in self._handles:
            self._handles[curve_name] = ql.RelinkableYieldTermStructureHandle()
        return self._handles[curve_name]

    def calibrate(self, target: CalibrationTarget, strategy: InstrumentStrategy, exogenous_discount=None):
        print(f"--- [Classic 2012] Bootstrapping {target.curve_name} ---")
        
        # Dependency Injection (Section 4.1)
        discount_handle = ql.YieldTermStructureHandle()
        if exogenous_discount:
            discount_handle = self.get_handle(exogenous_discount)

        helpers = []
        for tenor, rate, instr_type in strategy.instruments:
            quote = ql.QuoteHandle(ql.SimpleQuote(rate))
            
            if instr_type == 'Deposit':
                helpers.append(ql.DepositRateHelper(
                    quote, ql.Period(tenor), strategy.conventions['settlement'],
                    strategy.conventions['calendar'], ql.ModifiedFollowing,
                    False, strategy.conventions['day_count']
                ))
            elif instr_type == 'Swap':
                # Implements the 'Source Valuation' (Par) vs 'Target Valuation' logic
                # Note: Swaps here depend on the injected discount_handle
                helpers.append(ql.SwapRateHelper(
                    quote, ql.Period(tenor), strategy.conventions['calendar'],
                    ql.Annual, ql.Unadjusted, strategy.conventions['fixed_day_count'],
                    target.underlying_index, ql.QuoteHandle(), ql.Period(0, ql.Days),
                    discount_handle
                ))
            elif instr_type == 'OIS':
                helpers.append(ql.OISRateHelper(
                    strategy.conventions['settlement'], ql.Period(tenor),
                    quote, strategy.conventions['index']
                ))

        # The 'Optimizer' (Section 4.4): 1-d root search (Bootstrap) via QuantLib
        if target.interpolation == 'LogLinear':
            curve = ql.PiecewiseLogLinearDiscount(
                strategy.conventions['settlement'], strategy.conventions['calendar'],
                helpers, strategy.conventions['day_count']
            )
        elif target.interpolation == 'Linear':
             curve = ql.PiecewiseLinearZero(
                strategy.conventions['settlement'], strategy.conventions['calendar'],
                helpers, strategy.conventions['day_count']
            )
        
        curve.enableExtrapolation()
        
        # Update Model State
        handle = self.get_handle(target.curve_name)
        handle.linkTo(curve)
        return handle
