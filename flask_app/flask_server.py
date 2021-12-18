from flask import Flask, request
import pickle
import os
from hashlib import sha256
from datetime import datetime
import re
import random
import string

app = Flask(__name__)
COLLECTION = "my.pickle"

def hasher(password, salt = None):
	if salt == None:
		letters_and_digits = string.ascii_letters + string.digits
		salt = ''.join(random.sample(letters_and_digits, 16))
		salt = salt.encode('utf-8')

	password = sha256((password).encode('utf-8')+salt).hexdigest()
	return salt,password	

def loader():
	if os.path.exists(COLLECTION):
		with open(COLLECTION, "rb") as picklefile:
			buffered = pickle.load(picklefile)
		return buffered
	else:
		return {}	

def jsonify(result = True, description = "", exception = None):
	return {
		"result":result,
		"description":description
		}

def saver(infodate):
	password = infodate["password"]
	if not re.search("^(\w|\d|\_){8,}$", password):
		return False
	email = infodate["email"]
	date = datetime.now().strftime("%H:%M:%S, %d.%m.%Y")
	password = hasher(password)
	database = loader()
	database[email] = {"password": password, "date": date }
	with open(COLLECTION, "wb") as picklefile:
		pickle.dump(database, picklefile)
	return True

def authentification(log_pass):
	cllctns = loader()
	email = log_pass["email"]
	password = log_pass["password"]
	checked_password = cllctns.get(email)
	if not checked_password:
		return jsonify(False,"Had no user")
	checked_password = checked_password["password"]
	checked = hasher(password, checked_password[0])
	if checked_password == checked:
		return jsonify(True, "successful authentification")
	else:
		return jsonify(False, "Invalid password")


@app.route('/user/login', methods=['POST']) #authentification
def login():
	log_pass = request.get_json()
	return authentification(log_pass)

@app.route('/user/logon', methods=['POST']) #registration
def logon():
	infodate = request.get_json()
	datainfo = loader()
	flag = not bool(datainfo.get(infodate["email"]))
	if flag:
		if saver(infodate):
			return jsonify(True, "succssesfully registered")
		else:
			return jsonify(False,"only letters and digits")
	else:
		return jsonify(False,"email has already use")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)







