from flask import Response
from flask_restful import Resource, abort
from services.token_generator import HMACGenerator
import requests
import json

class SignatureGenerator(Resource):
    
    def generate(self, request, key):
        try:
            if not request.json:
                return self.bad_request()
            if 'signature' in request.json:
                return self.bad_request()
        except Exception as e:
            print(e)
            return self.bad_request()
        
        input_msg = request.json
        
        hmac_instance = HMACGenerator(key)
        
        input_msg.update(hmac_instance.get_signature(json.dumps(input_msg)))
        return Response(json.dumps(input_msg), mimetype='application/json', status=200)
    
    def bad_request(self):
        return Response('Incorrect data', mimetype= 'application/json', status=400)