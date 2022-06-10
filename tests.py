# import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__)) 
# parentdir = os.path.dirname(currentdir) 
# sys.path.append(parentdir)

from datetime import date
from this import d
from Config.config import *
from Model.endereco import *
from Model.pessoa import Pessoa
from Model.usuario import Usuario
from Model.colaborador import Colaborador
from Model.informacao_geral import InformacaoGeral
from Model.serie import Serie
from Model.temporada import Temporada
from Model.episodio import Episodio
from Model.genero import Genero
from Model.serie_favorita import SerieFavorita
from Model.temporada_assistida import TemporadaAssistida
from Model.estudio import Estudio


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()

#endereco

endereco1 = Endereco(numero="345", logradouro="Rua 15 de novembro", bairro="centro", cep="12345678", estado="SC", pais="Brasil")
endereco2 = Endereco(numero="534", logradouro="Rua 7 de setembro", bairro="centro", cep="82354671", estado="SC", pais="Brasil")
endereco3 = Endereco(numero="345", logradouro="Rua 1 de janeiro", bairro="fidélis", cep="87654321", estado="SC", pais="Brasil")

db.session.add(endereco1)
db.session.add(endereco2)
db.session.add(endereco3)

db.session.commit()

#colaborador

dataNasc1 = date(2002,5,20)
dataNasc2 = date(2003,6,21) 
dataNasc3 = date(1990,12,24)
dataNasc4 = date(1995,4,10)
dataNasc5 = date(2001,7,15)
dataNasc6 = date(1998,3,27)

colaborador1 = Colaborador(cpf="12345678910", dataNascimento = dataNasc1, endereco_id = 1, nome="Bernardo dos Santos", salario=1500, turno="Vespertino")
colaborador2 = Colaborador(cpf="10987654321", dataNascimento = dataNasc2, endereco_id = 2, nome="Cleber de Oliveira", salario=1500, turno="Vespertino")
colaborador3 = Colaborador(cpf="24685973245", dataNascimento = dataNasc3, endereco_id = 3, nome="Ana dos Santos", salario=1500, turno="Vespertino")


db.session.add(colaborador1)
db.session.add(colaborador2)
db.session.add(colaborador3)

db.session.commit()

#usuario

usuario1 = Usuario(cpf="52478965438", dataNascimento = dataNasc4, endereco_id = 1, nome="Ana Maria",email="anamaria@gmail.com",senha="12345", login="anamaria", telefone="487569875")
usuario2 = Usuario(cpf="48756924536", dataNascimento = dataNasc5, endereco_id = 2, nome="Bernardo de Oliveira",email="bernardooliveira@gmail.com",senha="678", login="bernardoOliveira", telefone="423687259")
usuario3 = Usuario(cpf="57896542354", dataNascimento = dataNasc6, endereco_id = 3, nome="Cleber dos Santos",email="cleberdossantos@gmail.com",senha="91011", login="clebersantos", telefone="142987654")

db.session.add(usuario1)
db.session.add(usuario2)
db.session.add(usuario3)

db.session.commit()

#genero

genero1 = Genero(titulo="Comédia", descricao="Pretende provocar o riso dos espectadores") 
genero2 = Genero(titulo="Terror", descricao="Pretende provocar medo nos espectadores")
genero3 = Genero(titulo="Suspense", descricao="Pretende causar agitação e nervosismo nos espectadores")

db.session.add(genero1)
db.session.add(genero2)
db.session.add(genero3)

#serie

dataLancamento1 = date(1994,7,22)
dataLancamento2 = date(2021,7,24)
dataLancamento3 = date(2011,12,4)
dataLancamento4 = date(1994,7,22)
dataLancamento5 = date(2021,8,29)
dataLancamento6 = date(2012,1,15)
dataLancamento7 = date(1994,7,22)
dataLancamento8 = date(2021,9,15)
dataLancamento9 = date(2012,2,10)


serie1 = Serie(titulo="Friends", dataLancamento=dataLancamento1, avaliacao=8, id_genero=1)
serie2 = Serie(titulo="Midnight Mass", dataLancamento=dataLancamento2, avaliacao=10, id_genero=2)
serie3 = Serie(titulo="Black Mirror", dataLancamento=dataLancamento3, avaliacao=9, id_genero=3)

db.session.add(serie1)
db.session.add(serie2)
db.session.add(serie3)

db.session.commit()

#temporada

temporada1 = Temporada(titulo="Primeira Temporada", dataLancamento=dataLancamento4, avaliacao=7, id_serie=1, qtdEpisodios=10)
temporada2 = Temporada(titulo="Segunda Temporada", dataLancamento=dataLancamento5, avaliacao=6, id_serie=2, qtdEpisodios=15)
temporada3 = Temporada(titulo="Terceira Temporada", dataLancamento=dataLancamento6, avaliacao=9, id_serie=3, qtdEpisodios=11)

db.session.add(temporada1)
db.session.add(temporada2)
db.session.add(temporada3)

db.session.commit()

#episodio

episodio1 = Episodio(titulo="Episódio 1", dataLancamento=dataLancamento7, avaliacao=6, id_temporada=4, duracao=20)
episodio2 = Episodio(titulo="Episodio 2", dataLancamento=dataLancamento8, avaliacao=10, id_temporada=5, duracao=40)
episodio3 = Episodio(titulo="Episodio 3", dataLancamento=dataLancamento9, avaliacao=7, id_temporada=6, duracao=60)

db.session.add(episodio1)
db.session.add(episodio2)
db.session.add(episodio3)

db.session.commit()

#serie favorita

serieFavorita1 = SerieFavorita(id_usuario = "52478965438", id_serie = 1, avaliacao = 5)
serieFavorita2 = SerieFavorita(id_usuario = "48756924536", id_serie = 2, avaliacao = 4)
serieFavorita3 = SerieFavorita(id_usuario = "57896542354", id_serie = 3, avaliacao = 5)

db.session.add(serieFavorita1)
db.session.add(serieFavorita2)
db.session.add(serieFavorita3)

db.session.commit()

#temporada assistida

temporadaAssistida1 = TemporadaAssistida(id_usuario = "52478965438", id_temporada = 4, qtdEpisodiosAssistidos = 2)
temporadaAssistida2 = TemporadaAssistida(id_usuario = "48756924536", id_temporada = 5, qtdEpisodiosAssistidos = 2)
temporadaAssistida3 = TemporadaAssistida(id_usuario = "57896542354", id_temporada = 6, qtdEpisodiosAssistidos = 2)

db.session.add(temporadaAssistida1)
db.session.add(temporadaAssistida2)
db.session.add(temporadaAssistida3)

db.session.commit()

#estudio

estudio1 = Estudio(nome="Warner Bros", endereco_id = 1)
estudio2 = Estudio(nome="Sony", endereco_id = 2)
estudio3 = Estudio(nome="Fox", endereco_id = 3)

estudio1.series.append(serie1)
estudio2.series.append(serie2)
estudio3.series.append(serie3)

db.session.add(estudio1)
db.session.add(estudio2)
db.session.add(estudio3)

db.session.commit()

#estudioSerie'

