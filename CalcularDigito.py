CPFdoUsuario= '111.444.777-05'
listaDeDigitos=[]
listaDosDigitosIniciais=[]
listaDosDigitosFinais=[]
CPFaSerValidado=int(CPFdoUsuario.replace(".","").replace("-",""))
fator = 1
somaDasVariaveis= 0

while CPFaSerValidado > 0:
    temp=CPFaSerValidado//10
    resto=CPFaSerValidado-10*temp
    listaDeDigitos.append(resto)
    CPFaSerValidado=temp
listaDeDigitos.reverse()

for i in range(2):
    varPop=listaDeDigitos.pop()
    listaDosDigitosIniciais.append(varPop)

for i in reversed(listaDeDigitos):
    fator += 1
    variavelTemporaria = i*fator
    somaDasVariaveis += variavelTemporaria
resto= somaDasVariaveis%11
if resto < 2:
    digito = 0
else:
    digito = 11-resto
listaDeDigitos.append(digito)
print(listaDeDigitos)