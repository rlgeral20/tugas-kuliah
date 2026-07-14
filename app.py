from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# Vulnerability 1: SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return str(cursor.fetchone())

# Vulnerability 2: Hardcoded credentials
DB_PASSWORD = "admin12345"
API_KEY = "sk-1234567890abcdef"

# Vulnerability 3: Command Injection
@app.route('/ping')
def ping_host():
    host = request.args.get('host')
    os.system("ping -c 1 " + host)
    return "pinged"

if __name__ == '__main__':
    app.run(debug=True)
