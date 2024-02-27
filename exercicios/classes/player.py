import random

class Player():
    def __init__(self, vida, dano) -> None:
        self.vida = vida
        self.dano = dano
    def atacar(self, chance_critico_min, chance_critico_max):
        chance_critico = random.randint(chance_critico_min, chance_critico_max)
        dano_critico = random.randint(6, 15)
        if chance_critico == chance_critico_max:
            print('Ataque Crítico! o alvo recebeu {} de dano!'.format(dano_critico))
        else:
            print('Ataque realizado, o alvo recebeu {} de dano!'.format(self.dano))

player1 = Player(10, 5)
player1.atacar(1, 4) # 25% chance de critico