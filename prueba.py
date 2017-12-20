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
lista = commands.getoutput("cat prueba.txt| grep '^uid:'")
while uid=="" or uid in lista:
	uid= raw_input("Dime un uid unico: ") 
num=commands.getoutput("cat prueba.txt | grep '^uidNumber:' | egrep  -o '[0-9]{4}'")
contra= getpass.getpass("Dime el passwd: ")
UID='4000'
if UID in num:
	UID = int(commands.getoutput("cat prueba.txt | grep '^uidNumber:' | egrep  -o '[0-9]{4}' | tail -n1")) +1

usuario=["dn: uid='"+uid+",ou=People,dc=bascon,dc=gonzalonazareno,dc=org \n",
		"objectClass: top \n",
		"objectClass: posixAccount' \n",
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

f=open('prueba.ldif','a')
f.writelines(usuario)
f.close()





commands.getoutput("rm -r uid a b cn sn ssha")


print "Enter LDAP Password:"
commands.getoutput("ldapadd -x -D 'cn=admin,dc=bascon,dc=gonzalonazareno,dc=org' -W -f genuser.ldif ")


commands.getoutput("sed -i'.bak' '$d' /etc/apache2/sites-available/www.conf")


