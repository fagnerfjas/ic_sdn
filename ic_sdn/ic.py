#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from ic_sdn.models.Model import Model
from ic_sdn.models.Controller import Controller

@click.group(invoke_without_command=True)
def cli():
    """Informacoes e configuracao da aplicacao
    IC SDN (Interface de Comando SDN)"""
    model = Model()
    click.echo('sdfgdfgvdbhdbhhhgbfh dgbhdvhdgf')


@cli.command()
def migrate():
    '''Cria o diretório ~/.ic_sdn, e o arquivo de banco de dados com as tabelas'''
    model = Model()
    model.migrate()
    click.echo( migrate )


@cli.command()
def ctl():
    '''Controllers configuration'''
    controler = Controller()
    click.echo(controler.all())