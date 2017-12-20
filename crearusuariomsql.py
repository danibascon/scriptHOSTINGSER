#!/usr/bin/python
# -+- coding: utf-8 .*.

import commands

nombre=raw_input('Dime tu uid: ')
basedatos=nombre+"database"
contra=raw_input('Dime la contra: ')
com='"'
commands.getoutput("mariadb -h 10.0.0.16 -u admin -p'admin' -e 'create database "+basedatos+"'")
commands.getoutput("mariadb -h 10.0.0.16 -u admin -p'admin' -e "+com+"grant all privileges on "+basedatos+".* to '"+nombre+"'@'%' identified by '"+contra+"'"+com)

