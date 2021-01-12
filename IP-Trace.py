#/usr/bin/python
import os
import sys
from time import sleep
from termcolor import colored

os.system('clear')
os.system('figlet -f slant IP-Trace | lolcat')
print (colored('==================================================', 'green'))
print (colored(' author    :   HadsXcode                     ', 'green'))
print (colored(' Youtube   :   GarudaTeamSecurity                   ', 'green'))
print (colored(' github    :   https://github.com/SubangProgramer   ', 'green'))
print (colored(' whatsapp  :   085793378137                         ', 'green'))
print ("")
print (colored(' Bila ada bug hubungi saya                          ', 'green'))
print (colored('==================================================', 'green'))
user=input(colored('[+] input target IP : ', 'green'))
PORT=input(colored('[+] input target port : ', 'green'))
os.system('curl http://ip-api.com/'+user)
print (colored('[!] succes trace on port an ip', 'yellow'))
print (colored('[+] IP : '+user, 'blue'))
print (colored('[+] PORT : '+PORT, 'blue'))

