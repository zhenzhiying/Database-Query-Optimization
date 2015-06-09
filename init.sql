drop table if exists basic;
drop table if exists city_id_city_pinyin;
drop table if exists city_id_province;
drop table if exists city_id_city;

show tables;

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
