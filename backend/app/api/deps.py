import torch
import xgboost as xgb
from joblib import load

from app.config import MODELS_PATH

def predict_transformer(data: list[list[float]], multithreaded: bool):
    if multithreaded:
        scaler = load("/app/model/scaler_mt.joblib")
        model = torch.load(f"/app/model/{MODELS_PATH["transformer"].format('mt')}")
    else:
        scaler = load("/app/model/scaler_st.joblib")
        model = torch.load(f"/app/model/{MODELS_PATH["transformer"].format('st')}")
    scaled_data = scaler.transform(data)
    tensor_data = torch.tensor(scaled_data, dtype=torch.float32).unsqueeze(1)
    model.eval()
    with torch.no_grad():
        predictions = model(tensor_data)
    return [float(p.items()) for p in predictions]


def predict_xgboost(data: list[list[float]], multithreaded: bool):
    model = xgb.Booster()
    if multithreaded:
        scaler = load("/app/model/scaler_mt.joblib")
        model.load_model(f"/app/model/{MODELS_PATH['xgboost'].format('mt')}")
    else:
        scaler = load("/app/model/scaler_st.joblib")
        model.load_model(f"/app/model/{MODELS_PATH['xgboost'].format('st')}")
    scaled_data = scaler.transform(data)
    dmatrix = xgb.DMatrix(scaled_data)
    predictions = model.predict(dmatrix)
    return predictions.tolist()


def predict_tabnet():
    raise NotImplementedError
