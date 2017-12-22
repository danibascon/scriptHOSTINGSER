#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands

uid= raw_input("Dime un uid (usuario del sistema): ")
commands.getoutput("a2dessite "+uid+".conf")
commands.getoutput("ssh root@172.22.200.109 rm -r /etc/apache2/sites-available/"+uid+".conf")
commands.getoutput("service apache2 restart")

