import numpy as np
from demand_patterns import generate_steady

sku_catalog = [
    {
        "sku_id": "FRRAWBEFRIBSTK-0001",
        "sku_name": "FRESH RAW BEEF RIB STEAK - HANABI GRILL",
        "category": "UNCOOKED PORTIONED BEEF",
        "pattern": "steady",
        "params": {"base_volume": 150000, "num_weeks": 52, "std_dev": 0.09},
    },
    {
        "sku_id": "FZCKDCHKBRSCUT-0001",
        "sku_name": "FROZEN COOKED CHICKEN BREAST CUTLET - CANE'S",
        "category": "COOKED PORTIONED CHICKEN",
        "pattern": "seasonal",
        "params": {
            "base_volume": 300000,
            "num_weeks": 52,
            "amplitude": 0.02,
            "period": 12,
        },
    },
]
