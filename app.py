from flask import Flask, json, Response
from bot import chatbot

app = Flask(__name__)


@app.route('/response/<string:msg>', methods=['GET'])
def get_response(msg):
    response_bot = chatbot.get_response(msg)
    if response_bot:
        data = {'Response': f'{response_bot}'}
        json_response = json.dumps(data, ensure_ascii=False)
        response = Response(json_response, content_type="application/json;charset=utf-8")
        return response, 200
    else:
        return 'O contéudo não foi encontrado.', 204


app.run(debug=True)
