# API LIVRE Full Stack

## DÉMARRAGE

### INSTALLATION DES DÉPENDANCES

#### Python 3.8.5

#### pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

Suivez les instructions pour installer la dernière version de python pour votre système dans le [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### ENVIRONNEMENT VIRTUEL

Nous vous recommandons de travailler dans un environnement virtuel lorsque vous utilisez Python pour vos projets.Cela vous permet de séparer et d'organiser vos dépendances pour chaque projet. Vous pourez trouver toutes les instructions vous permettant de mettre en place un environnement virtuel pour votre système dans [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### DÉPENDANCES PIP

Maintenant que vous avez configurer et lancer votre environnement virtuel, Installez les dépendances en vous rendant sur le repectoire `flask-book-api`, ensuite exécutez les commandes suivantes :

```bash
pip install -r requirements.txt
ou
pip3 install -r requirements.txt
```

Ceci installera toutes les pacquets requis dans le fichier `requirements.txt`.

##### DÉPENDANCES CLÉS

- [Flask](http://flask.pocoo.org/) est un framework de microservices backend léger. Flask est nécessaire pour gérer les demandes et les réponses.

- [SQLAlchemy](https://www.sqlalchemy.org/) est la boîte à outils Python SQL et l'ORM que nous utiliserons pour gérer la base de données sqlite légère. Vous travaillerez principalement dans app.py et pourrez référencer models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) est l'extension que nous utiliserons pour gérer les demandes d'origine croisée de notre serveur frontend.

## CONFIGURATION DE LA BASE DE DONNÉES

Avec Postgres en marche, restaurez une base de données en utilisant le fichier bookdb.sql fourni. Depuis le dossier backend, dans le terminal, exécutez :

```bash
psql booksdb < bookdb.sql
```

## DÉMARER LE SERVEUR

Depuis le répertoire `flask-book-api`, assurez-vous d'abord que vous travaillez dans l'environnement virtuel que vous avez créé.

Pour exécuter le serveur sur Linux ou Mac, exécutez :

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Pour exécuter le serveur sur Windows, exécutez :

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Mettre la variable `FLASK_ENV` à `development` va détecter les changements de fichiers et redémarrer le serveur automatiquement.

En mettant la variable `FLASK_APP` à `app.py`, flask utilisera le fichier `app.py` pour trouver l'application.

Vous pouvez aussi exécutez

```
python app.py
```

## RÉFÉRENCE API

Démarrer

URL de base : Actuellement, cette application ne peut être exécutée que localement et n'est pas hébergée comme une URL de base. L'application backend est hébergée par défaut à l'adresse http://localhost:5000, qui est définie comme un proxy dans la configuration du frontend.

## GESTION D'ERREURS

Les erreurs sont retournées sous forme d'objets JSON au format suivant :

```
    {
    "success":False
    "error": 400
    "message":"Bad request
    }
```

L'API retournera cinq types d'erreurs quand les requêtes échouent :

```
    . 400: Bad request
    . 500: Internal server error
    . 422: Unprocessable
    . 404: Not found
    . 405: Method not allowed
```

## TERMINAISON

##### CATEGORIE

. ## GET/categories

```
GENERAL:
Cette terminaison retourne une liste d'objets Categorie, une valeur 'success', nombre total de categories.
```

    SAMPLE: curl http://localhost:5000/categories
    {
        "categories": [
            {
                "description": "un sous-genre de la science-fiction qui exploite les ressorts de l'humour",
                "id": 1,
                "name": "Science-fiction humouristique"
            },
            {
                "description": "un court récit en vers ou en prose qui vise à donner de façon plaisante une leçon de vie",
                "id": 2,
                "name": "Fable"
            },
            {
                "description": "un genre théâtral dont l’origine remonte au théâtre grec antique",
                "id": 3,
                "name": "Tragédie"
            },
            {
                "description": "un roman relevant du genre policier",
                "id": 4,
                "name": "Roman policier"
            }
        ],
        "nombre_categories": 4,
        "success": true
    }

. ## GET/livres

```
GENERAL:
Cette terminaison retourne une liste d'objets livre, une valeur 'success', nombre total de livres.
```

    SAMPLE: curl http://localhost:5000/livres
    {
    "livres": [
            {
                "auteur": "Fredric Brown",
                "categorie_id": 1,
                "editeur": "Astounding",
                "id": 1,
                "titre": "Martiens, Go Home!"
            },
            {
                "auteur": "Jean de La Fontaine",
                "categorie_id": 2,
                "editeur": "Desaint & Saillant",
                "id": 2,
                "titre": "Le corbeau et le renard"
            },
            {
                "auteur": "William Shakespeare",
                "categorie_id": 3,
                "editeur": "John Danter",
                "id": 3,
                "titre": "Roméo et Juliette"
            },
            {
                "auteur": "Michael Connelly",
                "categorie_id": 4,
                "editeur": "null",
                "id": 5,
                "titre": "Séquences mortelles"
            }
        ],
        "nombre_livres": 4,
        "success": true
    }

. ## DELETE/Categories/(categorie_id)

```
GENERAL:
Supprime la catégorie avec l'ID donneé s'il existe. Retourne l'ID de la catégorie suprimée, la valeur du success, et le nombre total de catégories
```

        SAMPLE: curl -X DELETE http://localhost:5000/categories/4

    {
        "nombre_categories": 3,
        "success": true,
        "supprimer ": 4
    }

. ## DELETE/livres/(livre_id)

```
GENERAL:
Supprime le livre avec l'ID donneé s'il existe. Retourne l'ID du livre suprimé, la valeur du success, et le nombre total de livres
```

        SAMPLE: curl -X DELETE http://localhost:5000/livres/5

    {
        "success": true,
        "supprimer ": 5,
        "total_livres": 3
    }

```


```

. ##PATCH/categories(categorie_id)

GENERAL:
Cette terminaison est utilisé pour modifier une catégorie
Nous retournons l'ID de la catégorie modifiée

    SAMPLE.....For Patch

    curl -X PATCH http://localhost:5000/categories/5 -H "Content-Type:application/json" -d "{"name":"magasine", "description": "Des magasines"}"

    {
        "categorie_id": 5,
        "success": true
    }

. ##PATCH/livres(livre_id)

GENERAL:
Cette terminaison est utilisé pour modifier un livre
Nous retournons l'ID du livre modifié

    SAMPLE.....For Patch

    curl -X PATCH http://localhost:5000/livres/6 -H "Content-Type:application/json" -d "{"isbn":"8888"}"

    {
        "id": 6,
        "success": true
    }

. ## POST/categories

GENERAL:
Cette terminaison est utilisé pour créer une nouvelle categorie.
Dans le cas de la création d'une categorie :
Nous retournons l'ID de la nouvelle categorie créée, la categorie créée, la liste des categories et le nombre de categories.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/categories -H "Content-Type:application/json" -d "{"name":"Parodie","decripttion":"Une parodie"}"


    {
        "categorie_id": 6,
        "success": true,
        "total_categories": [
            {
                "description": "un sous-genre de la science-fiction qui exploite les ressorts de l'humour",
                "id": 1,
                "name": "Science-fiction humouristique"
            },
            {
                "description": "un court récit en vers ou en prose qui vise à donner de façon plaisante une leçon de vie",
                "id": 2,
                "name": "Fable"
            },
            {
                "description": "un genre théâtral dont l’origine remonte au théâtre grec antique",
                "id": 3,
                "name": "Tragédie"
            },
            {
                "description": "des magazines",
                "id": 5,
                "name": "magazine"
            },
            {
                "description": "une parodie",
                "id": 6,
                "name": "Parodie"
            }
        ]
    }

. ## POST/livres

GENERAL:
Cette terminaison est utilisé pour créer un nouveau livre.
Dans le cas de la création d'un livre :
Nous retournons l'ID du nouveau livre créé, le livre créé, la liste des livres et le nombre de livres.

    SAMPLE.....For create

    curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{"isbn":"111122","titre":"Pimento","categorie_id":2,"date_publication":"2021-02-01",
    "auteur":"Bosko","editeur="Bleach"}"


    {
        "livre_id": 13,
        "success": true,
        "total_livres": [
            {
                "auteur": "Fredric Brown",
                "categorie_id": 1,
                "editeur": "Astounding",
                "id": 1,
                "titre": "Martiens, Go Home!"
            },
            {
                "auteur": "Jean de La Fontaine",
                "categorie_id": 2,
                "editeur": "Desaint & Saillant",
                "id": 2,
                "titre": "Le corbeau et le renard"
            },
            {
                "auteur": "William Shakespeare",
                "categorie_id": 3,
                "editeur": "John Danter",
                "id": 3,
                "titre": "Roméo et Juliette"
            },
            {
                "auteur": "Loukoumane",
                "categorie_id": 3,
                "editeur": "Moise",
                "id": 6,
                "titre": "Au large de l'exellence"
            },
            {
                "auteur": "Bosko",
                "categorie_id": 1,
                "editeur": "Bleach",
                "id": 13,
                "titre": "Pimento"
            }
        ]
    }
