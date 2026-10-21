#Crie um algoritmo completo em Python que: 
# 1.  Peça o nome do jogador. 
# 2.  Peça o nível atual do jogador. 
# 3.  Calcule o próximo nível (Nível + 1). 
# 4.  Exiba uma mensagem motivadora: "Parabéns [Nome], seu próximo objetivo é o nível [Nível + 1]!". 
#pn: proximo nível




jogador = input("Digite o nome do seu jogador: ")
nivel = int(input("Digite o nível do seu jogador: "))

pn = int(nivel) + 1

print(f"Parabéns {jogador}, seu próximo objetivo é o nível {pn}!")