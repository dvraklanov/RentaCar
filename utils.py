import logging

file_log = logging.FileHandler('logs/app.log')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=[file_log, console_out],
                    level=logging.DEBUG,
                    format='%(asctime)s [%(filename)s] %(levelname)s: %(message)s')




