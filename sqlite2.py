import sqlite3
import os
#os.chdir('d:\\pycharm\\lesson\\sn01')

# conn = sqlite3.connect('D:\\pycharm\\lesson\\sn01\\SQL\\mytest.db')
conn = sqlite3.connect(r'./mytest.db')
cursor = conn.cursor()

# 查询所有的学生表
# sql = '''select * from students'''

''' 得到数据库中的名字'''
sql = "select rowid,  username from students"

# 执行语句
results = cursor.execute(sql)

# 遍历打印输出
all_students = results.fetchall()
for student in all_students:
    print(student)