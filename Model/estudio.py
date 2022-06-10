from Model.imports import *
from Model.endereco import Endereco
from Model.serie import Serie

class Estudio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    endereco_id = db.Column(db.Integer, db.ForeignKey(Endereco.id))
    endereco = db.relationship("Endereco", backref="estudio", lazy=True)
    series = db.relationship("Serie", secondary="estudio_serie")

    def __str__(self):
        return f"Estudio('{self.nome}', '{self.endereco})"


series = db.Table('estudio_serie', db.metadata,
    db.Column('id_estudio', db.Integer, db.ForeignKey(Estudio.id)),
    db.Column('id_serie', db.Integer, db.ForeignKey(Serie.id))
)