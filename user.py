import ChatExchange.chatexchange.client

#Login
def user(host, email, password):
  client = ChatExchange.chatexchange.client.Client(host)
  client.login(email, password)
  return client
