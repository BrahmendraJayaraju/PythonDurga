#finally block vs os_exit(0)
# 0 and 1

import os
try:
    print('try block')
    os._exit(0)

except ValueError:
    print('except block ')

finally:
    print('finally block ')