#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/12/28 21:59'

"""
task with process
进程

"""

import attr
import multiprocessing
from multiprocessing import cpu_count


@attr.s
class ProcessCreator(object):

    processcount = attr.ib(default=10, convert=int)
    async = attr.ib(default=True, convert=bool)

    def run_multi_consumer(self, consumerfunc=None, initializer=None, callback=None, dataqueue=None, timeout=None):
        funclist = [consumerfunc, initializer, callback]
        self._valid_func(funclist)

        applylist = []
        with multiprocessing.Pool(processes=self.processcount, initializer=initializer) as pool:
            while not dataqueue.empty():
                if self.async:
                    applyresult = pool.apply_async(func=self._get_data_from_queue,
                                                   args=(dataqueue, consumerfunc), callback=callback)
                else:
                    applyresult = pool.apply(func=self._get_data_from_queue,
                                             args=(dataqueue, consumerfunc), callback=callback)
                applylist.append(applyresult.get(timeout))
            pool.close()
            pool.join()
        return applylist

    def _get_data_from_queue(self, dataqueue, consumerfunc):
        return consumerfunc(dataqueue.get(not self.async))

    def _valid_func(self, funclist=None):
        for func in funclist:
            if func and not callable(func):
                raise TypeError("func[{}] is not callable.".format(func))


def main():
    pass


if __name__ == '__main__':
    main()
