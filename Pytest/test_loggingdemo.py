import logging


def test_loggingdemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    logger.addHandler(filehandler)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.debug("A debug statement is executed")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happend")
    logger.critical("Critical issue")









# def test_loggingofdemo():
#     logger = logging.getLogger(__name__)
#
#     filehandler = logging.FileHandler('logfile.log')
#     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
#     filehandler.setFormatter(formatter)
#
#     logger.addHandler(filehandler)  #filehandler object
#
#     logger.setLevel(logging.DEBUG)
#     logger.debug("A debug statement is executed")
#     logger.info("Information statement")
#     logger.debug("A debug statement is executed")
#     logger.warning("Something is in warning mode")
#     logger.error("A Major error has happend")
#     logger.critical("Critical issue")
