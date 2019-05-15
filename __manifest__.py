# -*- coding: utf-8 -*-
{
    'name': "Gestion des formations",

    'summary': """
        Ce module est destiné pour gérer un centre de formation.""",

    'description': """
        Ce module est destiné pour gérer un centre de formation.
    """,

    'author': "Quentin LAURENT",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'formations',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        'security/rights.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        #'views/rights.xml',
        'views/session.xml',
        'views/candidat.xml',
        'views/formateur.xml',
        'views/formation.xml',
        #'wizard/wizard_attestation.xml',
        'views/salle.xml',
        #'views/attestation.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}