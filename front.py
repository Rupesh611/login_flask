from flask_restful import Resource, Api , reqparse
from flask import Flask, request , jsonify
from model import *

class register(Resource):
    def post(self):
        response = request.get_json()
        inform = info(Age =response['info']['Age'], Born = response['info']['Born'])
        registering = User(Username=response['username'], Password=response['password'],information=inform).save()

        return "succesfully registered"