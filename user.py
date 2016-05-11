import ChatExchange.chatexchange.client

#Login
def user(host,email,p):
  client = ChatExchange.chatexchange.client.Client(host)
  client.login(email, password)
  return client
