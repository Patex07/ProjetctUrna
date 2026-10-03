#cadastro dos candidatos

class candidatos:
    def __init__(self, numero:str, nome :str, cargo: str, foto:str):
        self.numero = str(numero)
        self.nome = nome.upper()
        self.cargo = cargo.upper()
        self.foto =  foto

    def to_dict(self):
        return {
            "numero": self.numero,
            "nome": self.nome,
            "cargo": self.cargo,
            "foto": self.foto
        }

class gerenciador_candidatos:
    def __init__(self):
        self._candidatos = {}

    def add_candidato(self, numero:str, nome :str, cargo: str, foto:str):
        numero_str= str(numero)

        if numero_str in self._candidatos:
            print()

