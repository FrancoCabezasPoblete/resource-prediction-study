from typing import Union

import torch
from fastapi import UploadFile
from pydantic import BaseModel
from torch import nn


class InferenceIn(BaseModel):
    model: str
    data: list[list[float]]
    syscalls: Union[UploadFile, None] = None


class InferenceOut(BaseModel):
    model: str
    predictions: list[float]


class FeedforwardModel(nn.Module):
    def __init__(self, input_dim, dropout=0.1):
        super().__init__()
        # layers
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(p=dropout),
            nn.Linear(32, 1),
        )

    def forward(self, x):
        return self.model(x)

    def predict(model, X):
        model.eval()
        with torch.no_grad():
            prediction = model(X)
        return prediction


class MCDropoutModel(nn.Module):
    def __init__(self, input_dim, n_hidden_layers, dropout=0.1):
        super().__init__()
        if n_hidden_layers < 2:
            raise ValueError("n_hidden_layers must be greater than 1")
        # Input layer
        layers = [
            nn.Linear(input_dim, 200),
            nn.ReLU(),
            nn.Dropout(p=dropout),
        ]
        # Hidden layers
        layers.extend([nn.Linear(200, 500), nn.ReLU(), nn.Dropout(p=dropout)])
        for _ in range(n_hidden_layers - 2):
            layers.extend([nn.Linear(500, 500), nn.ReLU(), nn.Dropout(p=dropout)])
        layers.extend([nn.Linear(500, 200), nn.ReLU(), nn.Dropout(p=dropout)])
        # Output layer
        layers.append(nn.Linear(200, 2))
        self.model = nn.Sequential(*layers)

    def forward(self, x):
        params = self.model(x)
        loc = params[:, 0:1]
        scale = 1e-6 + torch.nn.functional.softplus(0.33 * params[:, 1:2])
        return torch.distributions.Normal(loc, scale)

    def predict(self, X):
        self.eval()
        with torch.no_grad():
            predictions = self(X).sample()
        return predictions
