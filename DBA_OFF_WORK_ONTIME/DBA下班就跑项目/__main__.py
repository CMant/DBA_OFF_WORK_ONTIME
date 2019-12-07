#!/usr/bin/env python
#-*- coding:utf-8 -*-
from flask import Flask,request,render_template,redirect,url_for,session
import decimal
import random
from wtforms import Form,TextField,PasswordField,validators
from mailcode import send_mail
from mailconfig import *
import os
import psycopg2
from datetime import timedelta
from sqldmlcheckexec import sqldmlcheckexec
from flask import g
import configparser
sqldmllist=None
app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
@app.route("/")
def index():   
    return app.send_static_file('index.html')
@app.route("/sqldml.html",methods=['GET','POST'])   
def sqldmld():
    cf = configparser.ConfigParser()
    cf.read("configureader.conf",encoding="utf-8-sig")
    secs = cf.sections()
 
    if request.method == 'POST':
    
        session['gwhoexec']= request.form['whoexec']

        session['gdmlarea']= request.form['dmlarea']
    
        session['gsysid']= request.form['sysid']
 
        session['code']=random.randrange(1000, 9999, 1)
        if session['gdmlarea'] == '':
            return redirect('http://www.example.com')
        else:
            sqllist = session['gdmlarea'].strip().rstrip(";").split(";")
        
        title = session['gwhoexec'] + '请求在' + session['gsysid'] + '执行sql' + '授权码' + str(session['code'])
        content = session['gdmlarea']
        send_mail(email_user, email_pwd, maillist, title, content)
        return redirect(url_for("sqldmlcheck"))
    return render_template('sqldml.html',u=secs)
@app.route("/sqldmlcheck.html",methods=['POST','GET'])
def sqldmlcheck():
    erocode=sqldmlcheckexec(session['gwhoexec'],session['gdmlarea'],session['gsysid'],session['code'])
    if erocode=="error":
        print(erocode)
        return render_template('errorpage.html')
    if erocode=="ok":
        return render_template('OK.html')
    return render_template('sqldmlcheck.html',u=session['code'])

if __name__ == '__main__':
    
    app.run(host='192.168.1.100', port=5000,debug=True)