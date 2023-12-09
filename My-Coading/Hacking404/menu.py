import cmd
import random
import time
import sys
import os
run = os.system


def logo(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
        

def ma():
    logo('''\033[32;1m             xMMM0.
              ,XMMMl
                oMMMK.
                 .KMMMd
                   lWMMX,
                    .0MMMk
                    .KMMMx
                   oMMMX'
                 'KMMWl
                dMMM0.
              ;NMMWc         .ooooooooooooo,
             xWWWO.          :WWWWWWWWWWWWWd\033[0m
         
         〔 \033[39;100mTOOL BY https://github.com/aungmoemyint404\033[0m 〕
         
''')
    print('01...Shell-GPT       \033[31mOpenAI: https://openai.com/blog/chatgpt\033[0m') 
    print('02...Osingram        \033[31mInstargem OSINT Hacking\033[0m')
    print('03...Cam-Hacking     \033[31mWebcam Phisher Tools\033[0m')
    print('04...Social-Tools    \033[31mFb Gmail Tiktok Instargram othr Phishing Tools\033[0m')
    print('05...Deface          \033[31mVideo & Photo Face Blur edit\033[0m')
    print('Bb...More            \033[31mEnder B & b\033[0m')
def mb():
     print('')
try:
    def menu():
          ma()
          ed = input('\033[32;5m♔\033[0m\033[39;1m 404~$\033[0m ')
          if ed == '1' or ed == '01':
               from Tools import shell_gpt
               animation = "⬖⬘⬗⬙"
               for i in range(20):
                   time.sleep(0.1)
                   sys.stdout.write("\r" + animation[i % len(animation)])
                   sys.stdout.flush()
               run('clear')
               run('figlet -f small  SHELL-GPT')
               shell_gpt.pkg()
               shell_gpt.menu()
          if ed == '2' or ed == '02':
                from Tools import osingram
                animation = "⬖⬘⬗⬙"
                for i in range(20):
                    time.sleep(0.1)
                    sys.stdout.write("\r" + animation[i % len(animation)])
                    sys.stdout.flush()
                osingram.file_check()    
                 
          if ed == '5' or ed == '05':
               from Tools import deface
               animation = "⬖⬘⬗⬙"
               for i in range(20):
                   time.sleep(0.1)
                   sys.stdout.write("\r" + animation[i % len(animation)])
                   sys.stdout.flush()
               run('clear') 
               run('figlet -f small  DEFACE')
               deface.pkg()
               deface.menu()

               
          else:
               print('ender menu number')
               menu()
    menu()
    
except KeyboardInterrupt:
       run('clear')
       print('EXID')
       




