# Macadamia_S011_ARB_CEX_DEX_Mul_Sym Arbitrage Bot

# Overview

Macadamia is an arbitrage bot written in pure Python that aims to capitalize on price differences between centralized exchanges (CEXs) and decentralized exchanges (DEXs). The project is still under development.

# Key Components

Exchange Configuration: The bot interfaces with various exchanges using their APIs. You’ve configured API keys  like Binance, KuCoin, OKEx, Poloniex, and others 30+ exchanges.
Fees Configuration: The fees dictionary specifies the trading fees for each exchange (base and quote fees).
Exchange Initialization: The exchanges list initializes instances of the exchanges using the provided API keys.
Symbol Definitions: The symbols list contains trading pairs (e.g., ‘BTC/USDT’, ‘ETH/USDT’, ‘XRP/USDT’) that the bot will monitor.
Timeframes: The timeframes list defines the candlestick intervals for price data (e.g., ‘1m’, ‘5m’, ‘1h’). These timeframes determine how frequently the bot checks for arbitrage opportunities.
Dataframe Initialization: The df DataFrame is created to store price data for the specified symbols.
Balance Retrieval: The get_balance function fetches the total USDT balance from each exchange.
Arbitrage Execution Loop:
The bot continuously checks for arbitrage opportunities.
It calculates the highest and lowest prices across exchanges.
If an opportunity exists (i.e., min_price < max_price), it executes arbitrage by buying on the exchange with the lowest price and selling on the exchange with the highest price.
The bot logs the opportunity and waits for the specified renewal time.

-------------------------------------------------------------------

## Features

- Interfaces with various 30+ exchanges (Binance, KuCoin, OKEx, etc.) using API keys.
- Calculates trading fees based on the configured fee structure.
- Monitors specified trading pairs (symbols) and timeframes.
- Executes arbitrage when profitable opportunities arise.
- Logs arbitrage events and handles errors.

## Getting Started

1. Clone this repository.
2. Install Python dependencies (`pip install -r requirements.txt`).
3. Configure your API keys in `exchange_config.py`.
4. Define the trading pairs (symbols) you want to monitor in `symbols`.
5. Set the desired candlestick intervals (timeframes) in `timeframes`.
6. Run `python Macadamia.py` to start the bot.

## Configuration

- Adjust the fee structure in `fees` if needed.
- Customize the renewal time (sleep interval) for checking opportunities.
- Monitor the bot's logs for executed arbitrage events.

## Disclaimer

- Keep your API keys secure and follow best practices.
- Ensure that you have sufficient funds and understand the risks before trading.
- Review and comply with the terms of use for each exchange.


## Telegram Integration

You can access and manage the Macadamia bot via Telegram Messenger. Follow these steps:

1. Create a Telegram bot:
   - Open Telegram and search for the "BotFather" user.
   - Start a chat with BotFather and use the `/newbot` command to create a new bot.
   - Follow the instructions to set a name and username for your bot.
   - Note down the generated API token.

2. Integrate with Macadamia.py:
   - In your Macadamia.py code, add the Telegram bot API token.
   - Implement Telegram bot commands (e.g., `/start`, `/status`, `/stop`) to interact with your bot.
   - Use the `python-telegram-bot` library to handle Telegram interactions.

3. Run your bot:
   - Start your Macadamia.py bot.
   - Chat with your Telegram bot to receive updates, check status, and manage arbitrage activities.

## License
Developed by : Smitajyoyi Adhikari & Team @macadamia 
Contact- (desibewdabbsr@gmail.com, 
imperialbluewisky@gmail.com, 
rumoldmunk@gmail.com)