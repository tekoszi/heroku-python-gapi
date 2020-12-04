from flask import Flask
import os
import markdown
from flask_restful import Resource, Api, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    with open(os.path.dirname(app.root_path) +'/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)


@app.route("/create")
def create():

    return 'add Hello World'


@app.route("/read")
def read():

    return 'add Hello World'

@app.route("/update")
def update():

    return 'add Hello World'


@app.route("/delete")
def delete():

    return 'add Hello World'

class Geo(Resource):
    def get(self):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM geo")
        return {'message': 'Success', 'data': c.fetchall()}
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ip', required=True)
        parser.add_argument('location', required=True)
        parser.add_argument('symbol', required=True)
        args = parser.parse_args()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        geoData = (args['ip'], args['location'], args['symbol'])
        c.execute('INSERT INTO geo VALUES (?,?,?)', geoData)
        conn.commit()
        return {'message': 'Success', 'data': args}

api.add_resource(Geo,'/geo')

