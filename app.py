from flask import Flask, json, Response
from bot import chatbot

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1 style="text-align: center">Bem vindo à minha API</h1>', 200


@app.route('/get_response/<string:msg>')
def get_response(msg):
    response_bot = chatbot.get_response(msg)
    data = {'Response': f'{response_bot}'}
    json_response = json.dumps(data, ensure_ascii=False)
    response = Response(json_response, content_type="application/json;charset=utf-8")
    return response, 200


app.run(debug=True)
