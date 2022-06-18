from Model.imports import *
from Model.informacao_geral import InformacaoGeral

class Temporada(InformacaoGeral):
    id_temp = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id', ondelete="CASCADE"))
    qtdEpisodios = db.Column(db.Integer)
    
    __mapper_args__ = {
            'polymorphic_identity':'temporada'
        }

    def __str__(self):
        return f"Temporada(Título: {self.titulo}, Data de Lançamento: {self.dataLancamento}, Avaliação: {self.avaliacao}, Quantidade de Episódios: {self.qtdEpisodios})"