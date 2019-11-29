# person 用户类,存储用户信息的
# 用户名，身份证号，手机号，卡
# name,userid,phone,card
class Person:
    def __init__(self,name,userid,phone,card):
        self.name = name
        self.userid = userid
        self.phone = phone
        self.card = card
