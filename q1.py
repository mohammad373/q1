# q1

import requests
import time
import sys
from colorama import Fore

def __1__():
        i = input("Enter Your Address WebSite ==>  ")
        my_list = ["admin" , "robots.txt" , "search"]
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
