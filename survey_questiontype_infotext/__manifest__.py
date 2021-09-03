# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2019- Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Extend Survey Question Type',
    'version': '14.0.1.0.3',
    'summary': 'This module adds information text only to survey question type.',
    'category': 'base',
    'description': """
         This module adds a new question-type that allows for an extra description to be added in a survey.
         it is maintained in this repository: https://github.com/08arvasi/08arvasi_odoo_survey/tree/14.0/survey_questiontype_infotext
    """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['survey', 'base'],
    'data': [
        'views/survey_question_view.xml',
    ],
    'installable': True,
}
