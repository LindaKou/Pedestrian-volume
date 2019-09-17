# # !/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# import queue
# import threading
# import time
#
# class WorkManager(object):
#     def __init__(self, work_num=1000,thread_num=2):
#         self.work_queue = queue.Queue()
#         self.threads = []
#         self.__init_work_queue(work_num)
#         self.__init_thread_pool(thread_num)
#
#     """
#         初始化线程
#     """
#     def __init_thread_pool(self,thread_num):
#         for i in range(thread_num):
#             self.threads.append(Work(self.work_queue))
#
#     """
#         初始化工作队列
#     """
#     def __init_work_queue(self, jobs_num):
#         for i in range(jobs_num):
#             self.add_job(do_job, i)
#
#     """
#         添加一项工作入队
#     """
#     def add_job(self, func, *args):
#         self.work_queue.put((func, list(args)))#任务入队，Queue内部实现了同步机制
#
#     """
#         等待所有线程运行完毕
#     """
#     def wait_allcomplete(self):
#         for item in self.threads:
#             if item.isAlive():item.join()
#
# class Work(threading.Thread):
#     def __init__(self, work_queue):
#         threading.Thread.__init__(self)
#         self.work_queue = work_queue
#         self.start()
#
#     def run(self):
#         #死循环，从而让创建的线程在一定条件下关闭退出
#         while True:
#             try:
#                 do, args = self.work_queue.get(block=False)#任务异步出队，Queue内部实现了同步机制
#                 do(args)
#                 self.work_queue.task_done()#通知系统任务完成
#             except:
#                 break
#
# #具体要做的任务
# def do_job(args):
#     time.sleep(0.1)#模拟处理时间
#     print(threading.current_thread(), list(args))
#
# if __name__ == '__main__':
#     start = time.time()
#     work_manager =  WorkManager(10000, 10)#或者work_manager =  WorkManager(10000, 20)
#     work_manager.wait_allcomplete()
#     end = time.time()
#     print("cost all time: %s" % (end-start))
# import threadpool
# def ThreadFun(arg1,arg2):
#     pass
# def main():
#     device_list=[]#需要处理的设备个数
#     task_pool=threadpool.ThreadPool(3)#8是线程池中线程的个数
#     request_list=[]#存放任务列表    #首先构造任务列表
#     for device in device_list:
#         request_list.append(threadpool.makeRequests(ThreadFun,[((device, ), {})]))    #将每个任务放到线程池中，等待线程池中线程各自读取任务，然后进行处理，使用了map函数，不了解的可以去了解一下。
#     map(task_pool.putRequest,request_list)    #等待所有任务处理完成，则返回，如果没有处理完，则一直阻塞
#     task_pool.poll()
# if __name__=="__main__":
#     main()
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time
import Shibie1
exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, video_name,location_id,location_site_max):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.video_name = video_name
        self.location_id=location_id
        self.location_site_max=location_site_max
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.video_name)
        print("%s"%(self.threadID))
        Shibie1.track_objects(self.video_name,self.location_id,self.location_site_max)
        print("Exiting " + self.video_name)


# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             (threading.Thread).exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1

def Main(video_name1,video_name2,video_name3,id1,id2,id3):
    thread1 = myThread(1, video_name1,id1)
    thread2 = myThread(2, video_name2,id2)
    thread3 = myThread(3, video_name3,id3)
    # 开启线程
    thread1.start()
    thread2.start()
    thread3.start()
    print("Exiting Main Thread")
