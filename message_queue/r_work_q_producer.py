import pika, json
import sys, uuid

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

my_dic = {
    "transaction_id": str(uuid.uuid4()),
    "target_url": "https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python",
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