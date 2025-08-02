 #################Practica  Ejercios 8-14

#############Pide al usuario 3 numeros e identificar el mayor:

##print ('Ingresa tu primer numero')
##primer_num =float(input ())
##print ('Ingresa tu segundo numero')
##segundo_num =float(input ())
##print ('Ingresa tu tercer numero')
##tercer_num =float(input ())
##mayor= max(primer_num,segundo_num,tercer_num)
##print ('el numero más grande es:',mayor)

########################## Suma de los digitos de un numero

##numero_s= input('Ingrese un numero:')
##suma=0
##for caracter in numero_s:
##    if caracter in '123456789':
##        suma += int (caracter)
##print(f'La suma de los digitos es: {suma}')

###################### Contar palabras en una frase

##frase=input('Ingresa tu frase:')
##palabras= frase.split()
##cantidad=len(palabras)
##print(f'La frase tiene {cantidad} palabras.')

#########################Lista inversa

##lista_1=[10,9,8,7,6,5,4,3,2,1]
##lista_In= lista_1[::-1]
##print('La lista invertida es:',lista_In)

##########################numeros aleatorios

##from random import random,uniform,randint,choice
##lista=[randint(0,20)for i in range (5)]
##print(lista)
##
######################Adivinar numero hasta que sea el correcto

##from random import random,uniform,randint,choice
##lista_1=[randint(0,10)for i in range (5)]
##numero =-1
##while numero not in (lista_1):
##    numero= int(input('Busca el numero entre el 0 y 10:  '))
##    if numero not in lista_1:
##        print('Sigue intentando')
##
##    else:
##        print('Encontraste el numero!!!!!!!!!!!!!')
##
####################Secuencia personaliza
##        
##lista_multi_3= [i for i in range(1,61)if i %3 == 0]
##print(lista_multi_3)
##







