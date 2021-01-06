import pymysql


def insertmany_func():
    '''插入多条数据的操作方法'''
    db = pymysql.connect(host='localhost', port=3306, user='root', password='guozhijia123', db='test_db')
    try:
        with db.cursor() as cursor:
            mysql = "insert into book (`id`, `name`) value (%s, %s)"
            datas = ((int(f'110{i}'), f"book110{i}") for i in range(3,9))
            cursor.executemany(mysql, datas)
        db.commit()
    except Exception as e:
        print(f"insert error:{e}")
    finally:
        db.close()

if __name__ == '__main__':
    insertmany_func()