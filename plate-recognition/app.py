# SmartPark OCR
# Autor: Cristiano Junior
# TCC 2026

from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

# Base simulada de veículos
VEICULOS = {
    "LQI2H93": {
        "fabricante": "BMW",
        "modelo": "320i",
        "cor": "Preto"
    },

    "POX4G21": {
        "fabricante": "Volkswagen",
        "modelo": "Gol",
        "cor": "Branco"
    },

    "LLW9116": {
        "fabricante": "Honda",
        "modelo": "Fit",
        "cor": "Cinza"
    },

    "DIC6B71": {
        "fabricante": "Toyota",
        "modelo": "Corolla",
        "cor": "Prata"
    },

    "FJQ4F96": {
        "fabricante": "Volkswagen",
        "modelo": "Fox",
        "cor": "Branco"
    },

    "QWE2R45": {
        "fabricante": "Volkswagen",
        "modelo": "Voyage",
        "cor": "Prata"
    }
}


# Função OCR simulada pelo nome do arquivo
def reconhecer_placa(nome_arquivo):
    nome = nome_arquivo.lower()

    if "bmw" in nome:
        return "LQI2H93"

    if "gol" in nome:
        return "POX4G21"

    if "fit" in nome:
        return "LLW9116"

    if "corolla" in nome:
        return "DIC6B71"

    if "fox" in nome:
        return "FJQ4F96"

    if "voyage" in nome:
        return "QWE2R45"

    return "Não identificada"


@app.route("/")
def home():
    return jsonify({
        "status": "SmartPark OCR funcionando"
    })


@app.route("/read-plate", methods=["POST"])
def read_plate():
    if "image" not in request.files:
        return jsonify({
            "error": "Nenhuma imagem enviada"
        }), 400

    file = request.files["image"]

    npimg = np.frombuffer(file.read(), np.uint8)

    img = cv2.imdecode(
        npimg,
        cv2.IMREAD_COLOR
    )

    if img is None:
        return jsonify({
            "error": "Imagem inválida"
        }), 400

    placa = reconhecer_placa(file.filename)

    dados = VEICULOS.get(placa, {
        "fabricante": "Não identificado",
        "modelo": "Não identificado",
        "cor": "Não identificado"
    })

    return jsonify({
        "placa": placa,
        "fabricante": dados["fabricante"],
        "modelo": dados["modelo"],
        "cor": dados["cor"]
    })


if __name__ == "__main__":
    print("Servidor SmartPark iniciado")

    app.run(
        port=5000,
        debug=True
    )