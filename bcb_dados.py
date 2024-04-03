# para pegar os dados do banco central
from bcb import sgs
dados_do_bcb = sgs.get({"DOLAR": 1, "IPCA": 433})
print(dados_do_bcb)