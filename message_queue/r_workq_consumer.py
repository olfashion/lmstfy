import pika
import time


class RabbitWorkQueueProducer(object):
    def __init__(self, host='localhost', queue_name='task_queue') -> None:
        self.host = host
        self.queue_name = queue_name


    def listen(self):
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=self.host))
        channel = connection.channel()

        channel.queue_declare(queue='task_queue', durable=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)



    def callback(self, ch, method, properties, body):
        print(" [x] Received %r" % str(body))
        ch.basic_ack(delivery_tag=method.delivery_tag)


