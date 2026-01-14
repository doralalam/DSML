# We can achieve advanced multi processing by using 'ProcessPoolExecutor' 
# which dynamically creates processes that runs on cores concurrently reducing the execution time

from concurrent.futures import ProcessPoolExecutor
import time

def squares(number):
    time.sleep(1)
    return f'Square of {number} is {number*number}'

numbers = [1,2,3,4,5,6]

## Entry point, i.e., worker/child processes will run the code above this line and returns the result to iterator, 
## otherwise, worker process will run the entire code which results in creating infinite pool-processes
## Detailed explanation is at the bottom of this file

if __name__ == "__main__":
    
    start_time = time.time()

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(squares, numbers)

    time_taken = time.time()-start_time

    for result in results:
        print(result)

    print(f'Time taken is {time_taken}')


'''
`if __name__ == "__main__":` is required here to prevent your process pool from recursively re‑starting itself when new processes are spawned.

## What `if __name__ == "__main__":` means

- Every Python file has a **`__name__`** variable.  
- When you run a file directly (e.g., `python script.py`), `__name__` is set to `"__main__"`.  
- When the same file is **imported** as a module, `__name__` is the module name, not `"__main__"`.

So:

```python
if __name__ == "__main__":
    # this block runs only when the file is executed directly
```

This protects the “entry point” code from running when the module is imported.

## Why it matters for `ProcessPoolExecutor`

`ProcessPoolExecutor` (and `multiprocessing` in general) **starts new Python processes**.  
On Windows and in many modern setups, child processes are started with the **spawn** method, which means:

- The child process **imports your main module** to recreate the state.  
- If your process‑pool code is at the top level (not inside `if __name__ == "__main__":`), then every child process will import the module and run that top‑level code again.[4][5]
- That causes each child to create its own `ProcessPoolExecutor` again, which can lead to:
  - Infinite process spawning  
  - `RuntimeError` / `RecursionError`  
  - Very confusing behavior

By wrapping the pool creation and `.map(...)` in:

```python
if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(squares, numbers)

    for result in results:
        print(result)
```

you guarantee:

- Only the **original main process** creates the process pool and submits tasks.  
- Worker processes just import the module to get the `squares` function; they do not rerun the main block.

So in your example, that `if __name__ == "__main__":` guard is not optional; it is the correct pattern whenever using `ProcessPoolExecutor` or `multiprocessing` in a script.

'''