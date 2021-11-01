class Veterinario:
    def _init_(self, nome_vet, end_vet, tel_vet):
        self.nome_vet = nome_vet
        self.end_vet = end_vet
        self.tel_vet = tel_vet

    def setveterinario(self,nome_vet, end_vet, tel_vet):
        self.nome_vet = nome_vet
        self.end_vet = end_vet
        self.tel_vet = tel_vet

    def getveterinario(self, nome_vet):
        return self.nome_vet, self.end_vet, self.tel_vet