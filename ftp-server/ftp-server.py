import socket
import os
import shutil
import csv
import re

'''
prnt - напечатать рабочий каталог
ls - содержимое каталога
cd (path) - перемещение
mkdir (dirname) - создать каталог
deldir (dirname) - удалить каталог
touch (filename) - создать файл
rm (filename) - удалить файл
mv (filename) (filename) - переименовать файл
cat (filename) - вывести содержимое файла
get (filename) - получить файл
send (filename) - отправить файл
'''

HU = b"HU&#"
FFL = b'FLD$$&'
TORT = 20039
global_root = os.path.join(os.getcwd())
usersfile = os.path.join(global_root, "users.csv")
log_file = os.path.join(global_root, "log.txt")
help_str = '''
prnt - напечатать рабочий каталог
ls - содержимое каталога
cd (path) - перемещение
mkdir (dirname) - создать каталог
deldir (dirname) - удалить каталог
touch (filename) - создать файл
rm (filename) - удалить файл
mv (filename) (filename) - переименовать файл
cat (filename) - вывести содержимое файла
get (filename) - получить файл
send (filename) - отправить файл
'''

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


def my_prnt(*strings):
    print(*strings)
    with open(log_file, "a") as logfile:
        logfile.write(" ".join([str(item) for item in strings]) + "\n")


def logon(message):
    global usersfile, global_root
    login, message = message.split("=login", 1)
    password, message = message.split("=password", 1)
    current_directory, message = message.split("=cur_dir", 1)
    size, message = message.split("=file_size", 1)
    if login == password == "EL":
         user_root = global_root
    else:
        user_root =  os.path.join(global_root, login)
        with open(usersfile, "a+", newline = "") as csvfile:
            csvfile.seek(0,0)
            reader = csv.reader(csvfile, delimiter = ";")
            for line in reader:
                if line[0] == login:
                    if line[1] == password:
                        break
                    else:
                        return None
            else:
                writer = csv.writer(csvfile, delimiter = ";")
                writer.writerow([login, password])

        try: 
            os.makedirs(user_root)
        except FileExistsError:
            pass

    return user_root, current_directory, message, size

def get_file(path):
    global conn, HU, FFL
    try:
        with open(path, "rb") as bytefile:
            while read_bytes := bytefile.read(1024):
                conn.send(read_bytes)

    except FileNotFoundError:
        returned = b'Invalid path'+FFL
    except PermissionError:
        returned = b"Permission denied"+FFL
    else:
        returned =HU
    my_prnt("Файл отправлен")
    return returned


def for_path(root, current, chdir):
    if current == "\\" and chdir[:2] == "..":

        return root + chdir[2:]
    elif chdir[0] in ["\\", "/"]:
        chdir = re.sub(r"^[\\/]+", "", chdir)
        my_prnt(chdir)
        return os.path.join(root, chdir)
    else:
        return os.path.join(root, current[1:], chdir)

def decor(path_func):
    def wrapper(*path):
        try:
            returned = path_func(*path)
            if returned == None:
                return "ALL OK"
            else:
                return returned
        except FileNotFoundError:
            return (f'Wrong path')
        except FileExistsError:
            return (f'Has already exists') 
        except PermissionError:
            return f"Smthng wrong, permission denied"
    return wrapper

def pwd(dirname):
    return os.path.join(dirname)

def ls(path):
    return '\n\r'.join(os.listdir(path))

def cd(path, current, root):
    try:
        os.chdir(path)
    except:
        return current
    return os.getcwd().replace(root,"")+"\\"
    
@decor
def mkdir(path):
    os.makedirs(path)

@decor
def rmtree(path):
    shutil.rmtree(path)

@decor
def remove(path):
    os.remove(path)

@decor
def touch(path):
    with open(path, 'x'):
        pass

@decor
def cat(path):
    with open(path, "r") as file:
        return "\n\r".join(file.readlines())

@decor
def rename(path1, path2):
    os.rename(path1, path2)



def send_file(path, root, size):
    global conn, HU, FFL
    available = pow(2,20)*10 - get_size(root)
    print(available, int(size))
    if available < int(size):
        return "Storage FULL!"
    else:
        conn.send(b"en&$")
    flag_finder = conn.recv(1024)
    with open (path, "wb") as bytefile:
            while True:
                if HU in flag_finder:
                    bytefile.write(flag_finder.replace(HU, b""))
                    break
                else:
                    bytefile.write(flag_finder)
                    flag_finder = conn.recv(1024)
    my_prnt("Файл получен")
    return "uploaded OK"


def main(req):
    req = logon(req)
    if req:
        user_root, current_directory, req, size = req
        req, *chdir = req.split()
        path = [for_path(user_root, current_directory, item) for item in chdir]
        if not path:
            path = [""]
        if req == 'prnt':
            return pwd(current_directory)
        elif req == 'ls':
            return ls(os.path.join(user_root, current_directory[1:]))
        elif req == "cd":
            return cd(path[0], current_directory, user_root)
        elif req == 'mkdir':
           
            return mkdir(path[0])
        elif req == 'deldir':
            return rmtree(path[0])
        elif req == 'touch':
            return touch(path[0])
        elif req == 'rm':
            return remove(path[0])
        elif req == 'cat':
            return cat(path[0])
        elif req == 'mv':
            return rename(*path[:2])
        elif req == "get":
            return get_file(path[0])
        elif req == "send":
            return send_file(path[0], user_root, size)
        elif req == 'help':
            return help_str
        else:
            return 'nothing commands'
    else:
        return "WRONG password"

sock = socket.socket()
sock.bind(('', TORT))
sock.listen()
my_prnt("Сервер повешен на порт", TORT)

while True:
    conn, addr = sock.accept()
    rqsts = conn.recv(1024).decode()
    my_prnt("Запрос:", rqsts)
    resps = main(rqsts)
    my_prnt("Ответ:", resps)
    if not resps:
        resps = "\00"
    try:
        conn.send(resps.encode())
    except AttributeError:
        conn.send(resps)
