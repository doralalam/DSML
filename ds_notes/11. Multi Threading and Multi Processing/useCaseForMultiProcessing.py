'''
Real World Example: Multi Processing for CPU bound tasks
Scenario: Factorial Calculation
Factorial Calculations, especially for a large numbers 
rquires high computational work.
Multi-processing can distribute this work across the
CPU cores, improving performance. 
'''

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
import time
import sys

## To set the maximum integer size, 
## because, using the biggest number will hang the CPU due to it's workload
## So, it is always a good practice to hold a limit for an integer while working on computational works

sys.set_int_max_str_digits(100000)

## Function to calculate facatorial of a number
def factorial(number):
    if number==1:
        return 1
    else:
        return number*(factorial(number-1))

## Input (Python has a recursion depth limit of nearly 1000. So, using numbers less than 1000)
numbers = [500, 400, 200]

## Entry Point
if __name__ == '__main__':

    start_time = time.time()

    ## Create Dynamic Wroker Processes. This can be done in 2 methods, below is the old method. 
    ## ProcessorPoolExecutor is the latest method
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)

    '''
     with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(factorial, numbers)
    '''
    
    time_taken = time.time()-start_time

    for i,j in zip(numbers,results):
        print(f'Factorial of {i} is {j}')
    
    print(f'Time taken to calucate the factorials is {time_taken} seconds')