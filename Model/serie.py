from Model.imports import *
from Model.informacao_geral import InformacaoGeral

class Serie(InformacaoGeral):
    id = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id', ondelete="SET NULL"))


    __mapper_args__ = {
        'polymorphic_identity':'serie'
    }
    
    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_genero}')"