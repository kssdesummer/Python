# view 视图界面 登陆（管理员账号登陆）,欢迎界面，操作界面
import time
class View:
    def run():
        name = input("请输入管理员账户:")
        pwd = input("请输入管理员密码:")
        if name != "admin" or pwd != "123":
            print("用户名或密码错误!")
            quit()
        else:

            print("*" * 52)
            print("*"," "*48,"*")
            print("*"," "*48,"*")
            print("*"," "*14,"Welcome To XD Bank"," "*14,"*")
            print("*"," "*48,"*")
            print("*"," "*48,"*")
            print("*" * 52)
            time.sleep(1)
            print("*" * 52)
            print("*", " " * 10, "(1)注册", " " * 10, "(2)查询", " " * 10, "*")
            print("*", " " * 10, "(3)存钱", " " * 10, "(4)取钱", " " * 10, "*")
            print("*", " " * 10, "(5)转账", " " * 10, "(6)改密", " " * 10, "*")
            print("*", " " * 10, "(7)锁卡", " " * 10, "(8)解卡", " " * 10, "*")
            print("*", " " * 10, "(9)补卡", " " * 10, "(0)退出", " " * 10, "*")
            print("*" * 52)
            return True
if __name__ == "main":
    View.run()
