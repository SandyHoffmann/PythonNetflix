from Model.imports import *

class TemporadaAssistida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporada.id_temp', ondelete="CASCADE"))
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.cpf', ondelete="CASCADE"))
    qtdEpisodiosAssistidos = db.Column(db.Integer)

    def __str__(self):
        return f"Serie('{self.id_temporada}', '{self.id_usuario}', '{self.qtdEpisodiosAssistidos}')"