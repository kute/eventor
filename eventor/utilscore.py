#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: utilscore.py
@ __mtime__: 2017/1/4 13:58

IO多路复用（单进程模块多线程）
select 模块

"""

import socket
import select


server = socket.socket()
server.bind(('localhost', 8801))
server.listen()


def multi_select(rlist=None, wlist=None, xlist=None, timeout=None):
    r_list, w_list, x_list = select.select(rlist, wlist, xlist, timeout)



def main():
    print("hello")


if __name__ == "__main__":
    main()
