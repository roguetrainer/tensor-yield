import QuantLib as ql
from .classic import ClassicModel

class ModernRFRModel(ClassicModel):
    def calibrate_sofr(self, strategy, curve_name="USD_SOFR"):
        """
        Specialized calibration for RFRs (SOFR/SONIA).
        In 2025, these curves are usually Single-Curve (Discount == Forward).
        """
        print(f"--- [Modern 2025] Bootstrapping RFR (SOFR) Curve ---")
        
        sofr_index = ql.Sofr()
        helpers = []
        
        for tenor, rate, instr_type in strategy.instruments:
            quote = ql.QuoteHandle(ql.SimpleQuote(rate))
            # RFR construction relies almost exclusively on OIS Helpers
            if instr_type == 'OIS':
                helpers.append(ql.OISRateHelper(
                    2, ql.Period(tenor), quote, sofr_index
                ))
        
        # Modern convention: often uses FlatForward or LogLinearDiscount
        curve = ql.PiecewiseLogLinearDiscount(
            0, ql.UnitedStates(ql.UnitedStates.Settlement),
            helpers, ql.Actual360()
        )
        curve.enableExtrapolation()
        
        handle = self.get_handle(curve_name)
        handle.linkTo(curve)
        return handle
