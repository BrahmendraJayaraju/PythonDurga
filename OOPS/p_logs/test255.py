import logging
import logging.config



# Load logging configuration from the file
logging.config.fileConfig('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/console_config.init')

# Get the logger you configured
l2 = logging.getLogger('demologger')

# Log messages at various levels
l2.critical('console is a critical message')
l2.error('console this is an error message')
l2.warning('console this is a warning message')
l2.info('console this is an info message')
l2.debug('console this is a debug message')