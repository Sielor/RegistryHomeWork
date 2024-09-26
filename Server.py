import winreg as wrg
import os
from socket import *


#lots of passed texts to check that the code works correctly multiple times
class Server:

    def __init__(self) -> None:
        #Insert checking if key is in registry


        #defining path and registry
        self.path = r"SOFTWARE\\CyberIsGood\\Ips\\"
        self.reg = wrg.HKEY_CURRENT_USER

        #creating soc and receiving client
        soc = socket()
        soc.bind(('127.0.0.1', 0))
        while(True):
            soc.listen(1)
            client, addr = soc.accept()
            self.handle_client(client, addr)
            
    #handling the received client
    def handle_client(self, client, addr):
        soft = wrg.OpenKeyEx(self.reg, self.path)
        print("passed2.0")
        try:
            value = wrg.QueryValueEx(soft, addr)
            print("passed2.1")
            wrg.SetValueEx(soft, addr, 0, wrg.REG_SZ, value + 1)
            print("passed2.2")
            client.send(("you connected to the server " + value + 1 + " times").encode())

        except:
            wrg.CreateKey(soft, addr)
            wrg.SetValueEx(soft, addr, 0, wrg.REG_SZ, 1)
            print("passed2.3")
    

    #Creating the library of CyberIsGood
    def create_library(self):       
        soft = wrg.OpenKeyEx(self.reg, r"SOFTWARE\\")
        #creating a key in the path
        wrg.CreateKey(soft, "CyberIsGood") 

        soft = wrg.OpenKeyEx(self.reg, r"SOFTWARE\\CyberIsGood\\")
        wrg.CreateKey(soft, "Server")

        soft = wrg.OpenKeyEx(self.reg, r"SOFTWARE\\CyberIsGood\\Server\\")
        wrg.CreateKey(soft, "Ips")

        #the path has been created and now we can access and read keys from the Ips
        soft = wrg.OpenKeyEx(self.reg, r"SOFTWARE\\CyberIsGood\\Ips")
        print("passed1.0")