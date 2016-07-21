#!/usr/bin/python3
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

from pymg_pkg import *
from subprocess import call
from os import path


how_to = '''
#
#   Mode Options
# 
# - help
#  --- Show This Help.
# 
# - exit
#  --- exit the software.
# 
# - files
#  --- Search in Files/Folders.
#  --- You can set a file or a folder to Search.
# 
# - url
#  --- Search in a single page.
# 
# - google
#  --- Search using Google.
# 
# - add_filter
#  --- set an external file as an adtional filter.
#  --- you can use a file with emails, to not repeat those emails.
#      ( "Items" in that file are separated by lines, espaces and tabulations )
#
'''



def log(pth_name, cntd):
    out_file = open(pth_name, 'a')
    out_file.write('%s\n' % cntd.strip())
    out_file.close()



def help_module():
    print(how_to)




def add_filter():
    f_p = None
    while (f_p==None):
        filter_file = input("* Set Here your adtional filter\n:")
        filter_file = ((str(filter_file)).strip()).strip("'")
        if path.isfile(filter_file):
            filter_in = open(filter_file, 'r')
            cnt = (filter_in.read()).strip().split()
            filter_in.close()
            global f_p
            f_p = cnt
            break
        else:
            print("It's not a file, please, try again\n")




def file_module():
    tgt = None
    while (tgt==None):
        try:
            tgt = input("* Set Target path\n- You can type the full path\n- or drag the folder/file to here.\n:")
            tgt = ((str(tgt)).strip()).strip("'")
            if (path.isdir(tgt) or path.isfile(tgt)):
                break
            else:
                tgt = None
                print("Path Error, please, try again\n")
        except Exception as err:
            if err == KeyboardInterrupt:
                quit()
            else:
                pass

    search_on_file(tgt, out_f, filter_plus=f_p)



def url_module():
    tgt_url = None
    while (tgt_url==None):
        try:
            tgt_url = input("* Set Target URL\n:")
            tgt_url = ((str(tgt_url)).strip()).strip("'")
            if 'http' not in tgt_url:
                tgt_url = ('http://'+tgt_url)
            if (len(tgt_url) >= 5):
                break
            else:
                tgt_url = None
                print("Error, please, try again\n")
        except Exception as err:
            if err == KeyboardInterrupt:
                quit()
            else:
                pass
    rst = search_on_page(tgt_url, filter_plus=f_p)
    rst.sort()
    rst = ('\n'.join(rst))
    log(out_f, rst)



def google_module():
        try:

            # search key
            s_keys = None
            while (s_keys==None):
                s_keys = input("* Set Keys to search\n:")
                s_keys = ((str(s_keys)).strip())
                if (len(s_keys) >= 5):
                    break
                else:
                    s_keys = None
                    print("too short")
            print("\n- Key: %s\n\n" % s_keys)

            # "stop" argument
            condition = False
            while (condition==False):
                print("* When Stop?\n* Set a page limit\n* Default is 10, just type enter.")
                print('* Or Type None to "unlimit", only will stop with CTRL+C')
                stop_arg = ((input(":")).strip()).lower()
                if len(stop_arg) == 0:
                    condition = True
                    stop_arg = 10
                    break
                elif str.isdigit(stop_arg):
                    stop_arg = int(stop_arg)
                    condition = True
                    break
                elif (str.isalpha(stop_arg) and (stop_arg.lower() == "None")):
                    stop_arg = None
                    condition = True
                    break
                else:
                    print("Try again...\n")
            print("\n- Stop: %s\n\n" % stop_arg)

            # "pause" argument
            condition = False
            while (condition==False):
                print('* Set a "Delay"\n* Default is 5, just type enter.')
                pause_arg = ((input(":")).strip()).lower()
                try:
                    pause_arg = float(pause_arg)
                    condition = True
                    break
                except:
                    if len(pause_arg) == 0:
                        condition = True
                        pause_arg = 5
                        break
                    else:
                        print("Try again...\n")
            print("\n- Pause: %s\n\n" % pause_arg)

            from pymg_pkg.g_search import search as g_search
            for lnk in g_search(s_keys, stop=stop_arg, pause=pause_arg):
                print("Working on: %s" % lnk)
                rst = search_on_page(lnk, filter_plus=f_p)
                rst.sort()
                rst = ('\n'.join(rst)).strip()
                log(out_f, rst)

        except Exception as err:
            if err == KeyboardInterrupt:
                quit()
            else:
                pass



def main():
    call('reset')

    options = {
        'help':help_module,
        'files':file_module,
        'url':url_module,
        'google':google_module,
        'add_filter':add_filter
                }

    print(' Copyright 2016 Eduardo Frazão ( https://github.com/fr4z40 )')
    print(' enter "help" any time if necessary.\n')
    print("Mode Selection")

    while 1:
        ent = ((str(input("~>"))).strip()).lower()
        if ('exit' not in ent):
            try:
                options[ent]()
            except Exception as err:
                print(err)
                if (len(ent) >= 1):
                    print("Error!")
                pass
        else:
            quit()




if __name__ == '__main__':

    global f_p
    f_p=None

    call('reset')
    out_f = None
    while (out_f==None):
        try:
            out_f = input("* Set output file path\n:")
            out_f = ((str(out_f)).strip()).strip("'")
            # write_test
            if ((path.exists(out_f) == False) and (len(out_f)>=5)):
                (open(out_f, 'w')).close()
            else:
                out_f = None
                raise(Exception)
        except Exception as err:
            if err == KeyboardInterrupt:
                quit()
            else:
                pass

    main()

