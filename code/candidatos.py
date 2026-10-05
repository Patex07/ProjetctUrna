#cadastro dos candidatos
import os.path

class Candidatos:
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

class Gerenciador_candidatos:
    def __init__(self):
        self._candidatos = {}

    def add_candidato(self, numero:str, nome :str, cargo: str, foto:str):
        numero_str= str(numero)

        if numero_str in self._candidatos:
            print(f'Erro: Candidato com número {numero_str} já existe')
            return False

        if not os.path.exists(foto):
            print(f'O arquivo da foto {foto} nao foi encontrado')

        novo_candidato = Candidatos(numero, nome, cargo, foto)
        self._candidatos[numero_str] = novo_candidato
        print(f'O candidato {nome} - {numero} foi criado com sucesso')
        return True

    def get_candidato(self, numero:str) -> Candidatos | None :

        return self._candidatos.get(str(numero), None)

    def listar_todos(self):
        return list(self._candidatos.values())


