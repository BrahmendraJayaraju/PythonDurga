#to get all levels

import logging

#logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log226.txt',level=logging.DEBUG)

#WE CAN USE NUMBERS ALSO
logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log226.txt',level=10)

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')

