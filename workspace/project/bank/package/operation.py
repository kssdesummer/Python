# 卡号：用户  user_dict   user.txt
# 身份证：卡号  user_id_dict    userid.txt
#operation类（具体的操作功能实现）
# 把我们需要的十个功能都放在这个类里
import random
import os
import pickle
from .card import Card
from .person import Person
class Operation:
    def __init__(self):
        self.load_user()
        self.load_user_id()
    #读取用户
    def load_user(self):
        if os.path.exists("./user.txt"):
            with open("./user.txt","rb") as f:
                self.user_dict = pickle.load(f)
        else:
            self.user_dict = {}
    #读取用户id
    def load_user_id(self):
        if os.path.exists("userid.txt"):
            with open("userid.txt","rb") as f:
                self.user_id_dict = pickle.load(f)
        else:
            self.user_id_dict = {}
    # 注册
    def register(self):
        name = self.get_name()
        userid = self.get_userid()
        phone = self.get_phone()
        money = 10
        password = self.get_pwd()
        cardid = self.get_cardid()
        card = Card(cardid,password,money)      # 对象
        person = Person(name,userid,phone,card)
        self.user_id_dict[userid] = cardid      # {"身份证号":"卡号"}
        self.user_dict[cardid] = person
        print("{}开户成功,卡号为{},余额为{}".format(name, cardid, money))
    # 判断名字是否合法
    def get_name(self):
        while True:
            name = input("请输入你的用户名:")
            if name == "" or " " in name or name.isalnum():
                print("输入不合法，请确认用户名使用中文和英文组成!")
                continue
            else:
                return name
    # 判断身份证长度:
    def get_userid(self):
        while True:
            userid = input("请输入身份证号:")
            if userid in self.user_id_dict:
                print("该身份证已被注册过,若忘记卡号,请去补卡!")
            elif len(userid) != 18 or " " in userid or userid.isdecimal() == False :
                print("输入身份证信息有误!")
                continue
            else:
                return userid
    def get_userid1(self):
        while True:
            userid = input("请输入身份证号:")
            if len(userid) != 18 or " " in userid or userid.isdecimal() == False :
                print("输入身份证信息有误!")
                continue
            else:
                return userid
    # 判断手机号长度
    def get_phone(self):
        while True:
            phone = input("请输入手机号:")
            if len(phone) != 11 or " " in phone or phone.isdecimal() == False:
                print("输入手机号信息有误!")
                continue
            else:
                return phone
    # 判断密码是否相等
    def get_pwd(self):
        password = input("请输入密码:")
        password1 = input("请确认密码:")
        if password != password1 or " " in password or len(password) != 6 or password.isdecimal() == False:
            print("两次输入密码不一致或输入不合法,只能6位纯数字!")
            password = input("请输入密码:")
            password1 = input("请确认密码:")
            if password != password1 or  " " in password or len(password) != 6:
                print("两次输入密码不一致或输入不合法,只能6位纯数字!")
                exit()
            else:
                return password
        else:
            return password
    #获取卡号
    def get_cardid(self):
        while True:
            cardid = str(random.randint(100000, 999999))
            if cardid not in self.user_id_dict:
                return cardid
    # 检测密码，不对的话就锁卡
    def check_pwd(self, card):
        n = 1
        while n < 4:
            pwd = input("请输入你的密码：")
            if pwd.isdecimal() == False:
                print("密码必须是纯数字！")
            elif pwd == card.password:
                return True
            print("密码错误，你还有{}次机会".format(3 - n))
            n += 1
        card.islock = True
        print("卡被锁了！")
    # 检测卡是否存在
    def get_card_info(self):
        card_id = input("请输入您的卡号：")
        if card_id in self.user_dict:
            user = self.user_dict[card_id]
            card = user.card
            return card
        else:
            print("您查询的卡号不存在！")
    # 查询
    def query(self):
        card = self.get_card_info()
        if card:
            if card.islock:
                print("此卡已被冻结！")
            else:
                if self.check_pwd(card):
                    print("此卡余额为{}元".format(card.money))
    # 存钱
    def save_money(self):
        card = self.get_card_info()
        if card:
            if card.islock:
                print("您的卡被锁了！")
            else:
                user = self.user_dict[card.cardid]
                print("存入的账号名是{}".format(user.name))
                num = input("按1存款，其他返回上一层")
                if num == "1":
                    moneys = input("请输入你的存款金额：")
                    if moneys.isdecimal() and int(moneys) > 0:
                        moneys = int(moneys)
                        card.money += moneys
                        print("存款成功，存入{}元,卡内余额现为{}".format(moneys, card.money))
                    else:
                        print("输入的金额有误，请重新操作！")
    # 取钱
    def get_money(self):
        card = self.get_card_info()
        if card:
            if card.islock:
                print("您的卡被锁了！")
            else:
                self.check_pwd(card)
                try:
                    get_money = float(input("请输入你要取的金额："))
                    if 0 < get_money <= card.money - 10:
                        card.money -= get_money
                        print("成功取走了{}元，卡内余额{}元".format(get_money, card.money))
                    else:
                        print("卡内余额不足，不可以取款！")
                except:
                    print("输入的金额不合法！")
    # 判断对方账户
    def get_card_info1(self):
        card_id = input("请输入对方卡号：")
        if card_id in self.user_dict:
            user = self.user_dict[card_id]
            card = user.card
            return card
        else:
            print("此卡号不存在！")
    # 转账
    def trans_money(self):
        card1 = self.get_card_info()
        if card1:
            if card1.islock:
                print("您的卡被锁了！")
            else:
                self.check_pwd(card1)
                card2 = self.get_card_info1()
                if card2:
                    if card2.islock:
                        print("您的卡被锁了！")
                    else:
                        user = self.user_dict[card2.cardid]
                        if card1 == card2:
                            print("您不能向自己转账!")
                        else:
                            cho = input("您将向用户{}进行转账,确认输入1,返回输入其他:".format(user.name))
                            if cho == "1":
                                try:
                                    get_money = float(input("请输入你要转账的金额："))
                                    if 0 < get_money <= card1.money - 10:
                                        card2.money += get_money
                                        card1.money -= get_money
                                        print("您成功转出{}元，卡内余额{}元".format(get_money, card1.money))
                                        print("用户{}成功收到{}元，卡内余额{}元".format(user.name,get_money, card2.money))
                                    else:
                                        print("卡内余额不足，不可以转账！")
                                except:
                                    print("输入的金额不合法！")
    # 改密
    def change_pwd(self):
        card = self.get_card_info()
        if card:
            if card.islock:
                print("您的卡被锁了！")
            else:
                user = self.user_dict[card.cardid]
                # print(user.userid)
                cho = input("选择: 1.原密码改密 2.身份证改密")
                if cho == "1":
                    pwd = input("请输入原密码:")
                    if pwd == card.password:
                        pwd = self.get_pwd()
                        card.password = pwd
                elif cho == "2":
                    user_id = input("请输入您的身份证号:")
                    if user_id == user.userid:
                        pwd = self.get_pwd()
                        card.password = pwd
                else:
                    print("输入指令错误!")
    # 锁卡
    def lock(self):
        card = self.get_card_info()
        user = self.user_dict[card.cardid]
        if card.islock:
            print("您的卡已经被锁了！")
        else:
            cho = input("选择: 1.原密码锁卡 2.身份证锁卡")
            if cho == "1":
                pwd = input("请输入原密码:")
                if pwd == card.password:
                    card.islock = True
                    print("锁卡成功")
                else:
                    print("输入指令错误!")
            elif cho == "2":
                user_id = input("请输入您的身份证号:")
                if user_id == user.userid:
                    card.islock = True
                    print("锁卡成功")
                else:
                    print("输入指令错误!")
            else:
                print("输入指令错误!")
    # 解卡
    def unlock(self):
        card = self.get_card_info()
        user = self.user_dict[card.cardid]
        if card.islock == False:
            print("您的卡没有被冻结！")
        else:
            cho = input("选择: 1.原密码解卡 2.身份证解卡")
            if cho == "1":
                pwd = input("请输入原密码:")
                if pwd == card.password:
                    card.islock = False
                    print("解卡成功")
                else:
                    print("输入指令错误!")
            elif cho == "2":
                user_id = input("请输入您的身份证号:")
                if user_id == user.userid:
                    card.islock = False
                    print("解卡成功")
                else:
                    print("输入指令错误!")
            else:
                print("输入指令错误!")
    # 补卡
    def new_card(self):
        user_id = self.get_userid1()
        cardid = self.user_id_dict[user_id]
        if cardid in self.user_dict:
            if cardid:
                user = self.user_dict[cardid]
                card = user.card
                new_cardid = self.get_cardid()      # 得到新卡号
                self.user_dict.pop(card.cardid)
                self.user_id_dict.pop(user_id)
                self.user_id_dict[user_id] = new_cardid
                self.user_dict[new_cardid] = user
                print("新补办的卡号为:{},余额为:{}".format(new_cardid,card.money))
        else:
                print("您输入身份证号不存在，请核实！")
    # 保存
    def save(self):
        with open("./user.txt", "wb") as f:
            pickle.dump(self.user_dict, f)
        with open("./userid.txt", "wb") as f:
            pickle.dump(self.user_id_dict, f)