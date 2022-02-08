import logging
from flask import Flask



def create_app():
    # Приложение Flask
    app = Flask(__name__)
    [print(key) for key in logging.Logger.manager.loggerDict]
    logging.info('Starting app.')

    return app
