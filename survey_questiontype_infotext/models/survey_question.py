from odoo import models, api, fields, _


class SurveyQuestions(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection(selection_add=[('information_only', 'Information Text Only')])
    information = fields.Text(string="Information")
