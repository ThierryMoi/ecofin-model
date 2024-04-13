import os

from langchain.embeddings import LlamaCppEmbeddings

from config import MULTILANGUE_MODEL_LARGE,MULTILANGUE_MODEL_FAST_EMBED


class Embedding:
    """Classe d'embedding de text et de liste de text."""

    def __init__(self):
        pass

    def embeddings_multilangue_large_models(self, texte):
        input_texts = ["query:" + texte]
        embedding = MULTILANGUE_MODEL_LARGE.encode(input_texts, normalize_embeddings=True)
        return list(embedding[0])
    def embeddings_multilangue_fast_embed(self, documents):

        embedding = list(MULTILANGUE_MODEL_FAST_EMBED.embed(documents))
        return list(embedding[0])
