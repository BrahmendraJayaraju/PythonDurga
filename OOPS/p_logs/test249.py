from test247 import get_custom_logging
import logging


def log_student():
    l1=get_custom_logging(logging.DEBUG)

    l1.critical('this is critical message')
    l1.error('this is error message')
    l1.warning('this is warning message')
    l1.info('this is info message')
    l1.debug('this is debug message')

log_student()