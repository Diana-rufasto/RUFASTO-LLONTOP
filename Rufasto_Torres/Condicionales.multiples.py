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


#Ejercicio07
#Programa de pasar pedido
import os
#Declaracion de variables
cliente,producto1,cantidad_prod1,costo_uni_prod1,producto2,cantidad_prod2,costo_uni_prod2,total="","",0,0.0,"",0,0.0,0.0

#INPUT via OS
cliente=os.sys.argv[1]
producto1=os.sys.argv[2]
cantidad_prod1=int(os.sys.argv[3])
costo_uni_prod1=float(os.sys.argv[4])
producto2=os.sys.argv[5]
cantidad_prod2=int(os.sys.argv[6])
costo_uni_prod2=float(os.sys.argv[7])

#PROCESING
total=(cantidad_prod1*costo_uni_prod1)+(cantidad_prod2*costo_uni_prod2)

#Condicion multiple
#Si el total => 120.00 y 180.00 (pedido aprobado)
if(total>=120.00 and total <=180.00):
    print(cliente, " pedido aprobado ")
#Si el total >=70.00 y 110.00 (no puede pasar pedido)
if(total>=70.00 and total <=110.00):
    print(cliente, " no puede pasar pedido")

#Ejercicio08
#Programa de comprador compulsivo
import os

#Declaracion de variables
cliente,producto,cant,costo_uni,total="","",0,0.0,0.0

#INPUT via OS
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
cant=int(os.sys.argv[3])
costo_uni=float(os.sys.argv[4])

#PROCESING
total=cant*costo_uni

#Condicion multiple
#Si el total => 200.00 y 250.00 (comprador compulsivo)
if(total>=200.00 and total <=250.00):
    print(cliente, "comprador complusivo ")
#Si el total >=120.00 y 190.00 (vuelva pronto)
if(total>=120.00 and total <=190.00):
    print(cliente, "vuelva pronto ")


#Ejercicio09
# Programa para pasar ciclo
import os

# Declaracion de variables
nota1,nota2,nota3,nota4,nota5,prom=0,0,0,0,0,0

# INPUT VIA OS
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])
nota5=int(os.sys.argv[5])

# PROCESSING
prom=int(round((nota1+nota2+nota3+nota4+nota5)/5,0))

# Condicion multiple
# Si el prom => 17 y 20 (Muy bien!)
if ( prom >=17 and prom <=20 ):
    print("Muy bien!")
# Si el prom 12  y 16 (Bien)
if ( prom >= 12 and prom <= 16):
    print("Bien")


#Ejercicio10
#Programa personal de avance de ajies
import os

#Declaracion de variables
obrero,total_de_ajies_por_min,horas_trabajadas,total="",0,0,0

#INPUT via OS
obrero=os.sys.argv[1]
total_de_ajies_por_min=int(os.sys.argv[3])
horas_trabajadas=int(os.sys.argv[4])

#PROCESING
total=int(round (total_de_ajies_por_min*horas_trabajadas),0)

#Condicion multiple
#Si el total => 40 y 50 (es personal de avance)
if(total>=40 and total <=50):
    print(obrero, "es personal de avance")
#Si el total 15 y 39 (esfuerzate en tu trabajo)
if(total >=15 and total <=39):
    print(obrero, "esfuerzate en tu trabajo")
