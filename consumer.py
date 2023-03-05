import pika
import time

def callback(ch, method, properties, body):
    time.sleep(0.1)
    print(f'Saving message to DB : {body.decode("utf-8")}')

connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection: 
    channel = connection.channel()
    channel.basic_consume(queue='fakerQueue',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
