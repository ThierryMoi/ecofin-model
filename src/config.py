from fastapi import FastAPI
from fastembed import TextEmbedding

from sentence_transformers import SentenceTransformer


MULTILANGUE_MODEL_LARGE = SentenceTransformer("intfloat/multilingual-e5-large")
MULTILANGUE_MODEL_FAST_EMBED = TextEmbedding()


app = FastAPI()
