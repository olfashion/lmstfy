import pika
import sys

class RabbitRoutingSender(object):
    def __init__(self, host='localhost', exchange='server_reply') -> None:
        self.host = host
        self.exchange = exchange

    def send_direct(self, message, routing_key):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host))
        channel = connection.channel()

        channel.exchange_declare(exchange=self.exchange, exchange_type='direct')

        channel.basic_publish(
            exchange='direct_logs', routing_key=routing_key, body=message)
        print(" [x] Sent %r:%r" % (routing_key, message))
        connection.close()