
from threading import Thread
import Request
class NewConnect(Thread):
    def __init__(self,clientAddress,clientsocket):
        Thread.__init__(self)
        self.socket = clientsocket
        self.address = clientAddress
    def run(self):
        print ("Connection from : ", self.address)
        data = "Chào bạn"
        self.socket.sendall(data.encode("utf-8"))
        while True:
            data = self.socket.recv(1024).decode('utf-8')
            print(data)
            if data == "bye":
                break
            data=Request.Request.GetApi(self,data)
            print(data)
            name=data['content']
            img=data['img']
            toUser= str(name)+str("\n ")+str(img)
            self.socket.sendall(toUser.encode('utf-8'))
            
            