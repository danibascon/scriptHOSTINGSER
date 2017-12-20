#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import commands
import sys
import getpass


CN=commands.getoutput("echo "+raw_input('Dime nombre y apellidos: ')+" | base64")
SN=commands.getoutput("echo "+raw_input('Dime el primer apellido: ')+" | base64")
correo=raw_input("Correo: ")
uid=""
lista=[]
lista = commands.getoutput("ldapsearch -x -h 172.22.200.109 -b 'ou=People,dc=superhosting,dc=com' | grep '^uid:'")
while uid=="" or uid in lista:
	uid= raw_input("Dime un uid unico: ") 
num=[]
num.append(int(commands.getoutput("ldapsearch -x -h 172.22.200.109 -b 'ou=People,dc=superhosting,dc=com' | grep '^uidNumber:' | egrep -o [0-9]{4}")))
contra= getpass.getpass("Dime el passwd: ")
UID='4000'
if UID in num:
	UID = int(commands.getoutput("ldapsearch -x -h 172.22.200.109 -b 'ou=People,dc=superhosting,dc=com'| grep '^uidNumber:' | egrep -o [0-9]{4} | tail -n1")) +1

usuario=["dn: uid="+uid+",dc=superhosting,dc=com \n",
		"objectClass: top \n",
		"objectClass: posixAccount \n",
		"objectClass: inetOrgPerson \n",
		"objectClass: person \n",
		"cn:: "+CN+" \n",
		"uid: "+uid+" \n",
		"uidNumber: "+UID+" \n",
		"gidNumber: 2000 \n",
		"homeDirectory: /var/www/superhosting/"+uid+" \n",
		"loginShell: /bin/bash \n",
		"userPassword: "+contra+" \n",
		"sn:: "+SN+" \n",
		"mail: "+correo+" \n",
		"givenName: "+SN+" \n"]

f=open('usuario.ldif','w')
f.writelines(usuario)
f.close()


commands.getoutput("ldapadd -x -h 172.22.200.109 -D 'cn=admin,dc=superhosting,dc=com' -w 'admin' -f usuario.ldif ")



