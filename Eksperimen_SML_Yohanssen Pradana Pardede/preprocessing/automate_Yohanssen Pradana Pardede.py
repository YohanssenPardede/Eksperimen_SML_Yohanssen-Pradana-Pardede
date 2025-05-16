import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

def preprocess_aqi_data(df):
    """
    Melakukan preprocessing pada dataset AQI.

    Tahapan preprocessing:
    1. Menghapus baris dengan missing values.
    2. Melakukan encoding pada kolom target (AQI Category).
    3. Melakukan normalisasi pada fitur numerik.
    4. Membagi data menjadi train dan test set.

    Args:
        df (pd.DataFrame): DataFrame input yang berisi data AQI.

    Returns:
        X_train, X_test, y_train, y_test (tuple): Data yang sudah dibagi.
        le (LabelEncoder): Encoder untuk label.
        scaler (StandardScaler): Scaler untuk fitur.
        df_encoded (pd.DataFrame): Data setelah pembersihan dan encoding (sebelum scaling dan split).
    """

    # 1. Menghapus nilai kosong
    df = df.dropna()

    # 2. Tentukan fitur dan target
    features = ['CO AQI Value', 'Ozone AQI Value', 'NO2 AQI Value', 'PM2.5 AQI Value']
    target = 'AQI Category'

    # 3. Encoding target label
    le = LabelEncoder()
    df[target] = le.fit_transform(df[target])

    # Simpan dataframe setelah encoding untuk output CSV
    df_encoded = df.copy()

    # 4. Normalisasi fitur
    X = df[features]
    y = df[target]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 5. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y)

    return X_train, X_test, y_train, y_test, le, scaler, df_encoded


if __name__ == "__main__":
    # Baca data
    # Mendapatkan direktori tempat skrip saat ini berada
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Membuat path ke direktori parent
    parent_dir = os.path.dirname(script_dir)

    # Membuat path lengkap ke file aqi_raw.csv di direktori parent
    file_path = os.path.join(parent_dir, 'aqi_raw.csv')

    df = pd.read_csv(file_path)

    # Panggil preprocessing
    X_train, X_test, y_train, y_test, le, scaler, df_encoded = preprocess_aqi_data(df)

    # Simpan data hasil preprocessing (sebelum scaling dan split) ke CSV
    output_file = "aqi_preprocessing.csv"
    df_encoded.to_csv(output_file, index=False)
    print(f"File hasil preprocessing telah disimpan pada file {output_file}")