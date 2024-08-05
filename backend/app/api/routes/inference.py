from typing import Any

from app.api.deps import (
    predict_feedforward,
    predict_mc_dropout,
    predict_tabnet,
    predict_xgboost,
)
from app.config import MODELS_PATH
from app.models import InferenceIn, InferenceOut
from fastapi import APIRouter, HTTPException

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
    predictions = {}
    if inference_in.model.count("mc_dropout") > 0:
        predictions["mc_dropout"] = predict_mc_dropout(inference_in.data)
    if inference_in.model.count("feedforward") > 0:
        predictions["feedforward"] = predict_feedforward(inference_in.data)
    elif inference_in.model.count("xgboost") > 0:
        predictions["xgboost"] = predict_xgboost(inference_in.data)
    elif inference_in.model.count("tabnet") > 0:
        predictions["tabnet"] = predict_tabnet(inference_in.data)
    return {
        "multithreaded": inference_in.multithreaded,
        "predictions": predictions
    }
