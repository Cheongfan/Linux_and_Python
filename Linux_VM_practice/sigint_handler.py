#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal, time
import sys

def handler(signum, time):
    print "\nI got a SIGINT, but I am not stopping"

signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    sys.stdout.write("\r%d" % i)
    sys.stdout.flush()
    i += 1
