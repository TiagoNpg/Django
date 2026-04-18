from votacao.models import Questao, Opcao
from django.utils import timezone

# def create_sample_question():
#  q = Questao.objects.create(questao_texto="Qual o teu clube favorito?",
#                             pub_data=timezone.now())
#  q.opcao_set.create(opcao_texto="Benfica", votos=3)
#  q.opcao_set.create(opcao_texto="Sporting", votos=5)
#  q.opcao_set.create(opcao_texto="Porto", votos=1)
#
# create_sample_question()

questoes = Questao.objects.filter(questao_texto__startswith="Qual")
print("Comecadas por 'Qual':", questoes)

questoes = Questao.objects.filter(questao_texto__contains="festa")
print ("Contendo 'festa':", questoes)

questoes = Questao.objects.filter(pub_data__year=timezone.now().year)
print("Publicadas este ano:", questoes)

questoes = Questao.objects.filter(pk=2)
print("Com chave primaria '2':", questoes)

opcoes = Opcao.objects.filter(questao__pub_data__year=timezone.now().year)
print("Opcoes das questoes publicadas este ano:", opcoes)

opcoes = Opcao.objects.filter(votos=0)
print("Opcoes com '0' votos:", opcoes)

opcoes = Opcao.objects.filter(votos=0).filter(opcao_texto__startswith="Nao")
print("Opcoes com '0' votos e que comecam por 'Nao':", opcoes)

opcoes = Opcao.objects.filter(votos=5).filter(questao__questao_texto__startswith="Qual")
print("Opcoes com '5' votos das questoes que comecam por 'Qual':", opcoes)