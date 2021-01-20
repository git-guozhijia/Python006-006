import redis
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

host = config.get(section="redis", option="host")
port = config.get(section="redis", option="port")
db = config.get(section="redis", option="db")

try:
	client = redis.Redis(host=host, port=port, db=db)
	for key in client.keys()[:5]:
		print(key.decode())
except Exception as e:
	print(f"client err: {e}")

client.set()
