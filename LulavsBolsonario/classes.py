
class Pernsonagens:
    def __init__(self,vida):
        self.vida = vida
    
    def getvida(self):
        return self.vida

    def setvida(self, x, y):
        if y  == "somar":
            if self.vida <= 41:
                self.vida = self.vida + x
            else:
                print("Vida cheia")
        elif y == "subtrair":
            self.vida = self.vida - x
    

    def esquivar(self):
        print(f"Você esquivou do ataque")

    def atacar(self, nome):
        print("POW POW POW - Você deu um soco!")
        nome.setvida(2, "subtrair")


class Lula(Pernsonagens):
    def amizade(self):
        print("VAMOS JUNTOS COMPANHEIROS!!! - Juntos vocês espancaram Bolsonaro")
        bolsonaro.setvida(5,"subtrair")

    def Picanhaecervejinha(self):
        print("É ISSO QUE O POVO QUER!! INHAMI INHAMI INHAMI - Lula come sua picanha e cerveja, recuperando sua vida")
        bolsonaro.setvida(4,"somar")

    def AjudaLGBTQIAPN(self):
        print("VAMOS JUNTES GAYS!! - Vocês todes ajudaram Lula, dando um golpe forte em Bolsonaro  ")
        bolsonaro.setvida(4, "subtrair")

class Bolsonaro(Pernsonagens):

    def Facadanoestomago(self):
        print("OLHA A FACA - Lula levou uma facada e está sangrando")
        lula.setvida(5,"subtrair")

    def Tossedacovid(self):
        print("COF COF COF - Lula se infectou")
        lula.setvida(5,"subtrair")

    def Tomacloroquina(self):
        print("VACINA JAMAIS, VIVA A CLOROQUINA - Bolsonaro virá jacaré e te morde")
        lula.setvida(5,"subtrair" )

lula = Lula(45)
bolsonaro = Bolsonaro(45)