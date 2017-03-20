#coding: utf8

import sys
import math

print "S-Salir"
print "1-Sumar"
print "2-Restar"
print "3-Multiplicar"
print "4-Dividir"

opcionmain = raw_input("Introduzca una opcion :")

while (opcionmain == False):
	print "Continue"
	
if (opcionmain == 'S' or opcionmain == 's'):
	print "Adios"
		
if (opcionmain == 1):
		variable1 = input("Introduzca el numero :")
		variable2 = input("Introduzca el numero :")
		print "El resultado es :" , variable1 + variable2
	
if (opcionmain == 2):
		variable1 = input("Introduzca el numero :")
		variable2 = input("Introduzca el numero :")
		print "El resultado es :" , variable1 - variable2
	
if (opcionmain == 3):
		variable1 = input("Introduzca el numero :")
		variable2 = input("Introduzca el numero :")
		print "El resultado es :" , variable1 * variable2
	
if (opcionmain == 4):
		variable1 = input("Introduzca el numero :")
		variable2 = input("Introduzca el numero :")
		print "El resultado es :" , variable1 / variable2
	

	
