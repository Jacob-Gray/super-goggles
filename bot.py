import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events

rooms = {}

def join(client, room_id, listen):
  if room_id not in rooms:
    room = client.get_room(room_id)
    room.join()
    room.watch(listen)
    rooms[room_id] = room
    return room
  else:
    return 0

def leave(room_id):
  rooms[room_id].leave()
  del rooms[room_id]
    
