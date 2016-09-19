# coding:utf-8
import json

import time
from tornado.websocket import WebSocketHandler
import threading
import commands

from logger_conf import logger

__author__ = 'uv2sun'


class ExecHandler(WebSocketHandler):
    def data_received(self, chunk):
        pass

    def on_message(self, message):
        logger.debug('received cmd, %s' % (message,))
        msg = json.loads(message)
        if msg and msg['cmds']:
            Executor(msg['cmds'], self).start()
        else:
            self.write_message(json.dumps({'msg_type': 'cmd_err', 'msg': 'no commands to execute'}))
            self.close(code=9, reason='no commands to execute')

    def open(self, *args, **kwargs):
        logger.debug("received exec request")
        logger.debug(self.request)

    def on_close(self):
        logger.debug('close websocket request')

    def check_origin(self, origin):
        """跨域检查永远通过"""
        return True


class Executor(threading.Thread):
    """命令执行器，单独线程执行"""

    def __init__(self, cmds, websocket):
        super(Executor, self).__init__()
        self.cmds = cmds
        self.websocket = websocket

    def exec_cmd(self):
        for cmd in self.cmds:
            msg = 'begin to exec [%s]' % (cmd,)
            self.websocket.write_message(json.dumps({'msg_type': 'status', 'msg': msg}))
            logger.debug(msg)
            result = commands.getstatusoutput(cmd=cmd)
            exit_code = result[0]
            echo = result[1]
            if exit_code == 0:
                msg = {'msg_type': 'status', 'msg': 'exec [%s] ok' % (cmd,)}
                time.sleep(5)
                self.websocket.write_message(json.dumps(msg))
                logger.debug(msg)
            else:
                logger.error('exec [%s] error, exit=%s, echo=%s', (cmd, exit_code, echo))
                # self.websocket.write_message('exec [%s] error, exit=%s, echo=%s', (cmd, exit_code, echo))
                self.websocket.write_message(json.dumps({'msg_type': 'cmd_err', 'msg': echo}))
                self.websocket.close(code=exit_code, reason=echo)
                break
        msg = {'msg_type': 'cmd_end', 'msg': 'exec cmds success'}
        logger.debug(msg)
        self.websocket.write_message(json.dumps(msg))
        logger.debug("exec over ok, send close event.")
        self.websocket.close(code=0)

    def run(self):
        self.exec_cmd()
