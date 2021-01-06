import pymysql

def insert_func(id, name):
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            mysql = "insert into book (`id`, `name`) value (%s, %s)"
            data = (id, name)
            cursor.execute(mysql, data)
            '''cousor.close() : with 链接方式在执行完with之后回去自动关闭游标的链接，免去了手动关闭链接 cousor.close()'''
        db.commit()
    except Exception as e:
        print(f"insert error:{e}")
    finally:
        db.close()

if __name__ == '__main__':
    insert_func(1002, '西游记')