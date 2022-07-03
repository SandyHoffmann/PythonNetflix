from Model.imports import *

class TemporadaAssistida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_temporada = db.Column(db.Integer, db.ForeignKey('temporada.id_temp', ondelete="CASCADE"))
    id_usuario = db.Column(db.String(11), db.ForeignKey('usuario.cpf', ondelete="CASCADE"))
    qtdEpisodiosAssistidos = db.Column(db.Integer)
    usuario = db.relationship("Usuario", backref="temporada_assistida", lazy=True)

    def __str__(self):
        return f"Temporada Assistida(Quantidade de Episodios Assistidos: {self.qtdEpisodiosAssistidos})"