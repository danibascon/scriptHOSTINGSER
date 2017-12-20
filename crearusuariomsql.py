#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import commands
import sys
import getpass

nombre=raw_input('Dime tu uid: ')
basedatos=nombre+"database"
contra=raw_input('Dime la contra: ')


#commands.getoutput("mariadb -u root -e 'create database bascon'")
#commands.getoutput("mariadb -u root -e 'grant all privileges on bascon.* to 'dani'@'%' identified by 'dani'") 






#commands.getoutput("mariadb -u root -e 'grant all privileges on "+bascon+".* to '"+dani+"'@'%' identified by '"+dani+"'") 






#mariadb -u root -p 'root' -e 'grant all privileges on bascon.* to 'dani'@'%' identified by 'dani''





commands.getoutput("mariadb -h 10.0.0.16 -u admin -p'admin' -e 'create database "+basedatos+"'")
commands.getoutput("mariadb -h 10.0.0.16 -u admin -p'admin' -e 'grant all privileges on "+basedatos+".* to '"+nombre+"'@'%' identified by '"+contra+"'")









































































































