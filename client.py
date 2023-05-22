from socket import *
from constCS import *
import pickle

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

op = ('add', (10, 20))
s.send(pickle.dumps(op))
data = s.recv(1024)
print(pickle.loads(data))

s.close()
