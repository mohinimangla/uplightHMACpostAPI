from flask import Flask, request
from flask_restful import  Api, abort
from flask_sqlalchemy import SQLAlchemy
from resources import SignatureGenerator
from middleware import Middleware

app = Flask(__name__)
api = Api(app)
app.config.from_object('config') 
app.wsgi_app = Middleware(app.wsgi_app, app.config)

sg = SignatureGenerator()

# register resource
@app.route('/generate-token', methods=["POST"])
def generatesignature():
    key = app.config["SECRET_KEY"]
    return sg.generate(request, key)

if __name__ == "__main__":
    app.run(debug=True)
    