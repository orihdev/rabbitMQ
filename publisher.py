import pika
from faker import Faker

fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.queue_declare(queue='fakerQueue')
    for i in range(100):
        person = fake.name()
        location = fake.city()
        msg = f'{person} is in city {location}'
        channel.basic_publish(exchange='',routing_key='fakerQueue',body= msg)