# -*- coding: utf-8 -*-

import MySQLdb
import csv

db = MySQLdb.connect(passwd="123123", db="test", host="10.131.237.11", user="root", charset='utf8')

cursor = db.cursor()

csv_file_path = './data.csv'

# with open(csv_file_path, 'rb') as f:
#     # try:
#     print "Start"
#     reader = csv.DictReader(f)
#     city = {}
#     for row in reader:
#         id = int(row['city_id'])
#         if id not in city.keys() and row['city'] != '':
#             city[id] =row['city']

    # for key in city.keys():
    #     cursor.execute("""insert into city_id_city (city_id, city)
    #                     values (%s, %s);""", (key, city[key]))
    # db.commit()
    # print "Done"
    # # except:
    # #     print "Error"
    # # finally:
    # db.close()


def csv_decorator(func):
    def __decorator():
        with open(csv_file_path, 'rb') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    func(row)
                except MySQLdb.IntegrityError:
                    pass
        db.commit()
    return __decorator

@csv_decorator
def city_id_city(row):
    city_id = int(row['city_id'])
    city = row['city']
    cursor.execute("""insert into city_id_city (city_id, city)
                    values (%s, %s);""", (city_id, city))

@csv_decorator
def basic(row):
    shop_id = int(row['shop_id'])
    name = row['name']
    alias = row['alias']
    address = row['address']
    phone = row['phone']
    hours = row['hours']
    avg_price = int(row['avg_price'])
    payment = row['payment']
    is_chains = int(row['is_chains'])

    cursor.execute("""insert into basic ( shop_id, name, alias, address, phone, hours, avg_price, payment, is_chains)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", ( shop_id, name, alias, address, phone, hours, avg_price, payment, is_chains, ))

@csv_decorator
def city_id_city_pinyin(row):
    city_id = int(row['city_id'])
    city_pinyin = row['city_pinyin']

    cursor.execute("""insert into city_id_city_pinyin (city_id, city_pinyin)
                    values (%s, %s);""", (city_id, city_pinyin))

@csv_decorator
def city_id_province(row):
    city_id = int(row['city_id'])
    province = row['province']

    cursor.execute("""insert into city_id_province (city_id, province)
                    values (%s, %s);""", (city_id, province))

@csv_decorator
def shop_id_city_id(row):
    shop_id = int(row['shop_id'])
    city_id = row['city_id']

    cursor.execute("""insert into shop_id_city_id (shop_id, city_id)
                    values (%s, %s);""", (shop_id, city_id))

@csv_decorator
def shop_id_area(row):
    shop_id = int(row['shop_id'])
    area = row['area']
    business_area = row['business_area']

    cursor.execute("""insert into shop_id_area (shop_id, area, business_area)
                    values (%s, %s, %s);""", (shop_id, area, business_area))

@csv_decorator
def small_cate_id_small_cate(row):
    small_cate_id = row['small_cate_id']
    small_cate = row['small_cate']

    cursor.execute("""insert into small_cate_id_small_cate (small_cate_id, small_cate)
                    values (%s, %s);""", (small_cate_id, small_cate))

print "Start"

basic()
city_id_city()
city_id_city_pinyin()
city_id_province()
shop_id_city_id()
shop_id_area()
small_cate_id_small_cate()

print "Complete"

db.close()
