from flask_restful import Resource, Api, reqparse
from flask import Flask, request, jsonify
from model import *


def funct(user):
    val = 0
    for a in user:
        val += ord(a)
    return val
class register(Resource):
    def post(self):
        response = request.get_json()
        inform = info(Age=response['info']['Age'], Born=response['info']['Born'])

        registering = User(Username=response['username'], information=inform)
        registering.Password = funct(response['password'])
        registering.save()

        return "succesfully registered"