import pika
connection_parameters = pika.ConnectionParameters(host='localhost')
with pika.BlockingConnection(connection_parameters) as connection:
    channel = connection.channel()
    method, properties, body = channel.basic_get(queue='helloWorldQueue',auto_ack=True)
    print(f'Got message: {body}')