import uvicorn
from config import app

from fastapi.middleware.cors import CORSMiddleware

from controller.embedding_controller import (
    embeddings_multilangue_large_models_controller
)


# Configuration des origines autorisées (Allow-Origin)
origins = ["*"]  # Autoriser toutes les origines

# Ajout du middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)
