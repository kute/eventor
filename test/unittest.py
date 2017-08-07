#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/12/25 17:47'

"""

"""

import unittest
from eventor.core import Eventor
from eventor.util import EventorUtil
import os


class SimpleTest(unittest.TestCase):

    def test_run_with_tasklist(self):
        times = 2
        elelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def func(x):
            return x + times
        e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=2)
        result = e.run_with_tasklist(elelist, async=True, timeout=3)
        self.assertEqual(sum(result), sum(elelist) + len(elelist) * times)

    def test_run_with_file(self):
        times = 2
        elelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        e = EventorUtil()
        file = os.path.join(e.get_dir(".."), "data.txt")

        def func(x):
            return int(x) + times
        e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=2)
        result = e.run_with_file(file, async=True, timeout=3)
        self.assertEqual(sum(result), sum(elelist) + len(elelist) * times)


if __name__ == '__main__':
    unittest.main()
