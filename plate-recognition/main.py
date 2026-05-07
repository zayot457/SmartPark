from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required
)

from image_processing import process_image

app = Flask(__name__)

# Chave JWT
app.config["JWT_SECRET_KEY"] = "parkguard-secret-key"

jwt = JWTManager(app)


# Rota inicial
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "Microserviço ParkGuard funcionando",
        "rotas": [
            "POST /login",
            "POST /detect"
        ]
    })


# Login para gerar token
@app.route("/login", methods=["POST"])
def login():

    access_token = create_access_token(
        identity="parkguard-user"
    )

    return jsonify({
        "access_token": access_token
    })


# Detectar placa
@app.route("/detect", methods=["POST"])
@jwt_required()
def detect():

    if "image" not in request.files:
        return jsonify({
            "error": "Nenhuma imagem enviada"
        }), 400

    file = request.files["image"]

    plate = process_image(file)

    if plate is None:
        return jsonify({
            "error": "Imagem inválida"
        }), 400

    return jsonify({
        "placa": plate
    })


# Iniciar servidor
if __name__ == "__main__":
    app.run(port=5000, debug=True)