## We can achieve advanced multi threading using the 'ThreadPoolExecutor' which dynamically allocates the threads instead of manually creating individual threads

from concurrent.futures import ThreadPoolExecutor
import time
import numpy as np

## Function to indicate the delay in execution
def print_number(number):
    time.sleep(1)
    return f'Number: {number}'

## Range of numbers from 1 to 19, we can give any list or numpy array or any input as per our requirement   
numbers = np.arange(1,20,1)

start_time = time.time()

## ThreadPoolExecutor will create at max 3 workers or threads dynamically to perform the execution concurrently
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    ## executor.map() function always returns the iterator. So, we must always iterate the results object to get the appropriate result

time_taken = time.time()-start_time

## Since the result is iterator, we need to iterate
for result in results:
    print(result)

print(f'Time taken for execution is {time_taken}')