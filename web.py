from flask import Flask, jsonify, request
from frasa import deteksi
import json

app = Flask(__name__)

@app.route('/')
def start():
    return 'Python'

@app.route('/gender')
def gender():
    nama = request.args.get('nama')
    if nama is None or nama == '':
        return jsonify(message="Parameter 'nama' tidak ditemukan.")
    else:
        return json.loads(deteksi.gender(nama).json())

app.run()