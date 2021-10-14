from os import read
from flask import Flask, request
import flask

from main import insertAccount

app = Flask("Youtube")

@app.route("/authentication", methods=["POST", "PUT"])
def cadastraUserPassword():
    if flask.request.method == 'PUT':
        body = request.get_json()
        arquivo = open('database.txt', 'r')
        read = arquivo.readlines()
        for element in read:
            if body["user"] == element.split()[0]:
                return "Esse Usuario já existe"
        account = insertAccount(body["user"], body["password"])
        return f"Sua conta foi criada com sucesso: {account}"
    if flask.request.method == 'POST':
        arquivo = open('database.txt', 'r')
        read = arquivo.readlines()
        body = request.get_json()
        for element in read:
            if body["user"] == element.split()[0] and body["password"] == element.split()[1]:
                return "SIM"
        return "NAO"
app.run()
