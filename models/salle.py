# -*- coding: utf-8 -*-

from odoo import models, fields, api

class salle(models.Model):
    _name = 'gestion_formation.salle'

    name = fields.Char()
    libre = fields.Boolean()
    nb_place = fields.Integer(default='20')
    sessions = fields.Many2many('gestion_formation.session')