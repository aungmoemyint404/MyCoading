import cmd
import random
import time
import sys
import os
run = os.system


import itertools
import threading

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
t = threading.Thread(target=animate)
t.start()
#long process here
time.sleep(2)
run('clear')
done = True
def net():
    run('''#!/bin/bash

ping -c 1 google.com > /dev/null 2>&1
if [ $? -eq 0 ]; then
  echo "\033[32;1m "ONLINE""
  python3 menu.py
else
  echo "No internet connection. \033[31;5mOffline\033[0m"
fi
    ''')