import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# 用logging.disable(logging.LEVEL)会禁止该级别和更低级别的所有日志消息
logging.disable(logging.CRITICAL)

logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')
