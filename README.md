# WeatherLens-India-project
End-to-end Indian weather analysis and rainfall prediction using Python, Streamlit, and Power

## Overview

WeatherLens India is an end-to-end data science project that analyzes 24+ years of Indian weather data to uncover climate patterns, understand rainfall behaviour, and predict whether it will rain on a given day.

The project combines exploratory data analysis, unsupervised clustering, supervised machine learning, and interactive dashboards — built in both Python (Streamlit) and Power BI — to tell a complete story from raw data to actionable insight.

## Project Highlights

- Cleaned and analyzed 24 years of multi-city Indian weather data (2000–2024)
- Discovered natural weather patterns using K-Means clustering (monsoon, dry-heat, mild)
- Handled class imbalance using SMOTE — same technique used in real fraud detection systems
- Trained a Random Forest classifier to predict rainfall with ROC-AUC as the primary metric
- Built an interactive Streamlit web app with a live ML prediction widget
- Built a dark-theme Power BI dashboard for business-friendly visual storytelling

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
Phase 4 — Dashboards (parallel)
  Streamlit (technical audience)    Power BI (business audience)
         ↓
Phase 5 — ML Prediction (Random Forest)
  · SMOTE for class imbalance
  · Evaluated using ROC-AUC + F1 Score
  · Embedded as prediction widget in Streamlit
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
| Data collection | ✅ Done |
| Data cleaning   | ✅ Done |
| EDA             | ✅ Done |
| Clustering      | 🔄 In Progress |
| Clustering | ⏳ Upcoming |
| ML model | ⏳ Upcoming |
| Streamlit dashboard | ⏳ Upcoming |
| Power BI dashboard | ⏳ Upcoming |
| Deployment | ⏳ Upcoming |

## Project Summary

WeatherLens India is an end-to-end data science project that analyzes 
24 years of Indian weather data to predict whether it will rain on a 
given day and understand the key atmospheric factors that contribute 
to rainfall across major Indian cities.

### Phase 1 — Data Collection
Data was sourced from Kaggle containing daily weather records of 10 
major Indian cities from 2000 to 2024, covering features like 
temperature, rainfall, wind speed and weather conditions. A second 
dataset containing live IMD weather data was considered but dropped 
due to an empty file issue on Kaggle's end. The primary dataset of 
91,320 rows was finalized for all downstream phases.

### Phase 2 — Data Cleaning and Feature Engineering
The raw dataset was cleaned and transformed to make it analysis-ready. 
Key steps included removing duplicate columns, fixing incorrect date 
formats, dropping unreliable features like wind direction which showed 
near-zero correlation with rainfall, and converting numeric weather 
codes into human-readable condition labels. New meaningful columns were 
engineered including season, temperature range, and a binary rainfall 
target variable — bringing the final dataset to 91,320 rows and 15 
clean columns.

### Phase 3 — Exploratory Data Analysis
Eight visualizations were created to understand the structure of Indian 
weather data. Key findings included that rainfall in India is strongly 
seasonal peaking in July during the Southwest Monsoon, Mumbai receives 
the highest average daily rainfall among all 10 cities, and temperature 
range — an engineered feature — turned out to be the single strongest 
predictor of rainfall with a -0.67 correlation. Outliers were handled 
using the IQR method and class imbalance between rainy and non-rainy 
days was identified and documented for ML model treatment.


## Author

**Apurva**
BSc Data Science — M.L. Dahanukar College, Mumbai
[LinkedIn](#) · [GitHub](#)
