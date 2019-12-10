#Ejercicio01
#programa aprobar curso
import os
#declara
alumno=""
curso=""
promedio=0.0

#Input via os
alumno=os.sys.argv[1]
curso=os.sys.argv[2]
promedio=float(os.sys.argv[3])

#procesing
#Si el promedio supera a 11
#mostrar "aprobaste el curso felicidades"
if(promedio>11):
    print(alumno,"aprobaste el curso felicidades")


#Ejercicio02
#programa imc con sobrepeso
import os
#declara
paciente=""
peso=0.0
talla=0.0
total=0.0

#Input via os
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#procesing
#Si el total supera a 24.99
#mostrar "paciente con sobrepeso"
if(total>24.99):
    print(paciente,"paciente con sobrepeso")


#Ejercicio03
#programa imc con delgadez severa
import os
#declara
paciente=""
peso=0.0
talla=0.0
total=0.0

#Input via os
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#procesing
#Si el total es menor a 19.99
#mostrar "paciente con delgadez severa"
if(total<19.99):
    print(paciente,"paciente con delgadez severa")


#Ejercicio04
#programa con imc normal
import os
#declara
paciente=""
peso=0.0
talla=0.0
total=0.0

#Input via os
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])
total=float(os.sys.argv[4])

#procesing
#Si el total es mayor a 20.00
#mostrar "tiene peso normal"
if(total>20.00):
    print(paciente,"tiene peso normal")


#Ejercicio05
#programa tercio superior
import os
#declara
estudiante=""
universidad=""
promedio=0

#Input via os
estudiante=os.sys.argv[1]
universidad=os.sys.argv[2]
promedio=int(os.sys.argv[3])

#procesing
#Si el promedio supera a 16
#mostrar "perteneces al tercio superior"
if(promedio>16):
    print(estudiante,"perteneces al tercio superior")


#Ejercicio06
#programa dias de vacaciones
import os
#declara
obrero=""
empresa=""
anios_trabajando=0

#Input via os
obrero=os.sys.argv[1]
empresa=os.sys.argv[2]
anios_trabajando=int(os.sys.argv[3])

#procesing
#Si anios trabajando supera los 5 anios
#mostrar "disfrute sus vacaciones"
if(anios_trabajando>5):
    print(obrero,"disfrute sus vacaciones")


#Ejercicio07
#programa de pasar pedido
import os
#declara
consultora=""
empresa=""
total_pedido=0.0

#Input via os
consultora=os.sys.argv[1]
empresa=os.sys.argv[2]
total_pedido=float(os.sys.argv[3])

#procesing
#Si el total pedido supera a 120.00
#mostrar "pedido aprobado"
if(total_pedido>120.00):
    print(consultora,"pedido aprobado")


#Ejercicio08
#programa de liquidacion
import os
#declara
trabajador=""
empresa=""
tiempo_trabajo=0

#Input via os
trabajador=os.sys.argv[1]
empresa=os.sys.argv[2]
tiempo_trabajo=int(os.sys.argv[3])

#procesing
#Si el tiempo trabajo es mayor a 3 anios
#mostrar "recibira liquidacion"
if(tiempo_trabajo>3):
    print(trabajador,"recibira liquidacion")


#Ejercicio09
#programa de comprador compulsivo
import os
#declara
cliente=""
total_de_productos=0
monto_pagar=0.0

#Input via os
cliente=os.sys.argv[1]
total_de_productos=int(os.sys.argv[2])
monto_pagar=float(os.sys.argv[3])

#procesing
#Si el monto pagar supera a 200.00
#mostrar "gano un canje de 30 soles"
if(monto_pagar>200.00):
    print(cliente,"gano un canje de 30 soles")


#Ejercicio10
#programa personal de avance de ajies
import os
#declara
obrero=""
horas=0.0
total_ajies=0

#Input via os
obrero=os.sys.argv[1]
horas=float(os.sys.argv[2])
total_ajies=int(os.sys.argv[3])

#procesing
#Si el total de ajies es mayor a 40 ajies
#mostrar "es personal de avance"
if(total_ajies>40):
    print(obrero,"es personal de avance")
