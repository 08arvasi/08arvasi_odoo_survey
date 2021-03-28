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
    'name': 'Extend Survey Email Template',
    'version': '13.0.1.0.5',
    'summary': 'This module adds logic to use these fields in the email-templates.',
    'category': 'base',
    'description': """
        This module adds logic to use these fields in the email-templates. \n
        v13.0.1.0.3 Adds a second email-template. \n
    """,
    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['survey', 'base', 'partner_extra_greeting_fields', 'partner_firstname'],
    'data': [
        'views/survey_view.xml',
        'data/mail_template_data.xml',
    ],
    'installable': True,
}
