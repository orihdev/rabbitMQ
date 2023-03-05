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
    channel.queue_declare(queue='interestingPhonesFinalTask')
    channel.queue_bind(exchange='FinalTask',queue='interestingPhonesFinalTask',routing_key='*.09-0733-229.*')
    channel.queue_bind(exchange='FinalTask',queue='interestingPhonesFinalTask',routing_key='*.*.09-0733-229')
    channel.basic_consume(queue='interestingPhonesFinalTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
