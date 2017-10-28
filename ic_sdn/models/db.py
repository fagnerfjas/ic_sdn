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
        return 'Database ok!'



    '''
        Faz a conexão com o banco de dados SqLite, 
        Cria o arquivo caso ele não exista
    '''
    def conect(self):
        self.conexao = sqlite3.connect(self.pathDb + 'ic_sdn.db')
        return self.conexao.cursor()

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
        dados = data.execute('SELECT * FROM ' + table).fetchall()
        self.disconect()
        return dados

    '''
        Seta as configuração do controlador
    '''
    def setConfig(self, ip, port, name):
        data = self.conect()
        data.execute(
            'UPDATE config set ip="{new_ip}", port={new_port}, name="{new_name}"'.format(new_ip=ip, new_port=port,
                                                                                         new_name=name))
        self.salveDisconect()