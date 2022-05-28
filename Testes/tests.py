import os, sys

from sqlalchemy import null
currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)


from datetime import date
from Model.model import *
from Config.config import *

usuario1 = Usuario(nome="Ana Maria",email="anamaria@gmail.com",senha="12345")
usuario2 = Usuario(nome="Bernardo de Oliveira",email="bernardooliveira@gmail.com",senha="678")
usuario3 = Usuario(nome="Cleber dos Santos",email="cleberdossantos@gmail.com",senha="91011")

db.session.add(usuario1)
db.session.add(usuario2)
db.session.add(usuario3)

db.session.commit()

usuarios = Usuario.query.all()

for user in usuarios:
    print(f'Usuario = {user}')

genero1 = Genero(titulo="Comédia", descricao="Pretende provocar o riso dos espectadores") 
genero2 = Genero(titulo="Terror", descricao="Pretende provocar medo nos espectadores")
genero3 = Genero(titulo="Suspense", descricao="Pretende causar agitação e nervosismo nos espectadores")

db.session.add(genero1)
db.session.add(genero2)
db.session.add(genero3)

dataAtual = date.today()

serie1 = Serie(titulo="Friends", dataLancamento=dataAtual, avaliacao=8, id_genero=1)
serie2 = Serie(titulo="Midnight Mass", dataLancamento=dataAtual, avaliacao=10, id_genero=2)
serie3 = Serie(titulo="Black Mirror", dataLancamento=dataAtual, avaliacao=9, id_genero=3)

db.session.add(serie1)
db.session.add(serie2)
db.session.add(serie3)

db.session.commit()

temporada1 = Temporada(titulo="Primeira Temporada", dataLancamento=dataAtual, avaliacao=7, id_serie=1, qtdEpisodios=10)
temporada2 = Temporada(titulo="Segunda Temporada", dataLancamento=dataAtual, avaliacao=6, id_serie=2, qtdEpisodios=15)
temporada3 = Temporada(titulo="Terceira Temporada", dataLancamento=dataAtual, avaliacao=9, id_serie=3, qtdEpisodios=11)

db.session.add(temporada1)
db.session.add(temporada2)
db.session.add(temporada3)

db.session.commit()

episodio1 = Episodio(titulo="Episódio 1", dataLancamento=dataAtual, avaliacao=6, id_temporada=4, duracao=20)
episodio2 = Episodio(titulo="Episodio 2", dataLancamento=dataAtual, avaliacao=10, id_temporada=5, duracao=40)
episodio3 = Episodio(titulo="Episodio 3", dataLancamento=dataAtual, avaliacao=7, id_temporada=6, duracao=60)

db.session.add(episodio1)
db.session.add(episodio2)
db.session.add(episodio3)

db.session.commit()

# Pessoa.query.filter(Pessoa.id == 1).delete()

series = Serie.query.all()

for serie in series:
    print(f'Serie = {serie}')

serieFavorita1 = SerieFavorita(id_usuario = 1, id_serie = 1, avaliacao = 5)
serieFavorita2 = SerieFavorita(id_usuario = 1, id_serie = 2, avaliacao = 4)
serieFavorita3 = SerieFavorita(id_usuario = 2, id_serie = 3, avaliacao = 5)

db.session.add(serieFavorita1)
db.session.add(serieFavorita2)
db.session.add(serieFavorita3)

db.session.commit()

seriesFavoritas = SerieFavorita.query.all()

for serie in seriesFavoritas:
    print(f'Serie Favorita= {serie}')

temporadaAssistida1 = TemporadaAssistida(id_usuario = 1, id_temporada = 4, qtdEpisodiosAssistidos = 2)
temporadaAssistida2 = TemporadaAssistida(id_usuario = 1, id_temporada = 5, qtdEpisodiosAssistidos = 2)
temporadaAssistida3 = TemporadaAssistida(id_usuario = 2, id_temporada = 6, qtdEpisodiosAssistidos = 2)

db.session.add(temporadaAssistida1)
db.session.add(temporadaAssistida2)
db.session.add(temporadaAssistida3)

db.session.commit()

temporadasAssistidas = TemporadaAssistida.query.all()

for temp in temporadasAssistidas:
    print(f'Temporada Assistida= {temp}')




