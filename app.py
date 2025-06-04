import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("Prediksi Status Mahasiswa")
st.write("Isi data lengkap berikut untuk memprediksi status mahasiswa:")

# Input lengkap sesuai fitur model
Marital_status = st.selectbox("Status Pernikahan", [1, 2, 3, 4, 5, 6])
Application_mode = st.selectbox("Metode Aplikasi", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
Application_order = st.slider("Urutan Pilihan Aplikasi", 0, 9, 1)
Course = st.selectbox("Kode Kursus", [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991])
Daytime_evening_attendance = st.radio("Kehadiran", [0, 1])
Previous_qualification = st.selectbox("Kualifikasi Sebelumnya", list(range(1, 45)))
Previous_qualification_grade = st.slider("Nilai Kualifikasi Sebelumnya", 0.0, 200.0, 100.0)
Nacionality = st.selectbox("Kebangsaan", [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109])
Mothers_qualification = st.selectbox("Kualifikasi Ibu", list(range(1, 45)))
Fathers_qualification = st.selectbox("Kualifikasi Ayah", list(range(1, 45)))
Mothers_occupation = st.selectbox("Pekerjaan Ibu", [0,1,2,3,4,5,6,7,8,9,10,90,99,122,123,125,131,132,134,141,143,144,151,152,153,171,173,175,191,192,193,194])
Fathers_occupation = st.selectbox("Pekerjaan Ayah", [0,1,2,3,4,5,6,7,8,9,10,90,99,101,102,103,112,114,121,122,123,124,131,132,134,135,141,143,144,151,152,153,154,161,163,171,172,174,175,181,182,183,192,193,194,195])
Admission_grade = st.slider("Nilai Penerimaan", 0.0, 200.0, 100.0)
Displaced = st.radio("Mahasiswa Terpindahkan?", [0, 1])
Educational_special_needs = st.radio("Kebutuhan Khusus?", [0, 1])
Debtor = st.radio("Memiliki Tunggakan?", [0, 1])
Tuition_fees_up_to_date = st.radio("Pembayaran Uang Kuliah Lancar?", [0, 1])
Gender = st.radio("Jenis Kelamin", [0, 1])
Scholarship_holder = st.radio("Penerima Beasiswa?", [0, 1])
Age_at_enrollment = st.slider("Usia Saat Masuk", 16, 60, 18)
International = st.radio("Mahasiswa Internasional?", [0, 1])

Curricular_units_1st_sem_credited = st.number_input("SKS Semester 1 Diakui", 0)
Curricular_units_1st_sem_enrolled = st.number_input("SKS Semester 1 Diambil", 0)
Curricular_units_1st_sem_evaluations = st.number_input("Evaluasi Semester 1", 0)
Curricular_units_1st_sem_approved = st.number_input("Lulus Semester 1", 0)
Curricular_units_1st_sem_grade = st.slider("Nilai Rata-rata Semester 1", 0.0, 20.0, 10.0)
Curricular_units_1st_sem_without_evaluations = st.number_input("Mata Kuliah Semester 1 Tanpa Evaluasi", 0)

Curricular_units_2nd_sem_credited = st.number_input("SKS Semester 2 Diakui", 0)
Curricular_units_2nd_sem_enrolled = st.number_input("SKS Semester 2 Diambil", 0)
Curricular_units_2nd_sem_evaluations = st.number_input("Evaluasi Semester 2", 0)
Curricular_units_2nd_sem_approved = st.number_input("Lulus Semester 2", 0)
Curricular_units_2nd_sem_grade = st.slider("Nilai Rata-rata Semester 2", 0.0, 20.0, 10.0)
Curricular_units_2nd_sem_without_evaluations = st.number_input("Mata Kuliah Semester 2 Tanpa Evaluasi", 0)

Unemployment_rate = st.slider("Tingkat Pengangguran (%)", 0.0, 100.0, 5.0)
Inflation_rate = st.slider("Tingkat Inflasi (%)", 0.0, 100.0, 2.0)
GDP = st.slider("Produk Domestik Bruto", 0.0, 100000.0, 5000.0)

# Susun data input ke DataFrame
input_data = pd.DataFrame([[
    Marital_status, Application_mode, Application_order, Course,
    Daytime_evening_attendance, Previous_qualification, Previous_qualification_grade,
    Nacionality, Mothers_qualification, Fathers_qualification, Mothers_occupation,
    Fathers_occupation, Admission_grade, Displaced, Educational_special_needs, Debtor,
    Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment, International,
    Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
    Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved,
    Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations,
    Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
    Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved,
    Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations,
    Unemployment_rate, Inflation_rate, GDP
]], columns=[
    'Marital_status', 'Application_mode', 'Application_order', 'Course',
    'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
    'Nacionality', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
    'Fathers_occupation', 'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
    'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment', 'International',
    'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
    'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
    'Unemployment_rate', 'Inflation_rate', 'GDP'
])

# Prediksi
if st.button("Prediksi Status"):
    prediction = model.predict(input_data)[0]

    # Mapping angka ke label status (silakan sesuaikan dengan model Anda)
    status_label = {
        0: "Dropout",
        1: "Enrolled",
        2: "Graduate"
    }

    predicted_status = status_label.get(prediction, "Tidak diketahui")
    st.success(f"Status Mahasiswa: **{predicted_status.upper()}**")

