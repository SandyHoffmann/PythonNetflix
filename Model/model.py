from imports import *
from endereco import Endereco
from pessoa import Pessoa
from usuario import Usuario
from colaborador import Colaborador
from informacao_geral import InformacaoGeral
from serie import Serie
from temporada import Temporada
from episodio import Episodio
from genero import Genero
from serie_favorita import SerieFavorita
from temporada_assistida import TemporadaAssistida
from estudio import Estudio

if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()

