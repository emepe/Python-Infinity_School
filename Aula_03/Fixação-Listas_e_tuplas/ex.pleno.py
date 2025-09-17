#=============================== Exercício 1 ================================                                                                                                                                                                                                                    

nomes = ["Gabriel","Juliano","Anna","Marcos"]

letra_procurada = "a"

letra_procurada.lower()

contador = 0
         
for nome in nomes: 

    if letra_procurada in nome:
        contador = contador + nome.lower().count(letra_procurada)


print(f'A quantidade de nomes que possuem a letra "{letra_procurada.upper()}" é {contador}')  

#=============================== Exercício 2 ================================                                                                                                                                                                                                                    




