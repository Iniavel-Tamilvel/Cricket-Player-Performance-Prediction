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
- Prediction error analysis
- Time-aware validation

The project was developed as part of my Data Science / Business Analytics portfolio, with a focus on applying machine learning to a real-world sports analytics problem.

---

## Dataset

The analysis uses IPL ball-by-ball match data sourced from Cricsheet.

### Dataset Scale

- IPL matches: **1,243**
- Delivery records: **295,732**
- Player-match records used for modelling: **18,842**
- Training records: **15,073**
- Testing records: **3,769**
- Unique players: **738**
- Seasons: **19**

The raw ball-by-ball dataset is not included in this repository because of its large file size.

The repository contains the processed modelling dataset used by the machine learning workflow.

---

## Business / Analytical Question

### Can a player's historical performance and match context be used to predict their runs in an upcoming IPL innings?

The prediction features include information available before the target innings, such as:

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

**IPL Ball-by-Ball Data**

↓

**Data Cleaning**

↓

**Player-Match Aggregation**

↓

**Historical Feature Engineering**

↓

**Recent Form Features**

↓

**Opponent Performance Features**

↓

**Exploratory Data Analysis**

↓

**Baseline Model**

↓

**Regression Models**

↓

**Classification Model**

↓

**Time-Aware Evaluation**

↓

**Predictions & Error Analysis**

---

## Results

### Regression Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Recent 5-Match Baseline | 17.482 | 23.648 | -0.002 |
| Linear Regression | 16.837 | 23.905 | -0.024 |
| Random Forest | **16.399** | **22.300** | **0.109** |

The Random Forest regression model produced the lowest MAE among the evaluated regression approaches.

On the chronological test set, the Random Forest achieved:

- **MAE:** 16.399 runs
- **RMSE:** 22.300 runs
- **R²:** 0.109

The results indicate that the model captures some predictive signal from historical player performance and match context, while substantial prediction error remains.

---

## Classification Analysis

The classification experiment divided player innings into three performance categories:

- **Low:** 0–19 runs
- **Moderate:** 20–39 runs
- **High:** 40+ runs

### Class Distribution

- Low: **62.02%**
- Moderate: **21.11%**
- High: **16.87%**

### Initial Random Forest Classifier

- Accuracy: **58.3%**
- Weighted F1: **0.430**

### Balanced Random Forest

- Accuracy: **58.4%**
- Macro F1: **0.264**

The confusion matrix showed weak recognition of the Moderate and High classes. The balanced classifier also continued to predict the Low class substantially more frequently.

This indicates that the current classification formulation is strongly affected by class imbalance and should therefore be treated as an exploratory modelling analysis rather than a high-performing predictive classifier.

---

## Regression Error Analysis

The project also analyses prediction errors from the Random Forest regression model, including:

- Actual versus predicted runs
- Absolute prediction error
- Largest prediction errors
- Closest predictions
- Prediction error distribution

This provides additional insight into where the model performs well and where prediction uncertainty remains.

---

## Machine Learning Models

### Regression

The regression task predicts the number of runs scored by a player in an upcoming innings.

Models evaluated:

- Recent 5-Match Average Baseline
- Linear Regression
- Random Forest Regression

Evaluation metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R²

### Classification

The classification task categorises player innings into:

- Low
- Moderate
- High

The classification analysis evaluates:

- Accuracy
- Precision
- Recall
- F1-score
- Macro F1
- Confusion matrix

---

## Time-Aware Validation

Because cricket matches occur chronologically, the modelling process uses chronological training and testing rather than randomly mixing past and future observations.

This helps reduce the risk of future information influencing model evaluation.

---

## Repository Structure

```text
Cricket-Player-Performance-Prediction/
│
├── data/
│   └── player_match_model.csv
│
├── notebooks/
│   └── cricket_player_performance.ipynb
│
├── outputs/
│   ├── model_predictions.csv
│   ├── classification_predictions.csv
│   ├── regression_model_metrics.csv
│   ├── classification_model_metrics.csv
│   └── balanced_classification_predictions.csv
│
├── src/
│   └── build_features.py
│
├── README.md
└── requirements.txt
