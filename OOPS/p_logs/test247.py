#custom logger / generic logger and usage

import logging
import inspect


def get_custom_logging(level):
    #instead of root give this name functionnamelogger
    function_name=inspect.stack()[1][3]
    logger_name=function_name+'logger'

    #step1
    logger=logging.getLogger(logger_name)
    print(level)
    logger.setLevel(level)

    #step2
    filehandler=logging.FileHandler('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test247.log',mode='a')

    #step3
    formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',datefmt='%d/%m/%y %I:%M:%S %p')

    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    return logger
