from flask import Flask, request

from main import insertAccount

app = Flask("Youtube")

@app.route("/cadastro", methods=["POST"])
def cadastraUserPassword():
    body = request.get_json()
    account = insertAccount(body["user"], body["password"])
    return account
app.run()
