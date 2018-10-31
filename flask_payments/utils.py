import logging


def create_logger(logger_name, file_name):
    level = logging.DEBUG
    log = logging.getLogger(logger_name)
    fh = logging.FileHandler(file_name)
    fh.setLevel(level)

    fh.setFormatter(logging.Formatter("%(asctime)s - %(name)s: %(message)s"))
    log.setLevel(level)
    log.addHandler(fh)

    return log
