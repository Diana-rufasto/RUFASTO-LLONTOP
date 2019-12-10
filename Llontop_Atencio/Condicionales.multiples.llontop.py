# Programa para calcular 3 notas de lep2
import os

# Declaracion de variables
n1,n2,n3,prom=0,0,0,0

# INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])

# PROCESSING
prom=int(round((n1+n2+n3)/3,0))

# Condicion multiple
# Si el prom => 55 y 60 (Very Good)
if ( prom >=55 and prom <=60 ):
    print("Very Good!")
# Si el prom 50 y 54 (Good)
if ( prom >= 60 and prom <= 54):
    print("Good!")

#Ejercicio2
#programa alumno aprobado
import os
#declaracion
nombre,nota1,nota2,nota3,nota4,promedio="",0,0,0,0,0

#Input via os
nombre=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])
nota4=int(os.sys.argv[5])

#procesing
prom=int(round((nota1+nota2+nota3+nota4)/4.0))
#Condicion multiple
#si el promedio => 75 y 80 (felicitaciones!)
if ( promedio >=75 and promedio <=80 ):
     print("felicitaciones!")
#si el promedio 70 y 74 (muy bien)
if ( promedio >= 70 and promedio <=74):
    prin("muy bien")


#Ejercicio3
#programa de adulto alcoholico
import os
#declaracion
nombre_adulto,botella1,botella2,botella3="",0,0,0

#Input via os
nombre_adulto=os.sys.argv[1]
botella1=int(os.sys.argv[2])
botella2=int(os.sys.argv[3])
botella3=int(os.sys.argv[4])

#procesing
total=int(round(botella1+botella2+botella3))
#Condicion multiple
#si la suma total => 40 y 50 (usted tiene problemas con el alcohol)
if( total >= 40 and total <=50 ):
    print("usted tiene problemas con el alcohol")
#si la suma total =>30 y 39 (no tiene problemas con el alcohol)
if ( total >=30 and total <=39):
    print("no tiene problemas con el alcohol")


#Ejercicio4
#programa de consultora compulsiva
import os
#declaracion
nombre_consultora,mes1,mes2,mes3="",0.0,0.0,0.0

#Input via os
nombre_consultora=os.sys.argv[1]
mes1=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#procesing
total=float(round(mes1+mes2+mes3))
#Condicion multiple
#si la suma total =>1000 y 1500 (usted es una consultora compulsiva)
if( total >= 1000 and total <=1500):
    print("usted es una compradora compulsiva")
#si la suma total => 500 y 999 (usted no es compradora impulsiva)
if ( total >= 500 and total <=999):
    print("usted no es compradora compulsiva")


#Ejercicio5
#programa de empleado compulsivo
import os
#declaracion
nombre_empleado,mes1,mes2,mes3="",0.0,0.0,0.0

#Input via os
nombre_empleado=os.sys.argv[1]
mesl=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#procesing
total=float(round(mesl+mes2+mes3))
#Condicion multiple
#si la suma total =>7000 y 7500 (usted es un empleado compulsivo)
if(total >= 7000 and total <=7500 ):
    print("usted es un empleado compulsivo")
#si la suma total =>5000 y 6999 (usted no es empleado compulsivo)
if ( total >= 5000 and total <=6999 ):)
    print(" usted no es un empleado compulsivo")


#Ejercicio6
#programa de exceso de alumnos
import os
#declaracion
nombre_colegio,aula1,aula2,aula3,total="",0,0,0,0

#Input via os
nombre_colegio=os.sys.argv[1]
aula1=int(os.sys.argv[2])
aula2=int(os.sys.argv[3])
aula3=int(os.sys.argv[4])

#procesing
total=int(round(aula1+aula2+aula3))
#Condicion multiple
#si la suma total => 250 y 300( no alcanzo vacante)
if( total >= 250 and total <=300 ):
    print("no alcanzo vacante")
#si la suma total => 0 y 240(alcanzo vacante)
if( total >= 0 and total <=240 ):
    print("alcanzo vacante")

#Ejercicio7
#programa consultora
import os
#declaracion de variables
nombre_consultora,mes1,mes2,mes3,mes4,total="",0.0,0.0,0.0,0.0,0.0
#Input via os
nombre_consultora=os.sys.argv[1]
mes1=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])

#procesing
total=float(round(mes1+mes2+mes3))
#Condicion multiple
#si la suma total =>1000 y 1500 (Felicidades ganaste un pavo!)
if( total >= 1000 and total <= 1500 ):
    print("Felicidades ganaste un pavo!")
#si la suma total => 500 y 999
if( total >= 500 and total <= 999 ):
    print("Sigue intentando!")


#Ejercicio8
#programa en venta de leche
import os
#declaracion de variables
ganadero,semana1,semana2,semana3,semana4,total="",0.0,0.0,0.0,0.0,0.0
#Input via os
ganadero=os.sys.argv[1]
semana1=float(os.sys.argv[2])
semana2=float(os.sys.argv[3])
semana3=float(os.sys.argv[4])
semana4=float(os.sys.argv[5])

#procesing
total=float(round(semana1+semana2+semana3+semana4))
#Condicion multiple
#si la suma total =>2000 y 2500 (Perfecto!)
if(total >= 2000 and total <= 2500):
    print("Perfecto!")
#si la suma total => 1000 y 999 (Oh vaya :( !)
if (total >= 1000 and total <= 999)
    print("Oh vaya :(!")

#Ejercicio9
#programa para pasar el anio
import os
#declaracion de variables
nombre_alumno,curso1,curso2,curso3,curso4,cruso5,promedio="",0,0,0,0,0,0
#Input via os
nombre_alumno=os.sys.argv[1]
curso1=int(os.sys.argv[2])
curso2=int(os.sys.argv[3])
curso3=int(os.sys.argv[4])
curso4=int(os.sys.argv[5])
curso5=int(os.sys.argv[6])

#procesing
promedio=int(round(curso1+curso2+curso3+curso4+curso5)/5.0))
#Condicion multiple
#si el promedio =>20 y 15 (Felicidades!)
if(promedio >= 20 and promedio <=15):
    print("Felicidades!")
#si el promedio => 11 y 14 (Aprobaste!)
if(promedio >=11 y and promedio <=14):
    print("Aprobaste!")


#Ejercicio10
#programa en venta de ropa
import os
#declaracion de variables
vendedora,mes1,mes2,mes3,mes4,total="",0.0,0.0,0.0,0.0,0.0
#Input via os
vendedora=os.sys.argv[1]
mes1=float(os.sys.argv[2])
mes2=float(os.sys.argv[3])
mes3=float(os.sys.argv[4])
mes4=float(os.sys.argv[5])

#procesing
total=float(round(mes1+mes2+mes3+mes4))
#Condicion multiple
#si la suma total =>8000 y 10000 (Perfecto!)
if(total >= 8000 and total <= 10000):
    print("Perfecto!")
#si la suma total => 5000 y 7999 (Oh vaya :( !)
if (total >= 5000 and total <= 7999)
    print("Oh vaya :(!")
