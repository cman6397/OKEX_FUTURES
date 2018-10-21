import hmac
import base64
import requests
import json
import time as pytime

BASE_URL = 'https://www.okex.com'
SERVER = "MEXICO-P2P"
PASSPHRASE = 'chrisdev'
API_KEY = '9a528fd0-b835-48eb-88dd-d84e867dfdd9'
SECRET_KEY = '375C0334A132DB17F8DEE8DFF216A26B'
APPLICATION_JSON = 'application/json'

class okex():
    def __init__(self, route, method):
        self.route = route
        self.method = method
        self.time = 0
        self.header={}
        self.signature=''
        
    def set_time(self):
        self.time = str(pytime.time())

    def set_signature(self, body = None):
        if str(body) == '{}' or str(body) == 'None':
            body = ''
        message = str(self.time) + str.upper(self.method) + self.route + str(body)
        mac = hmac.new(bytes(SECRET_KEY, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
        d = mac.digest()
        self.signature = base64.b64encode(d)

    # set request header
    def set_header(self):
        header = dict()
        header['OK_ACCESS_KEY'] = API_KEY
        header['OK_ACCESS_SIGN'] = self.signature
        header['OK_ACCESS_TIMESTAMP'] = self.time
        header['OK_ACCESS_PASSPHRASE'] = PASSPHRASE
        self.header = header
        
    def get(self):
        self.set_time()
        self.set_signature()
        self.set_header()

        response = requests.get(self.route, headers=self.header).json()
        
        return response

    def parse_params_to_str(self,params):
        url = '?'
        for key, value in params.items():
            url = url + str(key) + '=' + str(value) + '&'

        return url[0:-1]