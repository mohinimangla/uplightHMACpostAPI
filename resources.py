from flask import request
from flask_restful import Resource, abort
from services.token_generator import HMACSignature
import requests
import json

class TokenGenerator(Resource):
    def __init__(self):
        self.key = "This is the first key ever"
        self.encoded_key = str.encode(self.key)
        
    def post(self):
        input_msg = request.json.get('id')
        if not input_msg:
            return Response(u'Empty String Provided', mimetype= 'application/json', status=400)
        hmac_instance = HMACSignature()
        
        return hmac_instance.get_signature(input_msg)