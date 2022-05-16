from flask import Flask, abort, jsonify, request
from sqlalchemy import null
from Models import Livre, Categorie, setup_db
from flask_cors import CORS, cross_origin

app = Flask(__name__)
setup_db(app)
CORS(app)

#CORS(app, ressorces={r"/api/*":{"origins" : "*"}})
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
    try:
        categories = Categorie.query.order_by(Categorie.id).all()
        categorie_format = [categorie.format() for categorie in categories]
        if categories is None:
            abort(404)
        return jsonify({
            'success': True,
            'categories': categorie_format,
            'nombre_categories': len(categories)
        })
    except:
        abort(400)

##################################
# Récupérer une catégorie
##################################
@app.route('/categories/<int:id>', methods=['GET'])
def get_categorie(id):
    try:
        categorie = Categorie.query.get(id)
        if categorie is None: 
            abort(404)
        else:
            return jsonify ({
                'success' : True,
                'categorie': categorie.format()
            })
    except:
        abort(400)

##################################
# Ajouter une categorie
##################################
@app.route('/categories', methods=['POST'])
def add_categorie():
    
    body = request.get_json()
    try:
        new_name = body.get("name")
        new_description = body.get("description")


        categorie = Categorie(name=new_name,description=new_description)
        categorie.insert()
        return jsonify({
            "success" : True,
            "categorie_id" : categorie.id,
            "total_categories" : [categorie.format() for categorie in Categorie.query.all()]
        })
    except :
        abort(400)

##################################
# Modifier une categorie
##################################
@app.route('/categories/<int:id>',methods=['PATCH'])
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
            'supprimer ': categorie.id,
            'nombre_categories':len(Categorie.query.all())
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
    try:
        livres = Livre.query.order_by(Livre.id).all()
        livre_format = [livre.format() for livre in livres]
        return jsonify({
            'success': True,
            'livres': livre_format,
            'nombre_livres': len(livres)
        })
    except:
        abort(400)

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
    
    try:
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
            "total_livres" : [livre.format() for livre in Livre.query.all()]
        })
    except:
        abort(400)

##################################
# Modifier un livre
##################################
@app.route('/livres/<int:id>',methods=['PATCH'])
def update_livre(id):
    body = request.get_json()
    try:
        livre=Livre.query.get(id)
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
            'supprimer ': livre.id,
            'total_livres':len(Livre.query.all())
        })
    except:
      abort(422) #Unprocessable Entity


##################################
# LISTE DES LIVRES PAR CATEGORIE
##################################

@app.route('/livres/categorie/<int:id>', methods=['GET'])
def get_livresinid(id):
    try:
        categorie = Categorie.query.get(id) 
        livres = Livre.query.filter_by(categorie_id = categorie.id).all()
        livre_format = [livre.format() for livre in livres]
        return jsonify({
            'success': True,
            'livres': livre_format,
            'nombre_livres': len(livres)
        })
    except:
        abort(400)
    
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

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        'success' : False,
        'error' : 500,
        'message': "Internal Server Error",
    }), 500
    
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