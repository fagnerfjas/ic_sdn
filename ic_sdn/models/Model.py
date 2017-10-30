#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

from ic_sdn.models.db import Db

class Model(object):

    tableName = ''
    attributes = []
    db = Db()

    def __init__(self):
        self.tableName = self.__class__.__name__.lower() + 's'


    '''Retorna um JSON com todos os registros da tabela'''
    def all(self):
        data = self.db.getAll(self.tableName)
        if data:
            return data
        return 'Error! Inaccessible database.'

    '''Instala diretórios e banco de dados da aplicação'''
    def migrate(self):
        return self.db.migrate()


    '''Verifica se o banco de dados está configurado'''
    def isConfigured(self):
        return self.db.isConfigured()

    '''
        Recebe um mapa de valores e resume este mapa, deixando apenas
        os valores correspondentes a os atributos(self.attributes) da classe
    '''
    def validAttributes(self, data):
        list_maped = {}
        for attibute in self.attributes:
            if attibute in data.keys():
                list_maped[attibute] = data[attibute]
        return list_maped


    def create(self, data):
        data = self.validAttributes(data)
        return self.db.queryInsert(self.tableName, data);

