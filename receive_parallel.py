import pika, sys, os
import time
import concurrent.futures

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    print("실행 중...")
    start_time =  time.time()

    total = 0
    for i in range(100000000) : # 1억번 반복 : 약 5초 소요
        total += i

    print(f"실행 완료! {time.time()-start_time:.5f}s")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def start_consumer() :
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    #queue를 선언(declare)
    channel.queue_declare(queue='hello')

    #Queue가 'hello'의 consuming 설정
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback)

    #consuming start
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        WORKERS = 2
        consumers = []
        # executor = concurrent.futures.ThreadPoolExecutor()
        executor = concurrent.futures.ProcessPoolExecutor()
        for i in range(WORKERS):
            job = executor.submit(start_consumer)
            print('-----', type(job), job)
            consumers.append(job)

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
