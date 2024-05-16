sexo = int(input('Digite seu sexo: (1)Para homem (2)Para mulher: '))

if sexo == 1:
    aH = float(input('Digite sua altura: '))
    vH = (72.7 * aH) - 58
   
    print ('Seu peso ideal é ',vH,'quilos')
elif sexo == 2:
    aM = float(input('Digite sua altura: '))
    vM = (62.1 * aM) - 44.7
   
    print ('Seu peso ideal é ',vM,'quilos')