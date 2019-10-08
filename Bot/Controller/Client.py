import os, sys
lib_path = os.path.abspath(os.path.join('Const'))
sys.path.append(lib_path)
from Const import consts
import socket            
def Init():
    sk = socket.socket()       
    sk.connect((consts.Const.host, consts.Const.post))
    data=sk.recv(1024)
    print (data.decode('utf-8'))
    while True:      
        ques= input()
        sk.sendall(ques.encode('utf-8'))
        print(sk.recv(1024).decode('utf-8'))
if __name__=="__main__":
    Init()