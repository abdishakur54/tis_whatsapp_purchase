# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd. - ©
# Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

{
    'name': 'WhatsApp Purchase Integration ',
    'version': '16.0.0.0',
    'summary': 'Send Whatsapp message to vendor in Purchase',
    'sequence': 1,
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'description': 'Show Whatsapp icon on RFQ and Purchase order to send message to selected vendor.',
    'website': 'http://www.technaureus.com',
    'price': 8,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'depends': [
        'purchase'
    ],
    'data': [
        'views/purchase_views.xml',
    ],
    'qweb': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
