from abc import ABC, abstractmethod


class SearchModel(ABC):
    def __init__(self, name: str, model_path: str):
        self.name = name
        self.model_path = model_path
        self._load_model()

    @abstractmethod
    def _load_model(self): ...

    @abstractmethod
    def __call__(self, inputs): ...


class ClassificationModel(SearchModel):

    def _load_model(self):
        pass

    def __call__(self, inputs):
        pass
