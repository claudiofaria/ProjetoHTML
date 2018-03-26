#!/usr/bin/python
#-*- coding: utf8 -*-

var=raw_input()
usuario=var.split("&")[0].split("=")[1]
senha=var.split("&")[1].split("=")[1]

def cabecalho():
	print("content-type: text/html")
	print("")

def menu():
	cabecalho()
	f = open("menu.html", "r")
	pagina = f.read()
	f.close()
	print(pagina)

def errou():
	cabecalho()
	print("<h1> Login Falhou </h1>")

if usuario == "claudio" and senha == "faria":
	menu()
else:
	errou()
