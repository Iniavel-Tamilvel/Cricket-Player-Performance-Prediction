# IPL Player Performance Prediction — Data Science Portfolio Project

## Project Overview

This project develops a machine learning pipeline for predicting an IPL cricket player's runs in an upcoming innings using historical player performance and match context.

The project demonstrates an end-to-end data science workflow including:

- Data preparation
- Exploratory Data Analysis (EDA)
- Feature engineering
- Historical and recent-form analysis
- Baseline modelling
- Regression modelling
- Classification modelling
- Model evaluation
- Prediction analysis
- Time-aware validation

The project was developed as part of my Data Science / Business Analytics portfolio, with a focus on applying machine learning to a real-world sports analytics problem.

---

## Dataset

The analysis uses IPL ball-by-ball match data sourced from Cricsheet.

### Dataset scale

- IPL matches: **1,243**
- Delivery records: **295,732**
- Player-match records: **23,856**
- Modelling records: **21,711**
- Unique players: **785**
- Seasons: **19**

The raw ball-by-ball dataset is not included in this repository because of its large file size.

The repository instead contains the processed modelling dataset used by the machine learning workflow.

---

## Business / Analytical Question

### Can a player's historical performance and match context be used to predict their runs in an upcoming IPL innings?

The model uses information that would be available before the target innings, including:

- Previous match performance
- Previous strike rate
- Career batting average
- Career strike rate
- Recent five-match average
- Recent ten-match average
- Previous boundaries
- Recent boundaries
- Opponent performance history
- Batting team
- Opponent
- Innings
- Season

Current-match performance variables are excluded from the prediction features to reduce data leakage.

---

## Project Workflow

```text
IPL Ball-by-Ball Data
        ↓
Data Cleaning
        ↓
Player-Match Aggregation
        ↓
Historical Feature Engineering
        ↓
Recent Form Features
        ↓
Opponent Performance Features
        ↓
Exploratory Data Analysis
        ↓
Baseline Model
        ↓
Regression Models
        ↓
Classification Model
        ↓
Time-Aware Evaluation
        ↓
Predictions & Analysis

## Results

### Regression Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Recent 5-Match Baseline | 17.482 | 23.648 | -0.002 |
| Linear Regression | 16.837 | 23.905 | -0.024 |
| Random Forest | 16.399 | 22.300 | 0.109 |

The Random Forest regression model produced the lowest MAE among the evaluated regression approaches. On the chronological test set, it achieved an MAE of 16.399 runs, RMSE of 22.300 runs and R² of 0.109.

### Classification Analysis

The classification experiment divided player innings into Low, Moderate and High performance classes.

The dataset was imbalanced:

- Low: 62.02%
- Moderate: 21.11%
- High: 16.87%

The initial Random Forest classifier achieved 58.3% accuracy and a weighted F1-score of 0.430. A class-balanced Random Forest achieved 58.4% accuracy and a macro F1-score of 0.264.

The confusion matrix showed weak recognition of the Moderate and High classes. This indicates that the current classification formulation is strongly affected by class imbalance and should be treated as an exploratory analysis rather than a high-performing predictive model.
