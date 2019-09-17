from flask import Flask, render_template, request, json
import control
import re
import Shibie1
import SqlDao
import Xiancheng
import pymysql
import numpy as np
import cv2
import os
import collections
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import matplotlib
import json
import datetime



import sys
app = Flask(__name__)
db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
cursor = db.cursor()
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/login', methods=['POST'])
def Login():
    username = str(json.loads(request.values.get("userName")))
    password = str(json.loads(request.values.get("password")))
    print(username)
    print(password)
    sql = "SELECT * from user where username='%s'and password='%s' " % (username, password)
    print(sql)
    cursor.execute(sql)
    result1 = cursor.fetchall()
    sql1 = "SELECT * from user where username='%s'and password='%s' " % (username, password)
    print(sql1)
    cursor.execute(sql1)
    result = cursor.rowcount
    print(result)
    if result == 1:
        res="0"
        return json.dumps({'res':res,'username': username}, ensure_ascii=False)
    else:
        print(result)
        res="1"
        return json.dumps({'res':res,'username': username}, ensure_ascii=False)


@app.route('/regist', methods=['POST'])
def regist():
    username = str(json.loads(request.values.get("username")))
    password = str(json.loads(request.values.get("password")))
    phonenumber = str(json.loads(request.values.get("phonenumber")))
    # print(username)
    print(password)
    # print(user_iden)
    print(phonenumber)
    # sql="INSERT INTO user (username,password,phonenumber,user_iden) values(%s,%s,%s)"%(username,password,phonenumber,user_iden)
    sql = "INSERT INTO user (username,password,phonenumber,user_iden) values('%s','%s','%s')" % (username, password, phonenumber)
    print(sql)
    cursor.execute(sql)
    db.commit()
    res = '1'
    return json.dumps(res)


@app.route('/getUserByLoginName', methods=['POST'])
def getUserByLoginName():
    username = str(json.loads(request.values.get("loginName")))
    print(username)
    sql = "SELECT * from user where username='%s'" % (username)
    print(sql)
    cursor.execute(sql)
    result = cursor.rowcount

    print(result)
    if result == 1:
        res = '0'
        return json.dumps(res)
    else:
        res = '1'
        return json.dumps(res)


@app.route('/Shibie/track_objects', methods=['GET', 'POST'])
def Start():
        username = str(json.loads(request.values.get("loginName")))
        #username="寇肖萌"
        id=SqlDao.loaduser_id(username)
        result=SqlDao.loadlocation_id(id)
        print(result)
        num1=1
        num=len(result)
        for item in result:
            result1=SqlDao.seach_location_max1(item[0])
            for item1 in result1:
                print(item1)
                thread1 = Xiancheng.myThread(num1, "test_videos/test"+str(item[0])+".mp4",item[0],item1[0])
            num1+=1
            while num1>num:
                break
        # thread2 = myThread(2, video_name2,id2)
        # thread3 = myThread(3, video_name3,id3)
            thread1.start()
        # Xiancheng.Main("test_videos/test1.mp4","test_videos/test2.mp4","test_videos/test3.mp4",1,2,3)
        res="1"
        return json.dumps(res)
        # location_site=str(json.loads(request.values.get('location_site')))
        # print(location_site)
        # id=SqlDao.search_location_id(location_site)
        # print(id)
        # for item in id:
        #     print(item)
        #     video="test_videos/test"+str(item)+".mp4"
        #     print(video)
        #     cap = cv2.VideoCapture(video)
        #     ret, frame = cap.read()
        #     #print(frame)
        #     #print(video)
        #     Shibie1.track_objects(video)
        #     return json.dumps(Shibie1.track_objects(video))

@app.route('/GetAdress',methods=['POST'])
def load_adress():
    username = str(json.loads(request.values.get("loginName")))
    print(username)
    result=SqlDao.loaduser_id(username)
    result1=SqlDao.loadlocation_site(result)
    print(result1)
    return json.dumps({'adress':result1},ensure_ascii=False)
