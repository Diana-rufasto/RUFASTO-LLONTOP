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

