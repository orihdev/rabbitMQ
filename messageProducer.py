import pika
from faker import Faker

def reverse(x):
  return x[::-1]



fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='TopicPractice',exchange_type='topic')


    for i in range(10000):
        phone1 = fake.phone_number()
        phone2 = fake.phone_number()
        person = fake.name()
        location = fake.city()
        msg = f'{reverse(person)} is in city {reverse(location)}'
        channel.basic_publish(exchange='TopicPractice',routing_key=f'location.{location}',body= msg)