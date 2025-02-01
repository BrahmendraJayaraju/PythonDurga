import logging

#overwrite logfile
logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log227.txt',level=logging.WARNING,filemode='w')

print('logging demo')
logging.critical('this is critical message')
logging.error('this is error message')
logging.warning('this is warning message')
logging.info('this is info message')
logging.debug('this is debug message')
