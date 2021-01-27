import pika
import json

credentials = pika.PlainCredentials('guest', 'guest')

parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。
# durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(
    exchange='topic_exchange',
    durable=True,
    exchange_type='topic'
)

routing_key = "OrderId.test_routing_key"
for i in range(10):
    message = json.dumps({'OrderId': "1000%s" % i})
    # 指定 routing_key。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
    # routing_key参数：标识交换机下发消息给队列的标识
    channel.basic_publish(
        exchange='topic_exchange',
        routing_key=routing_key,
        body=f"{routing_key}:{message}"
        # properties=pika.BasicProperties(delivery_mode = 2)
    )
    print(message)
connection.close()
