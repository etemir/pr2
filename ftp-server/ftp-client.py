import socket
import re
import os

TOAST = 'localhost'
TORT = 20039
HU = b"HU&#"
FFL = b'FLD$$&'
login = input("Введите логин: ")
password = input("Введите пароль: ")
crnt_dir = "\\"



def gett(rqst):
    global sock, FFL, HU
    
    getFlg = sock.recv(1024)
    if FFL in getFlg:
        print((getFlg.replace(FFL, b"")).decode())
    else:
        fln = re.split("[ \\/]+", rqst)[-1]
        with open (fln, "wb") as bytefile:
            while True:
                if HU in getFlg:
                    getFlg, endf = getFlg.split(HU)
                    bytefile.write(getFlg.replace(HU, b""))
                    break
                else:
                    bytefile.write(getFlg)
                    getFlg = sock.recv(1024)
    

def goto(rqst):
    global sock, HU
    fln = re.split("[ \\/]+", rqst)[-1]
    if os.path.exists(fln):
        size = os.path.getsize(fln)
        sock.send(render(rqst, size))
        en_flg = sock.recv(1024).decode()
        if en_flg != 'en&$':
            print(en_flg)
            return
        with open(fln, "rb") as bytefile:
    
            while read_bytes := bytefile.read(1024):
                sock.send(read_bytes)
        sock.send(HU)
    else:
        print("Файл несуществует")
    print(sock.recv(1024).decode())


def render(message, size=0):
    global login, password, crnt_dir
    return f"{login}=login{password}=password{crnt_dir}=cur_dir{size}=file_size{message}".encode()

print('Введите help для справки по командам')
while True:
    rqst = input(crnt_dir+'$: ')
    rqst = rqst.strip()
    if rqst == "exit":
        break
    sock = socket.socket()
    sock.connect((TOAST, TORT))
    if rqst[:9] == "send":
        if rqst == "send":
            print("Файл несуществует")
        else:
            goto(rqst)
    else:
        sock.send(render(rqst))
        if rqst[:9] == "get " or rqst == "get":
            gett(rqst)
        else:
            rspns = sock.recv(1024).decode()
            # print("recieved:", rspns)
            if rqst[:3] == "cd " or rqst == "cd":
                crnt_dir = rspns
            else:
                print(rspns)
    
    sock.close()