from odoo import models, fields, api, _


class Survey(models.Model):
    _inherit = 'survey.survey'

    user_id = fields.Many2one('res.users', string="User", compute='_user_id')

    @api.depends('title')
    def _user_id(self):
        for rec in self:
            rec.user_id = self.env.user.id


class SurveyUser(models.Model):
    _inherit = 'survey.user_input'

    user_id = fields.Many2one('res.users', string="User", compute='_user_id')

    @api.depends('partner_id')
    def _user_id(self):
        for rec in self:
            rec.user_id = self.env.user.id
