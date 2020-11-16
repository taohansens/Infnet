"""
Q.1 Usando Python, faça o que se pede (código e printscreen):
    Crie uma lista vazia;
    Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
    Imprima a lista;
    Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
    Imprima a lista modificada;
    Imprima também o tamanho da lista usando a função len();
    Altere o valor do último elemento para 6 e imprima a lista modificada.
"""

# Criada lista
lista = []

# Adicionando elementos 1,2,3,4,5.
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

# Imprimindo a lista
print("Lista: ",lista)

# Removendo os elementos 3 e 6, se existirem
for numero in lista:
    if numero == 3 or numero == 6:
        lista.remove(numero)

# Imprimindo a lista modificada
print("Lista modificada: ", lista)

# Mostrando o tamanho da lista modificado
print("Elementos na lista: ", len(lista))

# Alterando último elemento da lista para 6.
lista[-1] = 6

# Mostrando lista com alteração do último elemento.
print("Último elemento alterado: ", lista)

