from os import getenv
from typing import Any

from dotenv import load_dotenv

load_dotenv()


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


BACKEND_CORS_ORIGINS = parse_cors(getenv("BACKEND_CORS_ORIGINS"))
SECRET_KEY = getenv("SECRET_KEY")
API_V1_STR = "/api/v1"
MODELS_PATH = {
    "mc_dropout": "mc_dropout_model.pt",
    "xgboost": "xgboost_model.model",
    "tabnet": "tabnet_model.pt",
    "feedforward": "feedforward_model.pt",
}
