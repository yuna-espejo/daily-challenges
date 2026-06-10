# Day 007 — Scraper de noticias tech
# Difficulty: Medium | Type: Project
# Time: 35 min | Tags: #api #file-io #automation
# Source: propio
# ─────────────────────────────────
# Obtiene las top 10 noticias de HackerNews y las guarda en un archivo .txt
# con la fecha de hoy. Usa dos endpoints: uno para los IDs y otro para el detalle.
# ─────────────────────────────────

import requests
from datetime import date

today = date.today()

def GetTopStories():
    stories = []

    api = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    dataApi = api.json()
    top10 = dataApi[:10]

    for id in top10:
        news = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
        data = news.json()

        title = data["title"]
        score = data["score"]
        url = data["url"]

        DataToTxt = f"Title: {title}, Score: {score}, URL: {url}"

        stories.append(DataToTxt)

    return stories

def SaveToFile(stories):
    file = open(f"newsHackerNews-{today}.txt", 'a')
    
    for line in stories:
        file.write(line + "\n")
    file.close()

stories = GetTopStories()
SaveToFile(stories)

# Aprendizaje: las APIs de dos pasos requieren una primera llamada para obtener
# IDs y una segunda por cada ID. Las funciones deben pasarse datos como argumentos,
# no depender de variables globales. 'a' en open() añade sin sobreescribir.