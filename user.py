import ChatExchange.chatexchange.client
import json

#Login
def user(host, email, password):
  client = ChatExchange.chatexchange.client.Client(host)
  client.login(email, password)
  return client
  
#check if user is privileged
def privileged(user_id){
  priv_users = open('privileged.json',"r")
  users = json.load(priv_users)
  if users[user_id]:
    return True
  else:
    return False
    
#sets user as privileged
def setPrivileged(user_id):
  priv_users = open('privileged.json',"w")
  users = json.load(priv_users)
  users[user_id] = True
  priv_users.write(json.dumps(users))
