#!/usr/bin/env python
# -*- coding: utf-8 -*-

total = 0
for numero in range (1,6):
	print numero
	
	if numero == 5:
		salir = True
		print "---"
	total = total + numero
	numero = numero + 1
print total
	
