__version__ = "0.1.0"

import socket
import time
import logging
from logging.handlers import RotatingFileHandler
import os, sys
from cmreslogging.handlers import CMRESHandler


class MyFilter(logging.Filter):
    def __init__(self, param=None):
        self.param = param

    def filter(self, record):
        if self.param is None:
            allow = True
        else:
            allow = self.param not in record.msg
        if allow:
            record.level = record.levelname
            # delattr(record, 'levelname')
            record.host = socket.gethostname()
            record.hostIp = socket.gethostbyname(record.host)

        return allow


logger = logging.getLogger(__name__)
logger.addFilter(MyFilter())
logger.setLevel(logging.DEBUG)


class LoggerFactory(object):
    def __init__(self, path_log_file="/tmp") -> None:
        self.path_log_file = path_log_file

        super().__init__()
