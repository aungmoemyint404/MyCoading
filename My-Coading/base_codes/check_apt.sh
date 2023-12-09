#!/bin/bash
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ found ]"
which msfconsole > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not found "
echo -e $yellow "[ ! ] Installing Metasploit-Framewor
echo -e $blue "[ ✔ ] Done installing ...."
which msfconsole > /dev/null 2>&1
sleep 2
fi
