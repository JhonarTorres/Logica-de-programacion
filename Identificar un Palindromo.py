palabra= input('Introduce la palabra:')
palabra_normal = palabra.lower().replace('','')
palabra_invertida = palabra_normal[::-1]

if palabra_normal == palabra_invertida:
    print('Es un palindromo!!!')
else:
    print('No es un palindromo')
    
