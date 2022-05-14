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

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## CONFIGURATION DE LA BASE DE DONNÉES

Avec Postgres en marche, restaurez une base de données en utilisant le fichier livredb.sql fourni. Depuis le dossier backend, dans le terminal, exécutez :

```bash

//for me :: pg-dump -u postgres nom_base > livredb.sql
psql livre_db < livredb.sql
```

## DÉMARER LE SERVEUR

Depuis le répertoire `flask-book-api`, assurez-vous d'abord que vous travaillez dans l'environnement virtuel que vous avez créé.

Pour exécuter le serveur sur Linux ou Mac, exécutez :

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Pour exécuter le serveur sur Windows, exécutez :

```bash
set FLASK_APP=flaskr
set FLASK_ENV=development
flask run
```

Mettre la variable `FLASK_ENV` à `development` va détecter les changements de fichiers et redémarrer le serveur automatiquement.

En mettant la variable `FLASK_APP` à `flaskr`, flask utilisera le répertoire `flaskr` et le fichier `__init__.py` pour trouver l'application.

Vous pouvez aussi exécutez

```
python app.py
```

## RÉFÉRENCE API

Démarrer

URL de base : Actuellement, cette application ne peut être exécutée que localement et n'est pas hébergée comme une URL de base. L'application backend est hébergée par défaut à l'adresse http://localhost:5000, qui est définie comme un proxy dans la configuration du frontend.

## GESTION D'ERREURS

Les erreurs sont retournées sous forme d'objets JSON au format suivant :
{
"success":False
"error": 400
"message":"Bad request
}

L'API retournera cinq types d'erreurs quand les requêtes échouent :

. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found
. 405: Method not allowed

## TERMINAISON

##### CATEGORIE

. ## GET/categories

    GENERAL:
        Cette terminaison retourne une liste d'objets Categorie, une valeur 'success', nombre total de categories.


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

    GENERAL:
        Cette terminaison retourne une liste d'objets livre, une valeur 'success', nombre total de livres.


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

```

. ## DELETE/livres (livre_id)

    GENERAL:
        Delete the book of the given ID if it exists. Return the id of the deleted plant, success value, total of plants a


        SAMPLE: curl -X DELETE http://localhost:5000/livres/10
```

         "deleted": 10,
        {
        "deleted": 10,
        "plants": [
            {
                "id": 1,
                "is_poisonous": false,
                "name": "Gnato",
                "primary_color": "Blue",
                "scientific_name": "Gnato Togo",
                "state": "TOGO"
            },
            {
                "id": 2,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 3,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 4,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 5,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 6,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 7,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 8,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 9,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            },
            {
                "id": 11,
                "is_poisonous": false,
                "name": "yébéssé",
                "primary_color": "Red",
                "scientific_name": "Pimento",
                "state": "TOGO"
            }
            ],
            "success": true,
            "totals_plants": 53
        }

````
. ##PATCH/livres(livre_id)
  GENERAL:
  This endpoint is used to update a primary_color of plant
  We return a plant which we update

  SAMPLE.....For Patch
  ``` curl -X PATCH http://localhost:5000/plants/1 -H "Content-Type:application/json" -d "{"primary_color":"yellow"}"
````

````
  {
    "id": 1,
    "primary_color": "yellow",
    "success": true
  }
  ```

. ## POST/livres

  GENERAL:
  This endpoint is used to create a new book.
  In the case of the creation of a new question:
  We return the ID of the new book created, the book that was created, the list of books and the number of books.



  SAMPLE.....For create

  curl -X POST http://localhost:5000/livres -H "Content-Type:application/json" -d "{"isbn":"","titre":"Pimento","categorie_id":false,"date_publication":"Togo",
  "auteur":"Togo","editeur="Blue"}"
````

    {
    "created": 58,
    "plants": [
        {
            "id": 1,
            "is_poisonous": false,
            "name": "Gnato",
            "primary_color": "Blue",
            "scientific_name": "Gnato Togo",
            "state": "TOGO"
        },
        {
            "id": 2,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 3,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 4,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 5,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 6,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 7,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 8,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 9,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        },
        {
            "id": 11,
            "is_poisonous": false,
            "name": "yébéssé",
            "primary_color": "Red",
            "scientific_name": "Pimento",
            "state": "TOGO"
        }
    ],
    "success": true,
    "totals_plants": 54

}

```


## Running
```

dropdb plants_database
createdb plants_database
psql plants_database_test < plants_database.sql

```

```
