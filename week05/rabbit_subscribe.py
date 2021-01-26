import pika
import time

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
# 声明消息队列，消息将在这个队列传递，如不存在，则创建,如果存在直接去使用队列(生产者和消费者都重建声明消息队列以防出现队列不存在导致的异常)
# durable=True 参数代表队列持久化
channel.queue_declare(queue='python-test', durable=False)


# ch, method, properties, body:默认自带的四个参数
def callback(ch, method, properties, body):
    # 手动确认消息接收成功，告诉mq使用者是否接收到消息，多个消费者时使用，单个消费者没有区别
    # ch.basic_ack(delivery_tag = method.delivery_tag)
    # 可以去编写处理获取消息后的处理逻辑
    print(body.decode())


# 告诉rabbitmq，用callback来接收消息
channel.basic_consume('python-test', on_message_callback=callback)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()

time.sleep(3)
connection.process_data_events()
