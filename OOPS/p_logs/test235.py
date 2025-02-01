
#to get time and asctime should be at first
#to get in 24 hrs format

import logging

#H FOR 24 HRS
#P FOR AM

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %H:%M%S  %p')

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')