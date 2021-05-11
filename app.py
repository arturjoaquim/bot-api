from flask import Flask, json, Response
from bot import chatbot

app = Flask(__name__)


@app.route('/bot/<string:message>', methods=['GET'])
def get_bot_response(message):
    bot_response = chatbot.get_response(message)
    if bot_response:
        data = {'Response': f'{bot_response}'}
        json_response = json.dumps(data, ensure_ascii=False)
        response = Response(json_response, content_type="application/json;charset=utf-8")
        return response, 200
    else:
        return 'O contéudo não foi encontrado.', 204


app.run(debug=True)
