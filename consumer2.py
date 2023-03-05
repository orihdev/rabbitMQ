# import pika
# import time

# def callback(ch, method, properties, body):
#     time.sleep(0.1)
#     if "city רנה רוא" in body.decode("utf-8") :
#         print(f'{body.decode("utf-8")}')

# connection_parameters = pika.ConnectionParameters(host='localhost')


# with pika.BlockingConnection(connection_parameters) as connection: 
#     channel = connection.channel()
#     channel.exchange_declare(exchange='FanoutPractice',exchange_type='fanout')
#     channel.queue_declare(queue='fanoutTask2')
#     channel.queue_bind(exchange='FanoutPractice',queue='fanoutTask2')
#     channel.basic_consume(queue='fanoutTask2',on_message_callback=callback,auto_ack=True)
#     channel.start_consuming()
