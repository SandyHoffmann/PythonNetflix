from Model.imports import *

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    descricao = db.Column(db.String(254))

    def __str__(self):
        return f"Genero('{self.titulo}', '{self.descricao}')"



    def __str__(self):
        return f"Serie('{self.titulo}', '{self.dataLancamento}', '{self.avaliacao}', '{self.id_genero}')"