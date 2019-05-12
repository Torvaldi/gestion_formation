# -*- coding: utf-8 -*-

from odoo import models,fields

class attestation(models.Model):
    _name = "gestion_formation.attestation"

    candidat = fields.Many2one('gestion_formation.candidat')
    description = fields.Char()
    date = fields.Date()
    formation = fields.Many2one('gestion_formation.formation')