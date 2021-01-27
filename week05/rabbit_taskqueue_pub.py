import pika
import json

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters(host='127.0.0.1',
                                       port=5672,
                                       virtual_host='/',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task-queue', durable=True)
message = json.dumps({'task-queue': "send message to task_queue"})
channel.basic_publish(exchange='', routing_key='task-queue', body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
connection.close()
