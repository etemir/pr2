import socket, random, threading, csv

class Server(object):
    def __init__(self, port = 3109):
        self.port = port

    def start(self):
        self.sock_bind()
        self.gen_keys()
        if self.ch_access():
        # if True:
            self.messaging_port()
            threading.Thread(target = self.listening, daemon = True).start()
            self.messaging()
            self.sock.close()
        else:
            print("Чужой клиент")
            self.sock.close()


    def encrypt(self, k, m):
        return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))

    def decrypt(self, k, c):
        return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))

    def listening(self):
        while True:
            msg = self.conn.recv(1024).decode()
            msg = self.decrypt(self.keys[5], msg)
            print(msg)

    def messaging(self):
        while True:
            cmd = input()
            if cmd == "stop":
                break
            cmd = self.encrypt(self.keys[5], cmd)
            self.conn.send(cmd.encode())

    def sock_bind(self):
        self.sock = socket.socket()
        self.sock.setblocking(True)
        self.sock.bind(('', self.port))
        print(f"Используется порт: {self.port}")
        self.sock.listen(0)
        self.conn, self.addr = self.sock.accept()

    def gen_keys(self):
        try:
            self.keys = [int(item) for item in self.read_keys()]
            self.conn.send(f"{self.keys[1]}|{self.keys[2]}|{self.keys[3]}".encode())
            B = int(self.conn.recv(1024).decode())
            self.keys[4] = B
        except FileNotFoundError:
            a, g, p = [random.randint(3901,4202) for _ in range(3)]
            A = pow(g, a) % p
            self.conn.send(f"{g}|{p}|{A}".encode())
            B = int(self.conn.recv(1024).decode())
            K = pow(B, a) % p
            self.keys = [a, g, p, A, B, K]

            with open("server.csv", "w", newline = "") as csvfile:
                writer = csv.writer(csvfile, delimiter = ";")
                writer.writerow((self.addr[0], *self.keys))



    def read_keys(self):
        with open("server.csv", "r", newline = "") as csvfile:
            reader = csv.reader(csvfile, delimiter = ";")
            for row in reader:
                if row[0] == self.addr[0]:
                    return row[1:]
            else:
                raise FileNotFoundError

    def ch_access(self):
        with open("access.csv", "r", newline = "") as csvfile:
            reader = csv.reader(csvfile, delimiter = ";")
            for row in reader:
                if int(row[0]) == self.keys[4]:
                    return True
            else:
                return False

    def messaging_port(self):
        self.port = random.randint(1024,65535)
        self.conn.send(self.encrypt(self.keys[5], str(self.port)).encode())
        self.sock.close()
        self.sock_bind()

server = Server()
server.start()