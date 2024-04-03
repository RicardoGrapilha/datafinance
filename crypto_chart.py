import ccxt
import pandas as pd
import plotly.graph_objects as go

# Definir a criptomoeda, exchange e período
crypto = "BTC/USDT"  # Par de negociação
exchange = "binance"  # Nome da exchange
timeframe = '1d'  # Período de tempo (1 dia)

# Inicializar a exchange
exchange = getattr(ccxt, exchange)()

# Obter os dados históricos
ohlcv = exchange.fetch_ohlcv(crypto, timeframe)

# Converter para DataFrame pandas
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# Criar o gráfico de velas
fig = go.Figure(data=[go.Candlestick(x=df['timestamp'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])

# Adicionar uma linha com preço personalizado
curso = 50000  # Preço personalizado
fig.add_trace(go.Scatter(x=df['timestamp'], y=[curso] * len(df), mode='lines', name='Curso'))

# Personalizar o layout do gráfico
fig.update_layout(title=f'Gráfico de Velas para {crypto} na {exchange.id}',
                   xaxis_title='Data',
                   yaxis_title='Preço (USD)',
                   template='plotly_dark')

# Mostrar o gráfico
fig.show()
