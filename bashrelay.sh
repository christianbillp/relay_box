#!/bin/bash

case "$1" in
  "setup")
    # Prepare GPIO4
    echo 4 > /sys/class/gpio/export

    # Set GPIO4 as output
    echo out > /sys/class/gpio/gpio4/direction
    ;;
  "on")
    # Set GPIO4 as high
    echo 1 > /sys/class/gpio/gpio4/value
    ;;
  "off")
    # Set GPIO4 as low
    echo 0 > /sys/class/gpio/gpio4/value
    ;;
  *)
    echo "You have failed to specify what to do correctly."
    exit 1
    ;;
esac

