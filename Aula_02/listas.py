clientes = ["joão","caio","zér"]

print(clientes[1][0])
print("Caio"[0])

# acrescentar elementos no final da lista
clientes.append("João do Caminhão")
print(clientes)


# acrescemtar em uma determinada posição
clientes.insert(0,"josef")
clientes.insert(357,"josef ultimo")
print(clientes)


# atualizar um valor 
indice = clientes.index("zér") # procura qual é o indice de "zér"
print(indice) # printa o indice do "zér"
clientes[indice] = "Josevaldo" # no índice do "zér" substitui o que está nesse indice por "Josevaldo"
print(clientes)

# delete

# deletar pelo valor:
clientes.remove("joão")
print(clientes)

# deletar pelo indíce:
clientes.pop(2)

print(clientes)