import redis
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config.get(section="redis", option="host")
port = config.get(section="redis", option="port")
# db = config.get(section="redis", option="db")

try:
	client = redis.Redis(host=host, port=port)
except Exception as e:
	print(f"client err: {e}")


# for key in client.keys()[:5]:
# 		print(key.decode())

    # def set(
    #     self,
    #     name: Union[Text, bytes],
    #     value: _Str,
    #     ex: Union[None, int, timedelta] = ...,
    #     px: Union[None, int, timedelta] = ...,
    #     
    #     xx: bool = ...,
    # )

# client.delete("guozhijia_key")

# nx: bool = True   如果当前key存在的值，如果存在不去操作覆盖，如果不存在就直接覆盖
client.set("guozhijia_key", 'guozhijia_value23', nx=True)
print(client.get("guozhijia_key").decode())




