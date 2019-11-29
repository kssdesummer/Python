# name = input("请输入管理员账户:")
# pwd = input("请输入管理员密码:")
# if name != "admin" or pwd != "123":
#     print("用户名或密码错误!")
# else:
#     print("登陆成功")
#     pass
# print("*" * 52)
# print("*"," " * 10,"(1)注册"," " * 10,"(2)查询"," " * 10, "*")
# print("*"," " * 10,"(3)存钱"," " * 10,"(4)取钱"," " * 10, "*")
# print("*"," " * 10,"(5)转账"," " * 10,"(6)改密"," " * 10, "*")
# print("*"," " * 10,"(7)锁卡"," " * 10,"(8)解卡"," " * 10, "*")
# print("*"," " * 10,"(9)不卡"," " * 10,"(0)退出"," " * 10, "*")
# print("*" * 52)

'''
while True:
    cho = input("请输入要选择的")
    if cho == "1":
        name = input("请输入用户名:")
        userid = input("请输入身份证号:")
        phone = input("请输入手机号:")
        password = input("请输入密码:")
        password1 = input("请确认密码:")
        if password != password1 :
            password = input("请输入密码:")
            password1 = input("请确认密码:")
            if password != password1:
                print("两次输入密码不一致!")
                break
            else:
                cardid = random.randint(100000,999999)
                money = 10,"
                print("{}开户成功,卡号为{},余额为{}".format(name,cardid,money))
    elif cho == "2":
        cardid1 = input("请输入卡号:")
        password2 = input("请输入密码:")
    elif cho == "3":
        cardid = input("请输入卡号:")
        password2 = input("请输入密码:")
        if password2 == password:
            num = int(input("请输入你要存的钱数:"))
    elif cho == "4":
        pass
    elif cho == "5":
        pass
    elif cho == "6":
        pass
    elif cho == "7":
        pass
    elif cho == "8":
        pass
    elif cho == "9":
        pass
    elif cho == "0":
        pass
'''



# class mi:
#     def __init__(self):
#         self.name = "ni shi "
#         self.i = " "
#     def demo(self):
#         nonlocal o
#         if self.i in self.name:
#             o = "nishshui"
#             return self.i
# a = mi()
# print(a.o)

'''
card = Card(cardid,password,money)      # 对象
person = Person(name,userid,phone,card)
self.user_id_dict[userid] = cardid      # {"身份证号":"卡号"}
self.user_dict[cardid] = person
'''
# 106011

            # card = user.card  #赋值类
            # print(card.money)
            # new_cardid = self.get_cardid()        # 得到一个新的卡号
            # user1 = self.user_dict[new_cardid]
            # card1 = user1.card
            # card1.money = card.money
            # self.user_id_dict.pop(user_id)        # 删除身份证号对应值
            # self.user_id_dict[user_id] = new_cardid     # 对身份证号做键,增加值
            # print("原卡号:",cardid)
p = "pop"
dict1 = {"po":"p","rap":"a"}
dict1.setdefault(p,"woaini")
dict1[p] = "nishabi"
print("pop:",dict1)

# print(self.user_id_dict[card_id])
# print(self.user_id_dict)
# print("新卡号:",self.user_id_dict[user_id])
# self.user_id_dict[user_id] = cardid
# self.user_dict[card_id] = user1

