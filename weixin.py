#-*-coding: utf-8-*-

import requests
import json

class Weixin(object):
    def __init__(self, corpid = None, corpsecret = None):
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.access_token = ''
    def getToken(self):
      # 拼接请求地址
      requrl = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self.corpid +'&corpsecret=' + self.corpsecret
      # 存储接收到的数据
      res = requests.get(requrl).json()
      self.access_token = res['access_token']
      return res['errcode'], res['access_token']
    def sendMessage(self, option = None):
      # 拼接请求地址
      requrl = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.access_token
      # print(option)
      res = requests.post(requrl, data = json.dumps(option)).json()
      return res
