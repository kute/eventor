# eventor
使用多线程,进程以及协程实现的任务执行器,加快任务执行

# description

1.Eventor类,初始化参数如下:
- threadcount: 开启多少个线程 
- taskunitcount: 每个线程处理多少任务
- func: 实际的处理任务的函数, 自己实现
- interval: 线程间隔
- async: 同步异步

2.start_multi_consumer方法, 场景:模拟多个消费者(进程) 消费共享资源, 参数如下:
- consumercount: 开启的消费者(进程)个数,默认 cput_count()
- iterable=None: 共享资源
- consumer_func=None: 具体的消费行为
- beforecallback=None: 每个消费者开启之前调用
- aftercallback=None: 每个消费者执行消费行为之后调用(仅当 arsync=True)
- errorcallback=None: 异常回调(仅当 arsync=True)
- async=False: 消费方式(同步or异步)
- timeout=None: 超时时间(仅当 arsync=True)

# exmaples

exmaple-1: 直接传递要处理的任务集合

    >>> from eventor import Eventor
    >>> elelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> func = lambda x: x + 10
    >>> e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=1)
    >>> result = e.run_with_tasklist(elelist)
    >>> print(result)
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    
上述例子是开启3个线程,将任务(共有10个task)分割为每份3个task执行的, 间隔1s

exmaple-2: 处理文件和直接传递任务集合类似

    >>> from eventor import Eventor
    >>> file = "test/data.txt"
    >>> func = lambda x: int(x) + 10
    >>> e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=1)
    >>> result = e.run_with_file(file)
    >>> print(result)
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

exmaple-3: 开启 4 个进程, 每个进程打印 当前进程名以及准备消费的 数据

    >>> from multiprocessing import cpu_count
    >>> from eventor import start_multi_consumer
    >>> consumer_count = 4
    >>> def confunc(data):
    ....    print("process[{}] deal with {}".format(multiprocessing.current_process().name, data))
    >>> datalist = [1, 2, 5, 3, 6, 8, 23, 'data', 232]
    >>> start_multi_consumer(consumercount=consumer_count, iterable=datalist, consumer_func=confunc)
    process[ForkPoolWorker-3] deal with 1
    process[ForkPoolWorker-2] deal with 2
    process[ForkPoolWorker-4] deal with 5
    process[ForkPoolWorker-5] deal with 3
    process[ForkPoolWorker-3] deal with 6
    process[ForkPoolWorker-2] deal with 8
    process[ForkPoolWorker-4] deal with 23
    process[ForkPoolWorker-5] deal with data
    process[ForkPoolWorker-3] deal with 232



Very stupid!

