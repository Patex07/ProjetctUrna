from code.VoteRepository import VoteRepository
from code.candidatos import GerenciadorCandidatos
from code.screen import Screen
from code.votos import Votos

gerenciador = GerenciadorCandidatos()
sistema_votos = Votos(gerenciador)
repositorio = VoteRepository("apuracao_2026.json")

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


a = False
while not a:
    vote = input('\nDigite o número do voto (ou 11 para encerrar): ')

    if vote == '11':
        a = True
    else:
        # 2. Chamando o método a partir da instância (objeto) e capturando o retorno
        status = sistema_votos.confirma_voto(vote)
        print(f"--> Feedback da Urna: {status}")
        repositorio.salvar_votos(sistema_votos.apuracao)

# 3. Conferindo o resultado final da apuração
print("\n" + "=" * 30)
print("ENCERRANDO VOTAÇÃO - RESULTADOS")
print("=" * 30)

vencedores, total_votos = sistema_votos.obter_vencedor()

if vencedores:
    nomes = [candidato.nome for candidato in vencedores]
    print(f"Vencedor(es): {', '.join(nomes)}")
    print(f"Total de votos do vencedor: {total_votos}")
    print(f"Apuração completa: {sistema_votos.apuracao}")
else:
    print("Nenhum voto válido foi registrado.")

#urna = Screen()
#urna.run()

