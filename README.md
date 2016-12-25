# eventor
使用多线程,进程以及协程实现的任务执行器,加快任务执行

# description

目前只有一个Eventor类,初始化参数如下:
- threadcount: 开启多少个线程 
- taskunitcount: 每个线程处理多少任务
- func: 实际的处理任务的函数, 自己实现
- interval: 线程间隔
- async: 同步异步

# exmaples

直接传递要处理的任务集合

    >>> from eventor import Eventor
    >>> elelist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> func = lambda x: x + 10
    >>> e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=1)
    >>> result = e.run_with_tasklist(elelist)
    >>> print(result)
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    
上述例子是开启3个线程,将任务(共有10个task)分割为每份3个task执行的, 间隔1s

处理文件和直接传递任务集合类似

    >>> from eventor import Eventor
    >>> file = "test/data.txt"
    >>> func = lambda x: int(x) + 10
    >>> e = Eventor(threadcount=3, taskunitcount=3, func=func, interval=1)
    >>> result = e.run_with_file(file)
    >>> print(result)
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


详细例子见 test/unittest.py 

Very stupid!

