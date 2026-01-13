import multiprocessing
import time

## Create 2 different functions or operations
def squares():
    for i in range(5):
        ## sleep for 1 second
        time.sleep(1)
        print(f'Square of {i} is {i*i}')

def cubes():
    for i in range(5):
        ## sleep for 1.5 seconds
        time.sleep(1.5)
        print(f'Cube of {i} is {i*i*i}')

if __name__ == "__main__":
    ## Create 2 processes
    p1 = multiprocessing.Process(target=squares)
    p2 = multiprocessing.Process(target=cubes)

    start_time = time.time()
    ## Start processes
    p1.start()
    p2.start()

    ## Wait till both the processes gets completed
    p1.join()
    p2.join()

    time_to_complete = time.time()-start_time
    print(f'Finished Time = {time_to_complete}')
