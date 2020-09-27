from twilio.rest import Client 
 
account_sid = 123
auth_token = 123 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12082734363',  
                              body='hi test',      
                              to='+18565057494' 
                          ) 
 
print(message.sid)