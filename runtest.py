import logging
logging.basicConfig(filename='example.log',level=logging.ERROR)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

# logger = logging.getLogger(__name__).addHandler(logging.NullHandler())

try:
    from out import *
except Exception as e:
    logging.exception("my message")
