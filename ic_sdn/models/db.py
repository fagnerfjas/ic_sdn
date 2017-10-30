#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

import sqlite3
import os.path

'''	Classe de gerenciamento de banco de dados '''
class Db:

    conexao = ''
    pathDb = ''

    '''Constructor'''
    def __init__(self):
        self.pathDb = os.path.expanduser("~/.ic_sdn/")


    '''Cria o diretório de base de dados, e cria as tabelas do banco de dados'''
    def migrate(self):
        if self.isConfigured():
            return 'Ok! Database is already configured!'
        self.createDirectory()

        data = self.conect()
        data.execute(
            '''CREATE TABLE IF NOT EXISTS controllers(
                  id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  controller TEXT, 
                  name TEXT,
                  ip TEXT, 
                  port INT,
                  active INTEGER DEFAULT 0,
                  user TEXT,
                  password TEXT
                  )
            ''')

        if len(data.execute('''SELECT * FROM controllers''').fetchall()) < 1:
            data.execute(
                """INSERT INTO controllers (controller, name, ip, port, user, password) 
                    VALUES ('floodlight', 'Controlador de teste', '192.168.1.1', 6635, 'admin', 'admin' )""")
        self.saveDisconect()
        return 'Ok! Database configured!'



    '''
        Faz a conexão com o banco de dados SqLite, 
        Cria o arquivo caso ele não exista
    '''
    def conect(self):
        try:
            self.conexao = sqlite3.connect(self.pathDb + 'ic_sdn.db')
            return self.conexao.cursor()
        except sqlite3.OperationalError:
            print False


    '''
        Disconecta do banco de dados
    '''
    def disconect(self):
        self.conexao.close()



    '''
        Salva os dados da query inseridas na conexão 
        e disconecta do banco de dados
    '''
    def saveDisconect(self):
        self.conexao.commit()
        self.conexao.close()



    '''
        Cria o diretório indicado na variável <pathDb>,
        Caso não tenha permissão o diretório deverá ser criado pelo usuário
    '''
    def createDirectory(self):
        if not self.isConfigured():
            os.mkdir(self.pathDb)



    '''Verifica se o arquivo de configuração já foi criado'''
    def isConfigured(self):
        if not os.path.isdir(self.pathDb):
            return False
        return True



    '''
        Retorna a configuração atual do sistema
    '''
    def getAll(self, table):
        data = self.conect()
        if data:
            query = data.execute('SELECT * FROM ' + table).fetchall()
            self.disconect()
        else:
            return data
        return query



    '''
        Seta as configuração do controlador
    '''
    def setConfig(self, ip, port, name):
        data = self.conect()
        data.execute(
            'UPDATE config set ip="{new_ip}", port={new_port}, name="{new_name}"'.format(new_ip=ip, new_port=port,
                                                                                         new_name=name))
        self.salveDisconect()


    '''
        Recebe um mapa do tipo chave valor, separa as chaves e valores nos formatos 
        para uma query sql
        Ex: 
        recebe -> {'name': 'Nome Controlador', 'ip': 4127, 'jack': 4098}
        retorna -> {'values': "(4127,'Nome Controlador', 4098)", 'columns': '(ip,name,jack)'}
    '''
    def columnAndVluesToQuery(self, data):
        columns = data.keys()
        columns = '('+','.join(columns)+')'

        values = data.values()
        strValues = '('
        for x in values:
            if isinstance(x, str) or isinstance(x, unicode):
                strValues += '\''+ x +'\','
            else:
                strValues += str(x) +','
        values = strValues[:-1] + ')'

        return {'columns': columns, 'values': values}


    '''
        Recebe um mapa e transforma em uma query para insert no fomrmato sql 
       Ex:
       recebe ->  {'name': 'Nome Controlador', 'ip': 4127, 'jack': 4098} e o nome da tabela ex: 'controllers'
       retorna -> INSERT INTO controllers (ip,name,jack) VALUES (4127,'Nome Controlador', 4098); 
    '''
    def queryInsert(self, tableName, data):
        colVal = self.columnAndVluesToQuery(data)

        query = '''INSERT INTO {table} {col} VALUES {val};'''\
            .format(col=colVal['columns'], val=colVal['values'], table=tableName)
        return query