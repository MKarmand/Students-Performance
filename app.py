import streamlit as st
import numpy as np
import pickle
import joblib

# --- Load model dan encoder ---
model = joblib.load("model.pkl")
encoder = joblib.load("encoder.pkl")


st.title("Prediksi Status Mahasiswa")
st.markdown("Silakan masukkan informasi mahasiswa di bawah ini:")

# Fungsi input nilai 0-200
def number_input_200(label):
    return st.number_input(label, min_value=0.0, max_value=200.0, step=1.0)

# --- Input fitur ---
marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6], format_func=lambda x: {
    1: "1 – Single", 2: "2 – Married", 3: "3 – Widower", 4: "4 – Divorced", 5: "5 – Facto Union", 6: "6 – Legally Separated"
}[x])

application_order = st.slider("Urutan Pilihan Saat Mendaftar", 0, 9, 0)
daytime_evening = st.radio("Waktu Kehadiran Kuliah", [1, 0], format_func=lambda x: "Siang" if x == 1 else "Malam")
previous_qualification_grade = number_input_200("Nilai rata-rata saat SMA")
admission_grade = number_input_200("Nilai Ujian Masuk Universitas")
displaced = st.radio("Apakah Mahasiswa Pengungsi?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
educational_special_needs = st.radio("Kebutuhan Khusus Pendidikan?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
debtor = st.radio("Memiliki Tunggakan?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
tuition_fees_up_to_date = st.radio("Pembayaran Kuliah Lancar?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
gender = st.radio("Jenis Kelamin", [1, 0], format_func=lambda x: "Laki-laki" if x == 1 else "Perempuan")
scholarship_holder = st.radio("Penerima Beasiswa?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")
age_at_enrollment = st.number_input("Usia Saat Mendaftar", min_value=15, max_value=70, step=1)
international = st.radio("Mahasiswa Internasional?", [1, 0], format_func=lambda x: "Ya" if x == 1 else "Tidak")

curricular_units_1st_sem_enrolled = st.number_input(
    "Jumlah Mata Kuliah Semester 1 yang Diambil", min_value=0, max_value=30, step=1)
curricular_units_1st_sem_approved = st.number_input(
    "Jumlah Mata Kuliah Semester 1 yang Lulus", min_value=0, max_value=30, step=1)
curricular_units_1st_sem_grade = st.number_input(
    "Nilai Rata-rata Semester 1", min_value=0.0, max_value=20.0, step=0.1)

curricular_units_2nd_sem_enrolled = st.number_input(
    "Jumlah Mata Kuliah Semester 2 yang Diambil", min_value=0, max_value=30, step=1)
curricular_units_2nd_sem_approved = st.number_input(
    "Jumlah Mata Kuliah Semester 2 yang Lulus", min_value=0, max_value=30, step=1)
curricular_units_2nd_sem_grade = st.number_input(
    "Nilai Rata-rata Semester 2", min_value=0.0, max_value=20.0, step=0.1)


# --- Prediksi ---
if st.button("Prediksi Status"):
    features = np.array([[marital_status, application_order, daytime_evening,
                          previous_qualification_grade, admission_grade, displaced,
                          educational_special_needs, debtor, tuition_fees_up_to_date,
                          gender, scholarship_holder, age_at_enrollment, international,
                          curricular_units_1st_sem_enrolled, curricular_units_1st_sem_approved, curricular_units_1st_sem_grade,
                          curricular_units_2nd_sem_enrolled, curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade]])

    prediction = model.predict(features)
    label = encoder.inverse_transform(prediction)[0]

    st.subheader("Hasil Prediksi:")
    st.success(f"Status Mahasiswa: **{label.capitalize()}**")
