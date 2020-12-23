import logging
# logging.basicConfig(filename='log.log',level=logging.DEBUG,format=)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(pathname)s %(filename)s %(lineno)d行 %(levelname)s %(message)s', datefmt='%Y/%m/%d %I:%M:%S')

logging.debug('debug massage!')
logging.info('info massgae!')
logging.warning('warning massage!')
logging.error('errpr massage!')
logging.critical('critical massage!')