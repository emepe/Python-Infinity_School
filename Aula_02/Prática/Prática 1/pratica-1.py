clientes = []

for i in range(3):
    
    cliente = {}
    
    cliente["Nome"] = input("\nDigite o nome do cliente:\n\nNome: ")
    cliente["Telefone"] = input("\n\nDigite o número de telefone:\n\nTelefone: ")
    cliente["E-mail"] = input("\n\nDigite o e-mail:\n\nE-mail: ")
    cliente["Profissão"] = input("\n\nDigite a profissão:\n\nProfissão: ")


    clientes.append(cliente)


for cli in clientes:
    print (cli)
