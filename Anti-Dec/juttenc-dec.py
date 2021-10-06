# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: jutt
import random, base64, marshal, hashlib, argparse
BLACK_MAGIC = '\x03\xf3\r\nd\x83\x8e^'

class obf:
    num = []

    def softex_charm(self, SatuBungkusMemek=None, kontolKadal=0, kontolMonyet=1, misq=''):
        psf = ['', '', '']
        psf[0] += str(kontolKadal)
        psf[2] = str(kontolMonyet)
        psf[1] = '&' + SatuBungkusMemek + '&'
        return misq.join(psf)

    def inum_depth(self, bigF, nim, pct=[], o=0):
        if 'list' not in type(bigF).__name__ and 'list' not in type(nim).__name__:
            raise TypeError('--- type not list --')
        index = random.randint(2, len(bigF) / 2 + 2)
        if index < 5 <= len(bigF):
            index += 2
        foad = {'index1': bigF[:index], 'index2': bigF[index:]}
        while o < len(foad['index1']):
            pct.append(foad['index1'][o])
            o += 1

        o -= o
        while o < len(nim):
            pct.append(nim[o])
            o += 1

        o -= o
        while o < len(foad['index2']):
            pct.append(foad['index2'][o])
            o += 1

        max_legth = len(pct[:len(foad['index1']) + len(nim)]) - 1
        return {'a': len(foad['index1']), 'z': max_legth + 1, 'depth': pct}

    def slice(self, strings=None, pt=[]):
        diff = len(strings) / 2
        fp = {'stiff': strings[:diff], 'numc': strings[diff:]}
        for of in fp['numc']:
            pt.append(ord(of))

        fop = self.selector_num(fp['stiff'])
        co = self.inum_depth(fop, pt)
        fo = self.swift(fp['stiff'], co['a'], co['z'])
        return 'import base64,marshal\nDIFENT_STACK = []\n(lambda ___ : sot.sort())(globals().update({(lambda : uc[i][p] ^ c[0][o] ** 5 != "").__code__.co_consts[3].join([chr(i) for i in (lambda _______, _, ___ : [(((((___>=_______)+(___>=___)+(_>=_))+((___>_)+(_______<=_)+(_<=___))+((___>=_)-(_______>___)))<<(((___>_)+(_<=___))+((_>=_______)+(___>=___))))+(((___>=_______)+(_______!=_)+(___<=___)))),(((((___>=___)+(___>=___)+(_______!=_))+((_______!=___)+(_______==_______)+(___!=_______))+((_>=_______)*(___>=_______)))<<(((_______!=_)+(___!=_))+((___!=_)+(_______<=_______))))-(((___>=___)*(_!=___)))),(((((___>_______)+(_>=_______)+(___>=___))+((_<___)+(_______<_)+(___!=_))+((_______>=_______)*(___!=_)))<<(((_______<___)+(_______<___))+((_______!=___)+(___!=_______))))+((((_==_)-(_______==_)))<<(((___!=_)+(_<___)))))])((((0x83273a==0x83273a)+(0b1001!=0o1663133)+(0x83273a!=0b1001))),((((((((((((0b1001>=0x83273a)+(0o1663133<0x83273a)))<<(((0x83273a<=0x83273a)+(0b1001>=0b1001)+(0o1663133!=0x83273a))))+(((0o1663133!=0x83273a)+(0b1001>0b1001)))))))))<<(((0b1001>0b1001)+(0b1001<=0b1001))))),(((((0x83273a==0x83273a)+(0b1001==0b1001)+(0b1001<=0x83273a))+((0x83273a>=0x83273a)+(0b1001<0x83273a)+(0o1663133!=0b1001))+((0b1001<=0o1663133)-(0x83273a<0b1001)))<<(((0b1001<=0o1663133)+(0x83273a<=0x83273a))))-(((0b1001!=0o1663133)*(0o1663133<=0x83273a)))))]):(lambda : [{int(c.split("$")[0])+int(c.split("$")[2]):c.split("$")[1]} for c in (lambda ___ : ___.split("@"))(\'' + str(fo) + '\')])()}))\n(lambda : globals().update({(lambda : uc[i][p] ^ c[0][o] ** 5 != "").__code__.co_consts[3].join([chr(i) for i in (lambda ______, __, ____ : [((((((((____==____)+(______!=__)+(____>=__))+((____!=__)+(____>__)+(__<____))+((______>=__)*(______<=____)))<<(((__<=______)+(__==__))))-(((____>=__)*(__<____)))))<<(((__<____)+(____>______))))-(((______<=______)-(__>____)))),((((((((____>=__)+(______!=____)+(__>=__)))<<(((______!=__)+(______!=____)+(____>=______))))+(((__!=______)-(______>____)))))<<(((______<=______)+(____>__))))+(((______>=____)+(____!=__)))),((((((((____<=____)+(__!=__)))<<(((____>=______)+(______!=__))+((____>=____)+(__!=____))))-(((______!=____)+(__==____)))))<<(((__>=__)+(____<=____)+(____!=______))))+(((__==__)+(____<=__))))])((((((0o1663133!=0b1001)*(0b1001>=0b1001)))<<(((0x83273a>=0b1001)+(0x83273a!=0o1663133))+((0x83273a!=0b1001)+(0b1001!=0x83273a))))),(((((0x83273a>0o1663133)+(0o1663133<=0x83273a)+(0x83273a>0b1001))+((0x83273a==0x83273a)+(0x83273a>0b1001)+(0b1001!=0x83273a))+((0o1663133==0o1663133)+(0b1001>=0o1663133)))<<(((0b1001<0o1663133)*(0x83273a==0x83273a))))),(((((0b1001<=0o1663133)+(0o1663133<=0x83273a))+((0o1663133>0b1001)+(0x83273a<=0x83273a))+((0b1001<=0o1663133)+(0x83273a==0o1663133)))<<(((0x83273a<=0x83273a)+(0b1001!=0o1663133))))))]):(lambda cz : cz[::-1].split("&"))((lambda x : (lambda : uc[i][p] ^ c[0][o] ** 5 != "").__code__.co_consts[3].join([c[1][c[0]] for c in enumerate(x)]))(sot))}))()\nMAX_LENGTH = int(key[0])\n___ = ' + str(co['depth']) + '\nwhile MAX_LENGTH<int(key[2]):\n    DIFENT_STACK.append(___[MAX_LENGTH])\n    MAX_LENGTH += 1\nexec(marshal.loads((lambda ____ : base64.b64decode(____[1]))(key)+(lambda : uc[i][p] ^ c[0][o] ** 5 != "").__code__.co_consts[3].join([chr(i) for i in DIFENT_STACK])))\ndel DIFENT_STACK,MAX_LENGTH,___,key,sot'

    def selector_num(self, code, tig=1):
        coprez = len(code) * 8
        if coprez > 100:
            coprez += len(code) * 10
        elif coprez > 200:
            coprez += len(code) * 9
        else:
            if coprez > 300:
                coprez += len(code) * 8
            elif coprez > 400:
                coprez += len(code) * 7
            elif coprez > 500:
                coprez += len(code) * 6
            for cin in range(coprez / 2):
                civ = random.randint(tig, 215)
                if civ > tig * 256 - cin:
                    civ += 5
                    if civ >= len(code) * 1 ^ tig:
                        civ += coprez % 195951 ^ 5 / 52
                else:
                    civ += coprez << 2 / len(code) ^ 2
                left = civ != coprez
                if left is True:
                    civ * 5
                self.num.append(civ / 2 / 2)

        return self.num

    
    if zof.out:
        obf().obfuscate(zof.file, out=[zof.out, True])
        print '\nSuccesfuly save %s ' % zof.out
    else:
        obf().obfuscate(zof.file)
        print '\nSuccesfuly save %s ' % zof.file.replace('.py', '_enc.py')
else:
    jutt.print_usage()
