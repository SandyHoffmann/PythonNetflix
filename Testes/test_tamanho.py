import os, sys

currentdir = os.path.dirname(os.path.realpath(__file__)) 
parentdir = os.path.dirname(currentdir) 
sys.path.append(parentdir)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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

tamanho = 0
tamanhoObj = 0

for x in range(4**7):
    serie = Serie(titulo="Game of Thrones",  id_genero=1, id_colaborador="12345678910")
    listaSerie.append(serie)
    tamanho += sys.getsizeof(1343)
    tamanho += sys.getsizeof(2)
    tamanho += sys.getsizeof('12345678910')
    # db.session.add(serie)
    # db.session.commit()

print(sys.getsizeof(listaSerie))
print(tamanho)

#Memoria Volatil

# Nas 4 séries iguais 464 Bytes
# Nas 16 séries iguais 1856 Bytes
# Nas 64 séries iguais 7424 Bytes
# Nas 256 séries iguais 29696 Bytes 
# Nas 1024 séries iguais 118784 Bytes 
# Nas 4096 séries iguais 475136 Bytes
# Nas 16384 séries iguais 1900544 Bytes

#Memoria Fisica

# Nas 4 séries iguais 49,152 Bytes
# Nas 16 séries iguais 49,152 Bytes
# Nas 64 séries iguais 49,152 Bytes 
# Nas 256 séries iguais 49,152 Bytes
# Nas 1024 séries iguais 147,456 Bytes 
# Nas 4096 séries iguais 393216 Bytes
# Nas 16384 séries iguais 2195456 Bytes


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

th = np.linspace(0, 2*np.pi, 128)

# l1 = [88,
# 184,
# 632,
# 2208,
# 9016,
# 33920,
# 140576]

l1 = [464,
1856,
7424,
29696,
118784,
475136,
1900544]

l2 = [49152,
49152,
49152,
49152,
147456,
393216,
2195456,]

def demo(sty):
    mpl.style.use(sty)
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.set_title('Diferença entre mem. Fisica e mem. Volatil'.format(sty), color='C0')
    ax.plot( l1, 'C1', label='M.Vol')
    ax.plot( l2, 'C2', label='M.Fis')
    ax.legend()
    plt.show()


demo('seaborn')
