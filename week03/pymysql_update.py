import pymysql,time

def update_func():
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            name = f"{time.time()}西游记"
            id = 1003
            sql = f'update book set `name` = "{name}" where id = {id}'
            print(sql)
            cursor.execute(sql)
        db.commit()
    except Exception as err:
        print(f"update error : {err}")
    finally:
        db.close()

if __name__ == "__main__":
    update_func()
