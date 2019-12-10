#Ejercicio01
#Programa aprobar curso
import os

#Declaracion de variables
alumno,curso,nota1,nota2,nota3,promedio="","",0.0,0.0,0.0,0.0

#INPUT via OS
alumno=os.sys.argv[1]
curso=os.sys.argv[2]
nota1=float(os.sys.argv[3])
nota2=float(os.sys.argv[4])
nota3=float(os.sys.argv[5])

#PROCESING
promedio= float(round((nota1+nota2+nota3)/3,0))

#Condicion multiple
# Si el prom => 15.00 y 20.00 (felicidades)
if ( promedio >=15.00 and promedio <=20.00 ):
    print(alumno, "felicidades")
# Si el prom 10.5 y 14.00 (sigue asi)
if ( promedio >= 10.5 and promedio <= 14.00):
    print(alumno, "sigue asi")

