#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask,request,render_template,redirect,url_for
#import pymysql.cursors
import psycopg2
import decimal
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from mailcode import send_mail
import mailconfig
import configparser
#gcheckcoden = random.randrange(1000, 9999, 1)

#具体的执行函数在此
def sqlexeccode(dbname,username,password,hostname,port,dmlarea):
    db = psycopg2.connect(dbname=dbname, user=username,password=password, host=hostname, port=port)
#   sqllist = dmlarea.strip().rstrip(";").split(";")
    execfinal=""
 #   for i in sqllist:

 #       print(db.dsn)
 #       print (i)

  #      execfinal+=i
    cur = db.cursor()
    cur.execute(dmlarea)
    db.commit()
    #cur.execute('commit')
    cur.close()
  #  print(execfinal)
##全库执行函数，函数可以执行到，但是没有加任何东西。
def alldatabaseexec(connstring,dmlarea):
    print(connstring,dmlarea)
    return("error")
    pass
#通过传入的参数来生成连接数据库的url
def sqldmlcheckexec(whoexec,dmlarea,sysid,gcheckcoden):
    cf = configparser.ConfigParser()
    cf.read("configureader.conf",encoding="utf-8-sig")
    secs = cf.sections()
    tag=sysid
    
 
    print(gcheckcoden)
 
    if request.method =='POST':
        checkcoden = request.form['checkcode']
        if checkcoden == str(gcheckcoden):
            #这里通过标记来分辨是否全库执行
            if tag=='全库':
                alldatabaseexec('11','22') 
            else:
                print (gcheckcoden,whoexec,dmlarea,sysid )
                sqlexeccode(cf.get(tag,'dbname'),cf.get(tag,'user'),cf.get(tag,'password'),cf.get(tag,'host'),cf.get(tag,'port'),dmlarea)
                return("ok")
        else:
            return("error")
  

