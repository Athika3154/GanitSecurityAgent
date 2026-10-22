import pickle
import sqlite3
import subprocess


def calc(expr):
    return eval(expr)  # code injection


def find_user(name):
    db = sqlite3.connect("users.db")
    return db.execute("SELECT * FROM users WHERE name = '%s'" % name).fetchall()  # SQL injection


def ping(host):
    return subprocess.check_output("ping -c 1 " + host, shell=True)  # command injection


def load_session(blob):
    return pickle.loads(blob)  # insecure deserialization
