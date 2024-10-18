from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)

"""
JWTManager : pour initialiser le système JWT dans notre application.
create_access_token : pour générer un jeton lorsque l’utilisateur se connecte.
jwt_required : pour protéger les routes.
get_jwt_identity : obtenir l’identité de l’utilisateur à partir du jeton JWT.
"""

# Initialise une instance de Flask qui sera notre application
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "secret_key"  # Définis une clé secrète pour signer les JWT
jwt = JWTManager(app)  # Initialise JWTManager avec notre application Flask


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Ajout de la route racine
@app.route("/")
def home():
    """Message de bienvenue."""
    return "Welcome to the Flask API!"  # Retourne un message de bienvenue


@auth.verify_password
def verify_password(username, password):
    """Vérifie si le mot de passe correspond."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username  # Retourne le nom d'utilisateur si tout est correct
    return None


@app.route("/basic-protected", methods=['GET'])
@auth.login_required  # Cette route nécessite une authentification pour être accessible
def basic_protected():
    """Retourne un message si l'authentification basique est réussie."""
    return "Basic Auth: Access Granted"  # On retourne un message si l'authentification est réussie


@app.route("/login", methods=["POST"])
def login():
    """
    Authentifie l'utilisateur et retourne un JWT si c'est réussi.
    """
    # Récupère les données envoyées dans la requête (JSON contenant 'username' et 'password')
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Ajout de la validation pour vérifier si username ou password sont absents
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    # On vérifie si l'utilisateur existe et si le mot de passe est correct
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Si l'utilisateur est authentifié, on crée un jeton JWT pour lui
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200  # Retourne le jeton JWT dans la réponse
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()  # Cette route nécessite un jeton JWT valide pour être accessible
def jwt_protected():
    """Retourne un message si l'authentification JWT est réussie."""
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur à partir du jeton JWT
    return f"JWT Auth: Access Granted for {current_user}"


@app.route("/admin-only", methods=['GET'])
@jwt_required()  # La route est protégée par JWT
def admin_only():
    """
    Retourne un message si l'utilisateur actuel est un administrateur.
    """
    current_user = get_jwt_identity()  # Récupère l'identité de l'utilisateur à partir du jeton JWT

    if current_user not in users:
        return jsonify({"error": "User not found"}), 404  # Retourne une erreur si l'utilisateur n'existe pas

    # Vérifie si l'utilisateur a un rôle d'administrateur
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403  # Retourne une erreur si l'accès admin est requis

    return "Admin Access: Granted"


# Gestion des erreurs pour JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère les tentatives d'accès non autorisées."""
    return jsonify({
        "error": "Missing or invalid token", "description": str(err)
    }), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère les erreurs de jeton invalide."""
    return jsonify({
        "error": "Invalid token", "description": str(err)
    }), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gère les erreurs de jeton expiré."""
    return jsonify({
        "error": "Token has expired", "description": str(err)
    }), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gère les erreurs de jeton révoqué."""
    return jsonify({
        "error": "Token has been revoked", "description": str(err)
    }), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gère les cas où un jeton frais est requis."""
    return jsonify({
        "error": "Fresh token required", "description": str(err)
    }), 401


if __name__ == '__main__':
    app.run()
