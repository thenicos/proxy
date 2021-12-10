from flask import Flask, render_template, request
from flask_basicauth import BasicAuth
import os
import requests

app = Flask(__name__)
#mettere questa variabile a True per attivare un'autenticazione con nome utente e password
app.config['BASIC_AUTH_FORCE'] = False
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')
#----------------------------------------------------------------------------------------#

TOKEN = os.environ.get('rentmanapitoken')
LINK = os.environ.get('rentmanlink')

basic_auth = BasicAuth(app)

@app.route('/')
#@basic_auth.required
def secret_view():
    return "funziona"

@app.route('/callrentman')
@basic_auth.required
def call_to_rentman():
    function = request.args.get('rentmanfunction')
    if function==None:
        return "null"

    payload = request.args.to_dict(flat=True)
    del payload['rentmanfunction']

    hed = {'Authorization': 'Bearer ' + TOKEN, 'Content-Type': 'application/json'}
    return requests.get("https://api.rentman.net/"+function, params=payload, headers=hed).json()

@app.route('/getrentmanlink')
@basic_auth.required
def link_to_rentman():
    return LINK

#se viene trovata una variabile d'ambiente chiamata CUSTOM_ATS, viene attivata la modalità custom, basata su tag che usiamo solo in ats e altre customizzazioni specifiche di rentman
@app.route('/atsmode')
@basic_auth.required
def isAtsMode():
    if (os.environ.get('CUSTOM_ATS') == None):
        return "False"
    return "True"


if __name__ == "__main__":
    app.run()
