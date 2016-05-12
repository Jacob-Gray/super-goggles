import ChatExchange.chatexchange.client
import json
import shelve

#Login
def user(host, email, password):
  client = ChatExchange.chatexchange.client.Client(host)
  client.login(email, password)
  return client
  
#check if user is privileged
def privileged(user_id, room_id, host_id):
  
  priv_users = shelve.open("privileged_users.db")
  
  if user_id in priv_users[host_id + room_id]:
    priv_users.close()
    return True
    
  else:
    priv_users.close()
    return False
    
#sets user as privileged
def setPrivileged(user_id, room_id, host_id):
  
  priv_users = shelve.open("privileged_users.db")
  
  if (host_id + room_id) not in priv_users:
    priv_users[host_id + room_id] = []
    
  if user_id in priv_users[host_id + room_id]:
    priv_users.close()
    return 1
    
  else:
    priv_users[host_id + room_id] += [user_id]
    priv_users.close()
    return 0
    

