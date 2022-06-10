from Model.imports import *

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