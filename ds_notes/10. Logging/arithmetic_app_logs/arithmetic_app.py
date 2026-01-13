from logger import logging

## Creating a logger for Arithmetic_App
logger = logging.getLogger('Arithmetic Logger')

## Create custom functions and work on log messages
def add(a,b):
    result = a+b
    logger.debug(f'Addition of {a} and {b} is {result}')
    return result

def sub(a,b):
    result = a-b
    logger.debug(f'Subtraction of {b} from {a} is {result}')
    return result

def mul(a,b):
    result= a*b
    logger.debug(f'Multiplication of {a} and {b} is {result}')
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a} by {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Zero Divison Error Occured while performing Divison')
        return None
    

## Call the functions
add(10,20)
sub(20,10)
mul(10,30)
div(100,40)
div(200,0)

    
    
