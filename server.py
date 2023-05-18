from socket  import *
from constCS import * #-
import pickle

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  msg = conn.recv(1024)   # receive data from client
  if not msg: break       # stop if client stopped
  data = pickle.loads(msg)
  print(data)
  if data[0] == 'add':
    result = data[1][0] + data[1][1]
  elif data[0] == 'subtract':
    result = data[1][0] - data[1][1]
  conn.send(pickle.dumps(result)) # return sent data plus an "*"
conn.close()               # close the connection
