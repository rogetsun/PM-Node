# coding:utf-8
import commands
import json
import re

from tornado.websocket import WebSocketHandler

from logger_conf import logger

__author__ = 'uv2sun'


class LogHandler(WebSocketHandler):
    def data_received(self, chunk):
        pass

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        try:
            msg = json.loads(message)
            logger.debug(msg)
            logs = commands.getoutput('tail -n %s %s' % (msg.get('n', 100), msg.get('logFile')))
            logger.debug('logs.size=%s' % (len(logs),))
            # rs = logs.splitlines()
            # for r in rs:
            #     logger.debug(r)
            self.write_message(json.dumps({'msg_type': 'log', 'msg': logs}))
            self.close(code=0)
        except Exception as e:
            self.write_message(json.dumps({'msg_type': 'cmd_err', 'msg': e.message}))
            self.close(code=1, reason=e.message)
