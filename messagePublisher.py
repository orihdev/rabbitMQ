import pika
from faker import Faker

def reverse(x):
  return x[::-1]



fake = Faker('iw_IL')
connection_parameters = pika.ConnectionParameters(host='localhost')

with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    channel.exchange_declare(exchange='FinalTask',exchange_type='topic')


    for i in range(10000):
        phone1 = fake.phone_number()
        phone2 = fake.phone_number()
        textMessege = fake.paragraph(nb_sentences=1)
        msg = f'{phone1} messaged {phone2}: {textMessege}'
        channel.basic_publish(exchange='FinalTask',routing_key=f'message.{phone1}.{phone2}',body= msg)