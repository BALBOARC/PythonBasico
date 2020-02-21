"""
Loop while

Forma geral

while expressão_booleana:
    //execução do loop

o bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana é toda expressão onde o resultado é verdadeiro ou falso.

ex:
num = 5
num < 5 (false)
num <10 (true)

# Exemplo 1:

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

# obs: Em um loop while é importante que cuidemos do critério de parada para não causar loop infinito.

"""
# Exemplo 2:

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')
    
"""
# C OU JAVA

while(expressão){
    //execução
}

# do while (C ou Java)

do {
    //execução
}while(expressão);

"""
