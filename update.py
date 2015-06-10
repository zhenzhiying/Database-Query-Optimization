# -*- coding: utf-8 -*-

import MySQLdb
import csv

db = MySQLdb.connect(passwd="123123", db="test", host="10.131.237.11", user="root", charset='utf8')

cursor = db.cursor()

csv_file_path = './data.csv'

with open(csv_file_path, 'rb') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        row['shop_id'] = int(row['shop_id'])
        row['avg_price'] = int(row['avg_price'])
        row['is_chains'] = int(row['is_chains'])
        row['big_cate_id'] = int(row['big_cate_id'])
        if row['map_type'] == '':
            row['map_type'] = 0
        else:
            row['map_type'] = int(row['map_type'])
        row['city_id'] = int(row['city_id'])
        row['all_remarks'] = int(row['all_remarks'])
        row['very_good_remarks'] = int(row['very_good_remarks'])
        row['good_remarks'] = int(row['good_remarks'])
        row['common_remarks'] = int(row['common_remarks'])
        row['bad_remarks'] = int(row['bad_remarks'])
        row['very_bad_remarks'] = int(row['very_bad_remarks'])
        data.append(row)

def csv_decorator(func):
    def __decorator():
        for row in data:
            try:
                func(row)
            except MySQLdb.IntegrityError:
                pass
        db.commit()
    return __decorator

def get_table_columns(name):
    sql = "show columns in " + name
    cursor.execute(sql)
    columns = cursor.fetchall()
    keys = []
    for column in columns:
        key = str(column[0])
        keys.append(key)
    return keys

def get_table_names():
    sql = "show tables;"
    cursor.execute(sql)
    columns = cursor.fetchall()
    keys = []
    for column in columns:
        key = str(column[0])
        keys.append(key)
    return keys

def insert_data_to_table(table_name):
    columns = get_table_columns(table_name)

    @csv_decorator
    def insert(row):
        columns_str = "(" + ", ".join(columns) + ")"
        escape_str = "(" + ", ".join((["%s"] * len(columns))) + ");"
        keys = []
        for column in columns:
            keys.append(row[column])
        sql = "insert into " + table_name + columns_str + " values " + \
              escape_str
        cursor.execute(sql, tuple(keys))

    insert()

print "Start insertation"

tables = get_table_names()

for table in tables:
    insert_data_to_table(table)

print "Complete insertation"

db.close()
