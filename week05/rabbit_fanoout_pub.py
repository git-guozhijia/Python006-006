import pika
import json

# mq用户名和密码
credentials = pika.PlainCredentials("guest", "guest")

# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
# host: RabbitMQ IP 地址
# port: RabbitMQ 端口
# virtual_host: RabbitMQ 虚拟主机
# credentials: 登录凭证
parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
# 阻塞方法，当使用方连接到mq之后没有消息时为阻塞状态，有消息之后就去消费处理
# parameters: 连接参数(包含主机/端口/虚拟主机/账号/密码等凭证信息)
connection = pika.BlockingConnection(parameters)
# 建立通道
# channel_number:信道个数, 一般采用默认值 None
channel = connection.channel(channel_number=None)
# 建立交换机
# callback=None : 当 Exchange.DeclareOk 时 调用该方法, 当 nowait=True 该值必须为 None
# exchange=None: 交换器名称,保持非空,由字母、数字、连字符、下划线、句号组成
# exchange_type=‘direct’: 交换器类型: fanout, topic
# passive=False: 执行一个声明或检查它是否存在
# durable=False: RabbitMQ 重启时保持该交换器的持久性,即不会丢失
# auto_delete=False: 没有队列绑定到该交换器时,自动删除该交换器
# internal=False: 只能由其它交换器发布-Can only be published to by other exchanges
# nowait=False: 不需要 Exchange.DeclareOk 的响应-Do not expect an Exchange.DeclareOk response
# arguments=None: 对该交换器自定义的键/值对, 默认为空
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 向队列插入数值
# exchange 参数指定交换机，默认为空，直接写入队列
# routing_key 是队列名，也就是队列标识关键字，表示要向那个队列发布消息
# body 参数的值就是要向队列发送的消息
# message = "send message to rabbitmq"
message = json.dumps({
    'python-test': "send message to rabbitmq"
})
# exchange: 要发布的目标交换器
# routing_key: 该交换器所绑定的路由键
# body: 携带的消息主体
# properties=None: 消息的属性,即文本/二进制等等
# mandatory=False: 当 mandatory 参数设置为 true 时，交换机无法根据自身的路由键找到一个符合的队列，
# 那么 RabbitMQ 会调用 Basic.Return 命令将消息返回给生产者，
# 当 mandatory 参数设置为 false 时，出现上述情况，消息会被丢弃
# immediate=False: 立即性标志
# delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

# 关闭rabbitmq server的链接
connection.close()
