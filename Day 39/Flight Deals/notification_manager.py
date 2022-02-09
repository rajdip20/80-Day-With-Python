from twilio.rest import Client

TWILIO_SID = "Your Twilio Account SID"
TWILIO_AUTH_TOKEN = "Your Twilio AUTH Token"
TWILIO_VIRTUAL_NUMBER = "Your Twilio Virtual Number"
TWILIO_VERIFIED_NUMBER = "Your Twilio Verified Number"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
