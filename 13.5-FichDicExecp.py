#!/usr/bin/python
#-*- coding: utf-8 -*-

fich = open("/etc/passwd","r");

maquinas = fich.readlines();
diccionario = {};

for usuarios in maquinas:
	separado = usuarios.split(":");
	login = separado[0];			# separado[0] contiene el usuario que sera la clave
	shell = separado[-1][:-1];		# separado[-1][:-1] contiene su shell que sera el valor
	diccionario[login] = shell; 

try:
	print ("El terminal que usa el usuario root es:" + diccionario['root'])
	print ("El terminal que usa el usuario imaginario es:" + diccionario['imaginario'])
except KeyError:
	print ("Usuario incorrecto, no se puede mostrar el terminal")
	
fich.close();

