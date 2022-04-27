import os
from flask import Flask, abort, jsonify, request
from Models import Livre, Categorie, setup_db


app = Flask(__name__)
setup_db(app)

# Route test
@app.route('/', methods=['GET'])
def index():
    return 'hello'


    #######################################################################################################
    #                                                                                                     #
    #                                                                                                     #
    #                                             CATEGORIE                                               #
    #                                                                                                     #
    #                                                                                                     #      
    #######################################################################################################

##################################
# Récupérer toutes les catégories
##################################
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Categorie.query.order_by(Categorie.id).all()
    categorie_format = [categorie.format() for categorie in categories]
    if categories is None:
        abort(404)
    return jsonify({
        'success': True,
        'categories': categorie_format,
        'nombre_categories': len(categories)
    })

##################################
# Récupérer une catégorie
##################################
@app.route('/categories/<int:id>', methods=['GET'])
def get_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None: 
        abort(404)
    else:
        return jsonify ({
            'success' : True,
            'categories': categorie.format()
        })

##################################
# Ajouter une categorie
##################################
@app.route('/categories', methods=['POST'])
def add_categorie():
    body = request.get_json()

    new_name = body.get("name")
    new_description = body.get("description")
    
    existe_categorie = Categorie.query.filter_by(new_name)
    if existe_categorie is not None:
       abort(400)
    categorie = Categorie(name=new_name,description=new_description)
    categorie.insert()
    return jsonify({
        "success" : True,
        "categorie_id" : categorie.id,
        "liste_categories" : [Categorie.format() for categorie in Categorie.query.all()]
    })

##################################
# Modifier une categorie
##################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def update_categorie(id):
    body = request.get_json()
    try:
        categorie = Categorie.query.get(id)
        if categorie is None:
            abort(404)
        categorie.name = body.get("name")
        categorie.description = body.get("description")
        
        categorie.update()
        return jsonify({
            'success':True,
            'categorie_id':categorie.id
        })
    except:
      abort(400) # Bad request. The user send request that server could not be understand

##################################
# Supprimer une categorie 
##################################
@app.route('/categories/<int:id>',methods=['DELETE'])
def delete_categorie(id):
    try:
        categorie= Categorie.query.get(id)
        if categorie is None:
            abort(404)
        categorie.delete()
        return jsonify({
            'success':True,
            'categorie_supprimé ': categorie.id,
            'total_categorie':len(Categorie.query.all())
        })
    except:
      abort(422) #Unprocessable Entity


    #######################################################################################################
    #                                                                                                     #
    #                                                                                                     #
    #                                               LIVRE                                                 #
    #                                                                                                     #
    #                                                                                                     #      
    #######################################################################################################

##################################
# Récupérer tous les livres
##################################
@app.route('/livres', methods=['GET'])
def get_livres():
    livres = Livre.query.order_by(Livre.id).all()
    livre_format = [livre.format() for livre in livres]
    return jsonify({
        'success': True,
        'livres': livre_format,
        'nombre_livres': len(livres)
    })

##################################
# Récupérer un livre
##################################
@app.route('/livres/<int:id>', methods=['GET'])
def get_livre(id):
    livre = Livre.query.get(id)
    if livre is None: 
        abort(404)
    else:
        return jsonify ({
            'success' : True,
            'livres': livre.format(),
        })

##################################
# Ajouter un livre
##################################
@app.route('/livres', methods=['POST'])
def add_livre():
    body = request.get_json()

    new_isbn = body.get("isbn")
    new_titre = body.get("titre")
    new_categorie_id = body.get("categorie_id")
    new_date_publication = body.get("date_publication")
    new_auteur = body.get("auteur")
    new_editeur = body.get("editeur")

    categorie = Categorie.query.get(new_categorie_id) # on vérifie si la catégorie existe
    if categorie is None:
       abort(404)
    livre = Livre(isbn=new_isbn,titre=new_titre,categorie_id=new_categorie_id,date_publication=new_date_publication,auteur=new_auteur,editeur=new_editeur)
    livre.insert()
    return jsonify({
        "success" : True,
        "livre_id" : livre.id,
        "liste_livre" : [livre.format() for livre in Livre.query.all()]
    })

##################################
# Modifier un livre
##################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def update_livre(id):
    body = request.get_json()
    try:
        livre=livre.query.get(id)
        if livre is None:
            abort(404)
        livre.isbn = body.get("isbn")
        livre.titre = body.get("titre")
        livre.categorie_id = body.get("categorie_id")
        livre.date_publcation = body.get("date_publcation")
        livre.auteur = body.get("auteur")
        livre.editeur = body.get("editeur")

        categorie = Categorie.query.get(body.get("categorie_id"))
        if categorie is None:
            abort(404)
        livre.update()
        return jsonify({
            'success':True,
            'id':livre.id
        })
    except:
      abort(400) # Bad request. L'utilisateur a envoyé une requête que le serveur ne peut pas comprendre The user send request that server could not be understand

##################################
# Supprimer un livre
##################################
@app.route('/livres/<int:id>',methods=['DELETE'])
def delete_livre(id):
    try:
        livre= Livre.query.get(id)
        if livre is None:
            abort(404)
        livre.delete()
        return jsonify({
            'success':True,
            'Livre_supprimé ': livre.id,
            'total_livre':len(Livre.query.all())
        })
    except:
      abort(422) #Unprocessable Entity



    #######################################################################################################
    #                                                                                                     #
    #                                                                                                     #
    #                                       GESTION DES ERREURS                                           #
    #                                                                                                     #
    #                                                                                                     #      
    #######################################################################################################


@app.errorhandler(404)
#ici on fait un get et la ressource n'existe pas http://localhost:5000?page=100
def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
      'success':False,
      "error":422,
      "message":"unprocessable"
    }),422
  
@app.errorhandler(400)
#Curl -X PATCH http://localhost:5000/books/1000 -H "Content-Type:application/json" -d "{\"rating\": \"2\"}"
def error_client(error):
    return jsonify({
      'success':False,
      "error":400,
      "message":"Bad request"
    }),400

@app.errorhandler(405)
#ici on veut envoyer un post sur une route qui donne des erreurs POST /books/6... On ne peut pas faire de post sur cette route....
def error_badRequest(error):
    return jsonify({
        'success':False,
        "error":405,
        "message":"Method not allowed"
    }),405



if __name__ == "__main__":
    app.run(debug=True)


