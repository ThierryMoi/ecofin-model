# Utilisez une image de base Python
FROM python:3.9

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposez le port utilisé par votre application FastAPI
EXPOSE 8005
#production
#EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python3","src/main.py"]
