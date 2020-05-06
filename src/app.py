
from flask import Flask
from redis import Redis
from typing import List, Dict
import mysql.connector
import json 
import pymysql

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
 
@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)
 
@app.route('/mysql')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})

def favorite_colors() -> List[Dict]:
    connection = pymysql.connect(user='root', password='root',
                        host='db', database='knights',port=3306)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)