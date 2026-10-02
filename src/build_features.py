import pandas as pd
import numpy as np

pm = pd.read_csv("../data/player_match_stats.csv", parse_dates=["date"])
pm = pm.sort_values(["date","match_id","player"]).reset_index(drop=True)
g = pm.groupby("player", group_keys=False)
pm["previous_matches"] = g.cumcount()
pm["previous_innings"] = g["runs"].cumcount()
pm["previous_runs_total"] = g["runs"].cumsum() - pm["runs"]
pm["previous_balls_total"] = g["balls"].cumsum() - pm["balls"]
pm["career_avg_runs"] = np.where(pm["previous_innings"]>0, pm["previous_runs_total"]/pm["previous_innings"], 0)
pm["career_strike_rate"] = np.where(pm["previous_balls_total"]>0, pm["previous_runs_total"]/pm["previous_balls_total"]*100, 0)
pm["previous_match_runs"] = g["runs"].shift(1).fillna(0)
pm["previous_match_sr"] = g["strike_rate"].shift(1).fillna(0)
pm["recent5_avg_runs"] = g["runs"].transform(lambda s:s.shift(1).rolling(5,min_periods=1).mean()).fillna(0)
pm["recent5_avg_sr"] = g["strike_rate"].transform(lambda s:s.shift(1).rolling(5,min_periods=1).mean()).fillna(0)
pm["recent10_avg_runs"] = g["runs"].transform(lambda s:s.shift(1).rolling(10,min_periods=1).mean()).fillna(0)
pm["recent10_avg_sr"] = g["strike_rate"].transform(lambda s:s.shift(1).rolling(10,min_periods=1).mean()).fillna(0)
pm["opp_avg_runs"] = pm.groupby(["player","opponent"])["runs"].transform(lambda s:s.shift(1).expanding().mean()).fillna(0)
pm["venue_avg_runs"] = pm.groupby(["player","venue"])["runs"].transform(lambda s:s.shift(1).expanding().mean()).fillna(0)
pm[pm["previous_innings"]>=3].to_csv("../data/player_match_model.csv", index=False)
print("Saved player_match_model.csv")
