#!/usr/bin/env python3
# Eduardo Frazão
# 2014/11/24
# yeah, it's an ugly code, but it works

from google import search
from sys import argv
import urllib.request

def writer(x,y):
  log = open(x, "a")
  log.write(("%s\n" % y))
  log.close()

def chk(x):
  try:
    cntd = (str((urllib.request.urlopen(x)).read().decode('utf8')))
    cntd = ((((((cntd.replace("\\r"," ")).replace(":"," ")).replace("\\t","\t")).replace("\\n","\n")).replace("="," ")).replace(")"," "))
    cntd = ((((((cntd.replace("("," ")).replace("!"," ")).replace("\\"," ")).replace("..", "  ")).replace("&quot", " ")).replace("|"," "))
    cntd = (((((((cntd.replace(">", " ")).replace("<"," ")).replace(";"," ")).replace(","," ")).lower()).replace("'"," ")).replace('"'," "))
    cntd = cntd.split()
    for blk in cntd:
      if (("@" in blk) and (".com" in blk)) and (("http" not in blk) and ("/" not in blk)):
        blk = (blk.strip("."))
        if (blk not in mails and "@xx" not in blk) and ("meudominio" not in blk and "seuemail" and "seublog" not in blk):
          if (len(blk[:(blk.find("@"))]) < 3):
            pass
          else:
            mails.append(blk)
            print("*\t%s" % blk)
            writer(file_name, blk)
  except Exception as erro:
    pass

if len(argv) != 3:
  print('\n\td_f.py file_name_output.ext "keys to find"\n\tor...\n\td_f.py file_name_output.ext %s\n' % (''' '"keys to find"' '''))
  quit()
else:
  file_name = argv[1]
  keys = argv[2]

mails = []

print("\noutput file: %s\nSearching Key(s): %s\n" % (argv[1], argv[2]))
for url in search(keys, stop=None):
  print("URL: %s" % url)
  mails = []
  chk(url)
