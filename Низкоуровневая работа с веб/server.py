import socket
import datetime
import random
import json
import os
import re
import threading
import magic

class Server(object):
    def __init__(self):
        self.log = "kee.txt"
        self.lock = threading.Lock()


    def get_cnfg(self):
        with open("cnfg.json", "r") as jsonfile:
            cnfg = json.load(jsonfile)
        self.port = cnfg["port"]
        self.vol = cnfg["request_volume"]
        self.root = cnfg["root"]


    def binder(self):
        self.sock = socket.socket()
        while True:
            try:
                self.sock.bind(('', self.port))
                print(f"Сервер развернут на сокете: {self.port}")
                break
            except OSError:
                print(f"Порт {self.port} занят")
                self.port = random.randint(1024, 65535)
        

    def start(self):
        self.get_cnfg()
        self.binder()
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            with self.lock:
                print("Подключен", addr)
            cli_thread = CliThread(conn, addr, self.vol, self.root, self.lock, self.log)
            threading.Thread(target = cli_thread.start,  daemon = True).start()


class CliThread(object):
    def __init__(self, conn, addr, vol, root, lock, log):
        self.conn = conn
        self.addr = addr
        self.vol = vol
        self.root = root
        self.lock = lock
        self.log = log

    def cur_dt(self):
        self.date =  datetime.datetime.utcnow().strftime(r"%a, %d %b %Y %H:%M:%S GMT")



    def resource_parser(self):
        self.request = self.request.split("\r\n")
        self.http = self.request[0].split()[1]

        self.path = re.split("[\\/]", self.http)
        if self.path == ["", ""]:
            self.path = ["index.html"]

        self.resolved = bool(re.search("\.(html|css|js|png|jpg|jpeg|pdf)$", self.path[-1]))



    def req_interp(self):
        self.resource_parser()
        self.path = os.path.join(self.root, *self.path)
        self.content_type = "text/html"
        if self.resolved:
            try:
                with open(self.path, "rb") as contentfile:
                    self.content = contentfile.read()
                self.resp_code = "200 OK"
                self.mime = magic.Magic(mime=True)
                self.content_type = self.mime.from_file(self.path)

            except:
                self.content = b""
                self.resp_code = "404 Not Found"
        else:
            self.content = b""
            self.resp_code = "403 Forbidden"

    def http_response(self):

        content_length = len(self.content)

        log = [str(item) for item in [self.date, self.addr, self.path, self.resp_code]]
        log = "; ".join(log)
        with self.lock:
            with open(self.log, "a", encoding = "utf8") as logfl:
                logfl.write(log+"\n")
        self.cur_dt()
        response = f"""HTTP/1.1 {self.resp_code}
Date: {self.date}
Content-length: {content_length}
Server: SelfMadeServer v0.0.1
Content-type: {self.content_type}
Connection: retry-after

"""
        self.response = response.encode() + self.content
        

    def start(self):
         while True:
            self.request = self.conn.recv(self.vol).decode() 
            self.cur_dt()
            if not self.request:
                continue
            self.req_interp()
            self.http_response()
            self.conn.send(self.response) 


server = Server()
server.start()

       

















    





