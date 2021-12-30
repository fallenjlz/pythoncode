import test2
import sys
import psutil

print(test2.name)
print(test2.__dict__['name'])
print(getattr(test2,'name'))
print(sys.modules['test2'].name)

psutil.pids()