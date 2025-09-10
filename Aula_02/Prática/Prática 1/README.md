# Projeto Guiado

Este projeto tem como objetivo criar uma lista de clientes onde cada cliente será representado por um dicionário com informações como nome, telefone, email e profissão. A seguir estão os passos para a construção do projeto:

### Passos

1. **Criar uma lista vazia chamada `clientes`:**
   - A lista `clientes` armazenará todos os dicionários representando os clientes.

2. **Criar um dicionário vazio chamado `cliente`:**
   - O dicionário `cliente` será utilizado para armazenar as informações de um único cliente.

3. **Solicitar o nome do cliente:**
   - Utilize a função `input()` para solicitar ao usuário o nome do cliente e armazene esse valor no dicionário `cliente` com a chave `"nome"`.

4. **Solicitar o telefone do cliente:**
   - Utilize a função `input()` para solicitar ao usuário o telefone do cliente e armazene esse valor no dicionário `cliente` com a chave `"telefone"`.

5. **Solicitar o email do cliente:**
   - Utilize a função `input()` para solicitar ao usuário o email do cliente e armazene esse valor no dicionário `cliente` com a chave `"email"`.

6. **Solicitar a profissão do cliente:**
   - Utilize a função `input()` para solicitar ao usuário a profissão do cliente e armazene esse valor no dicionário `cliente` com a chave `"profissao"`.

7. **Adicionar o dicionário `cliente` à lista `clientes`:**
   - Utilize o método `append()` para adicionar o dicionário `cliente` na lista `clientes`.

### Observações

- Este exercício pode ser expandido para permitir o cadastro de múltiplos clientes, utilizando um loop para continuar pedindo informações até que o usuário deseje encerrar o programa.
- A validação dos dados inseridos, como verificar se o telefone ou email são válidos, pode ser adicionada como um próximo desafio.
