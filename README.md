# WeatherLens-India-project
End-to-end Indian weather analysis and rainfall prediction using Python, Streamlit, and Power

## Objective

WeatherLens India is an end-to-end data science project built to analyze 
24 years of daily weather data across 10 major Indian cities and predict 
whether it will rain on a given day based on atmospheric conditions.

The project goes beyond simple analysis — it combines unsupervised machine 
learning (K-Means clustering) to discover hidden weather patterns, and 
supervised machine learning (Random Forest) to build a real working rainfall 
prediction system. Results are presented through two parallel dashboards — 
a Streamlit web app for technical users and a Power BI dashboard for 
business users — making weather insights accessible to both audiences.

## Overview

WeatherLens India is an end-to-end data science project that analyzes 24+ years of Indian weather data to uncover climate patterns, understand rainfall behaviour, and predict whether it will rain on a given day.

The project combines exploratory data analysis, unsupervised clustering, supervised machine learning, and interactive dashboards — built in both Python (Streamlit) and Power BI — to tell a complete story from raw data to actionable insights.

### Key Goals
- Analyze how Indian rainfall varies across cities, months and seasons
- Discover natural weather patterns using K-Means clustering
- Predict rainfall probability from atmospheric conditions using Random Forest
- Handle class imbalance using SMOTE for a fair and reliable model
- Build an interactive Streamlit app where users can input weather conditions 
  and get a live rainfall prediction
- Build a Power BI dashboard for visual business storytelling
- Deploy the Streamlit app on Render as a live accessible web application

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Unsupervised ML | Scikit-learn (K-Means, PCA) |
| Supervised ML | Scikit-learn (Random Forest), imbalanced-learn (SMOTE) |
| Web dashboard | Streamlit |
| BI dashboard | Power BI Desktop |
| Deployment | Render |
| Version control | Git + GitHub |

## Project Structure

```
weatherlens-india/
│
├── data/
│   ├── raw/                   # Original downloaded CSV files
│   └── processed/             # clean_weather.csv after cleaning
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_ml_model.ipynb
│
├── streamlit_app/
│   └── app.py                 # Streamlit dashboard + prediction widget
│
├── powerbi/
│   └── weatherlens.pbix       # Power BI dashboard file
│
├── models/
│   └── rainfall_model.pkl     # Saved Random Forest model
│
├── requirements.txt
└── README.md
```

## Workflow

```
Raw Weather Data (2000–2024)
         ↓
Phase 1 — Data Cleaning (Python / Pandas)
  · Handle nulls, fix data types, remove outliers
  · Feature engineering: season labels, heat index, anomaly flags
         ↓
Phase 2 — EDA
  · Correlation analysis, distributions, city-wise comparisons
  · Humidity vs rainfall relationships
         ↓
Phase 3 — Unsupervised Learning
  · K-Means clustering → 3 weather pattern groups
  · PCA → dimensionality reduction of 40+ features
  · Cluster label added as new feature column
         ↓
Phase 5 → ML Model (Random Forest + SMOTE)
Phase 6 → Streamlit Dashboard (with ML widget embedded)
Phase 7 → Power BI Dashboard
Phase 8 → Deployment on Render
```

## Key Questions Answered

- How much does humidity contribute to rainfall?
- Which Indian cities and regions receive the most rainfall?
- Which months and seasons are most prone to unexpected rainfall?
- What natural weather clusters exist in Indian climate data?
- Can we reliably predict rain from atmospheric conditions?

## ML Model Details

| Parameter | Value |
|---|---|
| Problem type | Binary Classification (Rain: Yes / No) |
| Algorithm | Random Forest Classifier |
| Class imbalance fix | SMOTE (Synthetic Minority Oversampling) |
| Primary metric | ROC-AUC |
| Secondary metric | F1 Score |
| Features | Humidity, temperature, pressure, wind speed, cluster label |

> Note: Accuracy was intentionally avoided as the primary metric due to class imbalance in Indian rainfall data.

## Dataset

