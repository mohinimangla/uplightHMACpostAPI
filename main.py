from flask import Flask
from flask_restful import  Api, abort
from flask_sqlalchemy import SQLAlchemy
from resources import TokenGenerator
from middleware import Middleware

app = Flask(__name__)
api = Api(app)
app.config.from_object('config') 
app.wsgi_app = Middleware(app.wsgi_app, app.config)

# register resource
api.add_resource(TokenGenerator, "/generate-token") # accessible at /generate-token

if __name__ == "__main__":
    app.run(debug=True)
    