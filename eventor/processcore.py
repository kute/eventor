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


@attr.s
class ProcessCreator(object):

    processcount = attr.ib(default=10, convert=int)
    async = attr.ib(default=False, convert=bool)

    def run_multi_consumer(self, consumerfunc=None, initializer=None, aftercallback=None,
                           errorcallback=None, dataqueue=None, timeout=None):
        funclist = [consumerfunc, initializer, aftercallback, errorcallback]
        self._valid_func(funclist)

        applylist = []
        with multiprocessing.Pool(processes=self.processcount, initializer=initializer) as pool:
            while not dataqueue.empty():
                if self.async:
                    applyresult = pool.apply_async(func=self._get_data_from_queue,
                                                   args=(dataqueue, consumerfunc), callback=aftercallback,
                                                   error_callback=errorcallback).get(timeout)
                else:
                    applyresult = pool.apply(func=self._get_data_from_queue,
                                             args=(dataqueue, consumerfunc))
                applylist.append(applyresult)
            pool.close()
            pool.join()
        return applylist

    def _get_data_from_queue(self, dataqueue, consumerfunc):
        return consumerfunc(dataqueue.get(not self.async))

    def _valid_func(self, funclist=None):
        for func in funclist:
            if func and not callable(func):
                raise TypeError("func[{}] is not callable.".format(func.__class__.__name__))


def start_multi_consumer(consumercount=multiprocessing.cpu_count(), iterable=None, consumer_func=None, beforecallback=None,
                         aftercallback=None, errorcallback=None, async=False,
                         timeout=None):
    if not iterable or not iter(iterable):
        raise ValueError("parameter {} is not iterable.".format(iterable))
    if not callable(consumer_func):
        raise TypeError("{} is not callable.".format(consumer_func))
    sharequeue = multiprocessing.Manager().Queue()
    for ele in iterable:
        sharequeue.put_nowait(ele)
    creator = ProcessCreator(processcount=consumercount, async=async)
    result = creator.run_multi_consumer(consumer_func, beforecallback, aftercallback, errorcallback, sharequeue, timeout)
    return result
