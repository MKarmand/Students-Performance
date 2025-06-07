
# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

🔗 [Klik di sini untuk melihat dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)
🔗 [Klik di sini untuk melihat dashboard Tableau](https://public.tableau.com/app/profile/muhammad.armand7202/viz/DrancangInstitute/DrancangInstitute)
🔗 [Klik untuk akses aplikasi prediksi](https://students-performance-mka.streamlit.app)

## Business Understanding

Drancang University menghadapi tantangan besar terkait **tingkat dropout mahasiswa yang tinggi**. Tingginya angka mahasiswa yang keluar berdampak pada efektivitas program pendidikan dan perencanaan anggaran institusi. Oleh karena itu, diperlukan analisis mendalam untuk memahami faktor-faktor yang memengaruhi dropout dan membangun solusi berbasis data.

### Permasalahan Bisnis

- Tingginya tingkat dropout mahasiswa (1.421 dari 4.424 mahasiswa / 32.12%).
- Ketidakseimbangan distribusi dropout berdasarkan usia, jenis kelamin, kehadiran, dan program studi.
- Belum adanya sistem yang dapat memprediksi risiko dropout mahasiswa secara dini.

### Cakupan Proyek

- Eksplorasi dan visualisasi data mahasiswa.
- Analisis distribusi dropout berdasarkan gender, usia, program studi, dan status sosial.
- Pembangunan model Machine Learning untuk memprediksi status mahasiswa.
- Pengembangan prototipe aplikasi prediksi berbasis Streamlit.
- Pembuatan dashboard visual untuk menyampaikan insight utama secara interaktif.

## Persiapan

**Sumber Data:**

Dataset yang digunakan dalam proyek ini adalah **Student Performance Dataset** dari Dicoding. Dataset ini berisi informasi akademik, demografis, dan sosial ekonomi mahasiswa, termasuk status kelulusan, nilai semester, beasiswa, serta kondisi pembayaran kuliah.



**Setup Environment:**

Untuk menjalankan proyek ini, siapkan environment pengembangan dengan langkah-langkah berikut:

```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/macOS
venv\Scripts\activate      # Untuk Windows

# Install library yang dibutuhkan
pip install -r requirements.txt

# Jalankan Streamlit
streamlit run app.py
```

## Data Overview

Dataset berisi informasi akademik, demografis, dan sosial ekonomi mahasiswa:
- Total mahasiswa: **4.424**
- Status:
  - Lulus: **2.209**
  - Masih Terdaftar: **794**
  - Dropout: **1.421**
- Fitur penting: status pernikahan, jenis kelamin, usia saat pendaftaran, nilai akademik, jenis kursus, dan lainnya.

## Dashboard Insight (Tableau Public)

Visualisasi berikut menggambarkan berbagai faktor yang memengaruhi dropout:

- **Dropout Rate**: 32.12%
- **Dropout by Gender**: Hampir seimbang antara laki-laki dan perempuan.
- **Dropout by Attendance**: Mayoritas dropout berasal dari kelas siang (85%).
- **Dropout by Course**: Tertinggi pada Manajemen, Keperawatan, dan Jurnalistik.
- **Dropout by Marital Status**: Mayoritas dropout adalah mahasiswa lajang.
- **Dropout by Age**: Umur muda (16–24 tahun) mendominasi kasus dropout.
- **Gender vs Age Group Dropout**: Terdapat perbedaan pola dropout berdasarkan kelompok usia dan gender.


## Machine Learning Prototype

Model Machine Learning berbasis **Random Forest** dibangun untuk memprediksi status mahasiswa (Dropout / Enrolled / Graduate). Fitur yang digunakan antara lain:
- Informasi akademik: admission grade, nilai semester, jumlah SKS.
- Demografi: usia, gender, status sosial.
- Sosio-ekonomi: beasiswa, pembayaran kuliah, pekerjaan orang tua.



## Conclusion

Analisis mendalam terhadap data mahasiswa Drancang University mengungkap karakteristik umum dari mahasiswa yang mengalami **dropout**:

- **Berusia muda (16–24 tahun)** saat mendaftar.
- **Belum menikah** (lajang).
- **Mengikuti kelas siang** (daytime attendance).
- Terdaftar dalam program studi seperti **Manajemen**, **Keperawatan**, dan **Jurnalistik**.
- Memiliki **nilai akademik rendah**, terutama di semester pertama.
- Berasal dari kelompok yang **tidak mendapatkan beasiswa** dan memiliki **tunggakan pembayaran kuliah** (debtor).

Dengan menggunakan model prediksi berbasis machine learning dan dashboard visualisasi, universitas kini dapat mengenali mahasiswa berisiko tinggi lebih dini dan mengambil langkah proaktif. Strategi ini dapat membantu menekan angka dropout yang saat ini mencapai 32.12% serta meningkatkan kualitas layanan pendidikan secara keseluruhan.

## Rekomendasi Action Items

Berdasarkan temuan data, berikut langkah-langkah konkret yang dapat diterapkan oleh institusi:

1. **Program Intervensi Akademik Dini**
   - Sediakan **kelas remedial** atau **pendampingan belajar** untuk mahasiswa dengan nilai rendah di semester pertama.
   - Terapkan sistem **monitoring nilai otomatis** yang terhubung dengan model prediktif, agar pihak akademik dapat langsung melakukan tindak lanjut.

2. **Perluasan Bantuan Finansial**
   - Mahasiswa dengan status **debtor** dan tanpa beasiswa memiliki risiko dropout yang tinggi.
   - Perlu dikembangkan program **beasiswa berbasis kebutuhan** dan **penghapusan denda keterlambatan** bagi mahasiswa yang menunjukkan motivasi belajar tinggi.

3. **Pendampingan Sosial dan Psikologis**
   - Bentuk **program mentoring** untuk mahasiswa baru, khususnya kelompok usia muda dan lajang, guna membantu adaptasi akademik dan sosial.
   - Sediakan layanan **konseling rutin** untuk mendeteksi tekanan mental atau masalah pribadi yang bisa memicu dropout.

4. **Evaluasi Jadwal Kelas Siang**
   - Karena mayoritas dropout berasal dari kelas siang, perlu dievaluasi beban kurikulum dan fleksibilitas jadwalnya.
   - Pertimbangkan penerapan **kelas sore atau hybrid** untuk meningkatkan retensi bagi mahasiswa yang bekerja atau memiliki tanggungan keluarga.

5. **Implementasi Sistem Prediksi Terintegrasi**
   - Gunakan **model prediksi dropout** dalam sistem informasi akademik untuk menghasilkan peringatan dini setiap semester.
   - **Perbaharui data dan model secara berkala** untuk menjaga akurasi dan menyesuaikan dengan dinamika mahasiswa dari tahun ke tahun.
