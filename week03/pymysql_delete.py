import pymysql
import time

def delete_func():
    db = pymysql.connect(host='localhost', port=3306,
                         user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            id = 1002
            sql = f'delete from book where id = {id}'
            print(sql)
            cursor.execute(sql)
        db.commit()
    except Exception as err:
        print(f"delete error : {err}")
    finally:
        db.close()


if __name__ == "__main__":
    delete_func()
