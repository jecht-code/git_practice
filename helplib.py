#Video 6 using helper libraries / sdk
#YT - https://www.youtube.com/watch?v=GZvSYJDk-us&list=WL&index=17&t=339s&ab_channel=freeCodeCamp.org
from twilio.rest import Client

account_sid = 123
auth_token = 14
client = Client(account_sid, auth_token)

for msg in client.messages.list():
   print(msg.body)

# for msg in client.messages.list():
#    print(f"Deleting {msg.body}")
#    msg.delete()

msg = client.messages.create(
    to="+18565057494",
    from_="+12082734363",
    body="Hello from VS studio in python"
)
print(f"Created a new messages: {msg.sid}")