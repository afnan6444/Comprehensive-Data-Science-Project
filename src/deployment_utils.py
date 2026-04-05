import joblib

def load_model(model_path="deployment/sales_model.pkl", scaler_path="deployment/scaler.pkl"):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler
