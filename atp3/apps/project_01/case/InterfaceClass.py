# -*- coding: utf_8 -*-
import urllib
import urllib3
import urllib.request
import urllib.error
import urllib.parse
import json
import unittest, time, re
from project_01.case.mysql_pubtwo import MysqlUtiltwo
import warnings
class APITest():
    '''
    接口测试类
    '''
    def __init__(self):
        mysql_info = {"host": '10.12.11.86',
                      "port": 3306,
                      "user": 'store_rw',
                      "passwd": 'Spts$201708',
                      "db": 'GiveU_Store',
                      "charset": 'utf8'}
        warnings.simplefilter("ignore", ResourceWarning)


    def apicall(self,method,url,getparams,postparams, headers=None):

        str1=''
        #user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        #
        # tokens = 'Authorization: Bearer ' + str(self.tk)
        #添加头信息
        # headers = {'User-Agent': user_agent,
        #          'Content-Type': 'application/json',
        #          #'token': tokens
        #          }
        #result = ''
        #GET方法调用
        if method=='GET':
            if getparams!="":
                for k in getparams:
                    str1=str1+k+'='+urllib.request.quote(str(getparams.get(k)))          
                    if len(getparams) > 2:
                        str1=str1+"&"
                url=url+"&"+str1
            result = urllib.request.urlopen(url).read()
        #POST方法调用
        response = ''
        if method=='POST':
            if postparams != "":
                http = urllib3.PoolManager()
                data = json.dumps(postparams, skipkeys=True)#urllib.parse.urlencode(postparams).encode(encoding="UTF-8")
                #req = urllib.request.Request(url, data, headers)
                response = http.request("POST",url, body=data, headers=headers) #urllib.request.urlopen(req)
        jsdata=json.loads(response.data)
        return jsdata

            
class APIGetAdList(unittest.TestCase):       
    #def test_call(self,method,postparams,getparams):
    def test_call(self):
        api=APITest()
        getparams=''
        postparams = {
              "saveTypeName": "livenessInfo",
              "saveContent": {
                "photoVOList": [
                    {
                        "fileName":"group1/M00/41/B9/CgoLiF0UZseAAEzGAACbyzv9ue4292.jpg",
                        "photoType":"52"
                    },
                    {
                        "fileName":"group1/M00/41/B9/CgoLiF0UZseAVFmcAACeORFhoYs604.jpg",
                        "photoType":"52"
                    },
                    {
                        "fileName":"group1/M00/41/B9/CgoLiF0UZseAcAQxAACfDGOg-xM043.jpg",
                        "photoType":"52"
                    },
                    {
                        "fileName":"group1/M00/41/B9/CgoLiF0UZseAPRBhAAChMMOxR4w858.jpg",
                        "photoType":"52"
                    }
                ],
                "fileName": "group2/M08/24/29/CgsMMFyxXj2AGqUTAABr8fiEcSk339.png",
                "photoType": "52",
                "biz_no": "30acb83c-53e1-4b72-94e5-1a3e951dfc71",
                "token_video": "c554ac43d9a08bff75e64232bf65c5d8",
                "request_id": "1547118731,d4f28ecc-6e30-4e86-aace-393eb4965e45",
                "passed": True,
                "liveness_score": 0,
                "image_timestamp": 0.840522
              },
              "userId": "10360486"
            }
        hdc = [
            {
                "idCredit": 13913754,
                "status": "string"
            }
        ]
        #postparams = bytes(urllib.parse.urlencode(postparamsO), 'utf8')
        data=api.apicall("POST",
                         #r"http://testdafyshop.dafycredit.cn/v1/cashloan/applyInfoRecord/substepSave",
                         r"http://10.10.11.132:9912/api/Decision/HandDecisionCredit",
                         getparams,
                         hdc
                         )
        print(data)
         
if __name__ == "__main__":
    unittest.main()
