#!/usr/bin/env python
# coding: utf-8

# In[4]:


import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('188.94.33.38', 9090))

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())


# In[ ]:




