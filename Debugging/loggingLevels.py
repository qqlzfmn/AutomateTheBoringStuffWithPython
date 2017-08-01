import logging

# 级别        日志函数            描述
# DEBUG       logging.debug()     最低级别。用于小细节。通常只有在诊断问题时，你才会关心这些消息
# INFO        logging.info()      用于记录程序中一般事件的信息，或确认一切工作正常
# WARNING     logging.warning()   用于表示可能的问题，它不会阻止程序的工作，但将来可能会
# ERROR       logging.error()     用于记录错误，它导致程序做某事失败
# CRITICAL    logging.critical()  最高级别。用于表示致命的错误，它导致或将要导致程序完全停止工作


# level=logging.DEBUG 控制显示的日志级别，若level=logging.ERROR，则只显示ERROR 和CRITICAL
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')
