import logging
import logging.config
import json
from . import terminal


with open(r"invest_terminal/logs/log_config.json") as f:
    conf = json.load(f)

logging.config.dictConfig(conf['logging'])
app = terminal.create_app()
