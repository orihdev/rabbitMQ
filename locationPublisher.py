import pika
from faker import Faker

def reverse(x):
  return x[::-1]



fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')


    for i in range(1000):
        phone1 = fake.phone_number()
        location = fake.city()
        msg = f'{phone1} is in city {reverse(location)}'
        channel.basic_publish(exchange='FinalTask',routing_key=f'location.{phone1}.{location}',body= msg)