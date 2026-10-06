from code.candidatos import GerenciadorCandidatos


class Votos:
    def __init__(self, gerenciador: 'GerenciadorCandidatos'):
        self.gerenciador = gerenciador
        self.apuracao = {"votos_candidatos": {}, "brancos": 0, "nulos": 0}

    def valida_voto(self, numero_digitado: str):
        """Busca e retorna o candidato pelo número recebido. Sem prints."""
        numero_str = str(numero_digitado)
        return self.gerenciador.get_candidato(numero_str)

    def confirma_voto(self, numero_digitado: str = "", voto_branco: bool = False):
        """Computa o voto final na apuração, retornando o status do voto."""
        if voto_branco:
            self.apuracao["brancos"] += 1
            return "BRANCO"

        candidato = self.valida_voto(numero_digitado)

        if candidato:
            num = candidato.numero
            self.apuracao["votos_candidatos"][num] = self.apuracao["votos_candidatos"].get(num, 0) + 1
            return f"VALIDO_{num}"
        else:
            self.apuracao["nulos"] += 1
            return "NULO"

    def obter_vencedor(self):
        """Retorna uma lista de vencedores (para lidar com empates) e o total de votos."""
        votos = self.apuracao["votos_candidatos"]

        if not votos:
            return [], 0  # Nenhum voto válido computado

        maior_voto = max(votos.values())

        # Encontra todos os números que têm a mesma quantidade de votos (trata empate)
        numeros_vencedores = [num for num, total in votos.items() if total == maior_voto]

        candidatos_vencedores = [self.gerenciador.get_candidato(n) for n in numeros_vencedores]

        return candidatos_vencedores, maior_voto