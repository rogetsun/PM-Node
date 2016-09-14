#!/usr/bin/env python
# coding:utf-8
import sys

from tornado.ioloop import IOLoop

from app import app
from logger_conf import logger

__author__ = 'uv2sun'

setting = {
    "max_buffer_size": 2048  # 2KB
}
if __name__ == "__main__":
    port = sys.argv.__len__() >= 2 and sys.argv[1] or 9128
    port = int(port)
    ip = sys.argv.__len__() >= 3 and sys.argv[2] or "0.0.0.0"
    app.listen(port, address=ip, **setting)
    logger.debug("app.listen %s:%s" % (ip, port))
    IOLoop.current().start()
