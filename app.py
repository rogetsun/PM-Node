# coding:utf-8
import os

import tornado
from tornado.web import Application

from router.exec_router import ExecHandler
from router.index_router import IndexHandler
from router.log_router import LogHandler

__author__ = 'uv2sun'

handlers = [
    ("/assets/(.*)", tornado.web.StaticFileHandler, {"path": os.path.dirname(__file__) + "/web/assets"})
    # 执行命令websocket handler
    , ('/ws/exec', ExecHandler)
    # 查看日志
    , ('/tail', LogHandler)
    # 默认显示
    , ('/(.*)', IndexHandler)
]

setting = dict(
    debug=True,
    template_path=os.path.dirname(__file__) + "/web"
)

app = Application(handlers=handlers, **setting)
