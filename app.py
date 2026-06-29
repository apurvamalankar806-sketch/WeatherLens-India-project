import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import joblib

st.set_page_config(page_title="WeatherLens India", page_icon="🌦️", layout="wide")

if 'started' not in st.session_state:
    st.session_state.started = False

if 'last_inputs' not in st.session_state:
    st.session_state.last_inputs = None
if 'last_prob' not in st.session_state:
    st.session_state.last_prob = None

if not st.session_state.started:
    st.markdown("<h1 style='text-align: center;'>🌦️ WeatherLens India</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>Indian Weather Intelligence System</h4>", unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Continue →", use_container_width=True):
            st.session_state.started = True
            st.rerun()

else:
    st.title("🌦️ WeatherLens India")

    @st.cache_resource
    def load_model():
        return joblib.load('rainfall_model.pkl')

    @st.cache_data
    def load_data():
        return pd.read_csv('clean_weather.csv')

    model = load_model()
    df = load_data()

    FEATURE_COLUMNS = ['temperature_2m_max', 'temperature_2m_min',
                        'apparent_temperature_max', 'apparent_temperature_min',
                        'wind_speed_10m_max', 'temp_range', 'month', 'weather_cluster']

    FEATURE_DISPLAY_NAMES = {
        'temperature_2m_max': 'Max Temperature',
        'temperature_2m_min': 'Min Temperature',
        'apparent_temperature_max': 'Apparent Max Temp',
        'apparent_temperature_min': 'Apparent Min Temp',
        'wind_speed_10m_max': 'Wind Speed',
        'temp_range': 'Temperature Range',
        'month': 'Month',
        'weather_cluster': 'Weather Cluster'
    }

    def get_weather_cluster(max_temp, temp_range):
        if temp_range <= 5:
            return 3  # Heavy Monsoon-like
        elif max_temp >= 33:
            return 2  # Dry Summer-like
        elif max_temp <= 26:
            return 0  # Cold Winter-like
        else:
            return 1  # Mild Transition-like

    def build_input_row(max_temp, min_temp, wind_speed, month):
        temp_range = max_temp - min_temp
        apparent_max = max_temp - 1
        apparent_min = min_temp - 1
        weather_cluster = get_weather_cluster(max_temp, temp_range)
        return pd.DataFrame([[max_temp, min_temp, apparent_max, apparent_min,
                              wind_speed, temp_range, month, weather_cluster]],
                            columns=FEATURE_COLUMNS)

    tab1, tab2 = st.tabs(["🔮 Predict", "📈 Prediction Insights"])

    # ---------------- TAB 1 — PREDICT ----------------
    with tab1:
        st.subheader("Will it rain today?")

        col1, col2 = st.columns(2)
        with col1:
            city = st.selectbox("Select City", sorted(df['city'].unique()), key="predict_city")

            st.markdown(
                f"💡 Don't know today's weather in {city}? "
                f"[Check live weather here ↗](https://www.google.com/search?q={city}+weather+today)"
            )
            st.caption("ℹ️ Note: City is for reference only — prediction is based on the atmospheric conditions you enter below.")

            month = st.selectbox("Select Month", list(range(1, 13)),
                                  format_func=lambda x: pd.Timestamp(2024, x, 1).strftime('%B'),
                                  key="predict_month")
        with col2:
            max_temp = st.slider("Max Temperature (°C)", 10, 50, 32, key="predict_max_temp")
            min_temp = st.slider("Min Temperature (°C)", 0, 35, 25, key="predict_min_temp")

        wind_speed = st.slider("Wind Speed (km/h)", 0, 70, 18, key="predict_wind")

        temp_range = max_temp - min_temp

        if st.button("Predict Rainfall 🔍", use_container_width=True, key="predict_button"):
            input_data = build_input_row(max_temp, min_temp, wind_speed, month)
            prob = model.predict_proba(input_data)[0][1]

            st.session_state.last_inputs = {
                'city': city, 'month': month,
                'max_temp': max_temp, 'min_temp': min_temp,
                'wind_speed': wind_speed, 'temp_range': temp_range
            }
            st.session_state.last_prob = prob

            if prob > 0.5:
                st.error(f"🌧️ HIGH chance of rain — {prob*100:.1f}% probability")
            else:
                st.success(f"☀️ LOW chance of rain — {prob*100:.1f}% probability")

            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob * 100,
                title={'text': "Rain Probability"},
                gauge={'axis': {'range': [0, 100]},
                       'bar': {'color': "steelblue"}}
            ))
            fig_gauge.update_layout(height=300, margin=dict(t=50, b=10))
            st.plotly_chart(fig_gauge, use_container_width=True)

            st.info("👉 Curious about how predictions works? Check out the **Prediction Insights** tab to see how your inputs affect the model's decision!")

    # ---------------- TAB 2 — PREDICTION INSIGHTS ----------------
    with tab2:
        st.subheader("Why did the model predict this?")

        if st.session_state.last_inputs is None:
            st.warning("⚠️ Make a prediction in the **Predict** tab first to see insights here!")
        else:
            inputs = st.session_state.last_inputs
            prob = st.session_state.last_prob

            st.write("**Your Input Summary**")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Max Temp", f"{inputs['max_temp']}°C")
            c2.metric("Min Temp", f"{inputs['min_temp']}°C")
            c3.metric("Wind Speed", f"{inputs['wind_speed']} km/h")
            c4.metric("Temp Range", f"{inputs['temp_range']}°C")

            st.markdown("---")

            # Temp range sensitivity
            st.write("**How Temperature Range affects Rain Probability**")
            st.caption("Keeping your other inputs fixed, this shows how probability shifts as temp range changes.")

            tr_values = list(range(0, 21))
            tr_probs = []
            for tr in tr_values:
                test_min = inputs['max_temp'] - tr
                row = build_input_row(inputs['max_temp'], test_min, inputs['wind_speed'], inputs['month'])
                tr_probs.append(model.predict_proba(row)[0][1] * 100)

            fig1 = px.line(x=tr_values, y=tr_probs,
                            labels={'x': 'Temperature Range (°C)', 'y': 'Rain Probability (%)'},
                            markers=True)
            fig1.add_vline(x=inputs['temp_range'], line_dash="dash", line_color="orange",
                            annotation_text="Your input")
            st.plotly_chart(fig1, use_container_width=True)

            # Wind speed sensitivity
            st.write("**How Wind Speed affects Rain Probability**")
            st.caption("Keeping your other inputs fixed, this shows how probability shifts as wind speed changes.")

            ws_values = list(range(0, 71, 5))
            ws_probs = []
            for ws in ws_values:
                row = build_input_row(inputs['max_temp'], inputs['min_temp'], ws, inputs['month'])
                ws_probs.append(model.predict_proba(row)[0][1] * 100)

            fig2 = px.line(x=ws_values, y=ws_probs,
                            labels={'x': 'Wind Speed (km/h)', 'y': 'Rain Probability (%)'},
                            markers=True)
            fig2.add_vline(x=inputs['wind_speed'], line_dash="dash", line_color="orange",
                            annotation_text="Your input")
            st.plotly_chart(fig2, use_container_width=True)

            st.markdown("---")
            st.metric("Final Predicted Rain Probability", f"{prob*100:.1f}%")