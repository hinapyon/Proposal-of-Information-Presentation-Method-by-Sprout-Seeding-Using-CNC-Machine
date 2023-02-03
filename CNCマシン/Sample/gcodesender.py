#!/usr/bin/python3
"""
Simple GCode streaming script
"""
import argparse
import time

from tqdm import tqdm

import serial

START_TIME = time.time()

ngc = 'sikaku.ngc'
sergrbl = serial.Serial("/dev/tty.usbmodem143301", 115200)
serservo = serial.Serial("/dev/tty.usbserial-14310", 115200)

def remove_comment(string):
    """Remove comments from GCode if any"""
    if string.find(';') == -1:
        return string
    return string[:string.index(';')]


def file_len(fname):
    """Counts lines in GCode source file"""
    counter = None
    with open(fname) as file:
        for counter, value in enumerate(file):
            pass
    return counter + 1


LENGTH_FILE = file_len(ngc)
# print('length: ' + str(lenght))
# Open serial port
# s = serial.Serial('/dev/ttyACM0',115200)
SERIAL_CONNECTION = serial.Serial(sergrbl, 115200)
print('Opening Serial Port')

# Open g-code file
# f = open('/media/UNTITLED/shoulder.g','r');
GCODE_FILE = open(ngc, 'r')
print('Opening GCode File')

# Hit enter a few times to wake up
SERIAL_CONNECTION.write(str.encode("\r\n\r\n"))
time.sleep(2)  # Wait for initialization
SERIAL_CONNECTION.flushInput()  # Flush startup text in serial input
print('Sending GCode')

# Stream g-code

if ARGS.verbose:
    for line in GCODE_FILE:
        cmd_gcode = remove_comment(line)
        cmd_gcode = cmd_gcode.strip()  # Strip all EOL characters for streaming
        if (cmd_gcode.isspace() is False and len(cmd_gcode) > 0):
            print('Sending: ' + cmd_gcode)
            SERIAL_CONNECTION.write(cmd_gcode.encode() +
                                    str.encode('\n'))  # Send g-code block
            # Wait for response with carriage return
            grbl_out = SERIAL_CONNECTION.readline()
            print(grbl_out.strip().decode("utf-8"))
    SERIAL_CONNECTION.write(str.encode('G0X0Y0Z0') + str.encode('\n'))
    print("--- %s seconds ---" % int(time.time() - START_TIME))

else:
    for x in range(1, ARGS.repetition + 1):
        for line in tqdm(GCODE_FILE, total=LENGTH_FILE,
                         unit='line', desc='Stage ' + str(x)):
            cmd_gcode = remove_comment(line)
            cmd_gcode = cmd_gcode.strip()  # Strip all EOL characters
            if (cmd_gcode.isspace() is False and len(cmd_gcode) > 0):
                SERIAL_CONNECTION.write(cmd_gcode.encode() +
                                        str.encode('\n'))  # Send g-code block
                # Wait for response with carriage return
                grbl_out = SERIAL_CONNECTION.readline()
                # print(grbl_out.strip().decode("utf-8"))
        GCODE_FILE.seek(0)
    SERIAL_CONNECTION.write(str.encode('G0X0Y0Z0') + str.encode('\n'))


# Wait here until printing is finished to close serial port and file.
input("  Press <Enter> to exit.")

# Close file and serial port
GCODE_FILE.close()
SERIAL_CONNECTION.close()
