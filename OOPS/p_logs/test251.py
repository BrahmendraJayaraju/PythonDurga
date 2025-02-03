from test250 import  get_custom_logging
import logging


def f1():
    l1=get_custom_logging(logging.DEBUG)

    l1.critical('f1  is critical message')
    l1.error('f1 this is error message')
    l1.warning('f1 this is warning message')
    l1.info('f1 this is info message')
    l1.debug('f1 this is debug message')


def f2():
    l2=get_custom_logging(logging.WARNING)

    l2.critical('f2  is critical message')
    l2.error('f2 this is error message')
    l2.warning('f2 this is warning message')
    l2.info('f2 this is info message')
    l2.debug('f2 this is debug message')


f1()
f2()
