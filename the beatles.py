# etapa 1
beatles = []
print("Etapa 1:", beatles)


# etapa 2

beatles.append('John Lennon')
beatles.append('Paul macCartney')
beatles.append('George Harrison')

print("Etapa 2:", beatles)


# etapa 3

for nomes  in range(2):
    nome = input('Nome: ')
    beatles.append(nome)

print("Etapa 3:", beatles)


# etapa 4

nome1  = beatles.index('John Lennon')
nome2  = beatles.index('Pete Best')

del  beatles[nome1]
del  beatles[nome2]

print("Etapa 4:", beatles)

# passo 5

beatles.insert(0,'Ringo Starr')

print("Etapa 5:", beatles)



# testando o tamanho da lista

("o fabuloso", len(beatles))
