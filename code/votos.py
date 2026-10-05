#contara e validara os votos
from code.candidatos import Gerenciador_candidatos


class Votes:
    def __init__(self, gerenciador : Gerenciador_candidatos, numero_digitado : str):
        self.gerenciador = gerenciador
        self.numero_digitado = str(numero_digitado)
        self.candidato_encontrado = None
        self.apuracao ={
            'Votos_candidatos' : {},
            'Branco' : 0,
            'Nulos' : 0
            }

    def valida_votes(self):
        self.candidato_encontrado = self.gerenciador.get_candidato(self.numero_digitado)

        if self.candidato_encontrado:
            print (f'Nome:' + self.candidato_encontrado.nome)
            print (f'numero:' + self.candidato_encontrado.numero)
            return self.candidato_encontrado
        else:
            print('Candidato não encontrado')
            return None

    def confirma_voto(self, numero_digitado: str, voto_branco: bool = False):

        if voto_branco:
            self.apuracao['Branco'] += 1
            print('Voto branco confirmado')
        else:
            candidato = self.valida_votes(numero_digitado)