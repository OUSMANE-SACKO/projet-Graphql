from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from config import Config
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB globally
mongo = PyMongo(app)

# Attach MongoDB instance to the models
from app.models.user_models import User
from app.models.mangas_models import Manga, Chapter, Genre, Collection

User.mongo = mongo
Manga.mongo = mongo
Chapter.mongo = mongo
Genre.mongo = mongo
Collection.mongo = mongo

# Enable JWT
jwt = JWTManager(app)

# Enable CORS
CORS(app)

# Register blueprints
from app.routes.user_routes import user_bp
from app.routes.mangas_routes import manga_bp
from app.routes.graphql_routes import graphql_bp

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(manga_bp, url_prefix="/manga")
app.register_blueprint(graphql_bp, url_prefix="")

@app.route("/")
def home():
    return {"message": "Welcome to the Manga Backend API!"}

if __name__ == "__main__":
    app.run(debug=True)
