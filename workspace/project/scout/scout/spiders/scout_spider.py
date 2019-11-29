# -*- coding: utf-8 -*-
import scrapy
from time import time,sleep
import time
import re
import requests
from fake_useragent import UserAgent
from scout.items import SaichengItem
from scout.items import Team_DataItem
from scout.items import Player_DataItem



class ScoutSpiderSpider(scrapy.Spider):
    '''定义爬虫名,域名'''
    name = 'scout_spider'
    allowed_domains = ['zq.win007.com']

    # 获取不同年份url,交给Scheduler
    def start_requests(self):
        now_time = time.strftime('%Y%m%d%H', time.localtime())  # 2019070616 时间戳
        url = 'http://zq.win007.com/jsData/matchResult/{}/s36.js?version={}'
        # js页面  http://zq.win007.com/jsData/matchResult/2003-2004/s36.js?version=2019070616
        date_lis = ['{}-{}'.format(i, i + 1) for i in range(2003,2020)] # 列表推导式,得到年份
        for date in date_lis:
            print("解析{}年..".format(date))
            req = scrapy.Request(url.format(date, now_time), callback=self.parse)   # 调用parse方法
            # sleep(1.5)
            req.meta['date'] = date
            req.meta['now_time'] = now_time
            yield req  # 将请求url的响应 yield出去

    # 获取每个队伍的id和队名,写到同一个列表里
    def team_data_id(self,response):
        pattern = re.compile("\[(\d+),'(.*?)'")
        ballteam = pattern.findall(response.text)[1:]
        lis_all_team = []
        for team_id_name in ballteam:
            lis_all_team.append(team_id_name[0])    # 队伍id
            lis_all_team.append(team_id_name[-1])   # 队伍名字
        return lis_all_team

    # 获取比赛轮次信息
    def parse(self, response):
        # 调用team_data_id函数,返回所有的每个队伍的id和队名lis_all_team
        lis_all_team = self.team_data_id(response)
        #获取每年所有队伍数据 38轮
        ball_lunci_team = re.findall('\[(\[\d{3,}.*?\])\];',response.text)
        num = 0
        #根据38轮遍历每一小轮
        for eve_turn in ball_lunci_team:
        #每小页数据,实例化item
            item = SaichengItem()
            num += 1
            # 每轮次的10条数据
            eve_turn_team = re.findall('\[\d{3,6}.*?\]',eve_turn)
            for eve_turn_team_data in eve_turn_team:
                #将每行数据转化为list类型 索引取值
                lis = eve_turn_team_data.strip('[|]').replace('\'','').split(',')
                #根据获取的战队id去之前的列表找索引位置
                index_num_h = lis_all_team.index(lis[4])
                index_num_g = lis_all_team.index(lis[5])
                item['lunci'] = num
                bs_num_id = lis[0]
                h_team_id = lis[4]
                item['bs_time'] = lis[3] #2014-05-04 23:00 <class 'str'>
                item['bs_num_id'] = bs_num_id   # 比赛的id
                item['host_team'] = lis_all_team[index_num_h+1]
                item['h_team_id'] = h_team_id
                item['res_score'] = lis[6]
                item['guest_team'] = lis_all_team[index_num_g+1]
                item['g_team_id'] = lis[5]
                item['all_rang'] = self.rangqiu(lis[10])
                item['half_rang'] = self.rangqiu(lis[11])
                item['sizes_balls_a'] = lis[12]
                item['sizes_balls_h'] = lis[13]
                item['half_score'] = lis[7]
                yield item
                
        team_url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/tdl{}.js?version={}'
        # 根据 偶数索引 取 球队id
        #['19', '阿森纳', '20', '阿斯顿维拉', '21', '布莱克本', '22', '博尔顿', '24', '切尔西', '25', '利物浦', '26', '曼彻斯特城', '27', '曼彻斯特联','29', '富勒姆', '31', '埃弗顿', '32', '伯明翰', '33', '托特纳姆热刺', '36', '朴茨茅斯', '46', '伯恩利', '52', '狼队', '58', '斯托克城','61', '维冈竞技', '62', '西汉姆联', '65', '桑德兰', '384', '赫尔城']
        for i in range(len(lis_all_team)):
            if i % 2 == 0:
                url = team_url.format(lis_all_team[i], response.meta['now_time'])
                req = scrapy.Request(url, callback=self.team_data)
                # sleep(0.5)
                req.meta['Referer'] = 'http://zq.win007.com/cn/team/Summary/{}.html'.format(lis_all_team[i])
                yield req



    # 球队信息
    def team_data(self, response):
        print("获取球队信息..")
        # 分析js页面,第一行数据有球队的所有信息
        teamDetail = re.findall('var teamDetail = \[(\d+.*)\]', response.text)
        teamDetail_lis = eval(teamDetail[0])
        # 获取教练,教练的格式不同
        var_coach = re.findall("var coach = \[\['\d+','','(.*?)','.*','.*',\d\]\];", response.text)
        item = Team_DataItem()
        team_id = teamDetail_lis[0]
        item['team_id'] = team_id
        item['team_name'] = teamDetail_lis[1]
        item['Eng_name'] = teamDetail_lis[3]
        item['team_city'] = teamDetail_lis[5]
        item['team_home'] = teamDetail_lis[8]
        item['build_team_time'] = teamDetail_lis[12]
        try:
            item['var_coach'] = var_coach[0]
        except:
            item['var_coach'] = 'NULL'

        # 球队特点
        item['team_youshi'] = str(re.findall('\[1,\d,"(.*?)\^', response.text))
        item['team_ruodian'] = str(re.findall('\[2,\d,"(.*?)\^', response.text))
        item['team_style'] = str(re.findall('\[3,\d,"(.*?)\^', response.text))
        yield item

        # 球员信息页面 js的 url
        re1 = time.strftime('%Y%m%d%H', time.localtime())
        url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/tdl{}.js?version={}'.format(team_id, re1)
        req = scrapy.Request(url, callback=self.player_info,dont_filter=True)
        # 测试时说超出域名范围,加上dont_filter=True,设置allowed_domains 的域名为非默认
        # sleep(0.5)
        yield req

    
    # 球员信息
    def player_info(self,response):
        item = Player_DataItem()
        # 从js 页面找到所有球员的部分信息在 var lineupDetail 里,正则取出
        lineupDetail = re.findall('var lineupDetail=\[(\[\d+.*\])\]', response.text)
        lineupDetail_lis = eval(lineupDetail[0])
        fun = lambda x: x if x else " "     # 处理空字符串
        for eve_player in lineupDetail_lis:
            # play_id = eve_player[0]
            item['play_id'] = eve_player[0]
            item['c_number'] = fun(eve_player[1])
            item['c_name'] = eve_player[2]
            item['fan_name'] = eve_player[3]
            item['birthday'] = eve_player[5]
            item['stature'] = eve_player[6]
            item['weight'] = eve_player[7]
            item['weizhi'] = eve_player[8]
            item['nation'] = eve_player[9]
            item['selfvalue'] = fun(eve_player[11])
            item['fin_date'] = fun(eve_player[12])
            yield self.parse_person(item)

    # 球员特点解析
    def parse_person(self,item):
        # 将球员特点单独拿出来,因为教练没有这些属性
        # teamDetail = re.findall('var teamDetail = \[(.?\d+.*),', response.text)
        # team_id = fun(eval(teamDetail[0])[0])
        l_time = time.strftime('%Y%m%d%H', time.localtime())
        requests.get('http://zq.win007.com/cn/team/Lineup/19.html')
        # url = 'http://zq.win007.com/jsData/playerInfo/player20972.js?version=2019070720'
        url = 'http://zq.win007.com/jsData/playerInfo/player{}.js?version={}'.format(item['play_id'], l_time)
        headers = {
            "user-agent": UserAgent().random,
            # "Referer": 'http://zq.win007.com/cn/team/player/{}/{}.html'.format(team_id,play_id)
            "referer": 'http://zq.win007.com/cn/team/Lineup/19.html'
        }
        try:
            response = requests.get(url, headers=headers)
            fun = lambda x: x if x else " "
            playerCharacter = fun(re.findall('var playerCharacter = \[(\[\d+.*\])\]', response.text))
            # print("整个特点:",playerCharacter)
            if playerCharacter == ' ':
                item['youshi'] = ''
                item['style'] = ''
                item['ruodian'] = ''
                item['nowteam'] = ''
            else:
                playerCharacter_lis = eval(playerCharacter[0])
                # print(str(playerCharacter_lis))
                # print("优势",re.findall('\[1, \d, .?(.*?)\^', str(playerCharacter_lis)))
                # print('style',re.findall('\[3, \d, .?(.*?)\^', str(playerCharacter_lis)))
                # print('ruodian',re.findall('\[2, \d, .?(.*?)\^', str(playerCharacter_lis)))
                item['youshi']= str(re.findall('\[1, \d, .?(.*?)\^', str(playerCharacter_lis)))
                item['style'] = str(re.findall('\[3, \d, .?(.*?)\^', str(playerCharacter_lis)))
                item['ruodian']= str(re.findall('\[2, \d, .?(.*?)\^', str(playerCharacter_lis)))
                # 现效力球队
                nowTeamInfo = re.findall("var nowTeamInfo = \[(\[\'\w+.*\])\]", response.text)
                nowTeamInfo_lis = eval(nowTeamInfo[0])
                if type(nowTeamInfo_lis[0]) == str:
                    item['nowteam'] = nowTeamInfo_lis[0]
                else:
                    item['nowteam'] = nowTeamInfo_lis[0][0]
            return item
        except Exception as e:
            self.parse_person(item)
            return item

    # 让球 输出转化
    def rangqiu(self, num):
        '''分析js数据,让数字转化为文字'''
        if num == '0':
            return '平手'
        elif num == '0.25':
            return '平/半'
        elif num == '0.5':
            return '半球'
        elif num == '0.75':
            return '半/一'
        elif num == '1':
            return '一球'
        elif num == '1.25':
            return '一/球半'
        elif num == '1.5':
            return '球半'
        elif num == '1.75':
            return '半/二'
        elif num == '2':
            return '二球'
        elif num == '2.25':
            return '二/半'
        elif num == '-0.25':
            return '*平/半'
        elif num == '-0.5':
            return '*半球'
        elif num == '-0.75':
            return '*半/一'
        elif num == '-1':
            return '*一球'
        elif num == '-1.25':
            return '*一/球半'
        elif num == '-1.5':
            return '*球半'
        else:
            return '暂未收录'