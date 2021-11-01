class Consulta:
    def _init_(self, data_con, historico ):
        self.data_con = data_con
        self.historico = historico

    def setconsulta(self,data_con, historico ):
        self.data_con = data_con
        self.historico = historico
        
    def getconsulta(self, data_con):
        return self.data_con, self.historico
    