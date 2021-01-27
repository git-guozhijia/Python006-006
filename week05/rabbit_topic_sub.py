import pika

credentials = pika.PlainCredentials('guest', 'guest')

parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
result = channel.queue_declare('topic_queue1',
                               exclusive=True)  # 创建临时队列，队列名传空字符，consumer关闭后，队列自动删除

channel.exchange_declare(exchange='topic_exchange',
                         durable=True,
                         exchange_type='topic')  # 声明exchange交换机，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储

# routing_key参数：标识获取队列的消息,模糊匹配的时候需要在单词后面加上"."之后再去添加*或者#
channel.queue_bind(exchange='topic_exchange',
                   queue="topic_queue1",
                   routing_key='OrderId.#')  # 绑定交换机和队列  exchange 使我们能够确切地指定消息应该到哪个队列去


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


channel.basic_qos(prefetch_count=1)

# 告诉rabbitmq，用callback来接受消息
channel.basic_consume(
    queue="topic_queue1",
    on_message_callback=callback,
    # 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
    auto_ack=False)

channel.start_consuming()
