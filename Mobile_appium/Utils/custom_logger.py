import logging

class Loggen:

    def __init__(self):
        logging.basicConfig(filename="/Users/hakumar/PycharmProjects/Experiments/Mobile_appium_Project/Logs/auto.log")
        self.logger = logging.getLogger(__name__)

    def loggen_setlevel(self):
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Inside the loggen class")

    def info(self, param):
        self.logger.info(param)

    def critical(self, param):
        self.logger.critical(param)
