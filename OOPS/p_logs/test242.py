#to write in file and console both
import logging

#1. Create a custom logger
logger = logging.getLogger('demologger')
logger.setLevel(logging.DEBUG)

#2. Create a console handler and file handler
consolehandler=logging.StreamHandler()
consolehandler.setLevel(logging.ERROR)

filehandler = logging.FileHandler('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log242.log',mode='w')
filehandler.setLevel(logging.WARNING)

#3. Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%y %I:%M%S  %p')

consolehandler.setFormatter(formatter)  #we can give seperate format if we want
filehandler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(consolehandler)
logger.addHandler(filehandler)

# Now using the logger to log messages
logger.critical('this is a critical message')
logger.error('this is an error message')
logger.warning('this is a warning message')
logger.info('this is an info message')
logger.debug('this is a debug message')
