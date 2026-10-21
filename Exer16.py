#Se o personagem está na  posição  X = 0  e o jogador aperta a "Seta Direita", 
# o personagem deve andar 5 passos. Desenhe ou escreva o algoritmo para essa ação. 



x = 0

tecla = input("Aperte a Seta Direita: ")
if tecla == "direita": 
    x = x + 5

print(f"Posição atual do personagem: {x} ")