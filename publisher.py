import pika
from faker import Faker

def reverse(x):
  return x[::-1]



fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='DirectPractice',exchange_type='direct')


    for i in range(10000):
        person = fake.name()
        location = fake.city()
        msg = f'{reverse(person)} is in city {reverse(location)}'
        channel.basic_publish(exchange='DirectPractice',routing_key=location,body= msg)