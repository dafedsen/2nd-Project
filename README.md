# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Meskipun telah mencetak banyak lulusan berkualitas, institusi ini juga menghadapi masalah signifikan yaitu tingginya angka siswa yang melakukan dropout. Hal ini berdampak buruk pada reputasi institusi dan dapat mempengaruhi keberlangsungan operasional serta kepercayaan calon mahasiswa.

### Permasalahan Bisnis

* Tingginya angka dropout mahasiswa setiap tahun.
* Kurangnya sistem pendeteksian dini terhadap siswa yang berpotensi dropout.
* Tidak adanya alat bantu monitoring performa siswa secara visual dan real-time.

### Cakupan Proyek

* Menganalisis data historis performa mahasiswa untuk menemukan pola-pola dropout.
* Membangun model machine learning untuk mendeteksi potensi dropout sejak dini.
* Membuat dashboard untuk memantau performa mahasiswa dan mendukung pengambilan keputusan.
* Membuat prototype sistem prediksi berbasis web menggunakan Streamlit.

### Persiapan

Sumber data: `data.csv` yang berisi data historis mahasiswa termasuk performa akademik, latar belakang, dan status akhir (dropout/graduate/enrolled).

## Setup environment:

```
# Buat Virtual Environtment
python -m venv venv

# Aktifkan Virtual Env
source venv/bin/activate      # Untuk Linux/Mac
venv\Scripts\activate.bat     # Untuk Windows

# Install library yang dibutuhkan
pip install -r requirements.txt
```

## Menjalankan Metabase
```
docker cp ./metabase.db.mv.db metabase:/metabase.db/metabase.db.mv.db
```

## Menggunakan Fungsi Predict
```
import pandas as pd
from predict_students import predict_students

# Load data siswa baru (tanpa kolom 'Status')
df_new = pd.read_csv("new_students.csv")

# Jalankan prediksi
df_predicted = predict_students(
    df_input=df_new,
    model_path="model/random_forest_model.pkl",
    scaler_path="model/feature_scaler.pkl",
    label_encoder_path="model/label_encoder_status.pkl"
)

# Tampilkan hasil
print(df_predicted[['Predicted_Status']])
```

## Business Dashboard

Dashboard dibuat menggunakan Metabase yang menampilkan:

* Distribusi status mahasiswa (dropout, graduate)
* Rata-rata nilai akademik berdasarkan status
* Visualisasi korelasi fitur-fitur penting dengan status dropout
* Tren performa berdasarkan semester

## Menjalankan Sistem Machine Learning

Sistem prediksi dropout dikembangkan dengan Random Forest Classifier. Aplikasi ini di-deploy menggunakan Streamlit Community Cloud.

Cara menjalankan prototype:

```
1. Buka link berikut: https://2nd-project-qknzasy4kp4jamd8xxntpd.streamlit.app
2. Pilih mahasiswa aktif dari data yang sudah ada.
3. Klik tombol prediksi untuk melihat apakah mahasiswa tersebut berpotensi dropout.
```

Model dan preprocessing disimpan dalam file `.pkl` untuk keperluan deployment:

* `random_forest_model.pkl`
* `feature_scaler.pkl`
* `label_encoder_status.pkl`

## Conclusion

Dari hasil analisis dan pemodelan:

* Terdapat korelasi kuat antara performa semester awal dan risiko dropout.
* Faktor-faktor seperti ketepatan membayar biaya kuliah, nilai akademik, dan usia saat masuk turut mempengaruhi dropout.
* Model machine learning yang dikembangkan memiliki performa memuaskan dalam mengklasifikasi siswa dropout dengan akurasi dan recall yang baik.

### Rekomendasi Action Items

* Memberikan intervensi awal kepada mahasiswa dengan nilai akademik rendah pada semester pertama.
* Menerapkan sistem monitoring berkala terhadap mahasiswa yang memiliki risiko tinggi dropout.
* Menyediakan bimbingan akademik dan keuangan untuk mahasiswa yang kesulitan.
* Mengintegrasikan sistem prediksi ini ke dalam proses onboarding mahasiswa baru.
