import pika
import time

def callback(ch, method, properties, body):
    time.sleep(0.1)
    print(f'{body.decode("utf-8")}')

connection_parameters = pika.ConnectionParameters(host='localhost')


with pika.BlockingConnection(connection_parameters) as connection: 
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')
    channel.queue_declare(queue='DBfinalTask')
    channel.queue_bind(exchange='FinalTask',queue='DBfinalTask',routing_key=f'#')
    channel.basic_consume(queue='DBfinalTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
