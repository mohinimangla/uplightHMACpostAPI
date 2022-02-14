import requests
import unittest
import json
from base64 import b64encode
from services.token_generator import HMACGenerator


BASE = "http://127.0.0.1:5000/"
 
class TestHMACEndpoint(unittest.TestCase):
    # test function
    validheader={
        'Authorization': 'Basic %s' % b64encode(bytes('{}:{}'.format('registeredQA','TestingMohinisHMACAPP'), "utf-8")).decode("ascii"),
        'Content-Type': 'application/json'}
    invalidheader={
        'Authorization': 'Basic unregisteredQA:kjdhkvjdnlbkfbjkf', 
        'Content-Type': 'application/json'}
    
    payload = [{"id": "Apiary: a place where bees and beehives are kept, especially a place where bees are raised for their honey"},
               {}]
    
    signatures = ["5aaa979c288f10d679bbd8c55d1c0b5bdfe9e41af4ed7dd4028a54ca75639f7a9634a6a531bf0156183afa8f566ba1392c575869e63814440ce00633219cbb6e"]
    
    def test_valid_signature(self):
        response = requests.post(BASE + "/generate-token", data=json.dumps(self.payload[0]), headers=self.validheader)
        self.assertEqual(response.status_code, 200)
        response_data = eval(response.text)
        self.assertEqual(response_data["signature"], self.signatures[0])

    def test_empty_json(self):
        response = requests.post(BASE + "/generate-token", json=self.payload[1], headers=self.validheader)
        self.assertEqual(response.status_code, 400)
    
    def test_empty_input(self):
        response = requests.post(BASE + "/generate-token", headers=self.validheader)
        self.assertEqual(response.status_code, 400)

    def test_invalid_cred(self):
        response = requests.post(BASE + "/generate-token", json=self.payload[0], headers=self.invalidheader)
        self.assertEqual(response.status_code, 401)
    
class TestHMACGenerator(unittest.TestCase):
    def setUp(self):
        self.signature_obj = HMACGenerator("This is a random key")


    def test_valid_string(self):
        input_json = {"id": "MDAwMDAwMDAtMDAwMC0wMDBiLTAxMmMtMDllZGU5NDE2MDAz"}
        expected_signature = "97fede1db2c68058bbbf5ffa28aa06f72a968a012563bfd950764afc6fcdc863f4420188e5664e274550a1beacb0278de5321d9d56617d28501571d1be0602cb"
        signature_detail = self.signature_obj.get_signature(json.dumps(input_json))
        self.assertEqual(signature_detail['signature'], expected_signature)
    
    def test_empty_string(self):
        signature_detail = self.signature_obj.get_signature("")
        self.assertEqual(signature_detail, None)

unittest.main()