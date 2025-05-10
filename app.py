import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load(r"model\random_forest_model.pkl")
scaler = joblib.load(r"model\feature_scaler.pkl")
label_encoder = joblib.load(r"model\label_encoder_status.pkl")

df_students = pd.read_csv("data.csv", delimiter=";")
df_enrolled = df_students[df_students['Status'] == 'Enrolled'].copy()
df_enrolled = df_enrolled.reset_index(drop=True)

st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")
st.title("🎓 Prediksi Kelulusan Mahasiswa Jaya Jaya Institut")
st.write("Pilih salah satu mahasiswa yang masih berstatus enrolled untuk memprediksi apakah mereka akan graduate atau dropout.")

student_options = df_enrolled.index.tolist()
selected_idx = st.selectbox("Pilih Mahasiswa (baris ke-)", student_options)

selected_student = df_enrolled.loc[selected_idx].copy()

st.subheader("Data Mahasiswa Terpilih")
st.dataframe(selected_student.to_frame().T)

features_to_use = [
    'Marital_status',
    'Application_mode',
    'Application_order',
    'Course',
    'Daytime_evening_attendance',
    'Previous_qualification',
    'Previous_qualification_grade',
    'Nacionality',
    'Mothers_qualification',
    'Fathers_qualification',
    'Mothers_occupation',
    'Fathers_occupation',
    'Admission_grade',
    'Displaced',
    'Educational_special_needs',
    'Debtor',
    'Tuition_fees_up_to_date',
    'Gender',
    'Scholarship_holder',
    'Age_at_enrollment',
    'International',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate',
    'Inflation_rate',
    'GDP'
]

input_data = selected_student[features_to_use].to_frame().T
scaled_input = scaler.transform(input_data)

if st.button("Prediksi Status Mahasiswa"):
    prediction = model.predict(scaled_input)
    predicted_label = label_encoder.inverse_transform(prediction)[0]
    st.success(f"📢 Prediksi: Mahasiswa ini kemungkinan akan **{predicted_label.upper()}**")