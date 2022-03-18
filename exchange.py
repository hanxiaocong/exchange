#!/usr/bin/python

import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='43.129.207.250',
                     user='quick_ins_dev',
                     password='cxX6S5nNkb3DNWTG',
                     database='quick_ins_dev')
#读入数据
f = open("acc.txt","r+")   #打开文件夹
list = f.readlines()

#获取游标对象
cursor = db.cursor()
sql = "INSERT INTO `quick_ins_dev`.`account` (cookie,username) values(%s,%s)"

for i in  range(0,len(list)):
    str = (list[i].split("|"))

    str[2]=str[2].replace("\\054",",")#替换054为逗号
    str[2]=str[2].replace("\"","")#替换054为逗号
   
    cookie = str[2]
    username = str[0]

    values = (cookie,username)

    print(values)
    cursor.execute(sql, values)
    #写入本地文档
    c = open("out.txt","a")
    c.write(str[2])
    c.write("\n")
    c.close() 

cursor.close()
db.commit()
db.close()