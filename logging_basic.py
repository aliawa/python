import logging

# Setup logging to file "example.log"
logging.basicConfig(format='%(levelname)s:%(message)s', 
        filemode='w',                                       # Don't append to existing log
        filename="example.log",
        level=logging.DEBUG)

# Now use the logger
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


