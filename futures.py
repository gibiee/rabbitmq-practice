import concurrent.futures
import os, time
import psutil

data = {'test': 1}

def calculate(iter=100000000) :
    start_time = time.time()

    data['test'] = data['test'] + 1
    print(id(data), data)

    total = 0
    for i in range(iter): # 1억번 반복 : 약 5초 소요
        total += i

    print(f"[PID {os.getpid()}] calculate() 실행 완료! {time.time()-start_time:.2f}s")
    return total

def calculate_sleep(iter=5) :
    start_time = time.time()

    total = 0
    for i in range(iter):
        total += i
        time.sleep(1)

    print(f"[PID {os.getpid()}] calculate_sleep() 실행 완료! {time.time()-start_time:.2f}s")
    return total

if __name__ == '__main__':
    cpu_core = psutil.cpu_count(logical=False)
    print(f'CPU core : {cpu_core}')

    WORKERS = cpu_core
    FOR_ITER = 10

    jobs = []
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=30)
    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS)
    for i in range(4):
        job = executor.submit(calculate, iter=100000000)
        jobs.append(job)
        print('-----', type(job), job)
        time.sleep(0.1)

    for i in range(10):
        job = executor.submit(calculate_sleep, iter=5)
        jobs.append(job)
        print('-----', type(job), job)
        time.sleep(0.1)
    
    for job in jobs :
        print('job result :', job.result())