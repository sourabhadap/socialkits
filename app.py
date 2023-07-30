from flask import Flask
from flask_restful import Api, Resource, reqparse

flaskapp = Flask(__name__)
flaskapi = Api(flaskapp)


if __name__ == '__main__':
    flaskapp.run(port=5000,host="0.0.0.0",debug=True)
