import math
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time

def f1(i):
    time.sleep(2)
    print(i)


def f2():
    for i in range(5):
        print(i+10)
        time.sleep(2)

def f3(i):
    time.sleep(2)
    return math.factorial(i)

nums=[1,2,3,4,5,6,7,8,9]

if __name__=='__main__':
    p1=multiprocessing.Process(target=f1(5))
    p2=multiprocessing.Process(target=f2)
    t=time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    


## using ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(f3,nums)
        
    print([res for res in results])

    print(time.time()-t)



