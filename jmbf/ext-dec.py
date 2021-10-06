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


def jutt():
    os.system('echo  "\n=============================================\n" | lolcat ')


def logo():
    os.system('echo  "\n       _       __  __ \n      (_)_  __/ /_/ /_\n     / / / / / __/ __/\n    / / /_/ / /_/ /_  \n __/ /\\__,_/\\__/\\__/  \n/___/   Jutt Badshah Brand~                       \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah x ?????\n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/juttbadshah6969\n\x1b[1;97m\xe2\x9e\xa3 WP NO  : +923100209977\n\x1b[1;91m-----------------------------------------------" | lolcat ')


def reg():
    os.system('clear')
    logo()
    try:
        to = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://juttkey.000webhostapp.com/30day.txt').text
    if to in r:
        print ''
    else:
        os.system('clear')
        logo()
        print ''
        print '\t\t \x1b[1;91mApproved Failed'
        print ''
        print '\t\x1b[1;93m    Your Api Is \x1b[1;92mNot Approved'
        print ''
        print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + to
        print ''
        raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
        os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
        time.sleep(5)
        print ''
        raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
        os.system('xdg-open https://t.me/joinchat/3Ls9bUMjqpJkN2Jk')
        reg()


def reg2():
    os.system('clear')
    logo()
    print '\t\t \x1b[4;31mApproval Not Detected'
    print ''
    print '\t   Your Api Is Not %sApproved'
    print ''
    id = uuid.uuid4().hex[:20]
    print ' \t\x1b[1;92mCopy Your Api: \x1b[1;91m' + id
    print ''
    raw_input('\t\x1b[1;97m  And Press \x1b[1;91menter \x1b[1;97mto Input Api')
    print ''
    os.system('xdg-open https://juttkey.000webhostapp.com/30day.php')
    time.sleep(5)
    sav = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'w')
    sav.write(id)
    sav.close()
    raw_input('\t\x1b[1;93m Press \x1b[1;96menter\x1b[1;93m To Check Approval ')
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
WORDS = ('\x1b[40m', '\x1b[41m', '\x1b[42m', '\x1b[43m', '\x1b[44m', '\x1b[45m', '\x1b[46m',
         '\x1b[47m')
word = random.choice(WORDS)
word_site = 'https://pastebin.com/raw/7ub7GLze'
line = requests.get(word_site)
line1 = line.content.splitlines()
line2 = random.choice(line1)

def ok():
    tok = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    print 47 * '\x1b[1;91m-'
    print '\t\x1b\x1b[37mActive Api: \x1b[1;36m' + tok
    print 47 * '\x1b[1;91m-'


def menu():
    os.system('clear')
    logo()
    ok()
    print word
    print line2
    print '\x1b[40m'
    print 47 * '\x1b[1;91m-'
    print ''
    print '\x1b[1;92m[1] Dump All New IDS'
    print '\x1b[1;92m[2] Dump All IDS'
    print '\x1b[1;92m[0] Back'
    menu_s()


def menu_s():
    ms = raw_input('\x1b[1;97m\xe2\x95\xb0\xe2\x94\x80jutt\xe2\x9e\xa4 ')
    if ms == '1':
        ex_id()
    elif ms == '2':
        ex_id2()
    elif ms == '0':
        os.system('python2 jmbf.so')
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()


def ex_id():
    global token
    idg = []
    try:
        token = open('__yayan__.txt', 'r').read()
    except IOError:
        print '\t\x1b[1;91mToken not found'
        print ''
        raw_input(' PRESS ENTER TO BACK AND USE OPTION 0')
        print ''
        time.sleep(1)
        menu()

    os.system('clear')
    logo()
    print '\x1b[40m'
    print 47 * '\x1b[1;91m-'
    print ''
    print '\t\x1b[1;92m CREATE PUBLIC New IDS File'
    print ''
    idh = raw_input('\x1b[1;93m INPUT ID: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' COLLECTIN FROM: ' + q['name']
    except KeyError:
        print '\t\x1b[1;91mToken not found'
        print ''
        raw_input(' PRESS ENTER TO BACK AND USE OPTION 0')
        print ''
        time.sleep(1)
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na
        idg.append(uid + '<=>' + nm)
        ids.write(uid + '<=>' + nm + '\n')

    ids.close()
    print ''
    jutt()
    print ''
    print '\x1b[1;92m THE PROCESS HAS COMPLETED'
    print ''
    jutt()
    print ''
    raw_input('\x1b[1;95m Press enter to download file')
    os.system('cat ids_friends.txt | grep "100069" >> /sdcard/NEWIDS.txt')
    os.system('cat ids_friends.txt | grep "100070" >> /sdcard/NEWIDS.txt')
    os.system('cat ids_friends.txt | grep "100071" >> /sdcard/NEWIDS.txt')
    os.system('cat ids_friends.txt | grep "100072" >> /sdcard/NEWIDS.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;93m File downloaded successfully'
    print '\x1b[1;92m Saved /sdcard/NEWIDS.txt'
    print ''
    time.sleep(1)
    menu()


def ex_id2():
    global token
    idg = []
    try:
        token = open('__yayan__.txt', 'r').read()
    except IOError:
        print '\t\x1b[1;91mToken not found'
        print ''
        raw_input(' PRESS ENTER TO BACK AND USE OPTION 0')
        print ''
        time.sleep(1)
        menu()

    os.system('clear')
    logo()
    print ''
    print '\t\x1b[1;92mCOLLECT PUBLIC ID FRIENDLIST'
    print ''
    idh = raw_input('\x1b[1;93m INPUT ID: ')
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers=header)
        q = json.loads(r.text)
        print ' COLLECTIN FROM: ' + q['name']
    except KeyError:
        print '\t\x1b[1;91mToken not found'
        print ''
        raw_input(' PRESS ENTER TO BACK AND USE OPTION 0')
        print ''
        time.sleep(1)
        menu()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers=header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        idg.append(uid + '<=>' + na)
        ids.write(uid + '<=>' + na + '\n')

    ids.close()
    print ''
    jutt()
    print ''
    print '\x1b[1;92m THE PROCESS HAS COMPLETED'
    print ''
    jutt()
    print ''
    raw_input('\x1b[1;95m Press enter to download file')
    os.system('cat ids_friends.txt | grep "10" >> /sdcard/OLDIDS.txt')
    os.system('rm -rf ids_friends.txt')
    print '\x1b[1;93m File downloaded successfully'
    print '\x1b[1;92m Saved /sdcard/OLDIDS.txt'
    print ''
    time.sleep(1)
    menu()


if __name__ == '__main__':
    reg()
menu()