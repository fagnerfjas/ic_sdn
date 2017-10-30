#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

import click
from ic_sdn.models.Model import Model
from ic_sdn.models.Controller import Controller

@click.group(invoke_without_command=True)
def cli():
    """Informacoes e configuracao da aplicacao
    IC SDN (Interface de Comando SDN)"""
    pass



@cli.command()
def migrate():
    '''Cria o diretório ~/.ic_sdn, e o arquivo de banco de dados com as tabelas'''
    model = Model()
    click.echo( model.migrate() )


@cli.command()
@click.option('--add', '-a', is_flag=True)
def ctl(add):
    '''Controllers configuration'''

    if add:
        ctl = click.prompt('Is the controller floodlight, odl or ryu')
        name = click.prompt('Name')
        ip = click.prompt('IP')
        port = click.prompt('Port')
        user = click.prompt('User')
        user = click.prompt('Password', hide_input=True)

    controler = Controller()
    c = controler.create({'name': 'Nome Controlador', 'ip': 4127, 'jack': 4098})

    click.echo(c)