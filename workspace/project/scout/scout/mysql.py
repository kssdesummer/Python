import pymysql


class MySql:

    def __init__(self, host, user, password, database):
        #conn = pymysql.connect(host="localhost", user="root", password="mysql", database="caoruonan")

        self.db = pymysql.connect(host=host, user=user, password=password, database=database,cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.db.cursor()

    def insert(self, sql, data):
        self.cursor.execute(sql, data)
        self.db.commit()

if __name__ == '__main__':
    db = MySql('localhost', 'root', 'mysql', 'python')