@app.route('/load_max',methods=['GET','POST'])
def load_max():
    location_site=str(json.loads(request.values.get('location_site')))
    result=SqlDao.search_location_all(location_site)
    return json.dumps(result,ensure_ascii=False)
#按月计算异常数据值
@app.route('/total_time',methods=['GET','POST'])
def total_data_time():
    location_site=str(json.loads(request.values.get('location_site')))
    print(location_site)
    start_time=str(json.loads(request.values.get('startTime')))
    print(start_time)
    end_time=str(json.loads(request.values.get('endTime')))
    print(end_time)
    result=[]
    result=SqlDao.total_num_month(start_time,end_time,location_site)
    #result=SqlDao.total_num_month()
    result1=[]
    listtime=[]
    result3=[]
    data=[]
    num1=0
    max=0
    num=[]
    sum=0
    average1=0
    average=[]
    for item in result:
        result2=list(item)
        print(result2)
        for item1 in result2:
            listtime=re.split(r";|,",str(item1))
            print(listtime)
            print(int((len(listtime)-1)/2))
            num.append(int((len(listtime)-1)/2))
            print(num)
            for k in range(len(listtime)):
                print(listtime[k])
                if k%2==1:
                    sum=sum+int(listtime[k])
                    if max<int(listtime[k]):
                        max=int(listtime[k])
                        print(max)

                else:
                    continue
                num1+=1
            average1=sum/(int((len(listtime)-1)/2))
            print(average1)
            data.append(max)
            average.append(average1)
            print(average)
            max=0
            sum=0
        print(data)
    print(data)
    time=[]
    timelist1 = start_time.split("-")
    timelist1 = [int(x) for x in timelist1]
    year1 = timelist1[0]
    month1 = timelist1[1]
    day1 = timelist1[2]
    begin = datetime.date(year1,month1,day1)
    print(begin)
    timelist2 = end_time.split("-")
    timelist2 = [int(x) for x in timelist2]
    year2 = timelist2[0]
    month2 = timelist2[1]
    day2 = timelist2[2]
    end = datetime.date(year2,month2,day2)
    print(end)
    for i in range((end - begin).days+1):
        day = begin + datetime.timedelta(days=i)
        time.append(str(day))
        print(time)

    # datestart=datetime.datetime.strptime(start_time,'%Y-%m-%d')
    # dateend=datetime.datetime.strptime(end_time,'%Y-%m-%d')
    # while datestart<dateend:
    #     datestart+=datetime.timedelta(days=1)
    #     print(datestart.strftime('%Y-%m-%d'))
    #     time.append(datestart.strftime('%Y-%m-%d'))
    #     result1.extend(result2)
    # print(result1)
    # for ite in result1:
    #     print(ite)
    #     listtime=re.split(r";|,", str(ite))
    #     print(listtime)
    #     for item2 in listtime:
    #         print(item2)
    #         if len(item2)==0:
    #             continue;
    #         else:
    #             result3.append(item2)
    # print(result3)
    # k=0
    # num1=0
    # data=[]
    # time=[]
    # for k in range(len(result3)-int(len(result3))%2):
    #     if num1==1:
    #         data.append(result3[k])
    #     else:
    #         num1=0
    #         time.append(result3[k])
    #     num1+=1
    # print(data)
    # print(time)
    # sum=0
    # for item1 in data:
    #     print(item1)
    #     sum=sum+int(item1)
    # print(sum)
    # average=sum/len(data)
    return json.dumps({'data':data,'time':time,'num':num,'average':average}, ensure_ascii=False)
