# 🌦️ WeatherLens India
### End-to-End Indian Weather Analysis & Rainfall Prediction System
An end-to-end predictive intelligence and climate analytics platform, analyzing 24 years of Indian weather data to uncover climate patterns and predict rainfall.
 
🚀 **[Live Interactive App](https://weatherlens-india.onrender.com)**
> Hosted on Render's free tier — first load after inactivity may take 30–60 seconds while the server wakes up.
 
---
 
## Objective
 
WeatherLens India is an end-to-end data science project built to analyze 24 years of daily weather data across 10 major Indian cities and predict whether it will rain on a given day based on atmospheric conditions.
 
The project goes beyond simple analysis — it combines unsupervised machine learning (K-Means clustering) to discover hidden weather patterns, and supervised machine learning (Random Forest) to build a real working rainfall prediction system. Results are presented through two parallel dashboards — a Streamlit web app for technical users and a Power BI dashboard for business users — making weather insights accessible to both audiences.
 
### Key Goals
- Analyze how Indian rainfall varies across cities, months and seasons
- Discover natural weather patterns using K-Means clustering
- Predict rainfall probability from atmospheric conditions using Random Forest
- Handle class imbalance using SMOTE for a fair and reliable model
- Build an interactive Streamlit app where users can input weather conditions and get a live rainfall prediction, along with explainability behind that prediction
- Build a Power BI dashboard for visual business storytelling
- Deploy the Streamlit app on Render as a live, publicly accessible web application
### Who is this for?
- **General users** → Want to know if it will rain today based on conditions
- **Data analysts** → Want to explore Indian weather trends interactively
- **Data scientists** → Want to understand the full ML pipeline and methodology, including a real data leakage debugging case
- **Business users** → Want clean visual insights through Power BI
---
 
## Project Description
 
Indian weather is famously unpredictable — a single country spans coastal monsoon belts, semi-arid deserts, and cold northern winters, often within the same week. WeatherLens India was built to make sense of that complexity using real data science, not just guesswork.
 
Rather than treating this as a single-model exercise, the project follows a genuine end-to-end pipeline: raw data was cleaned and feature-engineered by hand (including custom Indian season categories that account for the unpredictable October–November transition period), explored through 8 visualizations to uncover real climate patterns, and fed into both an unsupervised K-Means model to discover natural weather clusters and a supervised Random Forest model to predict rainfall.
 
Along the way, the project hit and solved real-world data science problems — a data leakage bug that produced suspiciously perfect predictions, a 143MB model file too large for GitHub, and a Streamlit bug where city selection had no actual effect on predictions. Each of these is documented below, because debugging and catching your own mistakes is as much a part of data science as building the model in the first place.
 
The final product is two parallel dashboards, each speaking to a different audience — a Streamlit app with a live rainfall predictor and personalized model explainability, and a Power BI report for business-style visual storytelling — both built from the same clean, leak-free dataset.
 
---
 
## Tech Stack
 
| Layer | Tools |
|---|---|
| Language | Python 3.10+ |
| Data manipulation | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Unsupervised ML | Scikit-learn (K-Means, PCA) |
| Supervised ML | Scikit-learn (Random Forest), imbalanced-learn (SMOTE) |
| Web dashboard | Streamlit |
| BI dashboard | Power BI Desktop |
| Deployment | Render |
| Version control | Git + GitHub |
 
---
 
## Project Structure
 
```
WeatherLens-India-project/
│
├── WeatherLens India Project_datacleaning.ipynb   # Phase 2 — Data cleaning & feature engineering
├── eda.ipynb                                      # Phase 3 — Exploratory Data Analysis
├── clustering.ipynb                               # Phase 4 — K-Means clustering & PCA
├── ml_model.ipynb                                 # Phase 5 — Random Forest model + SMOTE
│
├── india_2000_2024_daily_weather.csv              # Raw dataset
├── clean_weather.csv                              # Cleaned dataset (feeds all downstream phases)
│
├── app.py                                         # Streamlit app (Predict + Prediction Insights)
├── rainfall_model.pkl                             # Saved, size-optimized Random Forest model (39MB)
├── requirements.txt                               # Python dependencies for deployment
│
├── Weatherlens_India.pbix                         # Power BI dashboard file
│
└── README.md
```
 
---
 
## Workflow
 
```
Raw Weather Data (2000–2024, 10 cities, 91,320 rows)
         ↓
Phase 1 — Data Collection
  · Sourced from Kaggle
         ↓
Phase 2 — Data Cleaning & Feature Engineering
  · Removed duplicate/unreliable columns, fixed date formats
  · Custom Indian seasons (incl. Retreating Monsoon & Pre-Winter)
  · Engineered temp_range, weather_condition, rain_tomorrow
         ↓
Phase 3 — Exploratory Data Analysis
  · 8 visualizations, correlation analysis, outlier handling (IQR)
         ↓
Phase 4 — Unsupervised Learning
  · K-Means (K=4, chosen via Elbow Method + domain knowledge)
  · PCA for 2D cluster visualization
  · Cluster label added as a new feature
         ↓
Phase 5 — Supervised ML
  · Random Forest + SMOTE
  · Caught and fixed data leakage (rain_sum)
  · Model size optimized: 143MB → 39MB with improved accuracy
         ↓
Phase 6 — Streamlit Dashboard
  · Live rainfall prediction + personalized explainability
         ↓
Phase 7 — Power BI Dashboard
  · KPIs, slicers, DAX measures, cluster distribution
         ↓
Phase 8 — Deployment on Render
  · Live, publicly accessible web app
```
 
---
 
## Key Questions Answered
 
- How does temperature range relate to rainfall in India?
- Which Indian cities and regions receive the most rainfall, and why?
- Which months and seasons are most prone to rainfall?
- What natural weather clusters exist in Indian climate data, independent of any labels?
- Can we reliably predict rain from atmospheric conditions alone?
---
 
## Exploratory Data Analysis — Key Findings
 
- Rainfall in India is strongly seasonal, peaking in July during the Southwest Monsoon, with Retreating Monsoon (Oct) and Pre-Winter (Nov) still contributing meaningfully — validating the decision to model them as separate seasons rather than lumping them into "Post-Monsoon"
- Mumbai records the highest average daily rainfall among all 10 cities, driven by its west coast location and the Western Ghats; Kolkata follows via the Bay of Bengal monsoon branch
- `temp_range` (max temp − min temp) emerged as the single strongest predictor of rainfall, with a **-0.67 correlation** — smaller day-night temperature gaps (cloud cover) strongly indicate rain
- The dataset shows a moderate class imbalance: 58% no-rain days vs 42% rain days
---
 
## K-Means Clustering + PCA
 
Using the Elbow Method combined with domain knowledge of Indian climate diversity, **K=4** was selected as the optimal number of clusters:
 
| Cluster | Days | Characteristics |
|---|---|---|
| 🔵 Cold Winter | 13,116 | Low temps, large temp range, near-zero rain |
| 🟢 Mild Transition | 28,164 | Moderate temps, transitional pre/post-monsoon days |
| 🟠 Dry Summer | 30,705 | Highest temps, small temp gap, minimal rain |
| 🟣 Heavy Monsoon | 19,335 | Smallest temp range, highest rainfall |
 
PCA was used to compress the 7 clustering features into 2 dimensions for visualization, confirming that K-Means found genuinely well-separated, meaningful weather patterns — purely from data, without being told what seasons exist.
 
---
 
## ML Model Details
 
| Parameter | Value |
|---|---|
| Problem type | Binary Classification (Rain: Yes / No) |
| Algorithm | Random Forest Classifier (max_depth=15, min_samples_leaf=5) |
| Class imbalance fix | SMOTE (Synthetic Minority Oversampling), applied on training data only |
| Primary metric | ROC-AUC: **0.946** |
| Secondary metric | F1 Score: **0.852** |
| Features | Max/min temperature, apparent temperature, wind speed, temp range, month, weather cluster |
| Model size | 39MB (optimized from an initial 143MB with no loss in performance) |
 
> Accuracy was intentionally avoided as the primary evaluation metric due to class imbalance in Indian rainfall data — a model that always predicts "No Rain" would score ~58% accuracy while being useless.
 
### Key Challenge — Data Leakage Detection
 
An early version of the model showed suspiciously perfect predictions with probabilities of exactly 0.0 or 1.0 — a strong signal of data leakage rather than genuine performance.
 
**Root cause:** The `rain_sum` column (actual rainfall amount) had been accidentally included as an input feature. Since the target variable `rain_tomorrow` was directly derived from it (`rain_tomorrow = rain_sum > 0`), the model was effectively given the answer alongside the question. Feature importance confirmed this — `rain_sum` accounted for 70% of the model's decisions.
 
**Fix:** `rain_sum` was removed from the feature set entirely, and the model was retrained from scratch on genuinely predictive atmospheric features. This produced realistic, well-calibrated probabilities and a trustworthy model.
 
---
 
## Streamlit App Features
 
A two-tab interactive web app:
 
**🔮 Predict Tab**
Users select a city and month, then use sliders to enter max/min temperature and wind speed, and receive a live rainfall probability from the trained Random Forest model — visualized with a gauge chart. A quick link to check live weather for the selected city is included for users unsure of current conditions.
 
**📈 Prediction Insights Tab**
Rather than generic static analysis, this tab performs a live sensitivity analysis tied to the user's own prediction — showing how the rainfall probability would shift if temperature range or wind speed were different, with the user's actual input marked on each chart. This gives every user a personalized explanation of *why* the model predicted what it did.
 
---
 
## Power BI Dashboard
 
To bridge the gap between machine learning models and business decision-making, an executive Power BI dashboard was engineered. This interface aggregates 91K+ climate records, maps regional rainfall variations across major metropolitan hubs, and surfaces the real-world distribution of the unsupervised weather clusters (e.g., segmenting the data into Heavy Monsoon vs. Mild Transition periods).
 
It includes:
- 5 KPI cards (Total Records, Average Rainfall, Average Max/Min Temperature, Rainy Days %)
- Interactive slicers for City, Season, and Year
- Average Rainfall by Season and by City (validating the Python EDA findings)
- Monthly Rainfall Trend
- Weather Pattern Distribution donut chart — visually surfacing the K-Means clusters for a non-technical audience
Built using DAX measures for all key metrics, ensuring dynamic recalculation as users filter the dashboard.
 
---
 
## Dataset
 
- Source: [Kaggle — India Daily Weather 2000–2024](https://www.kaggle.com/datasets/developerghost/climate-in-india-daily-weather-data-2000-2024)
- Records: 91,320 daily weather observations across 10 major Indian cities (Delhi, Mumbai, Kolkata, Chennai, Bangalore, Hyderabad, Ahmedabad, Pune, Jaipur, Lucknow), 2000–2024
- Features: Temperature (max/min/apparent), rainfall, wind speed, weather codes, and more
---
 
## How to Run Locally
 
```bash
# Clone the repository
git clone https://github.com/apurvamalankar806-sketch/WeatherLens-India-project.git
cd WeatherLens-India-project
 
# Install dependencies
pip install -r requirements.txt
 
# Run the Streamlit app
streamlit run app.py
```
 
The Power BI dashboard can be opened directly with `Weatherlens_India.pbix` in Power BI Desktop.
 
---
 
## Status
 
| Phase | Status |
|---|---|
| Data collection | ✅ Done |
| Data cleaning & feature engineering | ✅ Done |
| Exploratory Data Analysis | ✅ Done |
| Clustering (K-Means + PCA) | ✅ Done |
| ML Model (Random Forest + SMOTE) | ✅ Done |
| Streamlit Dashboard | ✅ Done |
| Power BI Dashboard | ✅ Done |
| Deployment on Render | ✅ Done |
 
**Project Status: Complete 🎉**
 
---
 
## Key Takeaways
 
- Built a complete data science pipeline from raw data to a live, deployed product — not just a notebook exercise
- Applied genuine domain knowledge (custom Indian seasons, monsoon geography) rather than defaulting to generic assumptions
- Combined unsupervised and supervised learning in a hybrid approach, using cluster labels as engineered features
- Identified and fixed a real data leakage bug through feature importance analysis, rather than accepting suspiciously good results at face value
- Optimized model size by 73% (143MB → 39MB) while simultaneously improving ROC-AUC and F1 Score
- Delivered insights to two different audiences through two different tools — Streamlit for technical, interactive exploration, and Power BI for business-style reporting
---
 
## Author
 
**Apurva**
BSc Data Science — M.L. Dahanukar College of Commerce, Mumbai
[LinkedIn](#) · [GitHub](https://github.com/apurvamalankar806-sketch)
 
---
