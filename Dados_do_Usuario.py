"""
Recebendo Dados do Usuário

input() -> Todo dado recebido via input é do tipo string
Em python, String é Tudo que estiver:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas Duplas triplas;

Exemplos:
- Aspas simples -> 'Balboa'
- Aspas duplas -> "Balboa"
- Aspas simples triplas -> '''Balboa'''

"""
#  Aspas duplas triplas -> """Balboa """

#  Entrada de dados
print("Qual seu nome?")
nome = input() # Input -> Entrada

# Exemplo de Print antigo 2.x
# print('Seja bem-vindo(a) %s' % nome)
# Exemplo de Print antigo 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

print(f'Seja bem-vindo(a) {nome}')

#print("Qual a sua idade?")
#idade = input() # Input -> Entrada

idade= int(input('Qual a sua idade?'))

#Processamento

# Saída de dados
# Exemplo de Print antigo 2.x
#print(' %s tem %s anos' % (nome,idade))
# Exemplo de Print antigo 3.x
#print(' {0} tem {1} anos' .format(nome,idade))

print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'A {nome} nasceu em {2020 - idade}')

Finalizando teste de edição com o Branch do Github!
