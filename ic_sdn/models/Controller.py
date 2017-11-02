#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auth: Fagner Jefferson
# V = 0.2 2017

from Model import Model

class Controller(Model):

    attributes = ['id', 'controller', 'name', 'ip', 'port', 'active', 'user', 'password']

    def __init__(self):
        Model.__init__(self)

    def getActive(self):
        activeController = self.getFirstWhere('active', '1')
        if activeController != None:
            return activeController
        return self.getFirst()