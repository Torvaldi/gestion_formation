# -*- coding: utf-8 -*-

from odoo import models, fields, api

class formation(models.Model):
    _name = 'gestion_formation.formation'

    name = fields.Char()
    price = fields.Float()
    sessions = fields.One2many('gestion_formation.session', 'formation')