import pika
import time

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 声明消息队列，消息将在这个队列传递，如不存在，则创建,如果存在直接去使用队列(生产者和消费者都重建声明消息队列以防出现队列不存在导致的异常)
# durable=True 参数代表队列持久化
channel.queue_declare(queue='task-queue', durable=True)


def callback(ch, method, properties, body):
    # 手动确认消息接收成功，告诉mq使用者是否接收到消息，多个消费者时使用，单个消费者没有区别
    # ch.basic_ack(delivery_tag = method.delivery_tag)
    time.sleep(1)
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 如果确认消费者在channel上未确认的消息数达到了basic_qos(prefetch_count=1)函数传递的参数值时，channel将不会再向消费者提供消息
channel.basic_qos(prefetch_count=1)

# 消费者去消费的队列，得到消息之后使用哪个函数去处理消息
channel.basic_consume('task-queue', on_message_callback=callback)

# 开始接受信息，并进入阻塞状态
channel.start_consuming()
