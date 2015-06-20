# -*- coding: utf-8 -*-

import MySQLdb

def reset():
    db = MySQLdb.connect(passwd="123123", db="test", host="10.131.237.11", user="root", charset='utf8')

    cursor = db.cursor()

    with open('./init.sql', 'r') as f:
        sql = f.read()

        cursor.execute(sql)

    db.close()

print "Start reset"
reset()
print "Complete reset"
