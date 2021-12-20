import socket,sys,getpass,random
import csv
import threading

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
    with open('log_serv.txt', "a+") as txtfile:
        txtfile.write(string+'\n')

def secure_input():
    con_port=getpass.getpass(prompt = 'Введите порт: ')
    if con_port == '':
        con_port=13131
    return con_port

def try_bind(sock, c_port):
    while True:
        try:
            sock.bind(('', c_port))
            print("Подключен к порту {}".format(c_port))
            break
        except OSError as oserr:
            print("{} (порт {} занят)".format(oserr,c_port))
            c_port = random.randint(1024,65535)

def log_in(conn):
    conn.s_send("?login=?".encode())
    login = conn.s_recv(1024).decode()
    with open("users.csv", 'a+') as scvfile:
        scvfile.seek(0,0)
        reader = csv.reader(scvfile, delimiter = ';')
        for user in reader:
            
            if user and user[0] == login:
                auth(conn, user[1], login)
                return True
    return register(conn, login)

def auth(conn, passwd, login):
    conn.s_send("?password=?".encode())
    password = conn.s_recv(1024).decode()
    if password == passwd:
        conn.s_send(f'Hello {login}'.encode())
        return True
    else:
        return auth(conn, passwd, login)

def register(conn, login):
    conn.s_send("?password=?".encode())
    password = conn.s_recv(1024).decode()
    with open("users.csv", 'a') as scvfile:
        writer = csv.writer(scvfile, delimiter = ';')
        writer.writerow([login, password])
    conn.s_send(f'{login}, вы зарегестрированы!'.encode())
    return True

def messaging(sock):
    while True:
        
        msg = input()
        prnt('Отправка данных клиенту')
        conn.s_send(msg.encode())

def listening(sock):
    threading.Thread(target = messaging, args = (sock, ), daemon = True).start()
    try:
        while True:
            mas = sock.s_recv(1024).decode()
            prnt('Прием данных')
            print(mas)
    except ConnectionResetError as err:
        prnt('Клиент отключился')
        print('Клиент отключился(')
        raise
# sys.tracebacklimit = 0
prnt('Запуск сервера')
print('''При разрыве соединения сервер продолжает работать
При получении команды shutdown - завершает работу''')

c_port = 13131
sock = socket.socket()
try_bind(sock, c_port)
sock.listen(0)
prnt('Начало прослушивания порта')
while True:
    conn, addr = sock.accept()
    prnt('Подключен клиент: '+ str(addr))
    print('Подключен клиент: ', addr)
    log_in(conn)
    threading.Thread(target = listening, args = (conn, ), daemon = True).start()


prnt('Остановка сервера')

