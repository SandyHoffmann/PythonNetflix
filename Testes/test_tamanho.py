import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

from datetime import date
from Config.config import *
from Model.serie import Serie
from Model.colaborador import Colaborador
from Model.genero import Genero
from Model.endereco import Endereco

# Sem criar nenhum dado possui 69632 Byte

listaSerie = []

# Com dados de genero, endereço e colaborador = 69632 Byte

# endereco1 = Endereco(numero="345", logradouro="Rua 15 de novembro", bairro="centro", cep="12345678", estado="SC", pais="Brasil")

# db.session.add(endereco1)

# db.session.commit()



for x in range(4**5):
    serie = Serie(titulo="Game of Thrones",  id_genero=1, id_colaborador="12345678910")
    listaSerie.append(serie)
    db.session.add(serie)
    db.session.commit()

# print(os.path.getsize(arquivobd))

#Memoria Volatil

# Nas 4 séries iguais 88 Bytes
# Nas 16 séries iguais 184 Bytes
# Nas 64 séries iguais 632 Bytes
# Nas 256 séries iguais 2208 Bytes 
# Nas 1024 séries iguais 9016 Bytes 
# Nas 4096 séries iguais 33920 Bytes
# Nas 16384 séries iguais 140576 Bytes
# Nas 65536 séries iguais 2115944 Bytes
# Nas 1048576 séries iguais 8697456 Bytes

#Memoria Fisica

# Nas 4 séries iguais 49,152 Bytes
# Nas 16 séries iguais 49,152 Bytes
# Nas 64 séries iguais 49,152 Bytes
# Nas 256 séries iguais 49,152 Bytes 
# Nas 1024 séries iguais 147,456 Bytes 


"""
SELECT
  'serie' AS 'Table',
  ROUND((DATA_LENGTH + INDEX_LENGTH)) AS 'Size (Bytes)'
FROM
  information_schema.TABLES
WHERE
    TABLE_SCHEMA = 'netflix2'
  AND
    TABLE_NAME = 'serie'
ORDER BY
  (DATA_LENGTH + INDEX_LENGTH)
DESC;
"""

# print(sys.getsizeof(listaSerie))
# print(4**10)

