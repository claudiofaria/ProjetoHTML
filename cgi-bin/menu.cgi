#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
acao=var.split("=")[0]

import os

print("content-type: text/html")
print("")

if acao == "Iniciar":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 start &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Iniciou!</h1>")
elif acao == "Parar":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 stop &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Parou!</h1>")
elif acao == "Reiniciar":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 restart &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Reiniciou!</h1>")
elif acao == "Status":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh bind9 restart")
	print("<h1>Reiniciou!</h1>")

elif acao == "NagiosOn":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 start &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Iniciou!</h1>")
elif acao == "NagiosOff":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 stop &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Parou!</h1>")
elif acao == "NagiosR":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 restart &>> /var/www/html/cgi-bin/serv.log")
	print("<h1>Reiniciou!</h1>")
elif acao == "NagiosStatus":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/serv.sh nagios3 restart")
	print("<h1>Reiniciou!</h1>")

elif acao == "FirewallOn":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/regras.sh")
	print("<h1>Iniciou!</h1>")
elif acao == "FirewallOff":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/panico.sh")
	print("<h1>Parou!</h1>")
elif acao == "FirewallR":
	os.system("date >> /var/www/html/cgi-bin/serv.log")
	os.system("sudo /var/www/html/cgi-bin/fwr.sh")
	print("<h1>Reiniciou!</h1>")
elif acao == "FirewallStatus":
	os.system("sudo /var/www/html/cgi-bin/fws.sh")
#	os.system("sudo /var/www/html/cgi-bin/")
	print("<h1>Reiniciou!</h1>")

elif acao == "Agendar":
	os.system("sudo /var/www/html/cgi-bin/agendar.sh")
	print("<h1>Iniciou!</h1>")








