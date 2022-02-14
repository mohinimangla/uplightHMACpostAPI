import hmac
import hashlib
from flask import Response

class HMACGenerator:
    def __init__(self, key):
        self.secret_key = key
    
    def get_signature(self, input_msg):
        if not input_msg:
            return None
        encoded_input_msg = input_msg.encode('UTF-8')
        
        encoded_secret_key = self.secret_key.encode('UTF-8')
        
        hmac_instance = hmac.new(encoded_secret_key, encoded_input_msg, hashlib.sha512)
        signature = hmac_instance.hexdigest()
        
        return {"signature": signature}