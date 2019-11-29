from package.view import View
from package.operation import Operation
class Main():
    def run():
        if View.run():
            obj = Operation()
            while True:
                cho = input("请输入要选择的:")
                if cho == "1":
                    obj.register()
                elif cho == "2":
                    obj.query()
                elif cho == "3":
                    obj.save_money()
                elif cho == "4":
                    obj.get_money()
                elif cho == "5":
                    obj.trans_money()
                elif cho == "6":
                    obj.change_pwd()
                elif cho == "7":
                    obj.lock()
                elif cho == "8":
                    obj.unlock()
                elif cho == "9":
                    obj.new_card()
                elif cho == "0":
                    obj.save()
                    exit()
                else:
                    print("input error!")
Main.run()