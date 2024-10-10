#!/usr/bin/python3
""" Fetch and print and save"""


import csv
import requests


def fetch_and_print_posts():
    """ Fetch and print"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
            print(f"Status Code: {response.status_code}")
            for title in response.json():
                 print(title["title"])
    else:
         print(f"Error: {response.status_code}")


def fetch_and_save_posts():
    """ Fetch and save"""
    """Récupérer les données JSON de l'API"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    """Convertir les données JSON en une liste de dictionnaires"""
    posts = response.json()

    with open("posts.csv", mode="w", encoding="utf-8") as f:
        """Définition des noms de colonne"""
        name_colonne = ["id", "title", "body"]

        """création d'un objet DictWriter avec le nom des colonnes"""
        writer = csv.DictWriter(f, fieldnames=name_colonne)

        """Écrire les en-têtes dans le fichier csv"""
        writer.writeheader

        """Parcourir la liste des posts et écrire chaque post dans le csv"""
        for post in posts:
            writer.writerow(
                {
                    "id": post["id"],
                    "title": post["title"],
                    "body": post["body"]}
            )
