import logging

logging.basicConfig(filename='first.log',
                    filemode='a',
                    level=logging.ERROR,
                    format='%(asctime)s / %(levelname)s / %(message)s')

logging.info('ok')
logging.critical('Server malfunction!')