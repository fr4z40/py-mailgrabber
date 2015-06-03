#!/usr/bin/env python3
# Author: Eduardo Frazão ( http://github.com/fr4z40 )
# Created in: 24 Nov 2014

from google import search
from argparse import ArgumentParser, RawTextHelpFormatter
from urllib.request import urlopen
from string import punctuation


desc='''#
#
#  email_grabber.py "search keys" "/path/output_file.ext" --[optional args]
#
#
#  About keys:
#    '"multiple words, but one key" second_key third_key'
#
#
#  About Optional Args:
#
#    --inserver = Specify the "@server.com"
#    \tExample: --inserver="@hotmail.com"
#    \t\t return only emais with "@hotmail.com"
#
#    --inmail = find for specific "key" on email
#    \tExample: --inmail="teste"
#    \t\t return only emais with teste on "x"
#    \t\t => "xxxxxxxx@serve.com"
#
#'''


def writer(file_name, content):
    with open(file_name, 'a', encoding='utf8') as log:
        log.write(('%s\n' % content.strip()))
        log.close()


def out_p(file_name, blk):
    print("# *\t%s" % blk)
    writer(file_name, blk)


def repl(x):
    rmv = ((' '.join((((punctuation.replace('-', '')).replace('_', '')).replace('.', '')).replace('@', ''))).split())
    for p in rmv:
        x = x.replace(p, ' ')
    return(x.strip())


def filterr(x):
    flt = (('''
             xxxx xxx@ 12345 fulano seuemail @mail @email
             usuario meuemail @xx seublog meudominio
             meunome blabla .. @@ seunome user.name noone
             mailto username mail@ someone somebody nobody
             user@ yourusername fake ：
            ''').split())
    for n in flt:
        if n in x:
            cndc = False
            break
        else:
            cndc = True
    return(cndc)


def length(x):
    eml = (x[:(x.find('@'))])
    if (((len(eml) <= 30) and (len(eml) >= 6)) and (len(x) <= 36)):
        rst = True
    else:
        rst = False
    return(rst)


def check_r(x):
    bef = (x[:(x.find('@'))])
    aft = (x[(x.find('@')):])
    while 1:
        if (args.inmail != None):
            if args.inmail in bef:
                rst = True
            else:
                rst = False
                break
        else:
            rst = True
        if (args.inserver != None):
            if args.inserver in aft:
                rst = True
            else:
                rst = False
                break
        else:
            rst = True
        break
    return(rst)


def start(file_name, url):
    try:
        mails = []
        rept = []
        repl_data = str(((urlopen(url)).read().decode('utf8')).lower())
        cntd = repl(repl_data)
        cntd = cntd.split()
        for blk in cntd:
            blk = ((((blk.replace('\r', '')).replace('\t', '')).replace('\n', '')).strip())
            if (('@' in blk) and (blk not in mails)):
                if (filterr(blk) == True) and (length(blk) == True):
                    mails.append(blk)
                    if check_r(blk) == True:
                        if url not in rept:
                            print('# %s' % url)
                            rept.append(url)
                        out_p(file_name, blk)
                    else:
                        pass
            else:
                pass
    except:
        pass


parser = ArgumentParser(description=desc, formatter_class=RawTextHelpFormatter)
parser.add_argument('keys', help='Search Keys', type=str)
parser.add_argument('output', help='Output file', type=str)
parser.add_argument('--inmail', type=str)
parser.add_argument('--inserver', type=str)
args = parser.parse_args()

keys = args.keys
file_name = args.output

options = '# Search: %s\n# Output: %s\n#' % (keys, file_name[-15:])
if args.inmail != None:
    options = (options + ('\n# Specific search: %s' % args.inmail))
if args.inserver != None:
    options = (options + ('\n# Server search: %s' % args.inserver))
options = (options + '\n#')

print('#\n#   Py-mailgrabber\n#\n# Author: Eduardo Frazão (http://github.com/fr4z40)\n# Created in 24 Nov 2014\n#')
print(options)

for src in search(keys, stop=None, pause=3.7):
    urls = []
    if src not in urls:
        start(file_name, src)
        urls.append(src)
