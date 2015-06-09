# -*- coding: utf-8 -*-

import MySQLdb
import csv

def reset():
    db = MySQLdb.connect(passwd="123123", db="test", host="10.131.237.11", user="root", charset='utf8')

    cursor = db.cursor()

    cursor.execute("""
    drop table if exists city_id_city_pinyin;
    drop table if exists city_id_province;
    drop table if exists shop_id_city_id;
    drop table if exists city_id_city;
    drop table if exists shop_id_area;
    drop table if exists shop_id_small_cate_id;
    drop table if exists shop_id_big_cate_id;
    drop table if exists big_cate_id_big_cate;
    drop table if exists small_cate_id_small_cate;
    drop table if exists map_info;
    drop table if exists dazhong;
    drop table if exists remark;
    drop table if exists discount;
    drop table if exists basic;

    create table if not exists basic(
    shop_id int not null,
    name char(50) not null,
    alias char(40) not null,
    address char(125) not null,
    phone char(30),
    hours char(200),
    avg_price smallint not null,
    payment char(10),
    is_chains tinyint,
    primary key(shop_id)
    );

    create table if not exists city_id_city(
    city_id smallint not null,
    city char(15) not null,
    primary key(city_id)
    );

    create table if not exists city_id_city_pinyin(
    city_id smallint not null,
    city_pinyin char(15) not null,
    primary key(city_id),
    foreign key(city_id) references city_id_city(city_id)
    );

    create table if not exists city_id_province(
    city_id smallint not null,
    province char(10) not null,
    primary key(city_id),
    foreign key(city_id) references city_id_city(city_id)
    );

    create table if not exists shop_id_city_id(
    shop_id int not null,
    city_id smallint not null,
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id),
    foreign key(city_id) references city_id_city(city_id)
    );

    create table if not exists shop_id_area(
    shop_id int not null,
    area char(40) not null,
    business_area char(30),
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id)
    );

    create table if not exists small_cate_id_small_cate(
    small_cate_id char(6) not null,
    small_cate char(20) not null,
    primary key(small_cate_id)
    );

    create table if not exists shop_id_small_cate_id(
    shop_id int not null,
    small_cate_id char(6) not null,
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id),
    foreign key(small_cate_id) references small_cate_id_small_cate(small_cate_id)
    );

    create table if not exists big_cate_id_big_cate(
    big_cate_id smallint not null,
    big_cate char(10) not null,
    primary key(big_cate_id)
    );

    create table if not exists shop_id_big_cate_id(
    shop_id int not null,
    big_cate_id smallint not null,
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id),
    foreign key(big_cate_id) references big_cate_id_big_cate(big_cate_id)
    );

    create table if not exists map_info(
    shop_id int not null,
    map_type tinyint not null,
    original_latitude float,
    original_longtitude float,
    google_latitude float,
    google_longtitude float,
    traffic char(10),
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id)
    );

    create table if not exists dazhong(
    shop_id int not null,
    navigation char(150) not null,
    recommended_dishes text,
    photos char(100) not null,
    description char(55),
    tags char(200),
    atmosphere char(10),
    nearby_shops char(10),
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id)
    );

    create table if not exists remark(
    shop_id int not null,
    product_rating float,
    environment_rating float,
    service_rating float,
    all_remarks int not null,
    very_good_remarks int not null,
    good_remarks int not null,
    common_remarks int not null,
    bad_remarks int not null,
    very_bad_remarks int not null,
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id)
    );

    create table if not exists discount(
    shop_id int not null,
    group_info text,
    card_info char(50),
    primary key(shop_id),
    foreign key(shop_id) references basic(shop_id)
    );
    """)

    db.close()

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
