#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands
import getpass


CN=commands.getoutput("echo "+raw_input('Dime nombre y apellidos: ')+" | base64")
SN=commands.getoutput("echo "+raw_input('Dime el primer apellido: ')+" | base64")
correo=raw_input("Correo: ")
uid=""
lista=[]
lista = commands.getoutput("ldapsearch -x  | grep '^uid:'")
while uid=="" or uid in lista:
	uid= raw_input("Dime un uid (usuario del sistema): ") 
num=[]
num.append(commands.getoutput("ldapsearch -x | grep '^uidNumber:' | egrep -o [0-9]{4}"))
contra= getpass.getpass("Dime el passwd: ")
UID='4000'
if UID in num:
	UID = str(int(commands.getoutput("ldapsearch -x | grep '^uidNumber:' | egrep -o [0-9]{4} | sort | tail -n1")) +1)

usuario=["dn: uid="+uid+",ou=People,dc=superhosting,dc=com\n",
		"objectClass: top\n",
		"objectClass: posixAccount\n",
		"objectClass: inetOrgPerson\n",
		"objectClass: person\n",
		"cn:: "+CN+"\n",
		"uid: "+uid+"\n",
		"uidNumber: "+UID+"\n",
		"gidNumber: 4000\n",
		"homeDirectory: /var/www/superhosting/"+uid+"\n",
		"loginShell: /bin/bash\n",
		"userPassword: "+contra+"\n",
		"sn:: "+SN+"\n",
		"mail: "+correo+"\n",
		"givenName: "+SN+"\n"]

f=open('usuario.ldif','w')
f.writelines(usuario)
f.close()


commands.getoutput("ldapadd -x -h 172.22.200.109 -D 'cn=admin,dc=superhosting,dc=com' -w 'admin' -f usuario.ldif ")




