"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

obs: valor_de_parada não inclusive (início padrão 0, epasso de 1 em 1)

Exemplos:

# Forma 1
# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2
range(valor_de_início, valor_de_parada)

obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1, 11):
    print(num)

# Forma 3

range(valor_de_início, valor_de_parada, passo)

obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo também)

# Exemplo Forma 3
for num in range(5, 50, 5):
    print(num)

Forma 4 (inversa)
range(valor_de_início, valor_de_parada, passo)

obs: valor_de_parada não inclusive (início especificado pelo usuário, e passo também)

"""
# Exemplo forma 4

for num in range(10, -1, -1):
    print(num)


