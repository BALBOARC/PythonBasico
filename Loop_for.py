"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for (int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    /execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de iteráveis:
-String
 nome = 'Geek University'
-Lista
 lista =  [1, 3, 5, 7, 9]
-Range
 numeros = range(1, 10)

 # Exemplo de for 1 (Iterando sob uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)
obs: o valor final não é inclusive.
...
8
9
...

# Exemplo de for 1 (Iterando sob uma String)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

for numero in range(1, 10):
    print(numero)


range(valor_inicial, valor_final)
obs: o valor final não é inclusive.
...
8
9
...

Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k') ...

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

obs: quando não precisamos de um valor podemos descartar o índice com o (_) underline


for valor in enumerate(nome):
    print(valor[0])  ---------->>> somente o índice.

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é: {soma}')

Tabela de emojis: https://apps.timwhitlock.info/emoji/tables/unicode


nome = "Geek University"
for letra in nome:
    print(letra, end='')
"""

# Original: U+1F60D
# Modificado: U0001F60D

emoji = 'U0001F60D'

for _ in range(3):
    for num in range(1, 11):
        print(f'\U0001F60D' * num)

# Original: U+1F605
# Modificado: U0001F605

for _ in range(3):
    for num in range(1, 11):
        print(f'\U0001F605' * num)

