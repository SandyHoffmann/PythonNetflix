from Model.imports import *
from Model.informacao_geral import InformacaoGeral

class Episodio(InformacaoGeral):
    id_episodio = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporada.id_temp', ondelete="CASCADE"))
    duracao = db.Column(db.Integer)

    __mapper_args__ = {
            'polymorphic_identity':'episodio'
        }

    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_temporada}', '{self.duracao}')"