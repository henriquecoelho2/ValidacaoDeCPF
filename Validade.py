CPFdoUsuario= '111.444.777-05'
listaDeDigitos=[]
CPFaSerValidado=int(CPFdoUsuario.replace(".","").replace("-",""))
while CPFaSerValidado > 0:
    temp=CPFaSerValidado//10
    resto=CPFaSerValidado-10*temp
    listaDeDigitos.append(resto)
    CPFaSerValidado=temp
listaDeDigitos.reverse()