from code.candidatos import Gerenciador_candidatos
from code.screen import Screen

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


urna = Screen()
urna.run()