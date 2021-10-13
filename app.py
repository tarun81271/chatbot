from flask import Flask, request, jsonify, render_template

import dialogflow
import requests
import json
import pusher
from flask_ngrok import run_with_ngrok
from flask_cors import cross_origin
import os




app = Flask(__name__)
#run_with_ngrok(app)

credential_path = "tarun-chatbot-mxtq-3e59c692db1f.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        return response.query_result.fulfillment_text



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    data = request.get_json(silent=True)
    return{
        'fulfillmentText': 'Hello from the other side.'
    }
        
@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
    response_text = { "message":  fulfillment_text }
    return jsonify(response_text)

# run Flask app
if __name__ == "__main__":
    app.run(debug=True)
