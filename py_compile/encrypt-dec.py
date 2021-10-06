# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: JUTT_BADSHAH
import os, sys, py_compile, marshal, base64, zlib, time
from os import system
from time import sleep
try:
    import requests
except ImportError:
    print '\nModule Requests Not Installed'
    os.sys.exit()

def boyprint(s):
    for t in s + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.01)


logo = logo = '\n\x1b[1;92m              \n\x1b[1;92m                      \n\x1b[1;96m                        \n\x1b[1;92m     {} {}  {} {}{}{} {}{}{} \n\x1b[1;97m     {} {}  {}   {}     {} \n\x1b[1;93m     {} {}  {}   {}     {}  \n\x1b[1;96m     {} {}  {}   {}     {} \n\x1b[1;94m  {}{}   {}{}    {}     {}  \n\x1b[1;93m                      \n\x1b[1;92m         Jutt Badshah Brand~                       \n\x1b[1;91m-----------------------------------------------\n\x1b[1;97m\xe2\x9e\xa3 Author : Jutt Badshah    \n\x1b[1;97m\xe2\x9e\xa3 Github : https://github.com/SHOOTER-MAKER\n\x1b[1;97m\xe2\x9e\xa3 WP  NO : +923007574310\n\x1b[1;93m-----------------------------------------------\n\n\n_______ __   _ _______  ______ __   __  _____  _______\n |______ | \\  | |       |_____/   \\_/   |_____]    |   \n |______ |  \\_| |_____  |    \\_    |    |          |\n'

def juttbadshah():
    system('clear')
    boyprint(logo)
    file = raw_input('\x1b[1;97mnexample > /sdcard/folder/file.py\n\nName File > ')
    print '\x1b[1;92mJutt Badshah Converting Your Script\x1b[0;97m'
    time.sleep(5)
    print '\x1b[1;93mEnc Has Been Done File Name jutt-enc.py\x1b[0;97m'
    jutt = open(file).read()
    file = open('jutt-enc.py', 'w')
    file.write('juttbadshah=(\n')
    for i in range(3000):
        file.write('"Jutt Badshah","Jutt Badshah","Jutt Badshah","Jutt Badshah",\n')

    file.write(')\n')
    jutt1 = compile(jutt, 'JUTT_BADSHAH', 'exec')
    jutt2 = marshal.dumps(jutt1)
    jutt3 = zlib.compress(jutt2)
    jutt4 = base64.b64encode(jutt3)
    jutt5 = repr(jutt4)
    jutt6 = '# ECRYPT BY Jutt Badshah\n# Follow Github SHOOTER-MAKER\n\n\nimport marshal,zlib,base64\nexec marshal.loads(zlib.decompress(base64.b64decode("' + str(jutt5) + '")))'
    jutt7 = compile(jutt6, 'JUTT_BADSHAH', 'exec')
    jutt8 = marshal.dumps(jutt7)
    jutt9 = repr(jutt8)
    file.write('# ECRYPT BY Jutt Badshah\n# Follow Github SHOOTER-MAKER\n\n\nimport marshal\nexec marshal.loads(' + jutt9 + ')\n\n\n')
    file.write('juttbadshah=(\n')
    for i in range(3000):
        file.write('"Jutt Badshah","Jutt Badshah","Jutt Badshah","Jutt Badshah",\n')

    file.write(')\n')
    file.close()


if __name__ == '__main__':
    juttbadshah()