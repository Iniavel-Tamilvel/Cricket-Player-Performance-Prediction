import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/sample_player_match_data.csv")
features=["age","batting_average","strike_rate","balls_faced","batting_position","opposition_strength","venue_runs_avg","form_last5"]
print(df.shape); print(df.isna().sum())
sns.scatterplot(data=df,x="strike_rate",y="runs",hue="batting_position"); plt.title("Strike Rate vs Runs"); plt.tight_layout(); plt.savefig(ROOT/"visualisations/strike_rate_vs_runs.png",dpi=180); plt.close()
X,y=df[features],df["runs"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42)
models={"Linear Regression":LinearRegression(),"Random Forest":RandomForestRegressor(n_estimators=300,random_state=42)}
rows=[]
for name,m in models.items():
    m.fit(Xtr,ytr); pred=m.predict(Xte)
    rows.append([name,mean_absolute_error(yte,pred),mean_squared_error(yte,pred)**.5,r2_score(yte,pred)])
print(pd.DataFrame(rows,columns=["Model","MAE","RMSE","R2"]))
rf=models["Random Forest"]; cv=-cross_val_score(rf,X,y,cv=5,scoring="neg_mean_absolute_error"); print("5-fold CV MAE:",cv.mean())
rf.fit(X,y); pd.Series(rf.feature_importances_,index=features).sort_values().plot(kind="barh",title="Feature Importance"); plt.tight_layout(); plt.savefig(ROOT/"visualisations/feature_importance.png",dpi=180); plt.close()
