import jwt
import json
from flask_restful import Resource, Api, reqparse
from flask import Flask, request, jsonify
from model import *

key = 'secret'


class login(Resource):
    def post(self):
        response = (request.get_json())
        val = token_Ret(response)
        if type(val)==str:
            return val
        val = val.decode('UTF-8') # decoding bytes to string
        print(type(val))
        return (val)


# controller
def token_Ret(response):
    if authenticate(response['username'], response['password']):
        print(type(jwt.encode({'sub': response['username']}, key, algorithm='HS256')))
        return jwt.encode({'sub': response['username']}, key, algorithm='HS256')
    else:
        return ("Invalid credentials")


def funct(user):
    val = 0
    for a in user:
        val += ord(a)
    return val


def authenticate(username, password):
    for user in User.objects(Username=username):
        if user.Password != funct(password):
            return False
        else:
            return True


# controller
class info(Resource):
    def get(self):
        try:
            payload = jwt.decode(request.headers['Authorization'], key, algorithms='HS256')
            for user in User.objects:
                if user.Username == payload['sub']:
                    return json.loads(user.information.to_json())
                    break




        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'

        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'