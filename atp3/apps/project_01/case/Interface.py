#coding:utf-8
#conn = http.client.HTTPSConnection("http://app-client.ffzx.com")
#conn.request("POST","/app-client-web/member/login.do?params={'phone':'13410342891','sysType':'1','password':'52c69e3a57331081823331c4e69d3f2e','type':'1'}")

from selenium import webdriver
import time
import http.client
import urllib,json
import json, urllib
import urllib

#----------------------------------
# 网站安全检测调用示例代码 － 聚合数据

#----------------------------------
  
def main():
  
    #配置您申请的APPKey
    appkey = "*********************"
  
    #1.网站安全检测
    request1(appkey,"GET")
  
  
  
#网站安全检测
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/webscan/"
    params = {
        "domain" : "", #域名如:juhe.cn ,1jing.com
        "dtype" : "", #返回类型,xml/json/jsonp可选
        "callback" : "", #如返回的为JSONP，则须传递此参数
        "key" : appkey, #APP KEY
  
    }
    params = urllib.parse.urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
  
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"],res["reason"]))
    else:
        print("request api error")





if __name__ == "__main__":
    Interface.Interface_Logon()
