import pymysql

def testdb(sql):
    try:
        db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
        with db.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
        db.commit()
        return result
    except Exception as err:
        print(f"err:{err}")
    finally:
        db.close()

if __name__ == "__main__":
    testdb("select * from test_db.test_name")
    testdb("select * from test_db.test_name")