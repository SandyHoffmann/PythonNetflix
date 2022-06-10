from Model.imports import *
from Model.endereco import Endereco

class Pessoa(db.Model):

    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dataNascimento = db.Column(db.Date(), nullable=False)
    endereco_id = db.Column(db.Integer, db.ForeignKey(Endereco.id))
    endereco = db.relationship("Endereco", backref="pessoa", lazy=True)

     # atributo necessário para armazenar tipo de classe especializada (discriminador)
    type = db.Column(db.String(50))

     # definições de mapeamento da classe mãe
    __mapper_args__ = {
        'polymorphic_identity':'pessoa', 
        'polymorphic_on':type # nome do campo que vincula os filhos
    }

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return f"{self.cpf}, {self.nome}, {self.dataNascimento}"
