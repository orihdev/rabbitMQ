import pika
import time

def callback(ch, method, properties, body):
    time.sleep(0.1)
    print(f'{body.decode("utf-8")}')
def reverse(x):
  return x[::-1]

connection_parameters = pika.ConnectionParameters(host='localhost')


with pika.BlockingConnection(connection_parameters) as connection: 
    channel = connection.channel()
    channel.exchange_declare(exchange='DirectPractice',exchange_type='direct')
    channel.queue_declare(queue='directTask')
    channel.queue_bind(exchange='DirectPractice',queue='directTask',routing_key='אור הנר')
    channel.basic_consume(queue='directTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
