import concurrent.futures
import os, time
import psutil

data = {'test': 1}

def calculate(iter=100000000) :
    start_time = time.time()

    data['test'] = data['test'] + 1
    print(id(data), data)

    total = 0
    for i in range(iter) : # 1억번 반복 : 약 5초 소요
        total += i

    print(f"[PID {os.getpid()}] 실행 완료! {time.time()-start_time:.2f}s")
    return total

if __name__ == '__main__':
    cpu_core = psutil.cpu_count(logical=False)
    print(f'CPU core : {cpu_core}')

    WORKERS = cpu_core
    FOR_ITER = 10

    jobs = []
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS)
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS)
    for i in range(FOR_ITER):
        job = executor.submit(calculate, iter=100000000)
        print('-----', type(job), job)
        jobs.append(job)
        time.sleep(0.1)
    
    for job in jobs :
        print('job result :', job.result())