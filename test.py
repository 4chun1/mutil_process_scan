#!/usr/bin/python
# coding==gb2312 #python2.3 not support gb2312,gbk only support utf-8


import paramiko
import pexpect
import select
import socket
import sys
import time
import commands
import logging
from optparse import OptionParser, OptionGroup

__version__ = '2.1.1'


class ColorFormatter(logging.Formatter):
    FORMAT = ("[%(levelname)s] %(message)s")
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"

    COLORS = {
        'WARNING': YELLOW,
        'INFO': WHITE,
        'DEBUG': BLUE,
        'CRITICAL': YELLOW,
        'ERROR': RED
    }

    def __init__(self, use_color=True):
        msg = self.formatter_msg(self.FORMAT, use_color)
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def formatter_msg(self, msg, use_color=True):
        if use_color:
            msg = msg.replace("$RESET", self.RESET_SEQ).replace("$BOLD", self.BOLD_SEQ)
        else:
            msg = msg.replace("$RESET", "").replace("$BOLD", "")
        return msg

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in self.COLORS:
            fore_color = 30 + self.COLORS[levelname]
            levelname_color = self.COLOR_SEQ % fore_color + levelname + self.RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


def initLog(level="info"):
    LEVELS = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    print "shicy"
    global logger
    logger = logging.getLogger("proxy")
    logger.setLevel(LEVELS[level])

    # create console handler with a higher log level
    ch = logging.StreamHandler(sys.stdout)
    # ch.setLevel(logging.DEBUG)
    ch.setFormatter(ColorFormatter())
    logger.addHandler(ch)
    print "github_test"


class RetryException(Exception):
    pass
