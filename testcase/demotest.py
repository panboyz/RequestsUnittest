# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/19 16:22

"""

import ddt
import unittest
from public.request import request, logger
from public.getexceldata import get_excel_data
import logging

test_data = get_excel_data('all')
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - %(filename)s:%(lineno)s - %(levelname)s - %(message)s')


@ddt.ddt
class TestCase(unittest.TestCase):

    def setUp(self):
        pass

    @ddt.data(*test_data)
    def test_case(self, data):
        global assert_result
        url, method, header, data, ast, exc = data['url'], data['method'], data['header'], \
                                              data['data'], data['assert'], data['except']
        result = request(url, method, data=data)
        if 'Exception' not in result:
            logging.info('请求成功，地址为%s，参数为%s，方式为%s，返回结果为%s' % (url, data, method, result))
            check_ast = ast.split('.')
            if len(check_ast) == 1:
                assert_result = result[ast]
            elif len(check_ast) == 2:
                key, subkey = check_ast[0], check_ast[1]
                assert_result = result[key][subkey]
            elif len(check_ast) == 3:
                key, num, subkey = check_ast[0], check_ast[1], check_ast[2]
                assert_result = result[key][int(num)][subkey]
            self.assertEqual(assert_result, exc)
        else:
            logging.error('请求异常，地址为%s，异常为%s' % (url, result['Exception']))
            self.assertNotIn('Exception', result)


if __name__ == '__main__':
    unittest.main()
