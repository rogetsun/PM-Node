# coding:utf-8

import logging as _log_
import os
import sys

__author__ = 'uv2sun'

_log_.basicConfig(level=_log_.DEBUG,
                  format='%(asctime)s %(filename)-15s:[line:%(lineno)-4s]%(levelname)-8s: %(message)s',
                  datefmt='%Y-%m-%d %H:%M:%S',
                  stream=sys.stdout,
                  # filename=os.path.split(__file__)[0] + "/log/sm.log",
                  filemode='a+')
#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
#
console = _log_.FileHandler(os.path.split(__file__)[0] + "/logs/sm.log")
console.setLevel(_log_.INFO)
formatter = _log_.Formatter('%(filename)-15s:[line:%(lineno)-4s]%(levelname)-8s:[%(asctime)s]: %(message)s')
console.setFormatter(formatter)
_log_.getLogger('').addHandler(console)
#################################################################################################

# _log_.debug('This is debug message')
# _log_.info('This is info message')
# _log_.warning('This is warning message')
logger = _log_
