# coding=utf-8
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

# if __name__ == '__main__':

    # # 调休post请求
    # headers = {
    #     "Content-Type": "application/json",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"
    # }
    # url = 'http://loc.api.yungehuo.com/member/login'
    # data = {
    #     "mobile": "13800138001",
    #     "password": "5bc791b2da1b1efa077dd20b2211f6c1"
    # }
    # r = SendRequest().send_json_post(url, dict=data, header=headers)

    # 调休get请求
    # headers = {
    #     "Content-Type": "application/json",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
    #     "Token": "wyNzIxMTM2MzE4OTA1NjIsMTU3NzE3NTQyMS"
    #         }
    # url = 'http://loc.api.yungehuo.com/process/truckInfo?orderId=157527321420'
    # r = SendRequest().send_get_request(url=url, header=headers)
    # print(r)



