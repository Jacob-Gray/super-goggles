import ChatExchange.chatexchange.client
import ChatExchange.chatexchange.events

rooms = {}

def join(client, room_id, listen):
  room = client.get_room(room_id)
  room.join()
  room.watch(listen)
  rooms[room_id] = room
  return room

def leave(room_id):
    rooms[room_id].leave(room_id)
    del rooms[room_id]
    
