import shelve

groups = shelve.open("sg_groups.db")

#Create new groups
def create(group, room, host):
  
  #Adds host if it doesn't exist
  if host not in groups:
    groups[host] = []
    
  #Adds room if it doesn't exist
  if room not in groups[host]:
    groups[host][room] = []
  
  #Adds group if it doesn't exists, and return completion:
  #True means the group didn't exist, and was added
  #False means the group already existed, so no changes were made
  if group not in groups[host][room]:
    groups[host][room][group] = []
    return True
  else:
    return False
  
def remove(group, room, host):

  
  
def exists(group, room, host):
  
