from random import randint

class Roll:
    def __init__(self,qtd,faces,bonus=0):
        self.qtd = qtd
        self.faces = faces
        self.bonus = bonus
        self.rolls = []
    
    def roll(self):
        for _ in range(self.qtd):
            self.rolls.append(int(randint(1,self.faces)))

            if self.bonus < 0:
                print(f"{self.rolls}{self.bonus} = {sum(self.rolls) + self.bonus}")
            elif self.bonus > 0:
                print(f"{self.rolls} + {self.bonus} = {sum(self.rolls) + self.bonus}")
            else:
                print(f"{self.rolls} = {sum(self.rolls)}")

def get_dados(comando):
    try:
        loc_d = comando.find("d")
        if loc_d == -1:
            raise Exception("dados errados")
        
        loc_s = comando.find("+")
        if loc_s == -1:
            loc_s = comando.find("-")
        
        bonus = 0
        if loc_s != -1:
            faces = int(comando[loc_d+1:loc_s])
            bonus = int(comando[loc_s:])
        else:
            faces = int(comando[loc_d+1:])

        qtd = 1
        if comando[0] != "d":
            qtd = int(comando[:loc_d])
        return (qtd,faces,bonus)
        
    except Exception as e:
        print(f"Error: {e}" )
        return None
    
while True:
    comando = input("Roll:")    
    if comando == "":
         print("obrigado por jogar!") 
         break
        
    result = get_dados(comando)
    if result == None:
        continue

    (qtd,faces,bonus) = result
    rolling = Roll(qtd,faces,bonus)