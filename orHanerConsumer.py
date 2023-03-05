import pika
import time

def callback(ch, method, properties, body):
    time.sleep(0.1)
    print(f'in location consumer - {body.decode("utf-8")}')
def reverse(x):
  return x[::-1]

connection_parameters = pika.ConnectionParameters(host='localhost')


with pika.BlockingConnection(connection_parameters) as connection: 
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')
    channel.queue_declare(queue='OrHanerFinalTask')
    channel.queue_bind(exchange='FinalTask',queue='OrHanerFinalTask',routing_key='location.*.אור הנר')
    channel.basic_consume(queue='OrHanerFinalTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
