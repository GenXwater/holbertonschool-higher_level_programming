#!/usr/bin/python3
"""Flask put more words"""


from flask import request
from flask import Flask, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from functools import wraps
"""
JWTManager : pour initialiser le système JWT dans notre application.
create_access_token : pour générer un jeton lorsque l’utilisateur se connecte.
jwt_required : pour protéger les routes.
get_jwt_identity : obtenir l’identité de l’utilisateur à partir du jetonJWT
"""

"""initialise une instance de Flask qui sera notre application"""
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'bite_de_cheval'
# Définis une clé secrète pour signer les JWT. Change 'your-secret-key'
# par une clé sécurisée

jwt = JWTManager(app)  # Initialise JWTManager avec notre application Flask


users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password  # vérif si un nom d'utilisateur et un mdp sont valides
def verify_password(username, password):
    user = users.get(username)
    """Vérifie si le mot de passe correspond"""
    if user and check_password_hash(user['password'], password):
        return username  # Retourne le nom d'utilisateur si tout est correct
    return None


@app.route('/basic-protected')
# Décorateur qui exige une authentification pour accéder à cette route
@auth.login_required
def basic_protected():
    # On retourne un message JSON si l'authentification est réussie
    return jsonify(message="Basic Auth: Access Granted")


@app.route('/login', methods=['POST'])
def login():
    # Récupère données envoyées dans requête
    # (JSON contenant 'username' et 'password')
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # On vérifie si l'utilisateur existe et si le mot de passe est correct.
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"msg": "Invalid username or password"}), 401

    # Si l'utilisateur est authentifié, on crée un jeton JWT pour lui
    access_token = create_access_token(identity=username)
    # Retourne le jeton JWT dans la réponse
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected')
@jwt_required()  # Cette route nécessite 1 jetonJWT valide pour être accessible
def jwt_protected():
    # Récupère l'identité de l'utilisateur à partir du jeton JWT
    current_user = get_jwt_identity()
    return jsonify(message=f"JWT Auth: Access Granted for {current_user}"), 200


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # Récupère l'identité de l'utilisateur à partir du token JWT
        current_user = get_jwt_identity()
        user = users.get(current_user)
        # Vérifie si l'utilisateur est un admin
        if user and user['role'] == 'admin':
            return fn(*args, **kwargs)
        # Retourne une erreur 403 si l'utilisateur n'est pas un admin
        return jsonify({"error": "Admin access required"}), 403
    return wrapper


@app.route('/admin-only')
@jwt_required()  # La route est protégée par JWT
# La route est protégée par le contrôle d'accès basé sur les rôles
@admin_required
def admin_only():
    # Retourne un message si l'accès est accordé
    return jsonify(message="Admin Access: Granted")


if __name__ == '__main__':
    app.run(debug=True)
