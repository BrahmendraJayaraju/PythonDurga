import logging

logger = logging.getLogger('studenthandler')
logger.setLevel(logging.DEBUG)


#2. Create  file handler
filehandler = logging.FileHandler('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/student1.log',mode='w')
filehandler.setLevel(logging.WARNING)

#3. Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%y %I:%M%S  %p')


filehandler.setFormatter(formatter)

logger.addHandler(filehandler)

# Now using the logger to log messages
logger.critical('this is student a critical message')
logger.error('this is student an error message')
logger.warning('this  student is a warning message')
logger.info('this is student an info message')
logger.debug('...student this is a debug message.....')