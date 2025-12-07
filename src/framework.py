from dataclasses import dataclass
from typing import List, Any

@dataclass
class CalibrationTarget:
    """
    Defines the identity and structure of the curve to be built.
    Implements 'Definition 2: The Calibration Target' from Gibbs & Goyder (2012).
    """
    curve_name: str
    interpolation: str  # e.g. 'LogLinear', 'Linear'
    entity_type: str    # 'Discount', 'Forward'
    underlying_index: Any = None

@dataclass
class InstrumentStrategy:
    """
    Specifies which instruments to value during calibration.
    Implements 'Definition 3: InstrumentStrategy' from Gibbs & Goyder (2012).
    """
    strategy_name: str
    instruments: List[tuple]  # List of (Tenor, Rate, Type)
    conventions: dict
