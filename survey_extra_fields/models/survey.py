from odoo import models, fields, api, _


class Survey(models.Model):
    _inherit = 'survey.survey'

    user_id = fields.Many2one('res.users', string="User", default=lambda self: self.env.user)
