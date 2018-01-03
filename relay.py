import pigpio
import time

# Relays are active LOW

# Channels for pins
channels = [4, 17, 27, 22]

# Create gpio object
pi = pigpio.pi()

# Initialize GPIO
for pin in channels:
    pi.set_mode(pin, pigpio.OUTPUT)

# Test
for i in range(4):
    print('Running {}'.format(i))
    pi.write(channels[i], 0)
    time.sleep(1)
    pi.write(channels[i], 1)

if __name__ == '__main__':



