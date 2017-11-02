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
            data = [tuple(['ID'] + self.attributes)] + data
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


    '''
    Recebe um mapa contendo a chave e o respectivo valor, e  cria um objeto 
    salvando no banco de dados.
    '''
    def create(self, data):
        data = self.validAttributes(data)
        query = self.db.queryInsert(self.tableName, data);
        self.db.execQuery(query)


    '''
    Faz um select no banco de dados 
    os paramentros nao sao obrigatórios 
    retorna uma list com as tuplas de cada row 
    '''
    def select(self, field=False, value=False, oper=False):
        query = self.db.querySelect(self.tableName, field, value, oper)
        data = self.db.execQuery(query)
        return data


    '''Retorna uma tupla com os valores do primeiro elemento da lista'''
    def first(self, list):
        if len(list) > 0:
            return list[0]
        return None


    '''Busca o objeto com o id indicado como parametro, e retorna a instancia do obseto'''
    def get(self, id):
        data = self.select('id', id)
        if len(data) < 1:
            return None
        i = 0
        for var in self.attributes:
            self.__setattr__(var, data[0][i])
            i += 1
        return self


    '''Retorna o primeiro objeto que tiver o parametro indicado'''
    def getFirstWhere(self, field, value):
        select = self.select(field, value)
        data = self.first(select)
        if data != None:
            return self.get(data[0])

    def getFirst(self):
        select = self.select()
        data = self.first(select)
        if data != None:
            return self.get(data[0])
        return None