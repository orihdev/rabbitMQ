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
    channel.queue_declare(queue='locationFinalTask')
    channel.queue_bind(exchange='FinalTask',queue='locationFinalTask',routing_key='location.#')
    channel.basic_consume(queue='locationFinalTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
