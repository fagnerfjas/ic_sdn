#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

from Model import Model

class Controller(Model):

    attributes = ['controller', 'name', 'ip', 'port', 'user', 'password']

    def __init__(self):
        Model.__init__(self)