from config import *


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity':'pessoa', 
        'polymorphic_on':type
    }


class Usuario(Pessoa):
    id = db.Column(db.Integer, db.ForeignKey('pessoa.id',ondelete="CASCADE"), primary_key=True)
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))
    
    __mapper_args__ = { 
        'polymorphic_identity':'usuario',
    }

    def __str__(self):
        return f"Usuario('{self.nome}', '{self.email}')"

if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

# @event.listens_for(Engine, "connect")
# def set_sqlite_pragma(dbapi_connection, connection_record):
#     cursor = dbapi_connection.cursor()
#     cursor.execute("PRAGMA foreign_keys=ON")
#     cursor.close()

db.create_all()

usuario = Usuario(nome="Ana",email="a@a.com",senha="3444")
print(usuario)

db.session.add(usuario)
db.session.commit()

Usuario.query.filter(Usuario.id == usuario.id).delete()

db.session.commit()

