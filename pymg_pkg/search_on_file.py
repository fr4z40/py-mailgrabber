# -*- coding: utf-8 -*-
#
# Copyright 2016 Eduardo Frazão ( https://github.com/fr4z40 )
#
#   Licensed under the MIT License;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#

class search_on_file(object):

    import os
    from pymg_pkg.mailextract import mailextract

    def log(self, pth_name, cntd):
        out_f = open(pth_name, 'a')
        out_f.write('%s\n' % cntd.strip())
        out_f.close()


    def search(self, file_path, output_file, filter_plus=None):
        mailextract = self.mailextract
        file_in = open(file_path, 'rb')
        for line in file_in:
            try:
                line = (line.decode('utf8')).strip()
            except:
                line = (line.decode('iso-8859-1')).strip()
            line = line.strip()
            if (len(line) >= 11):
                for r in mailextract(line, filter_plus):
                    if (r != None):
                        self.log(output_file, r)
        file_in.close()


    def __init__(self, target_path, output_file, filter_plus=None):

        path = self.os.path
        walk = self.os.walk

        if (path.isfile(target_path) == True):
            self.search(target_path, output_file, filter_plus)

        elif (path.isdir(target_path) == True):
            try:
                for dr in walk(target_path):
                    for fl in dr[2]:
                        pth = ('%s/%s' % (dr[0], fl)).replace('//','/')
                        self.search(pth, output_file, filter_plus)
            except:
                pass

