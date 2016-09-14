# coding:utf-8
from tornado.web import RequestHandler

__author__ = 'uv2sun'


class IndexHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render('index.html', ret_code='PM-Node say:', ret_msg='i am running healthy!')
