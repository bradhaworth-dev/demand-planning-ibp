# Synthetic IBP System for Protein Manufacturer.
- Includes 
    - Demand planning
    - Forecasting
    - Production Scheduling
    - Accounting for shelf life risk

# Business problem
This company doesn't have a mature S&OP or IBP process. Much of it is in
separate systems and there's little connection between the siloed groups.
Shelf life, opportunistic protein purchases, line capacities, etc are 
not centralized for management to make decisions.

# Goal
Present the data in a unified way that tells management - here's our
current situation.

# Synthetic data disclaimer
All data is generated with a script. This data does not mirror another
company's customers, volumes, capacities, or capabilities.

# Module roadmap
Module 1 in progress
Module 2 - 6 planned

# Tech stack
numpy==2.4.6
pandas==3.0.3
python-dateutil==2.9.0.post0
six==1.17.0
SQLAlchemy==2.0.50
typing_extensions==4.15.0
Excel

# Repo structure
.
├── README.md
├── requirements.txt
└── src
    └── generators
        └── demand_patterns.py

# How to run
Clone, make a venv, pip install -r requirements.txt, run the generator.