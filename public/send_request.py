#coding=utf-8
import requests
import json


class SendRequest():
    def send_json_post(self, url, dict=None, header=None):
        re = requests.post(url, json=dict, headers=header)
        print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url, 'post', dict, re.json()))
        return re.json()

    def send_data_post(self, url, dict=None, header=None):
        re = requests.post(url, data=dict, headers=header)
        print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url, 'post', dict, re.json()))
        return re.json()

    def send_get_request(self, url, header=None):
        re = requests.get(url, headers=header)
        print('url:{}\r\nmethod:{}\r\nrequest_data:{}\r\nresponse:{}'.format(url, 'get', None, re.json()))
        return re.json()

if __name__ == '__main__':
    # url = 'http://172.16.0.8:8080/login'
    # headers = {
    #     'Content-Type': "application/json"
    # }
    # data = {
    #     "account":"13028812388",
    #     "password":"123456",
    #     "platform_code":"PLATFORM",
    #     "app_id":"a1287a3837f640e0"
    #     }
    # r = SendRequest().send_json_post(url=url, dict=data, header=headers)
    url = 'http://www.baidu.com'
    r = SendRequest().send_get_request(url=url)
    print(r)