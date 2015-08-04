#!/usr/bin/env python
#coding:utf-8
# Author        : tuxpy
# Email         : q8886888@qq.com.com
# Last modified : 2015-08-05 01:38:54
# Filename      : test.py
# Description   : 
import doctest
def func_1():
    """
    >>> func_1()
    你好
    """
    return '你好'

if __name__ == "__main__":
    doctest.testmod()

