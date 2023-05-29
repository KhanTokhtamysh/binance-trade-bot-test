#!python3
import time

from binance_trade_bot.binance_api_manager import BinanceAPIManager
from binance_trade_bot.config import Config
from binance_trade_bot.database import Database
from binance_trade_bot.logger import Logger
from binance_trade_bot.scheduler import SafeScheduler
from binance_trade_bot.strategies import get_strategy

logger = Logger()
logger.info("Starting")

config = Config()
db = Database(logger, config)
manager = BinanceAPIManager(config, db, logger)
