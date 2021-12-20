import socket
import getpass
import threading
from time import sleep

def s_send(sock, data):
    data = data.decode()
    data = bytearray(f'{len(data)}=len{data}'.encode())
    sock.send(data)

def s_recv(sock, vol):
    data = sock.recv(vol)
    length, data = data.split(b'=len', 1)
    return data

socket.socket.s_send = s_send
socket.socket.s_recv = s_recv


def prnt(string):
    with open('log_cli.txt', "a+") as txtfile:
        txtfile.write(string+'\n')

def secure_input():
    ip_addr= getpass.getpass(prompt = 'Введите IP address: ')
    if ip_addr == '':
        ip_addr = 'localhost'
    con_port=getpass.getpass(prompt = 'Введите порт: ')
    if con_port == '':
        con_port=13131
    return ip_addr, con_port

def log_in(sock):
    while True:
        data = sock.s_recv(1024).decode()
        if ('?password=?' in data):
            msg = input('Введите (придумайте) пароль: ')
            sock.s_send(msg.encode())
        elif "?login=?" in data:
            msg = input('Введите (придумайте) имя пользователя: ')
            sock.s_send(msg.encode())
        else:
            print(data)
            break

def listening(sock):
    while True:
        prnt('Прием данных от сервера')
        mas = sock.s_recv(1024).decode()
        print(mas)

ip_addr,con_port='localhost',13131
sock = socket.socket()
sock.setblocking(True)
sock.connect((ip_addr, con_port))
log_in(sock)
threading.Thread(target = listening, args = (sock, ), daemon = True).start()
while True:
    msg = input()
    if msg == 'exit':
        break
    prnt('Попытка отправить данные серверу:')
    sock.s_send(msg.encode())
    prnt('Успешно отправлено')

prnt('Разрыв соединения с сервером')
sock.close()