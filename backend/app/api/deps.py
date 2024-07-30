import numpy as np
import torch
import xgboost as xgb
from app.config import MODELS_PATH
from joblib import load
from pytorch_tabnet.tab_model import TabNetRegressor

x_scaler = load("/app/model/x_scaler.joblib")
y_scaler = load("/app/model/y_scaler.joblib")


def inv_scaling_pyt(y, y_scaler):
    return y_scaler.inverse_transform(y.cpu().numpy().reshape(-1, 1))


def inv_scaling(y, y_scaler):
    return y_scaler.inverse_transform(y.reshape(-1, 1))


def predict_feedforward(data: list[list[float]]):
    model = torch.load(f"/app/model/{MODELS_PATH["feedforward"]}")
    data = np.array(data)
    data[:, 0] = np.log1p(data[:, 0])
    scaled_data = x_scaler.transform(data)
    tensor_data = torch.tensor(scaled_data, dtype=torch.float32)
    predictions = model.predict(tensor_data)
    predictions = np.expm1(inv_scaling_pyt(predictions, y_scaler))
    return [float(p.items()) for p in predictions]


def predict_mc_dropout(data: list[list[float]]):
    model = torch.load(f"/app/model/{MODELS_PATH["mc_dropout"]}")
    scaled_data = x_scaler.transform(data)
    tensor_data = torch.tensor(scaled_data, dtype=torch.float32)
    predictions = model.predict(tensor_data)
    predictions = inv_scaling_pyt(predictions, y_scaler)
    return [float(p.items()) for p in predictions]


def predict_xgboost(data: list[list[float]]):
    model = xgb.Booster()
    scaler = load("/app/model/scaler_st.joblib")
    model.load_model(f"/app/model/{MODELS_PATH['xgboost']}")
    scaled_data = scaler.transform(data)
    dmatrix = xgb.DMatrix(scaled_data)
    predictions = model.predict(dmatrix)
    predictions = inv_scaling(predictions, y_scaler)
    return [float(p.items()) for p in predictions]


def predict_tabnet(data: list[list[float]]):
    model = TabNetRegressor()
    model.load_model(f"/app/model/{MODELS_PATH['tabnet']}")
    data = np.array(data)
    data[:, 0] = np.log1p(data[:, 0])
    scaled_data = x_scaler.transform(data)
    predictions = model.predict(scaled_data)
    predictions = np.expm1(inv_scaling(predictions, y_scaler))
    return [float(p.items()) for p in predictions]
