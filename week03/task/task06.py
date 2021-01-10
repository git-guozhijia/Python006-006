'''
张三给李四通过网银转账 100 极客币，现有数据库中三张表：
表一：用户表，包含用户 ID 和用户名字，
表二：用户资产表，包含用户ID 用户总资产，
表三：审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
'''
import time
from sqlalchemy import Column, Integer, String, DateTime, create_engine, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'user'
    uid = Column(Integer(), primary_key=True, autoincrement=True, unique=True, comment="用户id")
    name = Column(String(15), nullable=True, comment="用户名字")


class AssetTable(Base):
    __tablename__ = 'asset'
    uid = Column(Integer(), primary_key=True, nullable=True, unique=True, comment="用户id")
    asset = Column(Float(), nullable=True, comment="总资产")


class RecordTabl(Base):
    __tablename__ = 'record'
    id = Column(Integer(), primary_key=True, autoincrement=True, comment="主键ID")
    transfer_id = Column(Integer(), comment="转账ID")
    payee_id = Column(Integer(), comment="被转账id")
    money = Column(Float(), nullable=True, comment="转账金额")
    create_time = Column(DateTime(), nullable=True)

def isscalar(str):
    try:
        float(str)
    except ValueError:
    	return False
    else:
        return True

def deal(user_id01, user_id02, asset):
    '''
    :param user_id01: 转账人
    :param user_id02: 接收人
    :param asset: 转账金额
    '''
    if isscalar(user_id01) and isscalar(user_id02) and isscalar(asset):
        print("参数检测完成")
    else:
        return print("输入的参数类型有误，请确认！")

    user_id01_asset = session.query(AssetTable.asset).filter(AssetTable.uid == user_id01).first()
    if user_id01_asset != None:
        user_id01_asset = user_id01_asset[0]
    else:
        return print(f"输入的{user_id01}用户不存在")
    user_id02_asset = session.query(AssetTable.asset).filter(AssetTable.uid == user_id02).first()
    if user_id02_asset != None:
        user_id02_asset = user_id02_asset[0]
    else:
        return print(f"输入的 {user_id02} 用户不存在")

    if user_id01_asset > asset:
        try:
            session.query(AssetTable).filter(AssetTable.uid == user_id01).update(
                {AssetTable.asset: (user_id01_asset - asset)})
            session.query(AssetTable).filter(AssetTable.uid == user_id02).update(
                {AssetTable.asset: (user_id02_asset + asset)})
            try:
                record_tabl = RecordTabl(transfer_id=user_id01, payee_id=user_id02, money=asset, create_time=time.strftime("%Y-%m-%d %H:%M:%S"))
                session.add(record_tabl)
                session.commit()
            except Exception as e:
                print(f"insert 失败：{e}")
        except Exception as e:
            return print(f"update 操作失败: {e}")
    else:
        return print("当前账号的余额不足，请确认输入转账金额！！！")


if __name__ == '__main__':
    db_url = "mysql+pymysql://root:guozhijia123@localhost:3306/test_db?charset=utf8mb4"
    engine = create_engine(db_url, echo=False, encoding='utf-8')
    Base.metadata.create_all(engine)

    SessionClass = sessionmaker(bind=engine)
    session = SessionClass()

    deal(user_id01=10001, user_id02=10002, asset=100)
    deal(user_id01="3827rewrw", user_id02=10002, asset=100)