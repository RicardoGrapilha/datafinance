# Análise Financeira com Python

Este projeto consiste em uma aplicação para a leitura de dados financeiros por meio de robôs automatizados e a geração de planilhas robustas para análise e tomada de decisões no mercado financeiro.

## Objetivo

O objetivo principal deste projeto é fornecer uma ferramenta poderosa e flexível para a coleta, organização e análise de dados financeiros de diversas fontes, possibilitando uma melhor compreensão dos mercados e auxiliando na elaboração de estratégias de investimento mais informadas.

## Funcionalidades

- Coleta automatizada de dados financeiros de diversas fontes.
- Processamento e organização dos dados coletados em planilhas estruturadas.
- Geração de relatórios e análises personalizadas.
- Integração com APIs de mercado e exchanges.
- Suporte a diversos tipos de ativos financeiros, como ações, criptomoedas, commodities, entre outros.


## Projetos

### bcb_dados.py

Este script utiliza a biblioteca `python-bcb` para importar dados do Banco Central do Brasil (BCB). Ele se concentra em recuperar dados específicos do Sistema Gerenciador de Séries Temporais (SGS) do BCB.

### crypto_chart.py

Este script utiliza as bibliotecas `ccxt` e `plotly` para gerar gráficos de velas (candlesticks) para criptomoedas. Ele se conecta a diferentes exchanges de criptomoedas usando a biblioteca `ccxt` e cria gráficos de velas interativos com a biblioteca `plotly`.

### crypto.py

Este script utiliza a biblioteca `cryptocmd` para obter dados do CoinMarketCap. Ele se concentra em recuperar informações sobre diferentes criptomoedas, como preços, volumes de negociação e capitalização de mercado.

### acoes_yfinance.py

Este script utiliza a biblioteca `yfinance` para importar dados financeiros do Yahoo Finance. Ele se concentra em obter dados históricos de preços de ações e outras informações financeiras.

### fundamentus_selenium.py

Este script utiliza a biblioteca `selenium` para acessar o site do Fundamentus e extrair dados financeiros de empresas listadas na bolsa de valores brasileira. Ele é especialmente útil para coletar informações de empresas não disponíveis em outras fontes.

### install_webdriver_manager.py

Este script fornece instruções para instalar e desinstalar a biblioteca `webdriver_manager`, que é útil para gerenciar drivers de navegador necessários para automação web em Python.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:

- `python-bcb`
- `ccxt`
- `plotly`
- `cryptocmd`
- `yfinance`
- `selenium`
- `webdriver_manager`

Você pode instalar as bibliotecas listadas executando o comando `pip install -r requirements.txt`.

## Como Usar

1. Instale as dependências do projeto executando o comando `pip install -r requirements.txt`.
2. Cada script possui um propósito específico e pode ser executado individualmente. Certifique-se de ter as dependências necessárias instaladas antes de executar os scripts.

```bash
python bcb_dados.py
python crypto_chart.py
python crypto.py
python acoes_yfinance.py
python fundamentus_selenium.py
python install_webdriver_manager.py
```

## Tecnologias Utilizadas

- Python
- Pandas
- Requests
- Matplotlib

## Contribuição

Contribuições são sempre bem-vindas! Se você deseja contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (`git checkout -b feature/sua-feature`).
3. Faça commit das suas alterações (`git commit -am 'Adicionando uma nova feature'`).
4. Faça push para a branch (`git push origin feature/sua-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença [MIT](https://opensource.org/licenses/MIT) - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Esse README foi criado com ❤️ usando Markdown (MD).

Feito por Ricardo Grapilha