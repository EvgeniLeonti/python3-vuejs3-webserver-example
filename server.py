import os
import sqlite3
from sqlite3 import Error

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')


def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('database.db')
        print("Connection established!")
    except Error as e:
        print(e)
    return conn


@app.route('/', methods=['GET'])
def serve_dir_directory_index():
    return send_from_directory(static_file_dir, 'index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')

    return send_from_directory(static_file_dir, path)


@app.route('/api/data')
def get_data():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    data = []
    for row in rows:
        obj = {
            'id': row[0],
            'name': row[1],
            'value': row[2]
        }
        data.append(obj)
    conn.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
