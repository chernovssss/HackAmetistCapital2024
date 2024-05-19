from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

import pymorphy3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import (
    cosine_distances,
    haversine_distances,
    euclidean_distances,
)


class SearchModel(ABC):
    def __init__(self, name: str, model_path: str):
        self.name = name
        self.model_path = model_path
        self._load_model()

    @abstractmethod
    def _load_model(self): ...

    @abstractmethod
    def update(self, new_classificator): ...

    @abstractmethod
    def __call__(self, inputs): ...


class ClassificationModel(SearchModel):

    def _load_model(self, file_path: str = None):
        self.norm_clsf = pd.read_csv(self.model_path)
        self.morph = pymorphy3.MorphAnalyzer()

        self.X = self.norm_clsf["text_lemm"]

        self.cv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), norm="l2")
        self.X = self.cv.fit_transform(self.norm_clsf["text_lemm"])

    def _get_lemm(self, text):
        text_lem = [self.morph.parse(word)[0].normal_form for word in text.split(" ")]
        return " ".join(text_lem)

    def __call__(self, inputs):
        Y = self.cv.transform([self.get_lemm(inputs)])
        found_idx = np.argmin(cosine_distances(self.X, Y))
        found_code = self.norm_clsf["code"].iloc[found_idx]
        return found_code

    def update(self, new_classificator):
        raise NotImplementedError()

        def extract_group(text, taget="Группа"):
            text = str(text)
            if taget in text:
                return text.split(":")[-1].replace(f"{taget} ", "").strip()
            return None

        classification = pd.read_excel("../data/train_Ametist/classification.xlsx")
        classification["group"] = classification[
            "Классификатор строительных ресурсов"
        ].apply(lambda x: extract_group(x, "Группа"))
        classification["group"] = classification["group"].fillna(method="ffill")
        classification["group"] = classification[
            "Классификатор строительных ресурсов"
        ].apply(lambda x: extract_group(x, "Группа"))
        classification["group"] = classification["group"].fillna(method="ffill")
        classification["group"] = classification[
            "Классификатор строительных ресурсов"
        ].apply(lambda x: extract_group(x, "Группа"))
        classification["group"] = classification["group"].fillna(method="ffill")
        classification["part"] = classification[
            "Классификатор строительных ресурсов"
        ].apply(lambda x: extract_group(x, "Раздел"))
        classification["part"] = classification["part"].fillna(method="ffill")

        clear_mask = (
            classification.dropna(axis=0, how="any")
            .iloc[:, 0]
            .apply(lambda x: all(c in "0123456789.- " for c in x))
        )

        cleared_classification = classification.dropna(axis=0, how="any")[
            clear_mask
        ].rename(
            columns={
                "Классификатор строительных ресурсов": "code",
                "Unnamed: 1": "name",
                "Unnamed: 2": "measure",
            }
        )

        cleared_classification = cleared_classification[
            cleared_classification["code"].apply(lambda x: len(x.split("."))) > 4
        ].reset_index(drop=True)
        cleared_classification.head()

        morph = pymorphy3.MorphAnalyzer()
        lemm_texts_list = []

        for text in clsf["name"]:
            text_lem = [morph.parse(word)[0].normal_form for word in text.split(" ")]
            if len(text_lem) <= 2:
                lemm_texts_list.append("")
                continue
            lemm_texts_list.append(" ".join(text_lem))
        clsf["text_lemm"] = lemm_texts_list
        clsf = clsf[clsf["text_lemm"] != ""]
        clsf.head()
        cv = CountVectorizer(analyzer="char_wb", ngram_range=(3, 5))
        X = cv.fit_transform(clsf["text_lemm"])


class SearchService:

    def __init__(self, model: ClassificationModel, norm_vectors: pd.DataFrame):
        self.model = model

    def __call__(self, inputs):
        return self.model(inputs)
