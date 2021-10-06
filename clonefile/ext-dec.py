# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 jutt.py')

from os import system
from time import sleep

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def reg():
    os.system('clear')
    print ''
    print '\x1b[1;37mFacebook Dump IDS'
    print ''
    time.sleep(1)
    try:
        to = open('/data/data/com.termux/files/usr/libexec/awk/.termux.log', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://juttkey.000webhostapp.com/fuckyou.txt').text
    if to in r:
        print '\t     \x1b[1;92mEXECUTING EXTRACTOR\x1b[0m'
        time.sleep(1)
    else:
        os.system('clear')
        os.system('echo  "\n\x1b[1;92m              \n\x1b[1;92m                      \n\x1b[1;96m                        \n\x1b[1;92m     {} {}  {} {}{}{} {}{}{} \n\x1b[1;97m     {} {}  {}   {}     {} \n\x1b[1;93m     {} {}  {}   {}     {}  \n\x1b[1;96m     {} {}  {}   {}     {} \n\x1b[1;94m  {}{}   {}{}    {}     {}  \n\x1b[1;93m                      \n\x1b[1;92m         Jutt Badshah Brand~                       \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah x ?????\n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/juttbadshah6969\n\x1b[1;97m\xe2\x9e\xa3 WP NO  : +923100209977\n\x1b[1;91m-----------------------------------------------" | lolcat ')
        print '\t\x1b[4;31mApproved Failed'
        print '\x1b[0;97m    Your Id Is Not Approved'
        print ' \x1b[0;33mCopy the id input key our website'
        print ''
        print ' \x1b[1;92mYour id: \x1b[0;91m' + to
        print ''
        raw_input('\x1b[1;93m Press \x1b[0;91menter\x1b[1;93m to input key')
        os.system('xdg-open https://juttkey.000webhostapp.com/')
        time.sleep(5)
        os.system('xdg-open https://t.me/joinchat/3Ls9bUMjqpJkN2Jk')
        reg()


def reg2():
    os.system('clear')
    os.system('echo  "\n\x1b[1;92m              \n\x1b[1;92m                      \n\x1b[1;96m                        \n\x1b[1;92m     {} {}  {} {}{}{} {}{}{} \n\x1b[1;97m     {} {}  {}   {}     {} \n\x1b[1;93m     {} {}  {}   {}     {}  \n\x1b[1;96m     {} {}  {}   {}     {} \n\x1b[1;94m  {}{}   {}{}    {}     {}  \n\x1b[1;93m                      \n\x1b[1;92m         Jutt Badshah Brand~                       \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah x ?????\n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/juttbadshah6969\n\x1b[1;97m\xe2\x9e\xa3 WP NO  : +923100209977\n\x1b[1;91m-----------------------------------------------" | lolcat ')
    print '\t\x1b[4;31mApproval not detected'
    print '\t \x1b[0;97mCopy Key and press \x1b[0;91menter\x1b[0;97m , Past input key our website'
    id = uuid.uuid4().hex[:50]
    print ' \x1b[1;92mYour id: \x1b[0;91m' + id
    print ''
    raw_input('\x1b[1;93m Press \x1b[0;91menter\x1b[1;93m to input key')
    os.system('xdg-open https://juttkey.000webhostapp.com/')
    time.sleep(5)
    os.system('xdg-open https://t.me/joinchat/3Ls9bUMjqpJkN2Jk')
    sav = open('/data/data/com.termux/files/usr/libexec/awk/.termux.log', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press \x1b[0;91menter\x1b[1;92m to check Approval ')
    reg()


from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding('utf8')

def jutt():
    os.system('echo  "\n=============================================\n" | lolcat ')




login()
ex_id()
if __name__ == '__main__':
    reg()
