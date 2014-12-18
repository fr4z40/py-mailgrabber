#!/usr/bin/env python3
# Eduardo Frazão
# 2014/11/24
# yeah, it's an ugly code, but it works

from string import punctuation
from google import search
from sys import argv
import urllib.request

def writer(x,y):
    with open(x, 'a') as log:
        log.write(('%s\n' % y))
        log.close()

def repl(x):
    for p in (" ".join((((punctuation.replace('.', '')).replace('@',''))).split())):
        x = x.replace(p, ' ')
    return(x.strip())

def filtr(x):
    flt = (('''
             xxxx xxx@ 12345 fulano seuemail usuario meuemail @xx seublog meudominio meunome blabla .. @@ seunome user.name mailto username mail@
             user@ yourusername fake info@ ：
            ''').split())
    for n in flt:
        if n in x:
            cndc = False
            break
        else:
            cndc = True
    return(cndc)

def chk(x):
    try:
        cntd = repl((str((urllib.request.urlopen(x)).read().decode('utf8'))).lower())
        cntd = cntd.split()
        for blk in cntd:
            blk = ((blk.replace('\n','')).strip())
            if (("@" in blk) and ("." in blk)) and ((blk not in mails) and ((len(blk[:(blk.find("@"))]) > 2) and (len(blk) < 40))):
                if filtr(blk) == True:
                    mails.append(blk)
                    print("*\t%s" % blk)
                    writer(file_name, blk)
            else:
                pass
    except Exception as erro:
        pass


if len(argv) != 3:
    print('\n\td_f.py file_name_output.ext "keys to find"\n\tor...\n\td_f.py file_name_output.ext %s\n' % (''' '"keys to find"' '''))
    quit()
else:
    file_name = argv[1]
    keys = argv[2]


mails = []

# To long searchs, is better put a 'pause' to delay the search, or google will block you
# Search(keys, stop=None, pause=0.0) => Put a float value;
# A high value on the delay will cause the search to take more time, however, the chances
# of being blocked by google, become smaller.
# If you are blocked, solve the captcha or renew your IP address.

print("\noutput file: %s\nSearching Key(s): %s\n" % (argv[1], argv[2]))
for url in search(keys, stop=None):
    print("URL: %s" % url)
    chk(url)
