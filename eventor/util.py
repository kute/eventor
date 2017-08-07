#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: util.py
@ __mtime__: 2017/8/7 14:57

"""

import os


class EventorUtil(object):

    def __init__(self):
        pass

    def get_dir(self, relative=os.path.dirname(__file__), target_dir="resources"):
        return os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), relative)), target_dir)

    def get_sub_dir(self, relative=os.path.dirname(__file__), target_dir="resources", subdir="sources"):
        return os.path.join(self.get_dir(relative, target_dir), subdir)


if __name__ == "__main__":
    e = EventorUtil()
    print(e.get_dir())
    print(e.get_dir(relative=".."))
    print(e.get_dir(relative=os.path.dirname(__file__)))
    print(e.get_dir(relative="."))
    print(e.get_sub_dir())
    print(e.get_sub_dir(relative="..", subdir="images"))
    print(e.get_sub_dir(relative=os.path.dirname(__file__), subdir="images"))
    print(e.get_sub_dir(relative=".", subdir="images"))
