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


#Ejercicio02
#Programa imc con sobrepeso
import os

#Declaracion de variables
paciente,peso,talla,total="",0.0,0.0,0.0

#INPUT via OS
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])

#PROCESING
total= float(round(( peso/(talla*talla),0)))

#Condicion multiple
#Si el total => 24.99 y 30.99 (paciente con sobrepeso)
if(total>=24.99 and total <=30.99):
    print(paciente, " paciente con sobrepeso ")
#Si el total 20.00 y 24.00 (tiene imc normal)
if(total >= 20.00 and total <= 24.00):
    print(paciente, "tiene imc normal")


#Ejercicio03
#programa imc con delgadez severa
import os

#Declaracion de variables
paciente,peso,talla,total="",0.0,0.0,0.0

#INPUT via OS
paciente=os.sys.argv[1]
peso=float(os.sys.argv[2])
talla=float(os.sys.argv[3])

#PROCESING
total= float(round(( peso/(talla*talla),0)))

#Condicion multiple
#Si el total => 15.99 y 19.99 (paciente con delgadez severa)
if(total>=15.99 and total <=19.99):
    print(paciente, " paciente con delgadez severa ")
#Si el total 14.99 y 14.99 (bien tiene imc normal)
if(total >=14.99 and total <=14.99):
    print(paciente, "bien tiene imc normal")


#Ejercico04
# Programa para calcular 5 nota de ingles
import os

# Declaracion de variables
n1,n2,n3,n4,n5,prom=0,0,0,0,0,0

# INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])
n4=int(os.sys.argv[4])
n5=int(os.sys.argv[5])

# PROCESSING
prom=int(round((n1+n2+n3+n4+n5)/5,0))

# Condicion multiple
# Si el prom => 95 y 100 (Very Good)
if ( prom >=95 and prom <=100 ):
    print("Very Good!")
# Si el prom 90 y 94 (Good)
if ( prom >= 90 and prom <= 94):
    print("Good!")


#Ejercico05
# Programa para sustentar tesis
import os

# Declaracion de variables
n1,n2,n3,n4,n5,prom=0,0,0,0,0,0

# INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])

# PROCESSING
prom=int(round((n1+n2+n3)/3,0))

# Condicion multiple
# Si el prom => 17 y  20(Tesis aprobada)
if ( prom >=17 and prom <=20 ):
    print("Tesis aprobada")
# Si el prom 14 y 16 (Buen trabajo)
if ( prom >= 14 and prom <= 16):
    print("Buen trabajo")


#Ejercicio06
#Programa dias de vacaciones
import os

#Declaracion de variables
trabajador,anios,meses,dias,total="",0,0,0,0.0

#INPUT via OS
trabajador=os.sys.argv[1]
anios=int(os.sys.argv[2])
meses=int(os.sys.argv[3])
dias=int(os.sys.argv[4])

#PROCESING
total= ((anios*365)+(meses*30)+dias)

#Condicion multiple
#Si el total => 4 y 6 (disfrute sus vacaciones)
if(total >=4 and total <=6):
    print(trabajador, ", disfrute sus vacaciones ")
#Si el total >=1 y 3 (no dispone de vacaciones)
if(total>=1 and total <=3):
    print(trabajador, ", no dispone de vacaciones ")
