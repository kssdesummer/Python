import pymysql

# db = pymysql.connect("localhost", "root", "mysql", "python", cursorclass=pymysql.cursors.DictCursor)
# cursor = db.cursor()
# sql = 'show tables'
# res = cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# db.commit()
# cursor.close()
# db.close()

'''
id : 标号
type : 发表内容的类型
content : 发表内容
create_time : 创建时间
talk_count : 评论数
zan_count :点赞数
zhuan_count : 转发数
watch_count : 观看数(非视频为0)
'''

'''
微博数据的建表语句
# create table weibo_data (
#     id int(10) primary key auto_increment,
#     type char(20),
#     content text,
#     create_time char(50),
#     talk_count int(12),
#     zan_count int(12),
#     zhuan_count int(12),
#     watch_count int(12)
# ) default charset=utf8mb4;
'''

class Store(object):
    def __init__(self):
        self.db = pymysql.connect('localhost', 'root', 'mysql', 'python', cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def execute_sql(self, sql, data):
        self.cursor.execute(sql, data)
        self.db.commit()

    def __del__(self):
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    store = Store()
    sql = 'insert into weibo_data(type,content,create_time,talk_count,zan_count,zhuan_count,watch_count)VALUES(%s,%s,%s,%s,%s,%s,%s)'
    data = ('video', 'today is a good day', '2019-11-18', 456, 789, 4645, 54646)
    store.execute_sql(sql, data)
