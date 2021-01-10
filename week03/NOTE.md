学习笔记



    
    def fetchall_func():
        try:
            with db.cursor() as cursor:
                sql = "select * from member_info"
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


2. 使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:

用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交

4. 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

Table1

id name

1 table1_table2

2 table1

Table2

id name

1 table1_table2

3 table2

举例: INNER JOIN

复制代码
SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;
5. 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。

6. 张三给李四通过网银转账 100 极客币，现有数据库中三张表：

一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。

请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。

