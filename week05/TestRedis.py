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


"""
# list：

# 列表插入数据，左侧，右侧
client.lpush("guozhijia_list", "lift")
client.rpush("guozhijia_list", "right")
print(client.llen("guozhijia_list"))

print(f'client.lpop("guozhijia_list"):{client.lpop("guozhijia_list")}')
print(f'client.rpop("guozhijia_list"):{client.rpop("guozhijia_list")}')
print(client.llen("guozhijia_list"))
# 查看list一定范围内的数据
print(client.lrange("guozhijia_list", 0, 2))
"""

"""
# set
# 向集合内添加元素,集合内的元素不允许重复
# 第一次执行结果为1，添加成功，第二次执行，结果为2，添加失败，不允许出现重复数据
print(client.sadd("guozhijia_set", "set_001"))
print(client.sadd("guozhijia_set", "set_002"))
print(client.sadd("guozhijia_set", "set_003"))
# client.smembers()获取集合内的元素数据
print(client.smembers("guozhijia_set"))
# client.spop()取出来的数据是随机的没有任何顺序可查
print(client.spop("guozhijia_set"))
print(client.smembers("guozhijia_set"))


print(client.sadd("guozhijia_set01", "set_01"))
print(client.sadd("guozhijia_set01", "set_002"))
print(client.sadd("guozhijia_set01", "set_03"))
# 两个集合之间的运算
# 交集
print(client.sinter("guozhijia_set01", "guozhijia_set"))
# 并集
print(client.sunion("guozhijia_set01", "guozhijia_set"))
# 差集
print(client.sdiff("guozhijia_set01", "guozhijia_set"))
"""

'''
# 哈希结构
client.hset("vip_user", "1001", 1)
client.hset("vip_user", "1002", 0)

print(client.hexists("vip_user", "1002"))
client.hdel("vip_user", "1001", "1002")
print(client.hexists("vip_user", "1002"))

# 添加多个键值对hmset已经废弃了
# client.hmset("vip_user", {'1003':1, '1004':1})
print(client.hkeys("vip_user"))
print(client.hget("vip_user", "1003"))
print(client.hget("vip_user", "1004"))
print(client.hgetall("vip_user"))
'''

'''
# zset  有序集合
client.zadd("guozhijia_zset", {"a":1, "b":2, "c":4, "d":3, "e":5})
client.zincrby("guozhijia_zset", -3, "e")# 修改"e"的值-3
print(client.zrange("guozhijia_zset", 0, 100)) # 按照范围输出zset内的值，由小到大
print(client.zrevrange("guozhijia_zset", 0, 3))# 按照范围输出zset内的值，由大到小
# 显示评分
print(client.zrange("guozhijia_zset", 0, -1, withscores=True))#[(b'a', 1.0), (b'b', 2.0), (b'e', 2.0), (b'd', 3.0), (b'c', 4.0)]
print(client.zrevrange("guozhijia_zset", 0, -1, withscores=True))# [(b'c', 4.0), (b'd', 3.0), (b'e', 2.0), (b'b', 2.0), (b'a', 1.0)]


print(client.zrangebyscore("guozhijia_zset", 2, 3))
print(client.zcard("guozhijia_zset"))# 查询有序集合内有多少个值
'''

# redis如何管理和重要机制：
# 缓存的淘汰机制（生存时间）：
# 	定期过期
# 	惰性过期
# 主从复制机制：redis自身的复制机制
# 哨兵：
# 	自动故障迁移：主服务器出现故障不能工作时，会找到一个从服务器升级为一个主服务器，并通知客户端和所有的从服务器，通知从服务器的变更




