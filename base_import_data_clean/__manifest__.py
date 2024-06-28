{
    'name': 'Base import data clean',
    'description': """
Remove unnecessary whitespaces from imported data before saving into the database.
==================================================================================

Extends Odoo's file import system:
""",
    'summary': 'Cleanup import data before saving into the database.',
    'depends': ['web', 'base_import'],
    'version': '17.0.1.0.1',
    'category': 'Productivity',
    'author': 'Dipendra Karki<tech.enthusiast23@gmail.com>',
    'data': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
}
