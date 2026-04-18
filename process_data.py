
from votacao.models import Questao, Opcao
from django.utils import timezone

#Assumindo lista_de_opcoes como {'opcao_texto': 'Opcao A', 'votos': 9}
def create_question(questaoTexto, lista_de_opcoes):
    q = Questao.objects.create(questao_texto=questaoTexto,
                               pub_data=timezone.now())
    for opcao in lista_de_opcoes:
        q.opcao_set.create(opcao_texto=opcao['opcao_texto'], votos= opcao['votos'])

def testCreateQuestao():
    create_question(questaoTexto='Qual a tua cor favorita?',
                            lista_de_opcoes=[{'opcao_texto': 'Verde', 'votos': 3},
                                             {'opcao_texto': 'Azul', 'votos': 5},
                                             {'opcao_texto': 'Vermelho', 'votos': 4},
                                             ])
    create_question(questaoTexto='Qual a tua comida favorita?',
                              lista_de_opcoes=[{'opcao_texto': 'Lasanha', 'votos': 43},
                                               {'opcao_texto': 'Pizza', 'votos': 55},
                                               {'opcao_texto': 'Bacalhau', 'votos': 14},])
    create_question(questaoTexto='Para que é usado o Django?',
                    lista_de_opcoes=[{'opcao_texto': 'Desenvolvimento Web', 'votos': 100},
                                     {'opcao_texto': 'Desenvolvimento de Jogos', 'votos': 15},
                                     {'opcao_texto': 'Desenvolvimento de Apps', 'votos': 35}])
    create_question(questaoTexto='O que é o React?',lista_de_opcoes=[{'opcao_texto':'Framework de Javascript', 'votos': 52},
                                                                     {'opcao_texto':'Framework de CSS', 'votos': 51},
                                                                     {'opcao_texto':'Linguagem de Programação', 'votos': 45},])
    q = Questao.objects.filter(questao_texto__startswith="Qual")
    print("Comecadas por 'Qual':", q)
    q = Questao.objects.filter(questao_texto__contains="Django")
    print("Contendo 'Django':", q)
    q = Questao.objects.filter(questao_texto__contains="React")
    print("Contendo 'React':", q)

testCreateQuestao()