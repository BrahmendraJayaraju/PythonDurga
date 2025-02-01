import logging


#we can pass multiple all are in documentation
#process gives number
#module gives name of python  file
# line no give line number
#d means digit

logging.basicConfig(format='%(levelname)s:%(name)s:%(process)d:%(message)s:%(module)s:%(lineno)d')

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')