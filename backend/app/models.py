from typing import Union

from pydantic import BaseModel
from fastapi import UploadFile


class InferenceIn(BaseModel):
    model: str
    multithreaded: bool
    data: list[list[float]]
    syscalls: Union[UploadFile, None] = None


class InferenceOut(BaseModel):
    model: str
    multithreaded: bool
    predictions: list[float]
