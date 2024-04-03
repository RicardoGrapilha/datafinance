import yfinance as yf
lista_empresas = ["WEGE3.SA", "PETR4.SA"]
dados_empresas = yf.download(lista_empresas, start="2023-01-01")
print(dados_empresas)