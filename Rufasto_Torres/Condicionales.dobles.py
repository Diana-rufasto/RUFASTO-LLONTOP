#Ejercicio01
#Programa aprobar curso
import os
#Declaracion de variables
alumno,curso,promedio="","",0.0

#INPUT via OS
alumno=os.sys.argv[1]
curso=os.sys.argv[2]
promedio=float(os.sys.argv[3])

#PROCESING
#Si el promedio supera a 11
#mostrar "aprobaste el curso felicidades"
#Caso contrario mostrar "tienes que dar recuperacion"
if(promedio>11):
    print(alumno, ", aprobaste el curso felicidades ")
else:
    print(alumno, ", tienes que dar recuperacion ")
#fin_if
