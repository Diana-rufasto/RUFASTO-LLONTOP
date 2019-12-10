#programa alumno aprobado
import os
#declaracion
nombre=""
promedio=0.0

#Input via os
nombre=os.sys.argv[1]
promedio=float(os.sys.argv[2])

#procesing
#si el alumno supera a 11
#mostrar "felicidades aprobaste"
if( promedio > 11 ):
     print(nombre,"felicidades aprobaste")


#Ejercicio2
#programa de adulto alcoholico
import os
#declaracion
nombre_adulto=""
nro_botellas=0

#Input via os
nombre_adulto=os.sys.argv[1]
nro_botellas=int(os.sys.argv[2])

#procesing
#si el nro de botellas supera a 50
#mostrar "adulto alcoholico"
if( nro_botellas > 50 ):
    print(nombre_adulto,"adulto alcoholico")


#Ejercicio3
#programa de adolescente para ingreso a discoteca
import os
#declaracion
nombre_adolescente=""
nombre_discoteca=""
edad_adolescente=0

#Input via os
nombre_adolescente=os.sys.argv[1]
nombre_discoteca=os.sys.argv[2]
edad_adolescente=int(os.sys.argv[3])

#procesing
#si la edad supera a los 18 anios
#mostrar "bienvenido"
if( edad_adolescente > 18 ):
    print(nombre_adolescente,"bienvenido")


#Ejercicio4
#programa de consultora compulsiva
import os
#declaracion
nombre_consultora=""
total_de_la_compra=0.0

#Input via os
nombre_consultora=os.sys.argv[1]
total_de_la_compra=float(os.sys.argv[2])

#procesing
#si la compra supera los 600 soles
#mostrar "consultora compulsiva"
if( total_de_la_compra > 600 ):
    print(nombre_consultora,"compradora compulsiva")


#Ejercicio5
#programa de empleado compulsivo
import os
#declaracion
nombre_empleado=""
monto_total=0.0

#Input via os
nombre_empleado=os.sys.argv[1]
monto_total=float(os.sys.argv[2])

#procesing
#si el empleado supera los 2000
#mostrar "empleado compulsivo"
if( monto_total > 2000 ):
    print(nombre_empleado,"empleado compulsivo")

#Ejercicio6
#programa de exceso de alumnos
import os
#declaracion
nombre_colegio=""
cantidad_total=0

#Input via os
nombre_colegio=os.sys.argv[1]
cantidad_total=int(os.sys.argv[2])

#procesing
#si la cantidad de alumnos supera los 300
#mostrar "lo sentimos, exceso de alumnos"
if( cantidad_total > 300 ):
    print(nombre_colegio,"lo sentimos, exceso de alumnos")

#Ejercicio7
#programa de ninios con hemoglobina estable
import os
#declaracion
nombre_ninio=""
resultado_hemoglobina=0.0

#Input via os
nombre_ninio=os.sys.argv[1]
resultado_hemoglobina=float(os.sys.argv[2])

#procesing
#si el resultado supera el 12.5
#mostrar "felicidades, estas bien"
if( resultado_hemoglobina > 12.5 ):
    print(nombre_ninio,"felicidades, estas bien")


#Ejercicio8
#programa Cineplanet
import os
#declaracion de variables
nombre=""
nro_tickets=0
#INPUT via os
nombre=os.sys.argv[1]
nro_tickets=int(os.sys.argv[2])

#procesing
#Si el nro de tickets supera 150,
# mostrar "Ganaste un combo"
if ( nro_tickets > 150 ):
    print(nombre, " Ganaste un combo")


#Ejercicio9
#programa cliente
import os
#declaracion de variables
nombre_cliente=""
total=0.0
#Input via os
nombre_cliente=os.sys.argv[1]
total=float(os.sys.argv[2])

#procesing
#si el cliente supera los 300,
#mostrar "Felicidades ganaste una prenda de vestir"
if( total > 300 ):
    print(nombre_cliente, "Felicidades ganaste una prenda de vestir")


#Ejercicio10
#programa consultora
import os
#declaracion de variables
nombre_consultora=""
total_de_puntos=0
#Input via os
nombre_consultora=os.sys.argv[1]
total_de_puntos=int(os.sys.argv[2])

#procesing
#si la consultora sera los 500,
#mostrar "Felicidades ganaste un pavo!"
if( total_de_puntos > 500 ):
    print(nombre_consultora, "Felicidades ganaste un pavo!")
