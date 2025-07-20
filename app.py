from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    user_msg = request.form.get('Body').lower()
    response = MessagingResponse()

    if "menu" in user_msg:
        response.message(
            "📋 *Main Menu*:\n"
            "1. 📄 PDF\n"
            "2. 🖼️ Image\n"
            "3. ❓ Help\n\n"
            "कृपया 1, 2 या 3 भेजें।"
        )

    elif user_msg == "1" or "pdf" in user_msg:
        msg = response.message("✅ ये रहा आपका PDF:")
        msg.media("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")

    elif user_msg == "2" or "image" in user_msg:
        msg = response.message("🖼️ यह रही एक इमेज:")
        msg.media("https://www.w3schools.com/w3images/lights.jpg")

    elif user_msg == "3" or "help" in user_msg:
        response.message("ℹ️ सहायता के लिए हमारा YouTube चैनल देखें या 'menu' टाइप करें।")

    else:
        response.message("🙏 कृपया 'menu' टाइप करें विकल्प देखने के लिए।")

    return str(response)

if __name__ == "__main__":
    app.run()
