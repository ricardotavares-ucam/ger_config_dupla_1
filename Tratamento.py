class Tratamento:
    def _init_(self, data_ini, data_fim ):
        self.data_ini = data_ini
        self.data_fim = data_fim

    def settratamento(self,data_ini, data_fim ):
        self.data_ini = data_ini
        self.data_fim = data_fim
        
    def gettratamento(self, data_ini):
        return self.data_ini, self.data_fim
    