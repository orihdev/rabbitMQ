import pika
from faker import Faker


fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')


    for i in range(100):
        phone1 = fake.phone_number()
        phone2 = fake.phone_number()
        msg = f'{phone1} called {phone2}'
        channel.basic_publish(exchange='FinalTask',routing_key=f'phoneCall.{phone1}.{phone2}',body= msg)