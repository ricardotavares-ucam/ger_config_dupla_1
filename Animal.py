class Animal:
    def _init_(self, nome_animal, idade, sexo ):
        self.nome_animal = nome_animal
        self.idade = idade
        self.sexo = sexo

    def setnome_animal(self,nome_animal):
        self.nome_animal = nome_animal
    def setidade(self,idade):
        self.idade = idade
    def setsexo(self,sexo):
        self.sexo = sexo
    
    def getnome(self,nome_animal):
        return self.nome_animal
    def getidade(self,idade):
        return self.idade = idade
    def getsexo(self,sexo):
        return self.sexo = sexo