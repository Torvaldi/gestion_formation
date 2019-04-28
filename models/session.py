# -*- coding: utf-8 -*-

from odoo import models, fields, api

class session(models.Model):
    _name = 'gestion_formation.session'

    name = fields.Char()
    nb_participant = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    duree = fields.Char()
    state = fields.Selection(selection=[('prevue', 'Prévue'), ('acceptee', 'Acceptée'), ('en_cours', 'En cours'), ('terminee','Terminée')])