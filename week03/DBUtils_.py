import pymysql
from dbutils.pooled_db import PooledDB  # pip install DBUtils

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'guozhijia123',
    'db': 'test_db',
    'charset': 'utf8mb4',
    'maxconnections': 0,  # 链接池最大链接数
    'mincached': 4,  # 初始化链接池的时候，链接池中至少创建的空闲的链接。0表示不创建
    'maxcached': 0,  # 链接池中最大的空闲连接数
    'maxusage': 5,  # 每个链接最多被重复使用的次数， None标识为不限制重复使用
    'blocking': True  #链接池内如果没有可用链接h后是否进行阻塞，True标识等待进行阻塞，False标识为直接返回一个报错
}

spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cur = conn.cursor()
sql = 'select * from bookorm'
cur.execute(sql)
f = cur.fetchall()
print(f)
cur.close()
conn.close()


