# Run in IDA Pro
# Open -> Script file
# You need to have the 'companion' file in the same dir as the script
# the companion is generated by kext_tool_10 or joker and should be renamed to 'kext_companion'

import idc
import os

def add_to_ida(line):

    splitted = line.split(':')

    if len(splitted) <= 0:
        return # Invalid

    address = splitted[0]
    name = splitted[1]

    address = int(address, 16)

    idc.add_entry(address, address, name, 1)

if __name__ == "__main__":

    path = os.path.dirname(__file__)
    path = os.path.join(path, "kext_companion")

    file = open(path)

    for line in file:
        add_to_ida(line)
    file.close()
