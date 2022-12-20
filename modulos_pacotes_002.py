import modulos_pacotes_001
print(modulos_pacotes_001.dds('globo.com'))

from modulos_pacotes_001 import dds, ping
print(dds('globo.com'))
print(ping('robervan'))
from modulos_pacotes_001 import *   # importa tudo que esta na outra pasta
from modulos_pacotes_001 import ping as pi    # importa o ping da outra pasta e substitui o nome por PI
print(pi('globo.com'))
