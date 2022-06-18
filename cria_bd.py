# import os, sys

# currentdir = os.path.dirname(os.path.realpath(__file__)) 
# parentdir = os.path.dirname(currentdir) 
# sys.path.append(parentdir)

from datetime import date
from this import d
from Config.config import *
from Model.endereco import *
from Model.pessoa import Pessoa
from Model.usuario import Usuario
from Model.colaborador import Colaborador
from Model.informacao_geral import InformacaoGeral
from Model.serie import Serie
from Model.temporada import Temporada
from Model.episodio import Episodio
from Model.genero import Genero
from Model.serie_favorita import SerieFavorita
from Model.temporada_assistida import TemporadaAssistida
from Model.estudio import Estudio


if os.path.exists(arquivobd): 
    os.remove(arquivobd) 

db.create_all()