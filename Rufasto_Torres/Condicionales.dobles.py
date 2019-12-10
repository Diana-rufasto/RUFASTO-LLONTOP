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


#Ejercicio03
#programa imc con delgadez severa
import os
#Declaracion de variables
paciente,peso,talla,total="",0.0,0.0,0.0

#INPUT via OS
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#PROCESING
#Si el total es menor a 19.99
#mostrar "paciente con delgadez severa"
#Caso contrario mostrar "bien tiene imc normal"
if(total<19.99):
    print(paciente, ", paciente con delgadez severa ")
else:
    print(paciente, ", bien tiene imc normal ")
#fin_if


#Ejercicio04
#Programa con imc normal
import os
#Declaracion de variables
paciente,peso,talla,total="",0.0,0.0,0.0

#INPUT via OS
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#PROCESING
#Si el total es mayor a 20.00
#mostrar "tiene peso normal"
#Caso contrario mostrar "tiene que ir al medico"
if(total>20.00):
    print(paciente, ", tiene peso normal ")
else:
    print(paciente, ", tiene que ir al medico ")
#fin_if


#Ejercicio05
#Programa tercio superior
import os
#Declaracion de variables
estudiante,universidad,promedio="","",0

#INPUT via OS
estudiante=os.sys.argv[1]
universidad=os.sys.argv[2]
promedio=int(os.sys.argv[3])

#PROCESING
#Si el promedio supera a 16
#mostrar "perteneces al tercio superior"
#Caso contrario mostrar "no perteneces"
if(promedio>16):
    print(estudiante, ", perteneces al tercio superior ")
else:
    print(estudiante, ", no perteneces ")
#fin_if


#Ejercicio06
#Programa dias de vacaciones
import os
#Declaracion de variables
obrero,empres,anios_trabajando="","",0

#INPUT via OS
obrero=os.sys.argv[1]
empresa=os.sys.argv[2]
anios_trabajando=int(os.sys.argv[3])

#PROCESING
#Si anios trabajando supera los 5 anios
#mostrar "disfrute sus vacaciones"
#Caso contrario mostrar "no dispone de vacaciones"
if(anios_trabajando>5):
    print(obrero, ", disfrute sus vacaciones ")
else:
    print(obrero, ", no dispone de vacaciones ")
#fin_if


#Ejercicio07
#Programa de pasar pedido
import os
#Declaracion de variables
consultora,empresa,total_pedido="","",0.0

#INPUT via OS
consultora=os.sys.argv[1]
empresa=os.sys.argv[2]
total_pedido=float(os.sys.argv[3])

#PROCESING
#Si el total pedido supera a 120.00
#mostrar "pedido aprobado"
#Caso contrario mostrar "no puede pasar pedido"
if(total_pedido>120.00):
    print(consultora, ", pedido aprobado ")
else:
    print(consultora, ", no puede pasar pedido")
#fin_if

