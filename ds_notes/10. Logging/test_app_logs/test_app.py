## To import logging from logger.py under logs folder to test
from logger import logging

def add(a,b):
    logging.debug('Addition Operation is being performed')
    return a+b

logging.debug('Addition function is called !')
add(10,20)
