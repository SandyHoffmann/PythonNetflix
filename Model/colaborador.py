import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from Config.config import *
from Model.model import Pessoa

"""
Return que depende da classe Pessoa

return f"Colaborador('{self.nome}', '{self.cpf}', '{self.dtnasc}', '{self.salario}', '{self.turno}')"
"""

class Colaborador(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id', ondelete="CASCADE"), primary_key=True)
    salario = db.Column(db.Integer)
    turno = db.Column(db.String(254))
    
    __mapper_args__ = { 
        'polymorphic_identity':'colaborador'
    }

    """
    return que está utilizando a classe pessoa do Model.model
    """

    def __str__(self):
        return f"Colaborador('{self.nome}', '{self.salario}', '{self.turno}')"
