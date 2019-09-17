import SqlDao
import pymysql
from flask import Flask, render_template, request, json

def load_time(location_id):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT time_num from pedestrian_flow_information where location_id='%s'"%(location_id)
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()


def search_image_num(location_id):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT image_num from pedestrian_flow_information where location_id='%s'"%(location_id)
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()


def loaduser_id(username):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT user_id from user where username='%s'"%(username)
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()

def loadlocation_site(result):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT location_site from location_information where user_id='%s'"%(result)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()

def seach_location_max(location_site):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT location_max FROM location_information where location_site='%s'"%(location_site)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()
def seach_location_max1(location_id):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT location_max FROM location_information where location_id='%s'"%(location_id)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()
def search_location_all(location_site):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT * FROM location_information where location_site='%s'"%(location_site)
        cursor.execute(sql)
        result=cursor.fetchone()
        return result
    except:
        db.rollback()
    cursor.close()

def search_location_id(location_site):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT location_id from location_information where location_site='%s'"%(location_site)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchone()
        return result
    except:
        db.rollback()
    cursor.close()
def loadlocation_id(user_id):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="SELECT location_id from location_information where user_id='%s'"%(user_id)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
    except:
        db.rollback()
    cursor.close()
# def search_data(result,date):
#     db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
#     cursor = db.cursor()
#     try:
#         sql="SELECT abnormal_time_num from abnormal_information where location_id='%s' ans date='%s'"
#         cursor.execute(sql)
#
#     except:
#         db.rollback()
#     cursor.close()
#本周搜索
def total_num_week(start_time,end_time):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="select abnormal_time_num as totalmoney from abnormal_information where date BETWEEN '%s' AND '%s'"%(start_time,end_time)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()
#本日搜索
def total_num_day(start_time):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="select abnormal_time_num as totalmoney from abnormal_information where date ='%s'"%(start_time)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()
#本月搜索
def total_num_month(start_time,end_time,location_site):
#def total_num_month():
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        id=search_location_id(location_site)
        for item in id:
            #sql="select abnormal_time_num as totalmoney from abnormal_information where date BETWEEN '2019-05-01' AND '2019-05-31'"
            sql="select abnormal_time_num as totalmoney from abnormal_information where location_id='%s' and  date BETWEEN '%s' AND '%s'"%(item,start_time,end_time)
            print(sql)
            cursor.execute(sql)
            result=cursor.fetchall()
            print(result)
        return result
    except:
        db.rollback()
    cursor.close()
#任意选中天数
def total_num(start_time,end_time):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql="select abnormal_time_num as totalmoney from abnormal_information where date BETWEEN '%s' AND '%s'"%(start_time,end_time)
        print(sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        return result
    except:
        db.rollback()
    cursor.close()
def search_data(result,date):
    db = pymysql.connect(host="localhost", user="root", password="582607", database="ggdd", port=33060)
    cursor = db.cursor()
    try:
        sql1="SELECT abnormal_time_num from abnormal_information where location_id='%s' and date='%s'"%(result,date)
        cursor.execute(sql1)
        result1=cursor.fetchone()
        return result1
    except:
        db.rollback()

    cursor.close()
