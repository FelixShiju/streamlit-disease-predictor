"""
Created on Mon Jun 23 10:26:00 2025
@author: Felix
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load prediction models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_model.sav', 'rb'))
Park_model = pickle.load(open('Parkinson_model.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['🩺 Diabetes Prediction', '❤️ Heart Disease Prediction', '🧠 Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ========================= 🩺 DIABETES MODULE =========================
if selected == '🩺 Diabetes Prediction':
    st.title("🩺 Diabetes Prediction")
    st.markdown("___Provide basic health data to predict the likelihood of diabetes.___")

    st.markdown("#### 📋 Personal and Clinical Inputs")
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.slider('🤰 Pregnancies (times)', 0, 20, 2,
                                help="Number of times the patient has been pregnant")
        Glucose = st.slider('🩸 Glucose (mg/dL)', 70, 200, 100,
                            help="Plasma glucose concentration after fasting")
        BloodPressure = st.slider('🫀 Blood Pressure (mm Hg)', 40, 140, 80,
                                  help="Diastolic blood pressure")
        SkinThickness = st.slider('📏 Skin Thickness (mm)', 0, 100, 20,
                                  help="Thickness of triceps skin fold")

    with col2:
        Insulin = st.slider('💉 Insulin (µU/mL)', 0, 900, 79,
                            help="2-hour serum insulin level")
        BMI = st.slider('⚖️ BMI (kg/m²)', 10.0, 70.0, 30.0,
                        help="Body Mass Index = weight(kg)/height(m)^2")
        DiabetesPedigreeFunction = st.slider('🧬 Pedigree Function', 0.0, 2.5, 0.5, step=0.01,
                                             help="Likelihood of diabetes based on family history")
        Age = st.slider('🎂 Age (years)', 10, 100, 35,
                        help="Patient's age")

    st.markdown("----")
    if st.button('🔍 Get Diabetes Test Result'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        prediction = diabetes_model.predict([input_data])
        st.success("✅ The person is **not diabetic**." if prediction[0] == 0 else "⚠️ The person **is diabetic**.")


# ========================= ❤️ HEART DISEASE MODULE =========================
if selected == '❤️ Heart Disease Prediction':
    st.title("❤️ Heart Disease Prediction")
    st.markdown("___Evaluate cardiovascular health metrics to assess heart disease risk.___")

    st.markdown("#### 📋 Cardiovascular Metrics")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider('🎂 Age (years)', 20, 100, 45,
                        help="Patient's age in years")
        sex = st.radio('⚧️ Sex', ['Female (0)', 'Male (1)'],
                       help="Biological sex")
        cp = st.radio('💢 Chest Pain Type', [
            '0 = Typical Angina',
            '1 = Atypical Angina',
            '2 = Non-anginal Pain',
            '3 = Asymptomatic'
        ], help="Type of chest pain experienced")
        trestbps = st.slider('🩺 Resting BP (mm Hg)', 80, 200, 120,
                             help="Resting blood pressure")

    with col2:
        chol = st.slider('🧪 Cholesterol (mg/dL)', 100, 600, 200,
                         help="Serum cholesterol level")
        fbs = st.radio('🧫 Fasting Blood Sugar > 120 mg/dL?', ['False (0)', 'True (1)'],
                       help="Fasting blood sugar exceeding 120 mg/dL")
        restecg = st.radio('📈 ECG Result', [
            '0 = Normal',
            '1 = ST-T Abnormality',
            '2 = LV Hypertrophy'
        ], help="Resting electrocardiogram result")
        thalach = st.slider('🏃 Max Heart Rate', 60, 220, 150,
                            help="Maximum achieved heart rate during exercise")

    with col3:
        exang = st.radio('🏋️ Exercise-Induced Angina', ['No (0)', 'Yes (1)'],
                         help="Chest pain due to physical exertion")
        oldpeak = st.slider('📉 ST Depression', 0.0, 6.0, 1.0,
                            help="ST depression induced by exercise")
        slope = st.radio('📐 Slope of Peak Exercise', [
            '0 = Upsloping',
            '1 = Flat',
            '2 = Downsloping'
        ], help="Slope of ST segment during peak exercise")
        ca = st.slider('🔍 Major Vessels Colored (0–3)', 0, 3, 0,
                       help="Number of major vessels colored by fluoroscopy")
        thal = st.radio('🧬 Thalassemia Type', [
            '1 = Normal',
            '2 = Fixed Defect',
            '3 = Reversible Defect'
        ], help="Genetic blood disorder affecting red blood cells")

    st.markdown("----")
    if st.button('🔍 Get Heart Disease Test Result'):
        input_vals = [
            age, int(sex[-2]), int(cp[0]), trestbps, chol, int(fbs[-2]),
            int(restecg[0]), thalach, int(exang[-2]), oldpeak,
            int(slope[0]), ca, int(thal[0])
        ]
        prediction = heart_model.predict([input_vals])
        st.success("✅ The person has **no heart disease**." if prediction[0] == 0 else "⚠️ The person **has heart disease**.")


# ========================= PARKINSON’S MODULE =========================

if selected == '🧠 Parkinsons Prediction':
    st.title("🧠 Parkinson’s Disease Prediction")
    st.markdown("___Voice-based acoustic features are analyzed to detect signs of Parkinson’s.___")

    st.markdown("#### 🎙️ Voice & Acoustic Measurements")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        name = st.number_input("👤 Patient ID", help="Any unique identifier")
        fo = st.number_input("🎵 MDVP:Fo (Hz)", help="Average vocal fundamental frequency")
        fhi = st.number_input("📈 MDVP:Fhi (Hz)", help="Maximum vocal fundamental frequency")
        flo = st.number_input("📉 MDVP:Flo (Hz)", help="Minimum vocal fundamental frequency")
        jitter_percent = st.number_input("🎤 Jitter (%)", help="Variation in pitch")

    with col2:
        jitter_abs = st.number_input("📏 Jitter (Abs)", help="Absolute pitch variation")
        rap = st.number_input("🔁 RAP", help="Relative Average Perturbation")
        ppq = st.number_input("🎯 PPQ", help="Pitch Period Perturbation Quotient")
        ddp = st.number_input("📊 DDP", help="Average difference of durations")
        shimmer = st.number_input("🔊 Shimmer", help="Amplitude variation in voice signal")

    with col3:
        shimmer_db = st.number_input("📶 Shimmer (dB)", help="Amplitude variation in decibels")
        apq3 = st.number_input("🎛️ APQ3", help="Amplitude Perturbation Quotient over 3 cycles")
        apq5 = st.number_input("🎚️ APQ5", help="APQ over 5 cycles")
        apq = st.number_input("🧮 MDVP:APQ", help="Average amplitude perturbation")
        dda = st.number_input("🧬 DDA", help="Derivative of absolute differences between cycles")

    with col4:
        nhr = st.number_input("📡 NHR", help="Noise-to-Harmonics Ratio")
        hnr = st.number_input("📡 HNR", help="Harmonics-to-Noise Ratio")
        rpde = st.number_input("🌀 RPDE", help="Recurrence Period Density Entropy")
        dfa = st.number_input("📐 DFA", help="Detrended Fluctuation Analysis")
        spread1 = st.number_input("📊 Spread1", help="Nonlinear spread of signal")

    with col5:
        spread2 = st.number_input("📊 Spread2", help="Secondary signal spread descriptor")
        d2 = st.number_input("📈 D2", help="Signal complexity measure")
        ppe = st.number_input("🎙️ PPE", help="Pitch Period Entropy")

    st.markdown("---")
    if st.button("🔍 Get Parkinson's Test Result"):
        try:
            input_data = [
                name, fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp,
                shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr,
                rpde, dfa, spread1, spread2, d2, ppe
            ]
            prediction = Park_model.predict([input_data])
            if prediction[0] == 0:
                st.success("✅ The person is **not diagnosed** with Parkinson’s disease.")
            else:
                st.error("⚠️ The person **shows signs** of Parkinson’s disease.")
        except:
            st.warning("❗ Please ensure all inputs are provided as valid numbers.")
