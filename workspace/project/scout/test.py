import requests
import re
import time
from lxml import etree
from time import time,sleep
from fake_useragent import UserAgent


url = 'http://zq.win007.com/jsData/matchResult/2004-2005/s36.js?version=2019070809'
headers = {
    'Referer': 'http://zq.win007.com/cn/League/2003-2004/36.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
response = requests.get(url,headers = headers)
# print(response.text)

ball_lunci_team = re.findall('\[(\[\d{3,}.*?\])\];',response.text)
# print(ball_lunci_team)
pat = re.compile("\[(\d+),'(.*?)'")
ballteam = pat.findall(response.text)[1:]
lis_all_team = []
for item in ballteam:
    lis_all_team.append(item[0])
    lis_all_team.append(item[-1])
# print("lis_all_team",lis_all_team)
num = 0
#根据38轮遍历每一小轮
for eve_turn in ball_lunci_team:
#每小页数据,实例化item
    num += 1
    # 每轮次的10条数据
    # print(eve_turn)
    # [473,36,-1,'2004-08-14 19:45',33,25,'1-1','0-1','','',,,'','',0,1,1,1,0,0,'','',''],[474,36,-1,'2004-08-14 22:00',20,30,'2-0','2-0','','',,,'','',0,1,1,1,0,0,'','',''],[475,36,-1,'2004-08-14 22:00',21,18,'1-1','0-1','','',,,'','',0,1,1,1,0,0,'','',''],[476,36,-1,'2004-08-14 22:00',22,23,'4-1','2-0','','',,,'','',0,1,1,1,0,0,'','',''],[478,36,-1,'2004-08-14 22:00',36,32,'1-1','1-1','','',,,'','',0,1,1,1,0,0,'','',''],[477,36,-1,'2004-08-14 22:00',34,35,'1-1','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[479,36,-1,'2004-08-14 22:05',26,29,'1-1','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[480,36,-1,'2004-08-15 00:15',17,28,'2-2','0-1','','',,,'','',0,1,1,1,0,0,'','',''],[481,36,-1,'2004-08-15 21:00',31,19,'1-4','0-2','','',,,'','',0,1,1,1,0,0,'','',''],[20412,36,-1,'2004-08-15 23:05',24,27,'1-0','1-0','','',,,'','',0,1,1,1,0,0,'','','']
    # [483,36,-1,'2004-08-21 19:45',30,21,'3-2','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[487,36,-1,'2004-08-21 22:00',29,22,'2-0','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[484,36,-1,'2004-08-21 22:00',32,24,'0-1','0-0','','',,,'','',0,1,1,1,0,0,'','',''],[488,36,-1,'2004-08-21 22:00',25,26,'2-1','0-1','','',,,'','',0,1,1,1,0,0,'','',''],[486,36,-1,'2004-08-21 22:00',35,31,'1-3','1-1','','',,,'','',0,1,1,1,0,0,'','',''],[485,36,-1,'2004-08-21 22:00',23,36,'2-1','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[489,36,-1,'2004-08-21 22:00',28,33,'0-1','0-0','','',,,'','',0,1,1,1,0,0,'','',''],[20613,36,-1,'2004-08-22 00:15',27,34,'2-1','1-0','','',,,'','',0,1,1,1,0,0,'','',''],[491,36,-1,'2004-08-22 20:00',18,20,'1-1','1-1','','',,,'','',0,1,1,1,0,0,'','',''],[492,36,-1,'2004-08-22 23:05',19,17,'5-3','1-1','','',,,'','',0,1,1,1,0,0,'','','']

    eve_turn_team = re.findall('\[\d{3,6}.*?\]',eve_turn)
    # print(eve_turn_team)
    for eve_turn_team_data in eve_turn_team:
        #将每行数据转化为list类型 索引取值
        lis = eve_turn_team_data.strip('[|]').replace('\'','').split(',')
        #根据获取的战队id去之前的列表找索引位置
        index_num_h = lis_all_team.index(lis[4])
        index_num_g = lis_all_team.index(lis[5])
        lunci = num
        bs_num_id = lis[0]
        h_team_id = lis[4]
        bs_time = lis[3] #2014-05-04 23:00 <class 'str'>
        host_team = lis_all_team[index_num_h+1]
        res_score = lis[6]
        guest_team = lis_all_team[index_num_g+1]
        g_team_id = lis[5]
        sizes_balls_a = lis[12]
        sizes_balls_h = lis[13]
        half_score = lis[7]
        print(lunci ,bs_num_id, h_team_id,bs_time,host_team,res_score,guest_team,g_team_id,sizes_balls_a)
#
#
#
# str = "'akdjhakjh'"
# print(re.findall("(\w+.*)\'",str)[0])
# url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/tdl19.js?version=2019070717'
# headers = {
#     'Referer': 'http://zq.win007.com/cn/team/player/19/20972.html',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# response = requests.get(url,headers = headers)
# # print(response.text)
# teamDetail = re.findall('var teamDetail = \[(\d+.*),',response.text)
# team_id_lis = eval(teamDetail[0])
# print(team_id_lis[0])
# for eve_id in team_id_lis:
#     print(eve_id)
# lineupDetail = re.findall('var lineupDetail=\[(\[\d+.*\])\]', response.text)
# lineupDetail_lis = eval(lineupDetail[0])
# print(lineupDetail_lis)
# for eve_player in lineupDetail_lis[1:]:
#     play_id = eve_player[0]
#     number = eve_player[1]
#     c_name = eve_player[2]
#     fan_name = eve_player[3]
#     birthday = eve_player[5]
#     stature = eve_player[6]
#     weight = eve_player[7]
#     weizhi = eve_player[8]
#     nation = eve_player[9]
#     selfvalue = eve_player[11]
#     fin_date = eve_player[12]
#     # print(play_id,number,c_name,fan_name,birthday,stature,weight,weizhi,nation,selfvalue,fin_date)
url = 'http://zq.win007.com/jsData/playerInfo/player102987.js?version=2019070809'
headers = {
    "user-agent": UserAgent().random,
    "referer": "http://zq.win007.com/cn/team/Lineup/19.html"
}
response = requests.get(url, headers=headers)
# print(response.text)
playerCharacter = re.findall('var playerCharacter = \[(\[\d+.*\])\]', response.text)
print("球员特点集合:",playerCharacter)

playerCharacter_lis = eval(playerCharacter[0])
# for playerCharacter_lis_data in playerCharacter_lis:
#     print(playerCharacter_lis_data)
youshi = re.findall('\[1, \d, .?(.*?)\^',str(playerCharacter_lis))
style = re.findall('\[3, \d, .?(.*?)\^',str(playerCharacter_lis))
ruodian = re.findall('\[2, \d, .?(.*?)\^',str(playerCharacter_lis))
nowTeamInfo = re.findall("var nowTeamInfo = \[(\[\'\w+.*\])\]", response.text)
nowTeamInfo_lis = eval(nowTeamInfo[0])
print(nowTeamInfo_lis[0])
print(type(nowTeamInfo_lis[0]),len(nowTeamInfo_lis[0]))
if type(nowTeamInfo_lis[0]) == str:
    nowteam = nowTeamInfo_lis[0]
else:
    nowteam = nowTeamInfo_lis[0][0]
print("现效力:",nowteam)
#     except:
#         youshi = []
#         style = []
#         ruodian = []
#         nowteam = []
#     print(play_id,number,c_name,fan_name,birthday,stature,weight,weizhi,nation,selfvalue,fin_date)
#     print(" 优势",youshi," 风格" , style,  "弱点",ruodian,"效力:",nowteam)


# str1 = 'var playerCharacter = [[1,1,"争高空球^爭高空球"],[1,1,"带球^帶球"],[1,2,"拦截^攔截"],[3,1,"喜欢带球^喜歡帶球"],[3,2,"喜欢对抗^喜歡對抗"],[1,2,"截球^截球"],[1,2,"防守贡献^防守貢獻"]];'
# playerCharacter = re.findall('var playerCharacter = \[(\[\d+.*\])\]', str1)
# playerCharacter_lis = eval(playerCharacter[0])
# print(playerCharacter_lis)
# for i in playerCharacter_lis:
#     print(re.findall('\[1, \d, .?(.*?)\^', str(i)))



# teamDetail = re.findall('var teamDetail = \[(.?\d+.*),', response.text)
# team_id = eval(teamDetail[0])[0]
# l_time = time.strftime('%Y%m%d%H', time.localtime())
# url = 'http://zq.win007.com/jsData/playerInfo/player{}.js?version ={}'.format(play_id, l_time)
# headers = {
#     "user-agent": UserAgent().random,
#     "referer": "http://zq.win007.com/cn/team/Lineup/{}.html".format(team_id)
# }
# response = requests.get(url, headers=headers)
# playerCharacter = re.findall('var playerCharacter = \[(\[\d+.*\])\]', response.text)
# playerCharacter_lis = eval(playerCharacter[0])
# print(str(playerCharacter_lis))
# print("优势",re.findall('\[1, \d, .?(.*?)\^', str(playerCharacter_lis)))
# print('style',re.findall('\[3, \d, .?(.*?)\^', str(playerCharacter_lis)))
# print('ruodian',re.findall('\[2, \d, .?(.*?)\^', str(playerCharacter_lis)))

'''
list2=re.findall('playerCharacter.*?\[(.*?)\];', response.text)
print(list2)
# print(type(list2))
# a=list2[0]
# b=list2[1]
try:
    res=eval(list2[0])
    print(res)
    print(type(res))
    print(len(res))
    print('/'*100)
    print(res[0][0])
    print(type(res[0][0]))
    qytd_fg_list=[]
    qytd_ys_list=[]
    qytd_rd_list=[]
    for j in res:
        if j[0]==1:#ys
            print('#' * 100)
            print(j[2])
            print(type(j[2]))
            qytd_ys_list.append(re.search('\w+',j[2]).group())
        elif j[0]==2:#rd
            qytd_rd_list.append(re.search('\w+', j[2]).group())
        elif j[0]==3:#fg
            qytd_fg_list.append(re.search('\w+', j[2]).group())
        else:
            raise IndexError

    qytd_ys=''.join(qytd_ys_list)
    qytd_rd=''.join(qytd_rd_list)
    qytd_fg=''.join(qytd_fg_list)

    print(qytd_ys)
    print(qytd_rd)
    print(qytd_fg)

except:
    qytd_ys = '不详'
    qytd_rd = '不详'
    qytd_fg = '不详'
'''