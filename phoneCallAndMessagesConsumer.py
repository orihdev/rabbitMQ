import pika
import time

def callback(ch, method, properties, body):
    time.sleep(0.1)
    print(f'in phone call and messages consumer - {body.decode("utf-8")}')
def reverse(x):
  return x[::-1]

connection_parameters = pika.ConnectionParameters(host='localhost')


with pika.BlockingConnection(connection_parameters) as connection: 
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')
    channel.queue_declare(queue='phoneCallsFinalTask')
    channel.queue_bind(exchange='FinalTask',queue='phoneCallsFinalTask',routing_key='phoneCall.#')
    channel.queue_bind(exchange='FinalTask',queue='phoneCallsFinalTask',routing_key='message.#')
    channel.basic_consume(queue='phoneCallsFinalTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
