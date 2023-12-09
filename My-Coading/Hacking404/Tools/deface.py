import cmd
import random
import time
import sys
import os
run = os.system
command = os.system

def pkg():
    run('''#!/bin/bash
    which deface > /dev/null 2>&1
    if [ "$?" -eq "0" ]; then
       echo  \033[0m"[ ✔ ] Deface..............[ \e[32;1mfound\e[0m ]"
    else
       echo  "[ X ] Deface  -> \e[31;1mnot found\e[0m "
       echo  "[ ! ] Installing Deface "
       sudo python3 -m pip install deface
       echo  "[ ✔ ] Done installing ...."
       sleep 2
       clear 
    fi
    ''')

def menu():
    print('[ 1 ] image_replacewith')
    print('[ 2 ] Video_replacewith')
    print('')
    print('')
    ed = input('\033[32;5m☣\033[0m\033[39;1m DEFACE~$\033[0m ')