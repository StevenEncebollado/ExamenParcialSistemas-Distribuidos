from flask import Flask, jsonify
from pymongo import MongoClient
import os
import socket

app = Flask(__name__)

# Conexión a MongoDB
def get_db_connection():
    client = MongoClient('mongodb://mongo1:27017/', serverSelectionTimeoutMS=5000)
    return client.test_database

@app.route('/')
def hello():
    return "Aplicación Escalable con MongoDB!"

@app.route('/status')
def status():
    try:
        db = get_db_connection()
        db.command('ping')
        return jsonify({"status": "Conectado a MongoDB", "instance": socket.gethostname()})
    except Exception as e:
        return jsonify({"status": "Error", "message": str(e), "instance": socket.gethostname()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)