import logging
# logging.basicConfig(filename='log.log',level=logging.DEBUG,format=)
# logging.basicConfig(level=logging.DEBUG,
#                     filename='log.log',
#                     format='%(asctime)s %(pathname)s %(filename)s %(lineno)d行 %(levelname)s %(message)s',
#                     datefmt='%Y/%m/%d %I:%M:%S')
#
# logging.debug('debug massage!')
# logging.info('info massgae!')
# logging.warning('warning massage!')
# logging.error('errpr massage!')
# logging.critical('critical massage!')


def log(fileName):
    logger = logging.getLogger("nick")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        fh = logging.FileHandler(fileName, encoding="utf-8")
        ch = logging.StreamHandler()

        formatter = logging.Formatter(
            fmt='%(asctime)s-%(pathname)s-%(filename)s-[%(lineno)d]-%(levelname)s : %(message)s',
            datefmt='%Y/%m/%d %I:%M:%S'
            )

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger

if __name__ == "__main__":
    myLog = log()
    myLog.info("info")
    myLog.debug("debug")