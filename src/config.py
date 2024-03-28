from fastapi import FastAPI

from sentence_transformers import SentenceTransformer


MULTILANGUE_MODEL_LARGE = SentenceTransformer("intfloat/multilingual-e5-large")


app = FastAPI()
