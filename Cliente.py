class Cliente:
    def _init_(self, nome, cpf, endereco, telefone, email ):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def setnome(self,nome):
        self.nome = nome
    def setcpf(self,cpf):
        self.cpf = cpf
    def setendereco(self,endereco):
        self.endereco = endereco
    def settelefone(self,telefone):
        self.telefone = telefone
    def setemail(self,email):
        self.email = email
        
    def getnome(self,nome):
        return self.nome
    def getcpf(self,cpf):
        return self.cpf
    def getendereco(self,endereco):
        return self.endereco
    def gettelefone(self,telefone):
        return self.telefone
    def getemail(self,email):
        return self.email