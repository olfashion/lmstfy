import pika, json
import sys, uuid

my_dic = {
    "transaction_id": str(uuid.uuid4()),
    "target_url": "https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python",
    "requesters_ip": "192.168.220.17",
    "request_time": "12-10-2023 04:34:02.234",
    "requesters_broswer": "Chrome",
    "requesters_device": "Iphone"

}

class RabbitWorkQueueProducer(object):
    def __init__(self, host='localhost', queue_name='task_queue') -> None:
        self.host = host
        self.queue_name = queue_name



    def publish(self, message:str):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue=self.queue_name, durable=True)
        channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )

        print(" [x] Sent %r" % message)
        self.connection.close()