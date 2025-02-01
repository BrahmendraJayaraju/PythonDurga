#problem with logger file
#problem 1

import logging



logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log237.log',level=logging.INFO,filemode='w')

#CANT CHANGE FILE NAME BSE OF ROOT
logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/xyz237.log',level=logging.ERROR,filemode='w')


print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')