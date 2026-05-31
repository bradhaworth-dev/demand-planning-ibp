import numpy as np

def generate_steady(base_volume: int, num_weeks: int, std_dev: float, **kwargs) -> np.ndarray:
    """
    Takes a base volume and adds small +/- wobble while staying mostly flat.
    """
    steady_volume = (base_volume + (np.random.normal(0, std_dev, size = num_weeks))).round().astype(int)
    return steady_volume

def generate_trend(base_volume: int, num_weeks: int, std_dev: float, trend: float, **kwargs) -> np.ndarray:
    """
    A weekly demand series that grows or declines over weeks - a SKU trending up
    (gaining popularity) or down (dying off), instead of staying flat.
    """
    trend_volume = (base_volume + (np.arange(num_weeks) * trend) + (np.random.normal(0, std_dev, size = num_weeks))).round().astype(int)
    return trend_volume

def generate_seasonal(base_volume: int, num_weeks: int, amplitude: float, period: int = 52, **kwargs,) -> np.ndarray:
    """
    Generates seasonal demand with peaks and valleys 
    """
    seasonal_output = base_volume + amplitude * np.sin(2 * np.pi * np.arange(num_weeks)/period)
    return seasonal_output.round().astype(int)

PATTERN_GENERATORS = {
    "steady":   generate_steady,
    "trend":    generate_trend,
    "seasonal": generate_seasonal,
}

## Test ##
if __name__ == "__main__":
    param = {"base_volume": 500, "num_weeks": 104, "std_dev":5, "trend":-4.0, "amplitude": 150}
    test = PATTERN_GENERATORS["seasonal"](**param)
    print(test)