#按月计算异常数据值
@app.route('/total_data_week',methods=['GET','POST'])
def total_data_week():
    result=[]
    result=SqlDao.total_num_month()
    result1=[]
    listtime=[]
    result3=[]
    data=[]
    num1=0
    max=0
    for item in result:
        result2=list(item)
        print(result2)
        for item1 in result2:
            listtime=re.split(r";|,",str(item1))
            print(listtime)
            for k in range(len(listtime)):
                print(listtime[k])
                if k%2==1:
                    if max<int(listtime[k]):
                        max=int(listtime[k])
                        print(max)

                else:
                    continue
                num1+=1
            data.append(max)
            max=0
        print(data)
    print(data)
    #     result1.extend(result2)
    # print(result1)
    # for ite in result1:
    #     print(ite)
    #     listtime=re.split(r";|,", str(ite))
    #     print(listtime)
    #     for item2 in listtime:
    #         print(item2)
    #         if len(item2)==0:
    #             continue;
    #         else:
    #             result3.append(item2)
    # print(result3)
    # k=0
    # num1=0
    # data=[]
    # time=[]
    # for k in range(len(result3)-int(len(result3))%2):
    #     if num1==1:
    #         data.append(result3[k])
    #     else:
    #         num1=0
    #         time.append(result3[k])
    #     num1+=1
    # print(data)
    # print(time)
    # sum=0
    # for item1 in data:
    #     print(item1)
    #     sum=sum+int(item1)
    # print(sum)
    # average=sum/len(data)
    return json.dumps({'data':data}, ensure_ascii=False)
@app.route('/Shibie1',methods=['GET','POST'])
def load_data():
       #username = str(json.loads(request.values.get("loginName")))
       username="寇肖萌"
       print(username)
       user_id=SqlDao.loaduser_id(username)
       location_site=list(SqlDao.loadlocation_site(user_id))
       print(location_site)
       data1=[]
       time1=[]
       max1=[]
       baojing=[]
       location=[]
       image_num_all=[]
       for item in location_site:
           location.append(item)
           id=SqlDao.search_location_id(item)
           max=SqlDao.seach_location_max(item)
           print(max)

           image_num=SqlDao.search_image_num(id)
           for item in image_num:
               print(item)
               image_num_all.append(item)
           result1=list(SqlDao.load_time(id))
           print(result1)
           listtime=[]
           for ite in result1:
               #print(ite)
               listtime=re.split(r";|,", str(ite))
               # print(listtime)
           k=0
           num1=0
           data=[]
           time=[]
           for k in range(len(listtime)-int(len(listtime))%2):
               if num1==1:
                   data.append(listtime[k])
               else:
                   num1=0
                   time.append(listtime[k])
               num1+=1
           for item in max:
               if item>data[len(data)-1]:
                   baojing.append(1)
               else:
                   baojing.append(0)
               max1.append(item)
           print(baojing)
           data1.append(data)
           time1.append(time)
           print(data1)
           print(time1)
           print(max1)
       print(image_num_all)
       return json.dumps({'data':data1, 'time':time1,'max':max1,'location_site':location,'baojing':baojing,'image_num':image_num_all}, ensure_ascii=False)
       #return json.dumps(data,ensure_ascii=False)
@app.route('/Search',methods=['GET','POST'])
def search():
    date = str(json.loads(request.values.get("date")))
    location_site=str(json.loads(request.values.get('location_site')))
    result=SqlDao.search_location_id(location_site)
    result1=list(SqlDao.search_data(result,date))
    print(result1)
    listtime=[]
    for ite in result1:
        #print(ite)
        listtime=re.split(r";|,", str(ite))
        # print(listtime)
    k=0
    num1=0
    data=[]
    time=[]
    for k in range(len(listtime)-int(len(listtime))%2):
        if num1==1:
            data.append(listtime[k])
        else:
            num1=0
            time.append(listtime[k])
        num1+=1
    # print(data)
    # print(time)
    return json.dumps({'data':data, 'time':time}, ensure_ascii=False)
if __name__ == '__main__':
    # total_data_month()
    #Start()
    #total_data_time()
    debug=True
    app.run()
    #load_data()












