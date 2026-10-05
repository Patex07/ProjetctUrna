from code.candidatos import Gerenciador_candidatos
from code.screen import Screen
from code.votos import Votes

gerenciador = Gerenciador_candidatos()

gerenciador.add_candidato(
    numero = '71',
    nome = 'Manchinha',
    cargo = 'Presidente',
    foto = 'tste1'
)
gerenciador.add_candidato(
    numero = '84',
    nome = 'Osvaldinho',
    cargo = 'Presidente',
    foto = 'tste2'
)

vote = '71'

votacao = Votes(gerenciador = gerenciador, numero_digitado= vote )
votacao.valida_votes()

urna = Screen()
urna.run()