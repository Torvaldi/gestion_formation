# -*- coding: utf-8 -*-

from odoo import models, fields, api

class candidat(models.Model):
    _name = 'gestion_formation.candidat'

    name = fields.Char()
    num_ins = fields.Integer()
    sessions = fields.Many2many('gestion_formation.session')

    _sql_constraints = [('num_ins_unique', 'UNIQUE (num_ins)', 'Numéro d\'inscription déjà utilisé')]