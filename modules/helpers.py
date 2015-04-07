#!/usr/bin/env python3
# Author: Eduardo Frazão (https://github.com/fr4z40)
# Contributor: Jonatas Freitas (https://github.com/jonatasfreitasv)
# First commit date: 2014-11-24
'''Helpers module
'''
from string import punctuation

class Helpers:

    def writer(x, y):
        with open(x, 'a', encoding='utf8') as log:
            log.write(('%s\n' % y.strip()))
            log.close()

    def repl(x):

        to_join = punctuation.replace(
            '-', '').replace(
            '_', '').replace(
            '.', '').replace(
            '@', '').split()

        for p in " ".join(to_join):
            x = x.replace(p, ' ')
        return(x.strip())

    def filter(x):
        flt = (('''
                 xxxx xxx@ 12345 fulano seuemail @mail @email
                 usuario meuemail @xx seublog meudominio
                 meunome blabla .. @@ seunome user.name
                 mailto username mail@
                 user@ yourusername fake info@ ：
                ''').split())

        for n in flt:
            if n in x:
                cndc = False
                break
            else:
                cndc = True
        return(cndc)
