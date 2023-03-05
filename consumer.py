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
    channel.exchange_declare(exchange='TopicPractice',exchange_type='topic')
    channel.queue_declare(queue='topicTask')
    channel.queue_bind(exchange='TopicPractice',queue='topicTask',routing_key='location.אור הנר')
    channel.basic_consume(queue='topicTask',on_message_callback=callback,auto_ack=True)
    channel.start_consuming()
