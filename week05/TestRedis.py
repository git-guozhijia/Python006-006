import redis
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config.get(section="redis", option="host")
port = config.get(section="redis", option="port")

try:
	client = redis.Redis(host=host, port=port)
except Exception as e:
	print(f"client err: {e}")


# string:
"""
# for key in client.keys()[:5]:
# 		print(key.decode())

# 删除对应的key
# client.delete("guozhijia_key")

# name: Union[Text, bytes],
# value: _Str,
# ex: Union[None, int, timedelta] = ...,
# px: Union[None, int, timedelta] = ...,
# xx: bool = ...,
# nx: bool = True   如果当前key存在的值，如果存在不去操作覆盖，如果不存在就直接覆盖
client.set("gzj_str", 'guozhijia_value23', nx=True)
print(f'client.get("gzj_str").decode()  :  {client.get("gzj_str").decode()}')

client.append("gzj_str", "append_value")
print(f'client.append("gzj_str", "append_value")  :  {client.get("gzj_str").decode()}')

client.set("gzj_int", "100")
print(f'client.set("gzj_int", "100"): {client.get("gzj_int").decode()}')
client.incr("gzj_int")
print(f'client.incr("gzj_int"): {client.get("gzj_int").decode()}')
client.decr("gzj_int")
print(f'client.decr("gzj_int"): {client.get("gzj_int").decode()}')

print(client.type("gzj_int"))
print(client.type("gzj_str"))
"""


# list：
# client.lrange()

# 列表插入数据，左侧，右侧
client.lpush("guozhijia_list", "lift")
client.rpush("guozhijia_list", "right")
print(client.llen("guozhijia_list"))

print(f'client.lpop("guozhijia_list"):{client.lpop("guozhijia_list")}')
print(f'client.rpop("guozhijia_list"):{client.rpop("guozhijia_list")}')
print(client.llen("guozhijia_list"))
# 查看list一定范围内的数据
print(client.lrange("guozhijia_list", 0, 2))







