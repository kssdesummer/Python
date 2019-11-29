import pymysql


class Model():
    tablename = None    # 表名
    db = None           # 数据库连接对象
    cursor = None       # 游标对象

    # 初始化,传递一个参数表名
    def __init__(self,tablename):
        self.tablename = tablename
        self.connect()

    # 析构
    def __del__(self):
        # 关闭数据库连接
        self.db.close()

    # 链接数据库
    def connect(self):
        # 连接数据库
        self.db = pymysql.connect("localhost","root","mysql","python",cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cursor = self.db.cursor()
        # db.select_db() 当不指定库的时候,可以在这里选择库

    # 查询
    def query(self,sql):
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            # 提取结果并返回
            return res
        except:
            print("执行sql错误,检查sql")
            return False

    # 添加
    def insert(self,arr):
        sql = f"insert into {self.tablename} values "
        # 检查类型
        typ = isinstance(arr,list)
        if typ:
            for i in arr:
                s = ""
                for k,v in i.items():
                    if isinstance(v,str):
                        s += f"'{v}',"
                    else:
                        s += f"{v},"
                s =s.rstrip(',')
                s = f'({s}),'
                sql += s

            sql = sql.rstrip(',')+';'

        elif isinstance(arr,dict):
            sql += '({id},"{name}",{age},{sex},{phone}),'.format(**arr)
            sql = sql.rstrip(',') + ';'
        # 执行sql
        try:
            print(sql)
            res = self.cursor.execute(sql)
            # 提交
            self.db.commit()
            # 返回结果
            return f"新增{res}条数据"
        except:
            # 执行回滚
            self.db.rollback()
            print('数据添加失败')
            return False

    def delete(self,ids):
        sql = f'delete from {self.tablename} where '
        for i in ids:
            id =  f'id = {i} or '
            sql += id
        sql = sql.rstrip(' or ') + ';'
        print("执行语句: ",sql)
        try:
            res = self.cursor.execute(sql)
            self.db.commit()
            count = self.cursor.fetchall()
            return res
            # pass

        except:
            self.db.rollback()
            print("删除数据出错,检查语句")
            return False

    def update(self,data):
        id = data['id']
        info = data['info']
        sql = ''
        for k,v in info.items():
            if isinstance(v, str):
                data = f"{k} = '{v}',"
            else:
                data = f"{k} = {v},"
            sql += data
        sql = sql.rstrip(',')
        varsql = f"update {self.tablename} set {sql} where id = {id};"
        print('执行语句:',varsql)
        try:
            res = self.cursor.execute(varsql)
            self.db.commit()
            return res
            # pass

        except:
            self.db.rollback()
            print("删除数据出错,检查语句")
            return False



if __name__ == "__main__":
    # 实例化对象
    users = Model("users")


    # 查询操作
    data = users.query('select * from users')
    print(data)

    # # 添加操作 :支持列表和字典格式
    # varlist = [
    #     {"id":1,"name":"alexy","age":19,"sex":1,"phone":12754},
    #     {"id":2,"name":"alext","age":15,"sex":1,"phone":128554},
    #     {"id":3,"name":"alexd","age":29,"sex":0,"phone":14254},
    #     {"id":5,"name":"alexj","age":19,"sex":1,"phone":12154}
    # ]
    # varlist2 = {"id":15,"name":"alxy","age":19,"sex":1,"phone":12754}
    # res = users.insert(varlist)
    # print(res)

    # 删除  : 给定id能删除 {id:1}
    # ids = [5,8]
    # res = users.delete(ids)

    # 修改
    # data = {"id":1,"info":{"name":"alexjj","age":19,"sex":1,"phone":12754}}
    # res = users.update(data)
    # print(res)