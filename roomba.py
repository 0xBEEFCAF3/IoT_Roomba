import serial
import RPi.GPIO as GPIO
import time
import struct

dd_pin = 7
PASSIVE = 130
SAFE = 131
FULL = 132

port = serial.Serial("/dev/ttyAMA0", baudrate=19200, timeout=3.0)
port.close()
port.open()

def turn_on():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(7, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(7, GPIO.HIGH)
    time.sleep(2)

def set_mode(mode):
    write_num(128)
    write_num(mode)
    time.sleep(1)

def write_num(num):
    port.write(struct.pack('!B', num))

def safe_mode():
    set_mode(SAFE)

def full_mode():
    set_mode(FULL)

def passive_mode():
    set_mode(PASSIVE)

def set_digits(digit1, digit2, digit3, digit4):
    write_num(164)
    port.write(digit1)
    port.write(digit2)
    port.write(digit3)
    port.write(digit4)

def set_digits_string(msg):
    safe_mode()
    set_digits(msg[0], msg[1], msg[2], msg[3])

def clean():
    turn_on()
    write_num(135)

def dock():
    turn_on()
    write_num(143)

def power():
    write_num(133)

turn_on()
