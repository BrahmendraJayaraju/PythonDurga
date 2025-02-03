#by  using dictionary as config file

import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters=
    {
        'f':
        {
            'format': '%(asctime)s:%(name)s:%(levelname)s:%(message)s',
            'datefmt': '%d/%m/%y %I:%M:%S %p'
        }
    },
    handlers=
    {
        'h':
        {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.WARNING
        }
    },
    root=
    {
        'handlers': ['h'],
        'level': logging.DEBUG
    }
)

# Apply the logging configuration
dictConfig(logging_config)
# Test logging
l2 = logging.getLogger('brahmendra')
#l2 = logging.getLogger()


l2.critical('console is a critical message')
l2.error('console this is an error message')
l2.warning('console this is a warning message')
l2.info('console this is an info message')
l2.debug('console this is a debug message')
