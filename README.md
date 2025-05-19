# 🧪 AQI Data Preprocessing
Proyek ini bertujuan untuk melakukan preprocessing dataset *Air Quality Index (AQI)* secara otomatis menggunakan Python dan GitHub Actions. Proses ini mencakup pembersihan data, encoding label, normalisasi fitur, dan penyimpanan data yang telah diproses.

## 📁 Struktur Direktori
```
Eksperimen_SML_Yohanssen-Pradana-Pardede/
│
├── aqi_raw.csv 
├── requirements.txt             
├── preprocessing/
│   └── automate_Yohanssen Pradana Pardede.py  # Skrip preprocessing utama
│   └── Eksperimen_Yohanssen_Pradana_Pardede.ipynb
│   └── aqi_preprocessing.csv
├── .github/
│   └── workflows/
│       └── main.yml
└── README.md
```

## ⚙️ Alur Kerja Otomatisasi
Workflow otomatis akan dijalankan saat:
* Ada **push** ke repository.
* Kamu menjalankan **manual** melalui tab `Actions` di GitHub.

### Langkah-langkah Workflow:
1. Checkout kode dari repository.
2. Setup environment Python versi 3.12.7.
3. Instal dependensi dari `requirements.txt`.
4. Jalankan skrip `automate_Yohanssen Pradana Pardede.py`.
5. Simpan hasil data preprocessing ke file `aqi_preprocessing.csv`.
6. Upload file tersebut sebagai artifact bernama `processed-dataset`.

## 🛠️ Menjalankan Secara Lokal
Jika kamu ingin menjalankan preprocessing secara manual di lokal, ikuti langkah-langkah berikut:
### 1. Clone Repository
```bash
git clone https://github.com/YohanssenPardede/Eksperimen_SML_Yohanssen-Pradana-Pardede.git
cd Eksperimen_SML_Yohanssen-Pradana-Pardede
```

### 2. Buat Virtual Environment (Opsional tapi Disarankan)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Skrip Preprocessing
Pastikan file `aqi_raw.csv` ada di root folder. Kemudian jalankan:
```bash
python preprocessing/automate_Yohanssen Pradana Pardede.py
```

Hasilnya akan disimpan sebagai:
```
preprocessing/aqi_preprocessing.csv
```

## 🧾 Output
**aqi\_preprocessing.csv**: Dataset yang sudah dibersihkan dan diencoding, sebelum dilakukan scaling dan pembagian data.

## 🤖 CI/CD dengan GitHub Actions
File workflow dapat ditemukan di `.github/workflows/preprocess.yml`. Workflow ini memastikan proses preprocessing tetap konsisten di setiap perubahan kode.

## 📌 Catatan
* Dataset mentah `aqi_raw.csv` harus berada di **root direktori**.
* Script preprocessing hanya menyimpan data yang telah diencoding, belum diskalakan atau di-split.
