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


def counter(client, video_id:int):
    client.zincrby("count_number", 1, f"{video_id}")
    return client.zscore("count_number", f"{video_id}")

if __name__ == '__main__':
	linkRedis = linkRedis()
	print(counter(linkRedis, f"2343242"))