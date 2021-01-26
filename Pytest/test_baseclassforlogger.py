import logging

class baseclass:
    def test_loggingdemo(self):
        logger = logging.getLogger(__name__)

        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        return logger