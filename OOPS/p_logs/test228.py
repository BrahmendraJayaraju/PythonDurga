import logging

#default  it takes console and warning and append 

#overwrite logfile
logging.basicConfig()

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')