import sys
import requests
import json
from colorama import Fore

def __8__():
    try:
        site = input(Fore.RED + "Enter Your Address WebSite" + Fore.YELLOW + " ==>  ")
        r = {"remoteAddress" : site}
        b = requests.post("https://domains.yougetsignal.com/domains.php" , r)
        q = json.loads(b.content)
        print(q)
        for i in q["domainArray"]:
            print(" " +Fore.GREEN+ i[0] + "\n")
    except:
        pass
__8__()
