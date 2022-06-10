from Model.imports import *
from Model.informacao_geral import InformacaoGeral

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