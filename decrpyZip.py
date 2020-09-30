#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author: Hu Guanjie
create time:2020/9/30 13:49
"""

import zipfile
import time
import threading

startTime = time.time()
# 判断线程是否需要终止
flag = True


def extract(password, file):
    try:
        password = str(password)
        file.extractall(path='.', pwd=password.encode('utf-8'))
        print("the password is {}".format(password))
        nowTime = time.time()
        print("spend time is {}".format(nowTime - startTime))
        global flag
        # 成功解压其余线程终止
        flag = False
    except Exception as e:
        print(e)


def do_main():
    zfile = zipfile.ZipFile("3.zip", 'r')
    # 开始尝试
    for number in range(1, 999999):
        if flag is True:
            t = threading.Thread(target=extract, args=(number, zfile))
            t.start()
            t.join()


if __name__ == '__main__':
    do_main()