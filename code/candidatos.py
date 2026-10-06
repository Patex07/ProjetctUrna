#cadastro dos candidatos
import os.path
from dataclasses import dataclass

# Usar dataclass limpa o código e cria um __init__ e um __repr__ automáticos
@dataclass
class Candidato:
    numero: str
    nome: str
    cargo: str
    foto: str

    def __post_init__(self):
        # Padronização na criação
        self.nome = self.nome.upper()
        self.cargo = self.cargo.upper()

    def to_dict(self):
        return {
            "numero": self.numero,
            "nome": self.nome,
            "cargo": self.cargo,
            "foto": self.foto
        }

class GerenciadorCandidatos:
    def __init__(self):
        self._candidatos = {}

    def add_candidato(self, numero: str, nome: str, cargo: str, foto: str) -> bool:
        numero_str = str(numero)

        if numero_str in self._candidatos:
            raise ValueError(f"Erro: Candidato com número {numero_str} já existe.")

        if not os.path.exists(foto):
            # Agora ele bloqueia a criação se a foto não existir
            raise FileNotFoundError(f"O arquivo da foto '{foto}' não foi encontrado.")

        novo_candidato = Candidato(numero_str, nome, cargo, foto)
        self._candidatos[numero_str] = novo_candidato
        return True

    def get_candidato(self, numero: str) -> Candidato | None:
        return self._candidatos.get(str(numero))

    def listar_todos(self) -> list[Candidato]:
        return list(self._candidatos.values())