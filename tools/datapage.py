def datapage(num, pagina):
    #print("el numero es ", num)
    #print("la pag es ", pagina)
    contador = 0
    while num > 0:
        contador+=1
        num=num-5
    subcontador=contador
    if (int(contador)-(int(pagina)-1)) >= 10:
        subcontador = 10+(int(pagina)-1)
    return contador, subcontador