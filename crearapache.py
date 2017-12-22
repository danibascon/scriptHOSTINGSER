#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands
uid= raw_input("Dime un uid (usuario del sistema): ")


ultima=["Alias /"+uid+" /var/www/superhosting/"+uid+"\n",
		"	<Directory /home/nfs/"+uid+"/> \n",
		"       	Options +Indexes +SymLinksIfOwnerMatch \n",
		"       	AllowOverride None\n",
		"       	Require all granted\n",
		"	</Directory>\n",
		"</VirtualHost>\n"]

f=open("ssh root@172.22.200.109 /etc/apache2/sites-available/"+uid+".conf","w")
f.writelines(ultima)
f.close()

commands.getoutput("a2ensite "+uid+".conf")
commands.getoutput("service apache2 restart")

