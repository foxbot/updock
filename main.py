import json
import mimetypes
import random
import sqlite3
import string

from flask import Flask, Response, abort, g, request
from pathlib import Path

app = Flask(__name__)

def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choices(chars, k=size))

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('data.db')
    return db

@app.route('/', defaults={'file': 'index'})
@app.route('/<file>', methods=['GET'])
def get_file(file):
    print('file', file)

    c = get_db().cursor()
    c.execute('SELECT data, type FROM files WHERE name = ?;', [file])
    data = c.fetchone()

    if not data:
        abort(404)

    return Response(response=data[0], content_type=data[1])

@app.route('/create', methods=['POST'])
def post_file():
    names = []
    for _, file in request.files.items():
        ext = mimetypes.guess_extension(file.mimetype)
        name = id_generator() + ext # TODO: verify we don't duplicate IDs
        data = file.read()

        db = get_db()
        c = db.cursor()
        c.execute('INSERT INTO files (name, data, type) VALUES (?, ?, ?)', [name, data, file.content_type])
        db.commit()

        names.append(name)
    return (json.dumps(names), 201)

@app.teardown_appcontext
def teardown(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
