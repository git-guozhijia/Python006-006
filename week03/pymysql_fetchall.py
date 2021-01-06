import pymysql

def fetchall_func(sql):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            sql = sql
            cursor.execute(sql)
            print(f"当前sql获取出来的数据行数：{cursor.rowcount}")
            results = cursor.fetchall()
            print(results)
            for i in results:
                print(i)
        db.commit()
    except Exception as err:
        print(f"fetchall error : {err}")
    finally:
        db.close()

if __name__ == "__main__":
    fetchall_func('select * from book')
