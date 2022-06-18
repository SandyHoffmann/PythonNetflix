from Config.config import *

class Endereco (db.Model):

    '''
    Uma classe que representa o endereco da pessoa.
    ...
    Atributos
    ----------
    id (int):  id numérico do endereco (PK)
    numero (str): numero da residencia
    logradouro (str): logradouro da residencia
    cep (str): cep da residencia
    bairro (str): bairro da residencia
    estado (str): estado da residencia
    pais (str): pais da residencia

    Metodos
    -------
    '''

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(254))
    logradouro = db.Column(db.String(254))
    bairro = db.Column(db.String(254))
    cep = db.Column(db.String(254))
    estado = db.Column(db.String(254))
    pais = db.Column(db.String(254))

    # método para expressar o endereco em forma de texto
    def __str__(self):
        return f'Endereço: {self.numero}, {self.logradouro}, '+\
               f'{self.bairro}, CEP: {self.cep}, '+\
               f'{self.estado}, {self.pais}'

    #endereco

if (__name__ == "__main__"):

    endereco1 = Endereco(numero="345", logradouro="Rua 15 de novembro", bairro="centro", cep="12345678", estado="SC", pais="Brasil")
    endereco2 = Endereco(numero="534", logradouro="Rua 7 de setembro", bairro="centro", cep="82354671", estado="SC", pais="Brasil")
    endereco3 = Endereco(numero="345", logradouro="Rua 1 de janeiro", bairro="fidélis", cep="87654321", estado="SC", pais="Brasil")

    db.session.add(endereco1)
    db.session.add(endereco2)
    db.session.add(endereco3)

    db.session.commit()