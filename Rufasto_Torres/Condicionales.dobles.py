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


#Ejercicio02
#programa imc con sobrepeso
import os
#Declaracion de variables
paciente,peso,talla,total="",0.0,0.0,0.0

#INPUT via OS
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#PROCESING
#Si el total supera a 24.99
#mostrar "paciente con sobrepeso"
#Caso contrario mostrar "tiene imc normal"
if(total>24.99):
    print(paciente, ", paciente con sobrepeso ")
else:
    print(paciente, ", tiene imc normal")
#fin_if
