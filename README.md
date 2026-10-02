# IPL Player Performance Prediction — NatWest Data Science Portfolio Project

## Dataset processed
- IPL match JSON files: **1,243**
- Delivery records: **295,732**
- Player-match records: **23,856**
- Modelling rows (minimum 3 previous innings): **21,711**
- Unique players in player-match data: **785**

## Project
Predict a player's runs in the current IPL innings using historical player performance and match context. The modelling dataset uses chronological, leakage-aware features.

## Files
- `data/match_summary.csv` — 1 row per match
- `data/player_match_stats.csv` — player-level match statistics
- `data/player_match_model.csv` — modelling-ready data
- `data/ipl_deliveries.csv.gz` — delivery-level dataset
- `notebooks/01_IPL_Player_Performance_Prediction.ipynb` — complete Jupyter notebook
- `src/build_features.py` — feature-generation script
- `requirements.txt` — dependencies

## Run
Open the `notebooks` folder in Jupyter and run the notebook from top to bottom. If needed:
`pip install -r requirements.txt`

## Source
Cricsheet — https://cricsheet.org/
Retain appropriate source attribution when using or redistributing the dataset or derived work.
