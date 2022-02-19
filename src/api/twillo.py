import os
from twilio.rest import Client


account_sid=os.environ['TWILIO_ACCOUNT_SID']='AC50b8622e0b282f9d0eeedb756d6964c5'
auth_token=os.environ['TWILIO_AUTH_TOKEN']='d64706e96be6a76d76a86909ccbf4cae'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there',
                              from_='+19034377985',
                              to='+14049845569'
                          )

print(message.sid)

