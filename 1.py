# -*- coding:utf-8 -*-

"""

just for test

"""

import requests
import json

# url = 'http://api.adf.ly/api.php'
# init_params = 'key=youkeyid&youuid=uid&advert_type=int&domain=adf.ly&url=http://somewebsite.com'
header = {'Content-type': 'application/json'}


def request(url, method, data=None, header=None):
    code_dict = dict()
    if method == 'get' or method == 'GET':
        global params,result,response
        if data:
            try:
                params = dict(p.split('=') for p in (data.split('&')))
            except Exception as e:
                print('%s, 提取参数失败' % data)
        else:
            params = None
        try:
            response = requests.get(url, params=params, headers=header, timeout=3)
            result = response.content
            try:
                result = json.loads(result)
                code_dict['StatusCode'] = response.status_code
            except Exception:
                code = response.status_code
                code_dict['StatusCode'] = code
                result = code_dict
        except Exception as e:
            code_dict['StatusCode'] = 1000
            code_dict['Exception'] = e
            result = code_dict
        return result
    if method == 'post' or method == 'POST':
        try:
            response = requests.post(url, data=data, headers=header)
            result = json.loads(response.content)
            result['StatusCode'] = response.status_code
        except Exception as e:
            code_dict['StatusCode'] = 1000
            code_dict['Exception'] = e
            result = code_dict
        return result


data = '{"resultv2":1,"text":200498196496}'
# re = request(url,method='get',data=init_params, header=header)
# re_2 = request('http1://www.baidu.com', 'get')
re_3 = request(url='http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=200498196496',
               method='post',data=data,header=header)
# print(re)
# print(re_2)
print(re_3)
