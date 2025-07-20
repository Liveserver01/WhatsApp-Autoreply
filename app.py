from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "WhatsApp Auto Reply Bot is Running!"

@app.route('/', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body')
    from_number = request.form.get('From')

    response = f"आपने कहा: {incoming_msg}"
    return f"<Response><Message>{response}</Message></Response>"

if __name__ == "__main__":
    app.run()
