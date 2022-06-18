import pytest

import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)


from Model.imports import *
from datetime import date

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
from Model.endereco import Endereco

def restartBd():
    if os.path.exists(arquivobd): 
        os.remove(arquivobd) 
    db.create_all()

def test_endereco():
    restartBd()

    endereco1 = Endereco(numero="345", logradouro="Rua 15 de novembro", bairro="centro", cep="12345678", estado="SC", pais="Brasil")

    db.session.add(endereco1)

    db.session.commit()

    assert endereco1.numero == "345"


def test_usuario():
    dataNasc4 = date(1995,4,10)
    usuario1 = Usuario(cpf="1231231231", dataNascimento = dataNasc4, endereco_id = 1, nome="Ana Maria",email="anamaria@gmail.com",senha="12345", login="anamaria", telefone="487569875")
    db.session.add(usuario1)
    db.session.commit()

    assert usuario1.nome == "Ana Maria"

def test_colaborador():
    dataNascColab = date(2002,5,20)
    enderecoColab = Endereco(numero="345", logradouro="Rua 15 de novembro", bairro="centro", cep="12345678", estado="SC", pais="Brasil")
    db.session.add(enderecoColab)
    db.session.commit()
    colaborador1 = Colaborador(cpf="12345678910", dataNascimento = dataNascColab, endereco_id = 1, nome="Bernardo dos Santos", salario=1500, turno="Vespertino")
    db.session.add(colaborador1)
    db.session.commit()

    assert colaborador1.nome == "Bernardo dos Santos"   

def test_genero():
    genero = Genero(titulo="Ação", descricao="Ação é um gênero de filmes e séries de televisão que envolve ações de personagens.")
    db.session.add(genero)
    db.session.commit()
    assert genero.titulo == "Ação"

def test_serie():
    serie = Serie(titulo="Game of Thrones",  id_genero=1, id_colaborador="12345678910")
    db.session.add(serie)
    db.session.commit()
    assert serie.titulo == "Game of Thrones"

def test_temporada():
    dataAtual = date.today()
    temporada = Temporada(titulo="Primeira Temporada", dataLancamento=dataAtual, avaliacao=7, id_serie=1, qtdEpisodios=10)
    db.session.add(temporada)
    db.session.commit()
    print(temporada.id)
    assert temporada.id == 2

def test_temporada_assistida():
    temporadaAssistida = TemporadaAssistida(id_usuario = "1231231231", id_temporada = 2, qtdEpisodiosAssistidos = 2)
    db.session.add(temporadaAssistida)
    db.session.commit()
    assert temporadaAssistida.id_usuario == 1231231231

def test_serie_favorita():
    serieFavorita = SerieFavorita(id_usuario = "1231231231", id_serie = 1, avaliacao = 5)
    db.session.add(serieFavorita)
    db.session.commit()
    assert serieFavorita.id_usuario == 1231231231

def test_estudio():
    estudio = Estudio(nome = "Warner Bros", endereco_id = 1)
    db.session.add(estudio)
    db.session.commit()
    assert estudio.nome == "Warner Bros"

def test_estudio_serie():
    serie = Serie(titulo="Game of Thrones", id_genero=1, id_colaborador="12345678910")
    db.session.add(serie)
    db.session.commit()
    estudio = Estudio(nome = "Warner Bros", endereco_id = 1)
    db.session.add(estudio)
    db.session.commit()
    estudio.series.append(serie)
    db.session.commit()
    assert estudio.series[0].titulo == "Game of Thrones"

def test_episodio():
    dataAtual = date.today()
    episodio = Episodio(titulo="Episódio 1", dataLancamento=dataAtual, avaliacao=6, id_temporada=2, duracao=20)
    db.session.add(episodio)
    db.session.commit()
    assert episodio.titulo == "Episódio 1"