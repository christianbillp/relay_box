#%%
import os
import time
import sys

# Relays are active LOW

# Channels for pins
channels = [4, 17, 27, 22]
    
# Initialize GPIO
for pin in channels:
    os.popen('echo {} > /sys/class/gpio/export'.format(pin))
    os.popen('echo out > /sys/class/gpio/gpio{}/direction'.format(pin))

def activate(channel):
    os.popen('echo 1 > /sys/class/gpio/gpio{}/value'.format(channels[channel]))
    
def deactivate(channel):
    os.popen('echo 0 > /sys/class/gpio/gpio{}/value'.format(channels[channel]))
    
'''
# Test
#for i in range(4):
#    print('Running {}'.format(i))
#    pi.write(channels[i], 0)
#    time.sleep(1)
#    pi.write(channels[i], 1)
''';

if __name__ == '__main__':
    arguments = sys.argv
    if arguments[1] == '--help':
        print('Usage: python3 relay.py a 2 for activating channel 2, d for deactivate')
    elif arguments[1] == 'a':
        activate(int(arguments[2]))
    elif arguments[1] == 'd':
        deactivate(int(arguments[2])) 

