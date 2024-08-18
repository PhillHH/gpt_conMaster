# Verwende ein offizielles Python-Image als Basis
FROM python:3.12-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
COPY . .

# Setze Umgebungsvariablen für Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Exponiere den Port, auf dem Flask läuft
EXPOSE 5000

# Startbefehl für Flask
CMD ["flask", "run", "--host=0.0.0.0"]
