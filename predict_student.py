import joblib
import pandas as pd

def predict_students(df_input, model_path, scaler_path, label_encoder_path):

    # df_input: DataFrame siswa baru tanpa kolom 'Status'
    # model_path: path ke file model (.pkl)
    # scaler_path: path ke file scaler (.pkl)
    # label_encoder_path: path ke file label encoder (.pkl)

    # Load model dan preprocessing tools
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    label_encoder = joblib.load(label_encoder_path)

    # Salin data untuk diproses
    df_proc = df_input.copy()

    # Encode semua kolom kategorikal (jika ada)
    for col in df_proc.select_dtypes(include='object').columns:
        df_proc[col] = pd.factorize(df_proc[col])[0]

    # Scaling
    df_scaled = scaler.transform(df_proc)

    # Prediksi
    y_pred = model.predict(df_scaled)
    pred_labels = label_encoder.inverse_transform(y_pred)

    # Tambahkan hasil prediksi ke DataFrame
    df_input['Predicted_Status'] = pred_labels

    return df_input