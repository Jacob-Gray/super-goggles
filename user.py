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
    
#sets user as privileged
def removePrivileged(user_id, room_id, host_id):
  
  priv_users = shelve.open("privileged_users.db")
  
  if (host_id + room_id) not in priv_users:
    priv_users[host_id + room_id] = []
    
  if user_id in priv_users[host_id + room_id]:
    i = priv_users[host_id + room_id].index(user_id)
    print "-------"
    print "REMOVED USER " + priv_users[host_id + room_id][i]
    print priv_users[host_id + room_id].pop(i)
    print "__________"
    print "Users "+str(priv_users[host_id + room_id])
    print "INDEX: "+str(i)
    priv_users.close()
    return 0
    
  else:
    priv_users.close()
    return 1
    
def getPriv(host_id, room_id):
  out = ""
  priv_users = shelve.open("privileged_users.db")
  for x in priv_users[host_id + room_id]:
    out +=" [`#"+x+"`](http://"+host_id+"/users/"+x+"),"
  out = out[:-1]
  return out