- Source: [Kaggle — India Daily Weather 2000–2024](https://www.kaggle.com/datasets/developerghost/climate-in-india-daily-weather-data-2000-2024)
- Records: 24 years of daily weather observations across major Indian cities
- Features: Temperature, humidity, rainfall, wind speed, pressure, and more

## Live Demo

🔗 Streamlit App: `[link will be added after deployment]`

## Power BI Dashboard Preview

> Screenshot will be added after dashboard completion.

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/weatherlens-india.git
cd weatherlens-india

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app/app.py
```

## Status

| Phase | Status |
|---|---|
| Data collection            | ✅ Done        |
| Data cleaning              | ✅ Done        |
| EDA                        | ✅ Done        |
| Clustering (K-Means + PCA) | ✅ Done        |
| ML Model (Random Forest + SMOTE) | ✅ Done |
| Streamlit Dashboard | ✅ Done |
| Power BI dashboard | ⏳ Upcoming |
| Deployment | ⏳ Upcoming |

## Phases Completed (Summary)

### Phase 1 — Data Collection
- Dataset: India Daily Weather 2000–2024 (10 major cities)
- Source: Kaggle
- Records: 91,320 rows

### Phase 2 — Data Cleaning & Feature Engineering
- Removed duplicate columns (precipitation_sum)
- Fixed date format (dayfirst=True)
- Dropped unreliable features (wind_direction, wind_gusts)
- Engineered new columns: season, temp_range, weather_condition, rain_tomorrow
- Final dataset: 91,320 rows × 15 columns

### Phase 3 — Exploratory Data Analysis
- 8 visualizations created
- Key finding: temp_range is the strongest predictor of rainfall (-0.67 correlation)
- Mumbai records highest average daily rainfall among all 10 cities
- Rainfall peaks in July during Southwest Monsoon season
- Class imbalance identified: 58% no rain vs 42% rain

### Phase 4 — K-Means Clustering + PCA
- Elbow Method used to determine optimal K=4
- 4 weather patterns discovered:
  - 🔵 Cold Winter (13,116 days)
  - 🟢 Mild Transition (28,164 days)
  - 🟠 Dry Summer (30,705 days)
  - 🟣 Heavy Monsoon (19,335 days)
- PCA used to visualize clusters in 2D
- Cluster labels added as new feature for ML model

### phase 5:ML Model(Key Challenge — Data Leakage Detection)

While building the Random Forest model, an initial test showed 
suspiciously perfect predictions with probabilities of exactly 
0.0 or 1.0 — a strong indicator of data leakage rather than 
genuine model performance.

**Root cause identified:**
The `rain_sum` column (actual rainfall amount) was accidentally 
included as an input feature. Since the target variable 
`rain_tomorrow` was directly derived from `rain_sum` 
(`rain_tomorrow = rain_sum > 0`), the model was essentially 
given the answer alongside the question.

Feature importance analysis confirmed this — `rain_sum` 
accounted for 70% of the model's decision making, far higher 
than any genuine weather feature.

**Fix applied:**
`rain_sum` was removed from the feature set, leaving only 
genuine atmospheric indicators (temperature, wind speed, 
temp range, month, weather cluster) as inputs. The model 
was retrained from scratch on this leak-free feature set.

This highlights the importance of validating feature 
importance and being skeptical of suspiciously perfect 
results during model development.

### Phase 6 — Streamlit App

A two-tab interactive web app:

**🔮 Predict Tab**
Users input city, month, max/min temperature and wind speed 
to get a live rainfall probability prediction from the trained 
Random Forest model, displayed via a gauge chart.

**📈 Prediction Insights Tab**
Shows sensitivity analysis on the user's specific prediction — 
how rainfall probability would change if temperature range or 
wind speed were different, with the user's actual input marked 
on each chart. This adds model explainability directly tied to 
each user's prediction rather than generic static analysis.

### Who is this for?
- **General users** → Want to know if it will rain today based on conditions
- **Data analysts** → Want to explore Indian weather trends interactively
- **Data scientists** → Want to understand the ML pipeline and methodology
- **Business users** → Want clean visual insights through Power BI

## Author

**Apurva**
BSc Data Science — M.L. Dahanukar College, Mumbai
[LinkedIn](#) · [GitHub](#)
