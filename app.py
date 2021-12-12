from flask import Flask, render_template, request, abort
from flask_cors import CORS
import os
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/<path:text>', methods=['GET'])
def all_routes(text):
    data = str(request.headers).split()
    if "Bearer" not in data:
        abort(404)
    TOKEN = data[data.index("Bearer")+1]
    if (os.environ.get('BEARER')==TOKEN):
        hed = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}
        response =requests.get("https://api.rentman.net/"+text, headers=hed).json()    
        return str(json.dumps(response))

    abort(404)

if __name__ == "__main__":
    app.run()
