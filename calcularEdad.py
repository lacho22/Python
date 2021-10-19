#!/usr/local/bin/python
# -*- coding utf-8 -*-
import os, sys

###########################################
# Author : Horacio Rosales Velasco        #
# Fecha  : 19102021                       #
###########################################

fecha_nacimiento = input("Digite anio nacimiento: ")
diferencia = (2021 - int(fecha_nacimiento))

if diferencia >= 18:
    print("Con  ", diferencia,"  es mayor de edad")
else:
    print("Con  ", diferencia,"  es menor de edad")

