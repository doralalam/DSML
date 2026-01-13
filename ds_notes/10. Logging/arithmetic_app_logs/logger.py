## import logging
import logging

## Configuring Logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    ## handler is similar to filename and filemode, we can use any of the 2 methods to create a log file
    handlers=[
        ## name of the log file
        logging.FileHandler('arithmetic_app.logs'),
        logging.StreamHandler()
    ]
)

## FileHandler creates the file with the specified name and then writes the log messages which passes the level filter in that file

## StreamHandler writes all the log messages which passed the level filter in the terminal or console for quick readability instead of opening the log files