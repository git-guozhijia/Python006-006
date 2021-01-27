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

# 建立交换机
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 创建rabbitmq默认的队列
# callback : 当 Queue.DeclareOk 时的回调方法; 当 nowait=True 时必须为 None.
# queue=’’ : 队列名称
# passive=False : 只检查队列是否存在
# durable=False : 当 RabbitMQ 重启时,队列保持持久性
# exclusive=False : False：仅仅允许当前的连接访问，为True：当消费者与队列断开联系的时候，队列会自动删除
# auto_delete=False : 当消费者取消或者断开连接时, 自动删除该队列
# nowait=False : 当 Queue.DeclareOk 时不需要等待
# arguments=None : 对该队列自定义键/值对
result = channel.queue_declare(queue='',
                               exclusive=True)
# 获取自动创建的默认队列的名字
queue_name = result.method.queue
# 将队列绑定到交换机上，交换机获取消息之后就可以给有绑定关系的队列发送消息
# callback: 当 Queue.BindOk 时的回调函数, 当 nowait=True 时必须为 None
# queue: 要绑定到交换器的队列名称
# exchange: 要绑定的源交换器，就是交换器的名称
# routing_key=None: 绑定的路由键
# nowait=False: 不需要 Queue.BindOk 的响应
# arguments=None: 对该绑定自定义键/值对
channel.queue_bind(exchange="logs",
                   queue=queue_name)


# ch, method, properties, body:默认自带的四个参数
# 创建的接收队列消息的函数
def callback(ch, method, properties, body):
    # 手动确认消息接收成功，告诉mq使用者是否接收到消息，多个消费者时使用，单个消费者没有区别
    # ch.basic_ack(delivery_tag = method.delivery_tag)
    print(body.decode())


# 如果确认消费者在channel上未确认的消息数达到了basic_qos(prefetch_count=1)函数传递的参数值时，channel将不会再向消费者提供消息
channel.basic_qos(prefetch_count=1)
# 消费者去消费的队列，得到消息之后使用哪个函数去处理消息


# queue=’’: 要消费的消息队列
# on_message_callback：表示用哪个函数去接收这个队列的消息
# no_ack=False: 自动确认已经消费成功
# exclusive=False: 不允许其它的消费者消费该队列
# consumer_tag=None: 指定自己的消费标记
# arguments=None: 对该消费者自定义设置键值对
# auto_ack：自动接收和处理确认消息
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
channel.start_consuming()
