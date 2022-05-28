import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity':'pessoa', 
        'polymorphic_on':type
    }


class Usuario(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id', ondelete="CASCADE"), primary_key=True)
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))
    seriesFavoritas = db.relationship('SerieFavorita', backref='UsuarioSerie', lazy = True)
    TemporadaAssistida = db.relationship('TemporadaAssistida', backref='UsuarioTemporada', lazy = True)
    __mapper_args__ = { 
        'polymorphic_identity':'usuario'
    }

    def __str__(self):
        return f"Usuario('{self.nome}', '{self.email}')"

class InformacaoGeral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    dataLancamento = db.Column(db.Date)
    avaliacao = db.Column(db.Integer)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity':'informacao_geral',
        'polymorphic_on':type
    }

class Serie(InformacaoGeral):
    id = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id', ondelete="SET NULL"))


    __mapper_args__ = {
        'polymorphic_identity':'serie'
    }
    
    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_genero}')"

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    descricao = db.Column(db.String(254))

    def __str__(self):
        return f"Genero('{self.titulo}', '{self.descricao}')"



    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_genero}')"

class SerieFavorita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete="CASCADE"))
    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id', ondelete="CASCADE"))
    avaliacao = db.Column(db.Integer)

    def __str__(self):
        return f"Serie('{self.id_usuario}', '{self.id_serie}', '{self.avaliacao}')"

class Temporada(InformacaoGeral):
    id_temp = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id', ondelete="CASCADE"))
    qtdEpisodios = db.Column(db.Integer)
    # episodios = db.relationship('Episodio', backref='TemporadaEpisodios', lazy = True)
    
    __mapper_args__ = {
            'polymorphic_identity':'temporada'
        }

    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_serie}', '{self.qtdEpisodios}', '{self.episodios}')"

class TemporadaAssistida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporada.id_temp', ondelete="CASCADE"))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete="CASCADE"))
    qtdEpisodiosAssistidos = db.Column(db.Integer)

    def __str__(self):
        return f"Serie('{self.id_temporada}', '{self.id_usuario}', '{self.qtdEpisodiosAssistidos}')"

class Episodio(InformacaoGeral):
    id_episodio = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporada.id_temp', ondelete="CASCADE"))
    duracao = db.Column(db.Integer)

    __mapper_args__ = {
            'polymorphic_identity':'episodio'
        }

    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_temporada}', '{self.duracao}')"


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()

