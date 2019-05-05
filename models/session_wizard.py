from odoo import models, fields, api

class session(models.TransientModel):
    _name = 'gestion_formation.session_wizard'

    name = fields.Char()
    #nb_participant = fields.Integer()
    date_debut = fields.Date()
    date_fin = fields.Date()
    #duree = fields.Char()
    #state = fields.Selection(selection=[('prevue', 'Prévue'), ('acceptee', 'Acceptée'), ('en_cours', 'En cours'), ('terminee','Terminée')])
    formation = fields.Many2one('gestion_formation.formation')
    formateurs = fields.Many2many('gestion_formation.formateur')
    candidats = fields.Many2many('gestion_formation.candidat')
    #salles = fields.Many2many('gestion_formation.salle')

    # @api.one
    # @api.constrains('date_debut', 'date_fin')
    # def _check_dates(self):
    #     if self.date_debut and self.date_fin:
    #         if self.date_debut <= self.date_fin:
    #             return False
    #     return True

    # @api.onchange('date_debut', 'date_fin')
    # def _onchange_date(self):
    #     if self.date_debut and self.date_fin:
    #         if self.date_debut <= self.date_fin:
    #             diff = abs(self.date_fin - self.date_debut).days + 1
    #             if diff <= 1:
    #                 self.duree = '1 jour'
    #             else:
    #                 self.duree = '{} jours'.format(diff)