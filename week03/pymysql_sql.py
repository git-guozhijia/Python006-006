import pymysql
from week03 import ini_read
from week01 import logging_t

class my_mysql():
    def __init__(self, mysql_config):
        """mysql_config : 输入一个dict，包含链接db的参数"""
        self.mylog = logging_t.log().mylog()
        # self.sql_config = ini_read.read_ini_config().read_config_dict('mysql')
        self.sql_config = mysql_config
        self.db = pymysql.connect(host = self.sql_config['host'],
                                  port = int(self.sql_config['port']),
                                  user = self.sql_config['user'],
                                  password = self.sql_config['password'],
                                  db = self.sql_config['db'])

    def delete(self, table_name, condition):
        if condition:
            try:
                with self.db.cursor() as cursor:
                    sql = f'delete from {table_name} where {condition}'
                    self.mylog.info(f"delete func : {sql}")
                    cursor.execute(sql)
                self.db.commit()
            except Exception as err:
                print(f"delete error : {err}")
            finally:
                self.db.close()
        else:
            try:
                with self.db.cursor() as cursor:
                    sql = f'delete from {table_name}'
                    self.mylog.info(f"delete func : {sql}")
                    cursor.execute(sql)
                self.db.commit()
            except Exception as err:
                print(f"delete error : {err}")
            finally:
                self.db.close()


    def fetchall_func(self, sql):
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                # print(f"当前sql获取出来的数据行数：{cursor.rowcount}")
                results = cursor.fetchall()
                self.mylog.error(f"执行sql ： {sql}")
            self.db.commit()
            return results
        except Exception as err:
            self.mylog.error(f"fetchall_func error : {err}")
        finally:
            self.db.close()

    def fetchone_func(self, sql):
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                results = cursor.fetchone()
                self.mylog.error(f"执行sql ： {sql}")
            self.db.commit()
            return results
        except Exception as err:
            self.mylog.error(f"fetchone_func error : {err}")
        finally:
            self.db.close()

    def insert_one_func(self, keys=(), valus=()):
        try:
            with self.db.cursor() as cursor:
                sql = f"insert into book ({','.join(keys)}) value ({','.join(str('%s') for i in valus)})"
                cursor.execute(sql, valus)
                sql = f"insert into book ({','.join(keys)}) value ({','.join(str(i) for i in valus)})"
                self.mylog.info(f"执行sql ： {sql}")
                '''cousor.close() : with 链接方式在执行完with之后回去自动关闭游标的链接，免去了手动关闭链接 cousor.close()'''
            self.db.commit()
        except Exception as err:
            self.mylog.error(f"insert_one_func error : {err}")
        finally:
            self.db.close()

    def insertmany_func(self, keys=(), value_len=0, values_dict={}):
        try:
            with self.db.cursor() as cursor:
                sql = f"insert into book ({','.join(keys)}) value ({','.join('%s' for i in range(value_len))})"
                datas = (({i[0]}, {i[1]}) for i in values_dict.items())
                cursor.executemany(sql, datas)
            self.db.commit()
        except Exception as err:
            self.mylog.error(f"insert_one_func error : {err}")
        finally:
            self.db.close()

    def update_func(self, sql):
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql)
            self.db.commit()
            self.mylog.info(f"执行sql ： {sql}")
        except Exception as err:
            self.mylog.error(f"update error : {err}")
        finally:
            self.db.close()

if __name__ == "__main__":
    test_mysql = my_mysql(ini_read.read_ini_config().read_config_dict('mysql'))
    # test_mysql.delete('book', '')
    # print(test_mysql.fetchall_func('select * from book'))
    # print(test_mysql.fetchone_func('select * from book order by id desc limit 1'))
    # test_mysql.insert_one_func(('id','name'),(100006,'guozhijia'))
    # test_mysql.insertmany_func(('id','name'), 2, {10101:'21212', 10102:'21212'})
    test_mysql.update_func("update book set `name` = 'guozhijia' where id = 10102")