

import sys


print (''' Simulador de fila - Tera 3 filas em uma fila sera
        de pessoas normais, na outra tera gestantes, e na 
        ultima fileira tera idosos.''')

tuto = input ('Voce deseja jogar? [S/N]').lower()

if tuto == 'n':
    print ('Tchau!:)'), sys.exit()

elif tuto == 's':
    print ('Voce desejou Jogar...')

else:
    print ('Opçao invalida'), sys.exit()



print (''' Instruçao - Voce podera acrescentar pessoas nas fileira com 'add p',
            para adicionar gestantes 'add g', para adicionar Idosos 'add i',
             para fazer a fila andar 'walk' e para sair 'x' Divirta-se!''')

py = '''
________
        |
        |{}
PyBank  |{}
   $    |{}
        |
________|

'''

cont = 1
jog = input('Vode pode (add p, i ou g) adiconar uma pessoa voce pode andar (walk) e sair (x)').lower()
idosos = []
gestantes = []
pessoas = []

while jog != 'x': 
        if jog == 'add p':
            pessoas.append(cont)
            cont += 1

        
        if jog == 'add g':
            gestantes.append(cont)
            cont += 1     
        
    
        if jog == 'add i':
            idosos.append(cont)
            cont += 1
        if jog == 'walk':
            if len(idosos) > 0:
                print (idosos.pop(0))
            elif len(gestantes) > 0:
                print (gestantes.pop(0))
            else:
                print(pessoas.pop(0))


        print (py.format(pessoas, gestantes, idosos))
        jog = input('Vode pode (add p, i ou g) adiconar uma pessoa voce pode andar (walk) e sair (x)').lower()
        
if jog == 'x':
    print('Volte sempre :D'),sys.exit()
