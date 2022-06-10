from Model.imports import *

class SerieFavorita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cpf', ondelete="CASCADE"))
    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id', ondelete="CASCADE"))
    avaliacao = db.Column(db.Integer)

    def __str__(self):
        return f"Serie('{self.id_usuario}', '{self.id_serie}', '{self.avaliacao}')"