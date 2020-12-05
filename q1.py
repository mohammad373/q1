# q1

import requests
import time
import sys
from colorama import Fore

def __1__():
        i = input("Enter Your Address WebSite ==>  ")
        my_list = ['robots.txt',
      'search/',
      'admin/',
      'login/',
      'sitemap.xml',
      'sitemap2.xml',
      'config.php',
      'wp-login.php',
      'log.txt',
      'update.php',
      'INSTALL.pgsql.txt',
      'user/login/',
      'INSTALL.txt',
      'profiles/',
      'scripts/',
      'LICENSE.txt',
      'CHANGELOG.txt',
      'themes/',
      'inculdes/',
      'misc/',
      'user/logout/',
      'user/register/',
      'cron.php',
      'filter/tips/',
      'comment/reply/',
      'xmlrpc.php',
      'modules/',
      'install.php',
      'MAINTAINERS.txt',
      'user/password/',
      'node/add/',
      'INSTALL.sqlite.txt',
      'UPGRADE.txt',
      'INSTALL.mysql.txt']
        if "http" in i:
          pass
        elif "http" != i:
          i = "http://" + i
        for item in my_list:
          r = i + "/" + item  
          req = requests.get(r)
          if req.status_code == 200 or req.status_code == 405:
            print(Fore.GREEN + "This Is Ok " + Fore.GREEN + r)
          else:
            print(Fore.RED + "This Is Not Ok " + Fore.RED  + r)
__1__()
