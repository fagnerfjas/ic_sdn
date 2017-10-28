#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ic_sdn.models.db import Db

class Model(object):

    tableName = ''
    db = Db()

    def __init__(self):
        self.tableName = self.__class__.__name__.lower() + 's'

    '''Retorna um JSON com todos os registros da tabela'''
    def all(self):
        data = self.db.getAll(self.tableName)
        return data

    def migrate(self):
        return self.db.migrate()

    def isConfigured(self):
        if not self.db.isConfigured():
            return False
        return True