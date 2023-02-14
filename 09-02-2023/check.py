import os
from datetime import datetime
x = os.stat('xyz.txt')
print(datetime.fromtimestamp(x.st_ctime))
print(datetime.fromtimestamp(x.st_mtime))
print(datetime.fromtimestamp(x.st_atime))
print(os.path.splitext())