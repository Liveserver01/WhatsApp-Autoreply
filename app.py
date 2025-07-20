from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply():
    msg = request.form.get('Body')
    sender = request.form.get('From')

    reply = MessagingResponse()
    reply.message(f"आपका मैसेज मिला: {msg}\nधन्यवाद! ✅")
    return str(reply)

if __name__ == "__main__":
    app.run()

