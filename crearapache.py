
ultima=["Alias /"+UID+" /home/nfs/"+UID+"\n",
		"	<Directory /home/nfs/"+UID+"/> \n",
		"       	Options +Indexes +SymLinksIfOwnerMatch \n",
		"       	AllowOverride None\n",
		"       	Require all granted\n",
		"	</Directory>\n",
		"</VirtualHost>\n"]

f=open('/etc/apache2/sites-available/www.conf','a')
f.writelines(ultima)
f.close()


commands.getoutput("service apache2 restart")

