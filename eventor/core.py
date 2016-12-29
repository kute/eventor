#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/12/24 20:45'

"""

多线程,协称 执行器
"""

from gevent import monkey
from gevent.pool import Pool
from multiprocessing import cpu_count
import time
import os
import attr


monkey.patch_all()


def valide_func(instance, attribute, value):
        if not callable(value):
            raise TypeError("{} is not callable")


@attr.s
class Eventor(object):

    func = attr.ib(validator=valide_func)
    taskunitcount = attr.ib(default=100, convert=int)
    threadcount = attr.ib(default=cpu_count() * 5, convert=int)
    interval = attr.ib(default=0, convert=int)

    def _slice_list_by_size(self, tasklist, slicesize):
        """按指定大小分隔集合
        """
        size = len(tasklist)
        if size <= slicesize:
            yield tasklist
        else:
            for i in list(range(0, size // slicesize + 1)):
                posi = i * slicesize
                templist = tasklist[posi: posi + slicesize]
                if len(templist) > 0:
                    yield templist

    def _run(self, pool, tasklist, async=False):
        if async:
            return pool.map_async(self.func, tasklist)
        else:
            return pool.map(self.func, tasklist)

    def run_with_tasklist(self, tasklist=None, async=False):
        if not tasklist or len(tasklist) == 0:
            raise ValueError("parameters tasklist null value")
        if not isinstance(tasklist, list):
            raise ValueError("parameters tasklist wrong type, should be list, not {}".format(tasklist.__class__.__name__))
        if not callable(self.func):
            raise ValueError("func is illegal function")
        threadcount = self.threadcount or cpu_count() * 5
        taskunitcount = self.taskunitcount or 100
        pool = Pool(threadcount)
        size = len(tasklist)
        total = 0
        resultlist = []
        if size <= taskunitcount:
            result = self._run(pool, tasklist, async)
            resultlist.extend(result)
            print("finished {} total tasks".format(size))
        else:
            for slicelist in self._slice_list_by_size(tasklist, taskunitcount):
                result = self._run(pool, slicelist, async)
                resultlist.extend(result)
                total += len(slicelist)
                time.sleep(self.interval)
            print("finished {} total tasks".format(total))
        return resultlist

    def run_with_file(self, file=None, async=False):
        if not os.path.exists(file) or not os.path.isfile(file):
            raise ValueError("wrong file or not exists")
        if not callable(self.func):
            raise ValueError("func is illegal function")
        threadcount = self.threadcount or cpu_count() * 5
        taskunitcount = self.taskunitcount or 100
        pool = Pool(threadcount)
        plist = []
        total = 0
        resultlist = []
        with open(file, "r") as f:
            for line in f:
                plist.append(line.strip())
                if len(plist) >= taskunitcount:
                    result = self._run(pool, plist, async)
                    resultlist.extend(result)
                    total += len(plist)
                    plist.clear()
                    time.sleep(self.interval)
            if len(plist) > 0:
                result = pool.map(self.func, plist)
                resultlist.extend(result)
                total += len(plist)
                plist.clear()
            print("finished {} total tasks".format(total))
        return resultlist