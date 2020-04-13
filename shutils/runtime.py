import os
import sys
import time


def restart(delay=0):
    time.sleep(delay)
    python = sys.executable
    os.execl(python, python, *sys.argv)
