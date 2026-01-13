import logging

logging.basicConfig(
    filename='test_app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H-%M-%S'
)

logging.debug('This is the debug message')
logging.info('This is the info message')
logging.warning('This is the warning message')
logging.error('This is the error message')
logging.critical('This is the critical message')