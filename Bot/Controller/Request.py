import os, sys
lib_path = os.path.abspath(os.path.join('Const'))
sys.path.append(lib_path)
from Const import consts
import requests
import json
class Request:
    def GetApi(self, key):
        self.key= consts.Const.api+str(key)
        response = requests.get(self.key)
        jdata= json.loads(response.content.decode('utf-8'))
        infor=jdata.get('results')
       # print(s1)
        #s2=s1[1]
        #print(s2['content'])
        return infor[1]

