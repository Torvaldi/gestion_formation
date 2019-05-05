# -*- coding: utf-8 -*-

from odoo import models, fields, api

class formateur(models.Model):
    _name = 'gestion_formation.formateur'

    name = fields.Char()
    matricule = fields.Integer()
    diplome = fields.Char()
    sessions = fields.Many2many('gestion_formation.session')

    _sql_constraints = [('matricule_unique', 'UNIQUE (matricule)', 'Numéro de matricule déjà utilisé')]
