from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC30f6fe6eb0d1d674d103005bc1ff37b3"
auth_token  = "2eb491fe7086e79e7ec3829e346ad029"
client = TwilioRestClient(account_sid, auth_token)

while(True):
    from_number = request.values.get('From', None)
    message = "thanks for the message!"
    resp = twilio.twiml.Response()
    resp.message(message)

client.sms.messages.create(body=returnmsg,
    to="+13473419085",    # Replace with your phone number
    from_="+19787056029") # Replace with your Twilio number
