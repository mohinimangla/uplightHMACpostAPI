import hmac
import hashlib
from flask import current_app as app, Response

class HMACSignature:
    def get_signature(self, input_msg):
        encoded_input_msg = input_msg.encode('UTF-8')
        
        secret_key = app.config["SECRET_KEY"]
        encoded_secret_key = secret_key.encode('UTF-8')
        
        hmac_instance = hmac.new(encoded_secret_key, encoded_input_msg, hashlib.sha512)
        signature = hmac_instance.hexdigest()
        
        return Response(u'{"id": ' + input_msg + ', "signature": ' + signature + '}', mimetype= 'application/json', status=200)