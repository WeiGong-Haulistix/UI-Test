import logging.handlers
import os


class FinalLogger:
    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    cr = os.path.abspath(os.path.dirname(os.getcwd()))
    if "Haulistix_UITest" in cr:
        log_file = cr + '/Results/UI_test_logger.log'
    else:
        log_file = cr + '/Haulistix_UITest/Results/UI_test_logger.log'

    if log_file:
        with open(log_file, 'r+') as file:
            file.truncate(0)

    log_level = "d"
    log_max_byte = 10 * 1024 * 1024
    log_backup_count = 5

    @staticmethod
    def get_logger():
        if FinalLogger.logger is not None:
            return FinalLogger.logger

        FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=FinalLogger.log_file,
                                                           maxBytes=FinalLogger.log_max_byte,
                                                           backupCount=FinalLogger.log_backup_count)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)
        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
        return FinalLogger.logger


if __name__ == "__main__":
    logger = FinalLogger.get_logger()
    logger.debug("this is a debug msg!")
    logger.info("this is a info msg!")
    logger.warning("this is a warn msg!")
    logger.error("this is a error msg!")
    logger.critical("this is a critical msg!")
