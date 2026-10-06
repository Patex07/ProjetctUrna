import json
import os
from code.votos import Votos


class VoteRepository:
    def __init__(self, caminho_arquivo: str = "dados_votos.json"):
        """Define o arquivo alvo e o cria se não existir."""
        self.arquivo = caminho_arquivo
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        """(Create inicial) Cria o arquivo JSON com a estrutura zerada caso não exista."""
        if not os.path.exists(self.arquivo):
            self.limpar_dados()

    def ler_votos(self) -> dict:
        """(Read) Lê e retorna os dados de apuração salvos no JSON."""
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Prevenção caso o arquivo seja corrompido
            return {"votos_candidatos": {}, "brancos": 0, "nulos": 0}

    def salvar_votos(self, votos_atuais: dict):
        """(Create / Update) Sobrescreve o arquivo JSON com o dicionário de apuração atualizado."""
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(votos_atuais, f, indent=4)

    def somar_voto_incremental(self, numero_candidato: str = None, tipo: str = "valido"):
        """
        (Update Específico) Lê o JSON atual, soma +1 num candidato/nulo/branco e salva.
        Útil se você quiser salvar a cada voto digitado sem manter tudo na memória.
        """
        dados = self.ler_votos()

        if tipo == "branco":
            dados["brancos"] += 1
        elif tipo == "nulo":
            dados["nulos"] += 1
        elif tipo == "valido" and numero_candidato:
            dados["votos_candidatos"][numero_candidato] = dados["votos_candidatos"].get(numero_candidato, 0) + 1

        self.salvar_votos(dados)

    def limpar_dados(self):
        """(Delete) Reseta todos os dados do JSON, reiniciando a eleição."""
        dados_zerados = {"votos_candidatos": {}, "brancos": 0, "nulos": 0}
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_zerados, f, indent=4)