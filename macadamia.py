import ccxt
import time
import logging
import os
import pandas as pd
from exchange_config import (
    BINANCE_API_KEY,
    BINANCE_SECRET_KEY,
    KUCOIN_API_KEY,
    KUCOIN_SECRET_KEY,
    OKX_API_KEY,
    OKX_SECRET_KEY,
    POLONIEX_API_KEY,
    POLONIEX_SECRET_KEY,
    COINEX_API_KEY,
    COINEX_SECRET_KEY,
    BYBIT_API_KEY,
    BYBIT_SECRET_KEY,
    MEXC_API_KEY,
    MEXC_SECRET_KEY,
    UPBIT_API_KEY,
    UPBIT_SECRET_KEY,
    BINGX_API_KEY,
    BINGX_SECRET_KEY,
    GEMINI_API_KEY,
    GEMINI_SECRET_KEY,
    DEEPCOIN_API_KEY,
    DEEPCOIN_SECRET_KEY,
    XT_API_KEY, 
    XT_SECRET_KEY
)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Exchanges fees Configuration
fees = {
    'binance': {'base': 0, 'quote': 0.001},
    'kucoin': {'base': 0, 'quote': 0.001},
    'okx': {'base': 0, 'quote': 0.001},
    'poloniex': {'base': 0, 'quote': 0.001},
    'coinex': {'base': 0, 'quote': 0.001},
    'bybit': {'base': 0, 'quote': 0.001},
    'mexc': {'base': 0, 'quote': 0.001},
    'upbit': {'base': 0, 'quote': 0.001},
    'bingx': {'base': 0, 'quote': 0.001},
    'gemini': {'base': 0, 'quote': 0.001},
    'deepcoin': {'base': 0, 'quote': 0.001},
    'xt': {'base': 0, 'quote': 0.001},
}

# Initialize exchanges with actual API keys
exchanges = [
    ccxt.binance({'apiKey': BINANCE_API_KEY, 'secret': BINANCE_SECRET_KEY}),
    ccxt.kucoin({'apiKey': KUCOIN_API_KEY, 'secret': KUCOIN_SECRET_KEY}),
    ccxt.okex({'apiKey': OKX_API_KEY, 'secret': OKX_SECRET_KEY}),
    ccxt.poloniex({'apiKey': POLONIEX_API_KEY, 'secret': POLONIEX_SECRET_KEY}),
    ccxt.coinex({'apiKey': COINEX_API_KEY, 'secret': COINEX_SECRET_KEY}),
    ccxt.bybit({'apiKey': BYBIT_API_KEY, 'secret': BYBIT_SECRET_KEY}),
    ccxt.mexc({'apiKey': MEXC_API_KEY, 'secret': MEXC_SECRET_KEY}),
    ccxt.upbit({'apiKey': UPBIT_API_KEY, 'secret': UPBIT_SECRET_KEY}),
    ccxt.bingx({'apiKey': BINGX_API_KEY, 'secret': BINGX_SECRET_KEY}),
    ccxt.gemini({'apiKey': GEMINI_API_KEY, 'secret': GEMINI_SECRET_KEY}),
    ccxt.deepcoin({'apiKey': DEEPCOIN_API_KEY, 'secret': DEEPCOIN_SECRET_KEY}),
    ccxt.xt({'apiKey': XT_API_KEY, 'secret': XT_SECRET_KEY}),
]

# Define the symbols and timeframes
symbols = ['BTC/USDT', 'ETH/USDT', 'XRP/USDT']
timeframes = ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h']

# Initialize the dataframe
df = pd.DataFrame(columns=['timestamp'] + [f'price{i}' for i in range(1, len(symbols) + 1)])

def get_balance(exchange):
    balance = exchange.fetch_balance()
    return balance['total'].get('USDT', 0)

def execute_arbitrage(renew_time_minutes=1):
    while True:
        try:
            # Fetch balances and prices for all exchanges
            balances = [get_balance(ex) for ex in exchanges]
            prices = [ex.fetch_ticker(symbols[0])['last'] for ex in exchanges]

            # Find the highest and lowest prices
            min_price = min(prices)
            max_price = max(prices)

            # Execute arbitrage if there's an opportunity
            if min_price < max_price:
                min_index = prices.index(min_price)
                max_index = prices.index(max_price)
                amount_to_buy = balances[min_index] / min_price
                exchanges[min_index].create_market_buy_order(symbols[0], amount_to_buy)
                exchanges[max_index].create_market_sell_order(symbols[0], amount_to_buy)
                logging.info(f"Arbitrage opportunity: Buy on {exchanges[min_index].name}, sell on {exchanges[max_index].name}")

            time.sleep(renew_time_minutes * 60)

        except ccxt.BaseError as e:
            logging.error(f"Error: {e}")
            time.sleep(10)

if __name__ == '__main__':
    execute_arbitrage()
