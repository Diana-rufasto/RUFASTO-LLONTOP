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
