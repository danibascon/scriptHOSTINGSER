#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands

usuario=raw_input("Usuario que quieres borrar: ")

commands.getoutput("ldapdelete -x -h 172.22.200.109 -D 'cn=admin,dc=superhosting,dc=com' -w 'admin' -r 'uid="+usuario+",ou=People,dc=superhosting,dc=com' ")
commands.getoutput("ssh root@172.22.200.109 rm -r /var/www/superhosting/"+uid)
