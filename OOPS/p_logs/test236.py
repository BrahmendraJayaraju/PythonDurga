#how to add exception info to the log file and demo program



import logging



logging.basicConfig(filename='/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/log236.txt',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %H:%M%S  %p')


logging.info('new request came ')
try:
    x=int(input('enter the 1st number'))
    y=int(input('enter the 2nd number'))
    print('the result :',x/y)
except ZeroDivisionError as msg:
    print('cant divide by zero')
    logging.exception(msg)
except ValueError as msg:
    print('provide int value only ')
    logging.exception(msg)

logging.info('request processing completed')

