#!/usr/local/bin/python3.9
import subprocess
import time
import re
import sys

def getrx():
     x = subprocess.check_output(['ifconfig','eth0'])
     x = str(x)
     x = int(re.findall(r'RX packets \d+',x)[0].split()[2])
     return x

cal_count = input("calcauter times: \n")
if not (cal_count.isdigit() and  int(cal_count) > 0):
    print("count times must be a integer")
    sys.exit(1)

def cal_speed_rx(func,count):
    for x in range(count):
        b_rx = func()
        time.sleep(5)
        a_rx = func()
        speed_rx = (a_rx - b_rx) / 3
        print('%d. net rx speed is: %f bytes per sec ' % (x+1, speed_rx))
        yield speed_rx

if __name__ == '__main__':
    cal_count = input("calcauter times: \n")
    if not (cal_count.isdigit() and int(cal_count) > 0):
        print("count times must be a integer")
        sys.exit(1)
    stats = list(cal_speed_rx(getrx, int(cal_count)))
    average_speed = sum(stats) / len(stats)
    print('average net rx speed is: %.3f bytes per sec ' % (average_speed))

"""
for x in range(int(cal_count)):
    a += 1
    b_rx = getrx()
    time.sleep(5)
    a_rx = getrx()
    speed_rx = (a_rx - b_rx) / 3
    print('%d. net rx speed is: %f bytes per sec '%(a, speed_rx))
    stats.append(speed_rx)
"""


