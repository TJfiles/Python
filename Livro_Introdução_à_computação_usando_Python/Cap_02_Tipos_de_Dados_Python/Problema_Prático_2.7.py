notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# Uma expressão que avalia para o número de 7 notas
print(notas.count(7))

# Uma instrução que muda a última nota para 4
notas[-1] = 4
print(notas)

# Uma expressão que avalia para a nota mais alta
print(max(notas))

# Uma instrução que classifica as notas da lista
notas.sort()
print(notas)

#Uma expressão que avalia para a média das notas
print(sum(notas)/len(notas))
