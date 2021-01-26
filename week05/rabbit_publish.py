import pika
import json

# mq用户名和密码
credentials = pika.PlainCredentials("guest", "guest")

# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
# 阻塞方法，当使用方连接到mq之后没有消息时为阻塞状态，有消息之后就去消费处理
connection = pika.BlockingConnection(parameters)
# 建立通道
channel = connection.channel()
# 声明消息队列，消息将在这个队列传递，如不存在，则创建,如果存在直接去使用队列
# durable=True 参数代表队列持久化
channel.queue_declare(queue='python-test', durable=False)

# 向队列插入数值 
# exchange 参数指定交换机，默认为空，直接写入队列
# routing_key 是队列名，也就是队列标识关键字，表示要向那个队列发布消息
# body 参数的值就是要向队列发送的消息
# message = "send message to rabbitmq"
message = json.dumps({'python-test': "send message to rabbitmq"})
channel.basic_publish(exchange='', routing_key='python-test', body=message)

# 关闭rabbitmq server的链接
connection.close()
