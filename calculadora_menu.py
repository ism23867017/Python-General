#coding: utf8

import sys
import math

print "1-Sumar"
print "2-Restar"
print "3-Multiplicar"
print "4-Dividir"
print "5-Salir"

opcionmain = input("Introduzca la opcion deseada :")

while not opcionmain == 6:
	
	if opcionmain == 1:
		variable1 = input("Introduzca la primera cifra :")
		variable2 = input("Introduzca la segunda cifra :")
		print "El resultado es : ", variable1 + variable2
	
	if opcionmain == 2:
		variable1 = input("Introduzca la primera cifra :")
		variable2 = input("Introduzca la segunda cifra :")
		print "El resultado es : ", variable1 - variable2
		
	if opcionmain == 3:
		variable1 = input("Introduzca la primera cifra :")
		variable2 = input("Introduzca la segunda cifra :")
		print "El resultado es : ", variable1 * variable2
		
	if opcionmain == 4:
		variable1 = input("Introduzca la primera cifra :")
		variable2 = input("Introduzca la segunda cifra :")
		print "El resultado es : ", variable1 / variable2
	
	if opcionmain == 5:
		sys.exit(0)
	
