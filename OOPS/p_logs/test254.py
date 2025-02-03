import logging
import logging.config



# Load logging configuration from the file
logging.config.fileConfig('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/logging_config.init')

# Get the logger you configured
l2 = logging.getLogger('demologger')

# Log messages at various levels
l2.critical('f2 is a critical message')
l2.error('f2 this is an error message')
l2.warning('f2 this is a warning message')
l2.info('f2 this is an info message')
l2.debug('f2 this is a debug message')
