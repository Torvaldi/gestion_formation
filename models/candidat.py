# -*- coding: utf-8 -*-

from odoo import models, fields, api

class candidat(models.Model):
    _name = 'gestion_formation.candidat'

    name = fields.Char()
    num_ins = fields.Integer()
