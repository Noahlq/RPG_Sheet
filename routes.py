from os import read
from flask import Flask, request
import flask

from main import insertAccount

app = Flask("Youtube")

@app.route("/authentication", methods=["POST", "PUT"])
def cadastraUserPassword():
    if flask.request.method == 'PUT':
        body = request.get_json()
        account = insertAccount(body["user"], body["password"])
        return account
    if flask.request.method == 'POST':
        arquivo = open('database.txt', 'r')
        read = arquivo.readlines()
        body = request.get_json()
        for element in read:
            if body["user"] == element.split()[1] and body["password"] == element.split()[0]:
                return "SIM"
        return "NAO"
app.run()
