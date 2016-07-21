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

class search_on_page(list):

    from pymg_pkg.mailextract import mailextract

    header={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive'}

    def source(self, url):
        import urllib.request
        req = urllib.request.Request(url, data=None, headers=self.header)
        rst = (urllib.request.urlopen(req)).read()
        try:
            rst = rst.decode('utf8')
        except:
            rst = rst.decode('iso-8859-1')
        return(rst.strip())



    def __init__(self, url, filter_plus=None):
        mailextract = self.mailextract
        source = self.source
        for mail in mailextract(source(url), filter_plus):
            if ((mail != None) and (mail not in self)):
                self.append(mail)

