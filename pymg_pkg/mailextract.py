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

class mailextract(list):

    @staticmethod
    def server_dict(list_in):
        rst = {}
        for email in list_in:
            server = email.split('@')[-1]
            if server not in rst:
                rst[server] = []
            rst[server].append(email)
        return(rst)


    @staticmethod
    def isvalid(email, filter_plus=None):
        try:

            email = (email.strip()).lower()

            list_filter = list(set(('''
            xxxx xxx@ 12345 fulano seuemail @mail @email usuario meuemail
            @xx seublog meudominio meunome blabla .. @@ seunome user.name
            noone mailto username mail@ someone somebody nobody user@
            yourusername fake ： teste testing
            ''').strip().split()))
            if (filter_plus != None):
                list_filter = list(set(list_filter + filter_plus))

            if ((('@' in email) and ('.' in email)) and (email.count('@') == 1)):
                len_test = email.split('@')
                if (((len(len_test[0]) <= 36) and (len(len_test[0]) >= 3)) and
                    ((len(len_test[1]) >= 7) and (len(len_test[1]) <= 25))):

                    condition = True
                    for flt in list_filter:
                        if flt in email:
                            condition = False
                            break
                    return(condition)
                else:
                    return(False)
            else:
                return(False)

        except:
            return(False)


    def __init__(self, string_in, filter_plus=None):
        from string import punctuation
        for item in list('._-@'):
            punctuation = punctuation.replace(item,'')
        for item in punctuation:
            string_in = string_in.replace(item, ' ')
        string_in = list(set(string_in.strip().split()))
        for items in string_in:
            for l in list('._-@'):
                items = items.strip(l)
            if self.isvalid(items, filter_plus):
                self.append(items)

