from cryptocmd import CmcScraper

scraper = CmcScraper("BTC")
dados_cripto = scraper.get_dataframe()
print(dados_cripto)