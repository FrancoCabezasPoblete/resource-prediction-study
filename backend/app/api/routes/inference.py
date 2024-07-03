from typing import Any

from fastapi import APIRouter, HTTPException

from app.config import MODELS_PATH
from app.models import InferenceIn, InferenceOut
from app.api.deps import predict_transformer, predict_xgboost, predict_tabnet

router = APIRouter()


@router.get("/", response_model=list[str])
def read_models() -> Any:
    return list(MODELS_PATH.keys())


@router.post("/", response_model=InferenceOut)
def predict(inference_in: InferenceIn) -> Any:
    if inference_in.model not in MODELS_PATH.keys():
        raise HTTPException(status_code=404, detail="Model not found.")
    if inference_in.syscalls:
        raise HTTPException(status_code=501, detail="Syscalls not implemented.")
    predictions = []
    if inference_in.model == "transformer":
        predictions = predict_transformer(inference_in.data, inference_in.multithreaded)
    elif inference_in.model == "xgboost":
        predictions = predict_xgboost(inference_in.data, inference_in.multithreaded)
    elif inference_in.model == "tabnet":
        predictions = predict_tabnet(inference_in.data, inference_in.multithreaded)
    return {
        "model": inference_in.model,
        "multithreaded": inference_in.multithreaded,
        "predictions": predictions
    }
