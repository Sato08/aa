import os, sys
lib_path = os.path.abspath(os.path.join('Const'))
sys.path.append(lib_path)
from Const import consts
import socket  
import NewConnect
def Init():
    sever = socket.socket() 
    sever.bind((consts.Const.host, consts.Const.post))        # Bind to the port vừa khởi tạo
    print('Server is running....')
    while True:
       sever.listen(5)
       client, addr = sever.accept() 
       thread= NewConnect.NewConnect(addr,client)
       thread.start()
       
if __name__=="__main__":
    Init()
