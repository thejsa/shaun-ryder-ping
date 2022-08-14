#!/usr/bin/env python3
# python3 -m pip install play_sounds asyncio

import os
import platform  # For getting the operating system name
import subprocess  # For executing a shell command
import sys

from play_sounds import play_file, play_after
from time import sleep


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower() == 'windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    # command = ['ping', param, '1', host, '-t', '1']
    command = ['ping', host, '-t', '1']

    return subprocess.call(command) == 0


# print(os.path.dirname(os.path.realpath(__file__)))
os.chdir(os.path.dirname(os.path.realpath(__file__)))
dare = False
count = 0
while not dare or count < 6:
    play_file('its-coming-up-spleeter-2.wav', block=False)
    # print(count)
    print("It's coming up,")
    dare = ping(sys.argv[1])
    count += 1
    # ping('1.1.1.1')

# sleep(1.0)
print("IT'S DARE")
play_file('kick-its-dare-full.wav', block=True)
