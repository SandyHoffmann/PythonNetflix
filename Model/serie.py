from Model.imports import *
from Model.informacao_geral import InformacaoGeral
from Model.usuario import Usuario
from Model.temporada import Temporada
from Model.episodio import Episodio
from Model.temporada_assistida import TemporadaAssistida
from Model.serie_favorita import SerieFavorita

#https://github.com/hvescovi/dw2ed/blob/main/sup/python/merge_json_OO.py

class Serie(InformacaoGeral):
    id = db.Column(db.Integer, db.ForeignKey('informacao_geral.id', ondelete="CASCADE"), primary_key=True)
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id', ondelete="SET NULL"))
    genero = db.relationship("Genero", backref="serie", lazy=True)
    id_colaborador = db.Column(db.String, db.ForeignKey('colaborador.cpf', ondelete="SET NULL"))
    colaborador = db.relationship("Colaborador", backref="serie", lazy=True)

    __mapper_args__ = {
        'polymorphic_identity':'serie'
    }
    
    def __str__(self):
        return f"Serie(Título: {self.titulo}, Data de Lançamento: {self.dataLancamento}, Avaliação: {self.avaliacao})"

    def json(self):
        return {
            "id" : self.id,
            "titulo": self.titulo,
            "genero" : self.genero.json(),
            "colaborador": self.colaborador.json()
        }

    def relatorioSerie(self):
        print("---------------------------------------------------------------------------------------------" +
        "---------------------------------------")
        print("|", self)
        print("|", self.genero)
        print("|", self.colaborador)
        temporadas = db.session.query(Temporada).filter_by(id_serie=self.id).all()
        for temp in temporadas:
            print("|", temp)
            episodios = db.session.query(Episodio).filter_by(id_temporada=temp.id).all()
            for epis in episodios:
                print("| - " , epis)
            temporadasAssistidas = db.session.query(TemporadaAssistida).filter_by(id_temporada=temp.id).all()
            #print("| - - - - - - - - - - - - - - - ")
            for tempAssist in temporadasAssistidas:
                print("| - ", tempAssist)
                print("| - - - ", tempAssist.usuario)
                serieFavorita = db.session.query(SerieFavorita).filter_by(id_usuario=tempAssist.usuario.cpf).all()
                for serieFav in serieFavorita:
                    print("| - - - - - ", serieFav)
        print("---------------------------------------------------------------------------------------------" +
        "---------------------------------------" )      

    def addSerieFavorita(self,idUsuario):
        try:
            print(self.id)
            print(idUsuario)
            # usuario = db.query(Usuario).get(idUsuario)
            # print(usuario)

        except: 
           print("Algo deu errado!")
