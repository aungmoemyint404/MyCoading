import cmd
import random
import time
import sys
import os
run = os.system
command = os.system


def pkg():
    run('''#!/bin/bash
    which sgpt > /dev/null 2>&1
    if [ "$?" -eq "0" ]; then
       echo  \033[0m"[ ✔ ] Shell-GPT..............[ \e[32;1mfound\e[0m ]"
    else
       echo  "[ X ] Shell-GPT  -> \e[31;1mnot found\e[0m "
       echo  "[ ! ] Installing Shell-GPT "
       sudo python3 -m pip install shell-gpt
       echo  "[ ✔ ] Done installing ...."
       sleep 2
       clear
       sgpt --help 
       clear 
    fi
    ''')
def menu():
    print('[ 1 ] Code               Generate only code.')
    print('[ 2 ] Describe-shell     Describe a shell command.')
    print('[ 3 ] Shell              Generate and execute shell commands. ')
    print('')
    print('')
    ed = input('\033[32;5m☣\033[0m\033[39;1m SGPT~$\033[0m ')
    if ed == '1' or ed == '01':
       code = input('[C]Text~≽ ')
       command('rich -a square -p "sgpt --code '+code+' " -L')
       run('sgpt --code "'+code+'"')
       end = input(': ')
       menu()
    if ed == '2' or ed == '02':
       dshell = input('[DS]Text~≽ ') 
       run('sgpt -d "'+dshell+'"')
       end = input(': ')
       menu()
    if ed == '3' or ed == '03':
        shell = input('[S]Text~≽ ')
        run('sgpt --shell "'+shell+'"')
        end = input(': ')
    if ed == 'b' or ed == 'back':
        run('clear')
        run('python3 menu.py')
        exit()