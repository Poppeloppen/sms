import os
from dotenv import load_dotenv
from twilio.rest import Client


def send_sms(message):
    """ Send the provided message to my phone number
    """
    load_dotenv()
    
    account_sid = os.getenv('TWILIO_SID') 
    auth_token = os.getenv('TWILIO_AUTH_TOKEN') 

    client = Client(account_sid, auth_token)


    message = client.messages.create(
            body = message,
            from_ = os.getenv('TWILIO_PHONE_NUMBER'), 
            to = os.getenv('MY_PHONE_NUMBER') 
            )

    return


if __name__ == "__main__":
    message = input("What should text message say?: ")
    send_sms(message)


