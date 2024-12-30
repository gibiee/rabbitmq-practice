import pika

REPEAT = 10

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.queue_declare(queue='hello')
for i in range(REPEAT) : 
    channel.basic_publish(exchange='', routing_key='hello', body=f'Hello World! {i}')
    print(f" [x] Sent 'Hello World! {i}'")
 
connection.close()