import logging


#to get only level names  ,loggernames and messages

logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')