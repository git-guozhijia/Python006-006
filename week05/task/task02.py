import redis
import configparser


def linkRedis():
    config = configparser.ConfigParser()
    config.read("../config.ini")

    host = config.get(section="redis", option="host")
    port = config.get(section="redis", option="port")
    password = config.get(section="redis", option="password")
    try:
        pool = redis.ConnectionPool(host=host, port=port, password=password)
        client = redis.Redis(connection_pool=pool)
        return client
    except Exception as e:
        print(f"client err: {e}")


def sendsms(telephone_number: int, content: str, client=None):
    if client.ttl(f"{telephone_number}") == -2:
        client.set(f"{telephone_number}", 1)
        print(f"发送成功,内容为：{content}")
    elif client.ttl(f"{telephone_number}") == -1:
        if int(client.get(f"{telephone_number}")) == 4:
            print(f"发送成功,内容为：{content}")
            client.set(f"{telephone_number}", 5)
            client.expire(f"{telephone_number}", 60)
        else:
            print(f"发送成功,内容为：{content}")
            client.set(f"{telephone_number}", int(client.get(f"{telephone_number}")) + 1)
    else:
        print("1分钟内发送次数超过 5 次, 请等待1分钟")


if __name__ == '__main__':
    linkRedis = linkRedis()
    sendsms(18811572354, "测试发布送短信", client=linkRedis)
