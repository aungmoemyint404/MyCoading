import cmd
import random
import time
import sys
import os

import time
import os


import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
while True:
    i = (i + 1) % len(symbols)
    print('\r\033[K%s loading...' % symbols[i], flush=True, end='')
    time.sleep(0.1)

anime = ["|", "/", "-", "\\"]

done = False

while done is False:
    for i in anime:
        print('Please wait while system is Loading...', i)
        os.system('clear')
        time.sleep(0.1)

import itertools
import threading
import time
import sys
done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
t = threading.Thread(target=animate)
t.start()
#long process here
time.sleep(10)
done = True




animation = [" ◜","◝","◞","◟"]

for i in range(30):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

animation = "⬖⬘⬗⬙"

for i in range(30):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
    #do something
print("End!")