# Web Scraping no site Fundamentus:

# Bibliotecas Utilizadas:
# - Selenium: Ideal para interações complexas com páginas da web.
# - BeautifulSoup: Mais eficiente para análise de HTML simples.

# Escolha da Biblioteca:
# - Selenium: Utilizado quando é necessário realizar ações específicas, como baixar planilhas, preencher formulários, etc.
# - BeautifulSoup: Mais adequado para páginas simples, oferecendo melhor desempenho em situações menos complexas.

# Gerenciamento de Drivers:
# - WebDriver Manager: Facilita a instalação e atualização dos drivers necessários para o Selenium, automatizando esse processo.


from  selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from io import StringIO
import pandas as pd

# Para usar em outros navegadores, basta trocar webdriver.Firefox por webdriver.Edge, por exemplo.
# Início do Web Scraping e criação do robô.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

site_url = "https://www.fundamentus.com.br/resultado.php"
driver.get(site_url)

# Agora, acesse o site, vá para a seção de interesse e inspecione o elemento desejado.
# Em seguida, selecione a tabela (ou o elemento que deseja copiar), clique com o botão direito do mouse e escolha a opção 'Copy' -> 'Copy full XPath'.
# Isso irá gerar um texto semelhante a este:
# /html/body/div[1]/div[2]/table (é o caminho da tabela dentro do corpo do site)

local_tabela = "/html/body/div[1]/div[2]/table"
# Navegando até o elemento desejado na página.
# O mesmo conceito se aplica para encontrar inputs ou botões para interagir com o site.
elemento = driver.find_element("xpath", local_tabela)
html_tabela = elemento.get_attribute("outerHTML")
html_io = StringIO(html_tabela)
tabela = pd.read_html(html_io, thousands=".", decimal=",")[0] # Utilizando o índice 0 para selecionar a primeira tabela encontrada.

print(tabela)