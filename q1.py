# q

while True:
            import time
            import os
            from colorama import Fore
            print(Fore.RED + """
                                           ╔═════╗     ╔═════╗          
                                           ║ ███ ║     ║ ███ ║                      
                                           ║ ███ ║     ║ ███ ║       
                                           ║ ███ ╚═════╝ ███ ║
                                           ║ ███████████████ ║   H a c k e r     
                                           ║ ███████████████ ║   N w w b  :)
                                           ║ ███ ╔═════╗ ███ ║      
                                           ║ ███ ║     ║ ███ ║      
                                           ║ ███ ║     ║ ███ ║      
                                           ╚═════╝     ╚═════╝ 
                              ╔════════════════════════════════════════╗                         
                              ║                                        ║   
                              ║           Name : H A C K E R           ║ 
                              ║                                        ║  
                              ║           Family : N W W B             ║  
                              ║                                        ║
                              ║           Muzic : A M R O F - C O L    ║
                              ║                                        ║
                              ║           Live : M U Z I C             ║
                              ║****                                ****║
                              ║***                                  ***║ 
                              ║**                                    **║
                              ║*                                      *║
                              ╚════════════════════════════════════════╝
                              """)






            time.sleep(1)
            print("Pleass Enter Your 1 ~ 10")
            print(Fore.RED + "             [1] "+ Fore.GREEN + " - Ip WebSite" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [2] "+ Fore.GREEN + " - Your Ip" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [3] "+ Fore.GREEN + " - Cloud Flare For WebSite" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [4] "+ Fore.GREEN + " - Domain 1" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [5] "+ Fore.GREEN + " - Domain 2" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [6] "+ Fore.GREEN + " - Admin WebSite" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [7] "+ Fore.GREEN + " - Port - Nmap" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [8] "+ Fore.GREEN + " - WebSite In My Target" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [9] "+ Fore.GREEN + " - Pyda Kardan Bakhsh Hay Site" + Fore.BLUE + " ;) ")
            time.sleep(0.3)
            print(Fore.RED + "             [10] "+ Fore.GREEN + " - whois" + Fore.BLUE + " ;) ")
            time.sleep(0.3)

            n= int(input(Fore.GREEN + "Enter Your Number 1 ~ 10 " + Fore.BLUE + "==>  " ))
            time.sleep(0.3)


            #__________________________________________________________________________________________________________
            #==========================================================================================================

            # Ip Site Mamole

            if n == 1:

              import socket
              import time
              def __1__():
                  try:
                      site = input(Fore.RED + "Pleass Enter You Target Address " + Fore.YELLOW + "==>  ")
                      soc = socket.gethostbyname(site)
                      time.sleep(0.6)
                      print(Fore.GREEN + "Your Web Site " + Fore.YELLOW + "==>  "  + Fore.RED + str(soc))
                      time.sleep(1)
                      print(Fore.YELLOW + "End " + Fore.GREEN + ";)\n")
                  except:
                      pass
              __1__()




            #_____________________________________________________________________________________________
            # ============================================================================================

            # Ip Carbar

            if n == 2:        

              import os
              import socket
              import sys
              import time
              from colorama import Fore

              def __2__():
                try:
                  q = socket.gethostname()
                  qq = socket.gethostbyname(q)
                  print(Fore.GREEN + "Your Ip " +Fore.YELLOW + "==> " + Fore.RED + qq)
                  print(Fore.YELLOW + "End " + Fore.GREEN + ";)\n")
                except:
                  pass
              __2__()

            # _____________________________________________________________________________________________________
            #======================================================================================================

            #Cloud Flare
            if n == 3:


                import os
                import sys
                import time
                import socket
                from colorama import Fore

                def __3__():
                    try:
                        site = input(Fore.RED + "Enter Your Address Web Site " + Fore.YELLOW + "==>  ")
                        my_list = ["www",'ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
                        for item in my_list:
                            host = item + "." + site
                            bypass = socket.gethostbyname(str(host))
                            print(Fore.GREEN + "Your Ip "+ Fore.YELLOW + "==> " + Fore.RED + str(bypass) + Fore.YELLOW + " | " + Fore.RED + str(host))
                            time.sleep(2)
                    except:
                        pass
                __3__()



            #_______________________________________________________________________________________________________________________________
            # ==============================================================================================================================

            # Domain_ 1_
            if n == 4 :
              import time
              import requests, builtwith
              from colorama import Fore

              def __4__():
                  try:
                      target = input(Fore.RED + "Enter Your Address WebSite " + Fore.YELLOW + "==>  ")
                      if not 'https://' in target or not 'http://' in target:
                          target = 'http://'+target
                      req = builtwith.parse(target)
                      for item in req:
                          value = ""
                          for var in req[str(item)]:
                              item = item.replace("-" , " ")
                              item = item.title()
                              value += str(var)
                              print(Fore.GREEN +"\n" + item +" : " + value)
                  except:
                      pass
              __4__()



              #________________________________________________________________________________________________________
              #========================================================================================================


            if n == 5:
                  import sys
                  import requests
                  import sys
                  import time
                  from colorama import Fore

                  def __5__():
                      try:
                          target = input(Fore.RED  + "Enter Your Address WebSite" + Fore.YELLOW  + " ==>  ")
                          info = requests.get("http://api.hackertarget.com/dnslookup/?q=" + target).text
                          print(Fore.GREEN + info)
                      except:
                          pass
                  __5__() 

            # __________________________________________________________________________________________________________________
            # ==================================================================================================================

            # Admin WebSite


            if n == 6:
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
                      import requests
                      import sys
                      import time
                      from colorama import Fore
                      def __6__():

                              url = input( Fore.RED + "Enter Your Address webSite" + Fore.YELLOW  + " ==>  ")

                              if 'http' in url:
                                    pass
                              elif 'http' != url:
                                   url = 'http://'+url

                              for i in my_list:
                                  rq = url+ "/" + i
                                  r = requests.get(rq)
                                  if r.status_code   == 200 or r.status_code   == 405:
                                      print(Fore.GREEN + rq  + Fore.GREEN + " Found")
                                  else:
                                      print(Fore.RED + rq  + Fore.RED + " Not Found")
                      __6__()

            #__________________________________________________________________________________________________________________________________
            #==================================================================================================================================

            # Nmap For Port WebSite ;)

            if n == 7 :
                    import requests
                    import time
                    from colorama import Fore
                    def __7__():
                      try:
                          target = input(Fore.RED + "Enter Your address WebSite" + Fore.YELLOW + " ==>  ")
                          if target == "":
                            try:
                              print(Fore.YELLOW + "Ok Good Lounck" + Fore.RED + " ;)")
                              sys.exit()
                            except:
                              pass
                          req = requests.get("https://api.hackertarget.com/nmap/?q=" + target).text
                          print(Fore.BLUE + req)
                      except:
                        pass
                    __7__()




            #__________________________________________________________________________________________________________________
            #==================================================================================================================

            # WebSite In My Target

            if n == 8:
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
                                  print(Fore.WHITE + "")

                          __8__()        






            #_____________________________________________________________________________________________________________________________________________________
            #=====================================================================================================================================================

            # pyda kardn baksh hay sayt

            if n == 9:
                    import time
                    import requests
                    import sys
                    from colorama import Fore

                    def __9__():
                        try:
                            site = input(Fore.RED + "Enter Your Address WebSite" + Fore.YELLOW + " ==>  ")
                            if site == "":
                                try:
                                    print(Fore.BLUE + "Ok Good Lunch" + Fore.RED + " ;)")
                                    sys.exit()
                                except:
                                    pass
                            my_list = ['admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
                    'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
                    'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
                    'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
                    'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
                    'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
                    'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
                    'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
                    'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
                    'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
                    'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
                    'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
                    'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
                    'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
                    'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
                    'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
                    'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
                    'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
                    'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
                    'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
                    'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
                    'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
                    'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
                    'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
                    'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
                    'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
                    'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
                    'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
                    'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
                    'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
                    'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
                    'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
                    'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
                    'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
                    'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
                    'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
                    'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
                    'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
                    'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
                    'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
                    'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
                    'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
                    'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
                    'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
                    'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
                    'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
                    'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
                    'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
                    'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
                    'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
                    'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
                    'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
                    'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
                    'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
                    'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
                    'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
                    'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
                    'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
                    'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
                    'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
                    'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
                    'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
                    'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
                    'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
                    'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
                    'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
                    'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
                    'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html']


                            if "http" in site:
                                pass
                            elif "https" in site:
                                pass
                            else:
                                site = "http://" + site
                            for i in my_list:
                                r = site + "/" + i
                                req = requests.get(r)
                                if req.status_code == 200 or req.status_code == 405:
                                    print(Fore.GREEN + r +Fore.BLUE + " | " +Fore.YELLOW + "Found")
                                else:
                                    print(Fore.RED + r + Fore.BLUE + " | " + Fore.YELLOW + "Not Found")
                        except:
                            pass
                    __9__()

            # _____________________________________________________________________________________________________________________________________________________
            # =====================================================================================================================================================

            if n == 10:
                  import sys
                  import requests
                  import sys
                  import time
                  from colorama import Fore

                  def __10__():
                      try:
                          target = input(Fore.RED  + "Enter Your Address WebSite" + Fore.YELLOW  + " ==>  ")
                          info = requests.get("http://api.hackertarget.com/whois/?q=" + target).text
                          print(Fore.GREEN + info)
                      except:
                          pass
                  __10__() 
            #_______
            from colorama import Fore
            import os
            import sys
            
            s = input(Fore.RED + "\nAre You Tran Again" + Fore.GREEN + " (y / n)" + Fore.BLUE + " ?" + Fore.BLUE + " ==>  ")
            if s.lower() == "y":
                continue
            if s.lower() == "n":
                print(Fore.YELLOW + "\nOk Good Lunch" + Fore.RED + " ;)")
                time.sleep(3)       
                break


            
            



