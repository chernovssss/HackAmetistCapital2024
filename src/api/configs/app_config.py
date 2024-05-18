from typing import List

from pydantic import BaseModel


class ModelConfig(BaseModel):
    name: str
    weights_path: str


class AppConfig(BaseModel):
    # model parameters
    ml_models: List[ModelConfig]
    # app parameters
    port: int
    workers: int
    # async queues parameters
    timeout: float
    max_batch_size: int
    MOTD: str
