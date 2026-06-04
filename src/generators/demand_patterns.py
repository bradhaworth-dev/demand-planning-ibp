import numpy as np


def generate_steady(
    base_volume: int, num_weeks: int, std_dev: float, **kwargs
) -> np.ndarray:
    """
    Takes a base volume and adds small +/- wobble while staying mostly flat.
    """
    steady_volume = (
        (base_volume + (np.random.normal(0, std_dev, size=num_weeks)))
        .round()
        .astype(int)
    )
    return steady_volume


def generate_trend(
    base_volume: int, num_weeks: int, std_dev: float, trend: float, **kwargs
) -> np.ndarray:
    """
    A weekly demand series that grows or declines over weeks - a SKU trending up
    (gaining popularity) or down (dying off), instead of staying flat.
    """
    trend_volume = (
        (
            base_volume
            + (np.arange(num_weeks) * trend)
            + (np.random.normal(0, std_dev, size=num_weeks))
        )
        .round()
        .astype(int)
    )
    return trend_volume


def generate_seasonal(
    base_volume: int,
    num_weeks: int,
    amplitude: float,
    period: int = 52,
    **kwargs,
) -> np.ndarray:
    """
    Generates seasonal demand with peaks and valleys
    """
    seasonal_output = base_volume + amplitude * np.sin(
        2 * np.pi * np.arange(num_weeks) / period
    )
    return seasonal_output.round().astype(int)


def generate_discontinued(
    base_volume: int, num_weeks: int, std_dev: float, discontinue_week: int, **kwargs
) -> np.ndarray:
    """
    Takes a base volume with wobble and discontinues it at a given week.
    """
    discontinued_vol = (
        (base_volume + (np.random.normal(0, std_dev, size=num_weeks)))
        .round()
        .astype(int)
    )
    discontinued_vol[discontinue_week:] = 0
    return discontinued_vol


def generate_npi(
    base_volume: int,
    num_weeks: int,
    std_dev: float,
    launch_week: int,
    ramp_weeks: int,
    **kwargs,
) -> np.ndarray:
    """
    Generates new product introduction with 0 weeks starting then increases over a certain amount of weeks to full base volume.
    """
    npi_volume = (
        (base_volume + (np.random.normal(0, std_dev, size=num_weeks)))
        .round()
        .astype(int)
    )
    npi_volume[:launch_week] = 0
    ramp = np.linspace(0, 1, num=ramp_weeks)
    npi_volume[launch_week : launch_week + ramp_weeks] = (
        (npi_volume[launch_week : launch_week + ramp_weeks] * ramp).round().astype(int)
    )
    return npi_volume


def generate_lto(
    base_volume: int,
    num_weeks: int,
    std_dev: float,
    lto_start: int,
    lto_end: int,
    **kwargs,
) -> np.ndarray:
    """
    Generates LTO with variable demand with a start and end date.
    TODO: Add spike decay, hot at the start and decay's towards end.
    """
    lto_volume = (
        (base_volume + (np.random.normal(0, std_dev, size=num_weeks)))
        .round()
        .astype(int)
    )
    lto_volume[:lto_start] = 0
    lto_volume[lto_end:] = 0
    return lto_volume


PATTERN_GENERATORS = {
    "steady": generate_steady,
    "trend": generate_trend,
    "seasonal": generate_seasonal,
    "discontinued": generate_discontinued,
    "npi": generate_npi,
    "lto": generate_lto,
}

## Test ##
if __name__ == "__main__":
    param = {
        "base_volume": 500,
        "num_weeks": 104,
        "std_dev": 5,
        "trend": -4.0,
        "amplitude": 150,
        "discontinue_week": 60,
        "launch_week": 30,
        "ramp_weeks": 8,
        "lto_start": 30,
        "lto_end": 50,
    }
    test = PATTERN_GENERATORS["lto"](**param)
    print(test)
