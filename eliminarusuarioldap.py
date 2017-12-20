#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands
import getpass

commands.getoutput("ldapdelete -x -h 172.22.200.109 -D 'cn=admin,dc=superhosting,dc=com' -w 'admin' -r 'uid=usuario4,ou=People,dc=com' ")
