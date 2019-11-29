# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScoutItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SaichengItem(scrapy.Item):
    '''存储赛程信息'''
    lunci = scrapy.Field()
    bs_num_id = scrapy.Field()
    bs_time = scrapy.Field()
    host_team = scrapy.Field()
    h_team_id = scrapy.Field()
    res_score = scrapy.Field()
    guest_team = scrapy.Field()
    g_team_id = scrapy.Field()
    all_rang = scrapy.Field()
    half_rang = scrapy.Field()
    sizes_balls_a = scrapy.Field()
    sizes_balls_h = scrapy.Field()
    half_score = scrapy.Field()

    def get_insert_data(self):
        '''数据库执行sql语句'''
        insert_sql = 'INSERT INTO schedule_data values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = ( self['lunci'],self['bs_time'],self['host_team'],self['res_score'],self['guest_team'],
        self['all_rang'],self['half_rang'],self['sizes_balls_a'],self['sizes_balls_h'],self['half_score'])
        return insert_sql,data

'''
sql 建表 schedule_data 表

CREATE TABLE schedule_data(id INT PRIMARY KEY AUTO_INCREMENT,
lunci TINYINT,
bs_time VARCHAR(255),
host_team VARCHAR(255),
res_score VARCHAR(255),
guest_team VARCHAR(255),
all_rang VARCHAR(255),
half_rang VARCHAR(255),
sizes_balls_a VARCHAR(255),
sizes_balls_h VARCHAR(255),
half_score VARCHAR(255)
)DEFAULT CHARSET=utf8mb4;

'''
class Team_DataItem(scrapy.Item):

    '''存储队伍信息'''
    # define the fields for your item here like:
    # name = scrapy.Field()
    team_id = scrapy.Field()
    team_name = scrapy.Field()
    Eng_name = scrapy.Field()
    team_city = scrapy.Field()
    team_home = scrapy.Field()
    build_team_time = scrapy.Field()
    var_coach = scrapy.Field()
    team_youshi = scrapy.Field()
    team_style = scrapy.Field()
    team_ruodian = scrapy.Field()

    def get_insert_data(self):
        insert_sql = 'INSERT INTO team_data(team_id,team_name,Eng_name,team_city,team_home,build_team_time,var_coach,team_youshi,team_style,team_ruodian)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = (self['team_id'],self['team_name'],self['Eng_name'],self['team_city'],self['team_home'],self['build_team_time'],
        self['var_coach'],self['team_youshi'],self['team_style'],self['team_ruodian'])
        return insert_sql,data

'''
sql 建立team_data 球队信息表
CREATE TABLE team_data(id INT PRIMARY KEY AUTO_INCREMENT,
team_id INT,
team_name VARCHAR(20),
Eng_name VARCHAR(30),
team_city VARCHAR(30),
team_home VARCHAR(30),
build_team_time VARCHAR(20),
var_coach VARCHAR(20),
team_youshi VARCHAR(200),
team_style VARCHAR(200),
team_ruodian VARCHAR(200),
team_stats VARCHAR(300)
)DEFAULT CHARSET=utf8mb4;

'''
class Player_DataItem(scrapy.Item):
    '''存储球员信息'''
    play_id = scrapy.Field()
    c_number = scrapy.Field()
    c_name = scrapy.Field()
    fan_name = scrapy.Field()
    birthday = scrapy.Field()
    stature = scrapy.Field()
    weight = scrapy.Field()
    weizhi = scrapy.Field()
    nation = scrapy.Field()
    selfvalue = scrapy.Field()
    fin_date = scrapy.Field()
    youshi = scrapy.Field()
    style = scrapy.Field()
    ruodian = scrapy.Field()
    nowteam = scrapy.Field()

    def get_insert_data(self):
        insert_sql = '''INSERT INTO player_data(c_number,c_name,fan_name,birthday,stature,weight,weizhi,nation,selfvalue,fin_date,youshi,style,ruodian,nowteam)values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'''
        data = (self['c_number'],self['c_name'],self['fan_name'],self['birthday'],self['stature'],self['weight'],self['weizhi'],
        self['nation'],self['selfvalue'],self['fin_date'],self['youshi'],self['style'],self['ruodian'],self['nowteam'])
        return insert_sql,data

'''
建立 player_data球员信息表
CREATE TABLE player_data(id INT PRIMARY KEY AUTO_INCREMENT,
c_number VARCHAR(30),
c_name VARCHAR(30),
fan_name VARCHAR(30),
birthday VARCHAR(30),
stature VARCHAR(30),
weight VARCHAR(30),
weizhi VARCHAR(30),
nation VARCHAR(30),
selfvalue VARCHAR(230),
fin_date VARCHAR(230),
youshi VARCHAR(230),
style VARCHAR(230),
ruodian VARCHAR(230),
nowteam VARCHAR(230)
)DEFAULT CHARSET=utf8mb4;

'''