# Basic config parameters
PAPER_TRADING = True                        # Trading mode (True - paper, False - live)
LOG_LEVEL = "DEBUG"                          # Log level (DEBUG, INFO, WARNING, ERROR)
RUN_INTERVAL_SECONDS = 600                  # Trading interval in seconds (if the market is open)
BYPASS_MARKET_HOURS = True                 # Set to True to ignore market hours check

# Alpaca Live Trading Credentials
ALPACA_LIVE_API_KEY = ""                            # Alpaca live trading API key
ALPACA_LIVE_SECRET_KEY = ""     # Alpaca live trading secret key

# Alpaca Paper Trading Credentials
ALPACA_PAPER_API_KEY = ""                           # Alpaca paper trading API key
ALPACA_PAPER_SECRET_KEY = ""    # Alpaca paper trading secret key

# Set the active credentials based on PAPER_TRADING setting
ALPACA_API_KEY = ALPACA_PAPER_API_KEY if PAPER_TRADING else ALPACA_LIVE_API_KEY
ALPACA_SECRET_KEY = ALPACA_PAPER_SECRET_KEY if PAPER_TRADING else ALPACA_LIVE_SECRET_KEY

# Watchlist file
WATCHLIST_FILE = "watchlist.json"

# Trading config parameters
TRADE_EXCEPTIONS = []                       # List of stocks to exclude from trading (e.g. ["AAPL", "TSLA", "AMZN"])
WATCHLIST_NAMES = ["Primary", "TopAIPicks", "AIStocks"]               # Watchlist names (can be empty, or create in Alpaca dashboard)
WATCHLIST_OVERVIEW_LIMIT = 20                # Number of stocks to process in decision-making (e.g. 20)
PORTFOLIO_LIMIT = 12                         # Number of stocks to hold in the portfolio
MIN_SELLING_AMOUNT_USD = 1                   # Minimum sell amount in USD (False - disable setting)
MAX_SELLING_AMOUNT_USD = 10000               # Maximum sell amount in USD (False - disable setting)
MIN_BUYING_AMOUNT_USD = 1                    # Minimum buy amount in USD (False - disable setting)
MAX_BUYING_AMOUNT_USD = 10000                # Maximum buy amount in USD (False - disable setting)
PDT_PROTECTION = False                       # Pattern day trader protection (False - disable protection)

# OpenAI config params
OPENAI_MODEL_NAME = "gpt-4o"           # OpenAI model name
MAX_POST_DECISIONS_ADJUSTMENTS = False      # Maximum number of adjustments to make (False - disable adjustments)
OPENAI_API_KEY = ""  # OpenAI API key
