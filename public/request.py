# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/23 08:30

"""

import json
import requests
from public.log import Logger

logger = Logger()


def request(url, method, data=None, header=None):
    code_dict = dict()
    if method == 'get' or method == 'GET':
        global params, result, response
        if data:
            try:
                params = dict(p.split('=') for p in (data.split('&')))
            except Exception:
                params = str(data)
        else:
            params = None
        try:
            response = requests.get(url, params=params, headers=eval(header), timeout=3)
            result = response.content
            try:
                result = json.loads(result)
                result['StatusCode'] = response.status_code
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
            response = requests.post(url, data=data, headers=eval(header), timeout=3)
            result = json.loads(response.content)
            result['StatusCode'] = response.status_code
        except Exception as e:
            code_dict['StatusCode'] = 1000
            code_dict['Exception'] = e
            result = code_dict
        return result
