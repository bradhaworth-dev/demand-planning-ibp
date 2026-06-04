import numpy as np
import pandas as pd
from demand_patterns import PATTERN_GENERATORS

sku_catalog = [
    {
        "sku_id": "FRRAWBEFRIBSTK-0001",
        "sku_name": "FRESH RAW BEEF RIB STEAK - HANABI GRILL",
        "category": "UNCOOKED PORTIONED BEEF",
        "pattern": "steady",
        "params": {"base_volume": 150000, "num_weeks": 52, "std_dev": 1000},
    },
    {
        "sku_id": "FZCKDCHKBRSCUT-0001",
        "sku_name": "FROZEN COOKED CHICKEN BREAST CUTLET - CANE'S",
        "category": "COOKED PORTIONED CHICKEN",
        "pattern": "seasonal",
        "params": {
            "base_volume": 300000,
            "num_weeks": 52,
            "amplitude": 60000,
            "period": 52,
        },
    },
]

rows = []
for sku in sku_catalog:
    # this block runs once per sku
    # on each pass, 'sku' IS the current dict
    generator = PATTERN_GENERATORS[sku["pattern"]]
    demand = generator(**sku["params"])
    for week, qty in enumerate(demand, start=1):
        row = {
            "sku_id": sku["sku_id"],
            "sku_name": sku["sku_name"],
            "category": sku["category"],
            "week": week,
            "quantity": qty,
        }
        rows.append(row)

df = pd.DataFrame(rows)