"""
This file includes main class Framework and class PageNotFound404.
This is part of practical task on course 'pattern of programming' GB, 2023
Author: Maksim Sapunov, Jenny6199@yandex.ru
"""
from dataclasses import dataclass


@dataclass
class Framework:
    """Base for building"""
    routes: list
    fronts: list

    def __call__(self, environ, start_response):
        """
        redefinition of __call__ method
        :param environ - dict with variables of environment
        :param start_response - tuple
        :return body.encode('utf-8')
        """
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'
        # page controller
        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound404()
        request = {}
        # front controller
        for front in self.fronts:
            front(request)
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]


class PageNotFound404:
    """class with dead-end-page 404"""
    def __call__(self, request):
        """redefinition __call__ method"""
        return '404 WHAT', '404 Page not found'
