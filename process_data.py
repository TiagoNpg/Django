
from votacao.models import Questao, Opcao
from django.utils import timezone

#Assumindo lista_de_opcoes como {'opcao_texto': 'Opcao A', 'votos': 9}
def criar_questao(questaoTexto, lista_de_opcoes):
    q = Questao.objects.create(questao_texto=questaoTexto,
                               pub_data=timezone.now())
    for opcao in lista_de_opcoes:
        q.opcao_set.create(opcao_texto=opcao['opcao_texto'], votos= opcao['votos'])

def testCreateQuestao():
    criar_questao(questaoTexto='Qual a tua cor favorita?',
                            lista_de_opcoes=[{'opcao_texto': 'Verde', 'votos': 3},
                                             {'opcao_texto': 'Azul', 'votos': 5},
                                             {'opcao_texto': 'Vermelho', 'votos': 4},
                                             ])
    criar_questao(questaoTexto='Qual a tua comida favorita?',
                              lista_de_opcoes=[{'opcao_texto': 'Lasanha', 'votos': 43},
                                               {'opcao_texto': 'Pizza', 'votos': 55},
                                               {'opcao_texto': 'Bacalhau', 'votos': 14},])
    criar_questao(questaoTexto='Para que é usado o Django?',
                    lista_de_opcoes=[{'opcao_texto': 'Desenvolvimento Web', 'votos': 100},
                                     {'opcao_texto': 'Desenvolvimento de Jogos', 'votos': 15},
                                     {'opcao_texto': 'Desenvolvimento de Apps', 'votos': 35}])
    criar_questao(questaoTexto='O que é o React?',lista_de_opcoes=[{'opcao_texto':'Framework de Javascript', 'votos': 52},
                                                                     {'opcao_texto':'Framework de CSS', 'votos': 51},
                                                                     {'opcao_texto':'Linguagem de Programação', 'votos': 45},])
    q = Questao.objects.filter(questao_texto__startswith="Qual")
    print("Comecadas por 'Qual':", q)
    q = Questao.objects.filter(questao_texto__contains="Django")
    print("Contendo 'Django':", q)
    q = Questao.objects.filter(questao_texto__contains="React")
    print("Contendo 'React':", q)

testCreateQuestao()

def apagar_todas_questoes():
    Questao.objects.all().delete()
    print("Todas as questões e respetivas opções foram apagadas da Base de Dados.")

def mostrar_questao(questao):
    print(f"\nQuestão: {questao.questao_texto}")
    opcoes = questao.opcao_set.all()
    for opcao in opcoes:
        print(f"  - {opcao.opcao_texto}: {opcao.votos} votos")

def mostrar_todas_questoes():
    questoes = Questao.objects.all()
    for questao in questoes:
        mostrar_questao(questao)

def mostrar_questoes_por_prefixo(prefixo):
    questoes = Questao.objects.filter(questao_texto__startswith=prefixo)
    for questao in questoes:
        mostrar_questao(questao)

def mostrar_mais_votada(questao):
    print(f"\nQuestão: {questao.questao_texto}")
    opcoes = questao.opcao_set.all()
    
    if not opcoes:
        print("  (Sem opções registadas)")
        return

    max_votos = max(opcao.votos for opcao in opcoes)
    
    opcoes_vencedoras = [opcao for opcao in opcoes if opcao.votos == max_votos]
    
    for opcao in opcoes_vencedoras:
        print(f"  🏆 Vencedora: {opcao.opcao_texto} com {opcao.votos} votos")

def testar_mais_votadas():
    questoes = Questao.objects.all()
    for questao in questoes:
        mostrar_mais_votada(questao)

def total_de_votos_global():
    total = 0
    for opcao in Opcao.objects.all():
        total += opcao.votos
        
    print(f"Total de votos contabilizados em toda a BD: {total}")
    return total

testCreateQuestao()
if __name__ == "__main__":
    mostrar_todas_questoes()
    
    mostrar_questoes_por_prefixo("Qual")
    
    testar_mais_votadas()
    
    total_de_votos_global()