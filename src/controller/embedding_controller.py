import logging
from fastapi import APIRouter
from service.embedding_service import Embedding
from config import app

router = APIRouter(prefix="/embedding", tags=["embedding"])



@router.get("/text-embedding-muliti-langue-large")
def embeddings_multilangue_large_models_controller(texte: str):
    """Récupère un texte en entrée, l'incorpore avec Embedding, puis renvoie le résultat."""
    try:
        embedding_instance = Embedding()
        embed = embedding_instance.embeddings_multilangue_large_models(texte)
    except Exception as e:
        logging.error(e)
    return [float(x) for x in embed]


@router.get("/text-embedding-muliti-langue-fast-embed")
def embeddings_multilangue_large_fast_controller(texte: str):
    """Récupère un texte en entrée, l'incorpore avec Embedding, puis renvoie le résultat."""
    try:
        embedding_instance = Embedding()
        embed = embedding_instance.embeddings_multilangue_fast_embed(texte)
        return [float(x) for x in embed]
    except Exception as e:
        logging.error(e)
app.include_router(router)
