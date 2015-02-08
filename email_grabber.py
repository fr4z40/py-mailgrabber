#!/usr/bin/env python3
# Author: Eduardo Frazão
# Contributor: Jonatas Freitas
# First commit date: 2014-11-24
'''Main file
'''

from google import search
from sys import argv

from modules.engine import Engine


if len(argv) == 3:

    file_name = argv[1]
    keys = argv[2]

    print('\n %s \n %s \n %s \n %s \n %s\n\n' % (
        '############################################################',
        '##### Email Grabber Start ! #####',
        'Output file: ' + file_name,
        'Keys: ' + keys,
        '############################################################'
    ))

    for url in search(keys, stop=None):
        print("URL: %s" % url)
        Engine.start(file_name, url)

else:
    print('\n %s \n %s \n %s \n\n %s \n %s\n\n' % (
        '############################################################',
        '##### HOW TO USE #####',
        'python3 email_grabber.py output.txt "keys to search"',
        'To long searchs, google will block you.',
        '############################################################'
    ))

    quit()
