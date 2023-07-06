import logging

def blah():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
    

if __name__ == '__main__':

    # set logging level from command line arguments like -l DEBUG, or --log=DEBUG
    from argparse import ArgumentParser
    parser = ArgumentParser(description='My app which is mine')
    parser.add_argument('-l', '--log',
        type=str,
        choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'],
        help='Set the logging level')
    args = parser.parse_args()

    # Create a custom logger
    logger = logging.getLogger("some_name")

    # Set log level of the parent.
    # child loggers cannot have level lower that the parent
    logger.setLevel(logging.DEBUG) 

    # Create console handler
    c_handler = logging.StreamHandler()
    c_handler.setLevel(args.log)
    c_format = logging.Formatter('%(funcName)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)

    # Create file handler
    f_handler = logging.FileHandler('file.log')
    f_handler.setLevel(args.log)
    f_format = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    logger.warning('This is a warning')
    logger.error('This is an error')

    blah()



