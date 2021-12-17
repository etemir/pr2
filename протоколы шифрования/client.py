import socket, random, threading, csv




class Client(object):
    def __init__(self, port = 3109):
        self.port = port


    def encrypt(self, k, m):
        return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

    def decrypt(self, k, c):
        return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

    def sock_connect(self):
        self.sock = socket.socket()
        self.sock.setblocking(True)
        self.sock.connect(('localhost', self.port))
        print(f"Используется порт: {self.port}")

    def get_keys(self):
        srvr = self.sock.recv(1024).decode().split("|")
        srvr = [int(item) for item in srvr]
        try:
            self.read_keys()
        except FileNotFoundError:
            b = random.randint(3109,4202)
            g = srvr[0]
            p = srvr[1]
            B = pow(g, b) % p
            A = srvr[2]
            K = pow(A, b) % p
            self.keys = [b, g, p, B, A, K]
            with open("client.csv", "w", newline = "") as csvfile:
                writer = csv.writer(csvfile, delimiter = ";")
                writer.writerow(self.keys)
        self.sock.send(str(self.keys[3]).encode())

    def read_keys(self):
        with open("client.csv", "r", newline = "") as csvfile:
            reader = csv.reader(csvfile, delimiter = ";")
            self.keys = [int(item) for item in next(reader)]

    def listening(self):
        while True:
            msg = self.sock.recv(1024).decode()
            msg = self.decrypt(self.keys[5], msg)
            print(msg)

    def wrtng(self):
        while True:
            cmd = input()
            if cmd == "stop":
                break
            cmd = self.encrypt(self.keys[5], cmd)
            self.sock.send(cmd.encode())

    def start(self):
        self.sock_connect()
        self.get_keys()
        self.port = int(self.decrypt(self.keys[5],self.sock.recv(1024).decode()))
        self.sock.close()
        self.sock_connect()
        threading.Thread(target = self.listening, daemon = True).start()
        self.wrtng()
        self.sock.close()

client = Client()
client.start()











