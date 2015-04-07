#!/usr/bin/env python3
# Author: Eduardo Frazão (https://github.com/fr4z40)
# Contributor: Jonatas Freitas (https://github.com/jonatasfreitasv)
# First commit date: 2014-11-24
'''Engine Module
'''
from urllib.request import urlopen
import re
from modules.helpers import Helpers

class Engine:

    def start(file_name, url):
        try:

            mails = []

            repl_data = str(((urlopen(url)).read().decode('utf8')).lower())

            cntd = Helpers.repl(repl_data)
            cntd = cntd.split()

            for blk in cntd:

                blk = ((blk.replace('\n', '')).strip())

                if re.match('[^@]+@[^@]+\.[^@]+', blk) and blk not in mails:

                    if Helpers.filter(blk) == True:
                        mails.append(blk)
                        print("*\t%s" % blk)
                        Helpers.writer(file_name, blk)

                else:
                    pass

        except:
            pass
