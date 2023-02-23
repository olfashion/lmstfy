import pika, json
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

my_dic = {
    "transaction_id": "12ed2-223dfaa2958-12cdf",
    "target_url": "https://google.com",
    "requesters_ip": "192.168.220.17",
    "request_time": "12-10-2023 04:34:02.234",
    "requesters_broswer": "Chrome",
    "requesters_device": "Iphone"

}


channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=json.dumps(my_dic),
    properties=pika.BasicProperties(delivery_mode=2)
)

print(" [x] Sent %r" % message)
connection.close()