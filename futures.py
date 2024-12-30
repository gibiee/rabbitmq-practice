import concurrent.futures
import os, time

def calculate(iter=100000000) :
    start_time =  time.time()

    total = 0
    for i in range(iter) : # 1억번 반복 : 약 5초 소요
        total += i

    print(f"[PID {os.getpid()}] 실행 완료! {time.time()-start_time:.2f}s")
    return total

if __name__ == '__main__':
    WORKERS = 4
    FOR_ITER = 5

    jobs = []
    executor = concurrent.futures.ThreadPoolExecutor()
    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=WORKERS)
    for i in range(FOR_ITER):
        job = executor.submit(calculate, iter=100000000)
        print('-----', type(job), job)
        jobs.append(job)
    
    for job in jobs :
        print('job result :', job.result())