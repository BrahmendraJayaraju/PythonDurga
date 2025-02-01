#different module with different log files
import logging

import student1

#1. Create a custom logger
logger = logging.getLogger('testhandler')
logger.setLevel(logging.DEBUG)

#2. Create  file handler
filehandler = logging.FileHandler('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log243.log',mode='w')


#3. Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%y %I:%M%S  %p')


filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

# Now using the logger to log messages
logger.critical('test this is a critical message')
logger.error('test this is an error message')
logger.warning('test this is a warning message')
logger.info('test this is an info message')
logger.debug('test this is a debug message')