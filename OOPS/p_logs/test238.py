import logging
import student

#IT will not print in log file and it will not print from debug 

logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log238.log',level=logging.DEBUG)

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')


