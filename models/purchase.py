# -*- coding: utf-8 -*-
# This module and its content is copyright of Technaureus Info Solutions Pvt. Ltd. - ©
# Technaureus Info Solutions Pvt. Ltd 2020. All rights reserved.

from odoo import api, models, _
from odoo.exceptions import UserError
from datetime import datetime


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def send_whatsapp_msg(self):
        state = ''
        if self.state == 'draft':
            state = 'request for quotation ' + self.name + ' has been created.'
        elif self.state == 'sent':
            state = 'request for quotation ' + self.name + ' has been sent successfully.'
        elif self.state == 'to_approve':
            state = 'Purchase Order ' + self.name + ' is waiting for approval'
        elif self.state == 'purchase':
            state = 'Purchase Order ' + self.name + ' has been confirmed.'
        elif self.state == 'done':
            state = 'Purchase Order ' + self.name + ' has been locked.'
        elif self.state == 'cancel':
            state = 'Purchase Order ' + self.name + ' has been cancelled.'
        message = ' *Dear%20' + self.partner_id.name + '* ' + ',' + ' %0a' + '*Your%20' + state + \
                  '* %0a%0a%20%20%20' + ' *Order Date:* ' + datetime.strptime(
            str(self.date_order), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y %H:%M:%S") + ',%0a%20%20%20'
        if self.date_planned:
            message = message + ' *Scheduled Date:* ' + datetime.strptime(str(self.date_planned),
                                                                          '%Y-%m-%d %H:%M:%S').strftime(
                "%d-%m-%Y %H:%M:%S") + ',%0a%20%20%20'
        if self.date_approve:
            message = message + ' *Approval Date:* ' + datetime.strptime(str(self.date_approve),
                                                                         '%Y-%m-%d').strftime(
                "%d-%m-%Y") + ',%0a%20%20%20'
        message = message + ' *Amount Untaxed:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_untaxed) + ',%0a%20%20%20' + ' *Taxes:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_tax) + ',%0a%20%20%20' + '*Amount Total:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_total) + '%0a%0a _Thanks and Regards_,%20%0a%20*' + self.user_id.name + '* ,%0a%20*' + self.company_id.name + '* '
        message_string = ''
        message = message.split(' ')
        for msg in message:
            message_string = message_string + msg + '%20'
        message_string = message_string[:(len(message_string) - 3)]
        mobile = self.partner_id.mobile
        if mobile:
            mobile_num = self.partner_id.mobile.replace(" ", "").replace("+", "").replace("-", "").replace("(",
                                                                                                           "").replace(
                ")", "")
            return {
                'type': 'ir.actions.act_url',
                'url': "https://api.whatsapp.com/send?phone=" + mobile_num + "&text=" + message_string,
                'target': '_blank',
                'res_id': self.id,
            }
        else:
            raise UserError(_('Please Configure Whatsapp Number with country code to Vendor.'))

    def send_whatsapp_msg_web(self):
        state = ''
        if self.state == 'draft':
            state = 'request for quotation ' + self.name + ' has been created.'
        elif self.state == 'sent':
            state = 'request for quotation ' + self.name + ' has been sent successfully.'
        elif self.state == 'to_approve':
            state = 'Purchase Order ' + self.name + ' is waiting for approval'
        elif self.state == 'purchase':
            state = 'Purchase Order ' + self.name + ' has been confirmed.'
        elif self.state == 'done':
            state = 'Purchase Order ' + self.name + ' has been locked.'
        elif self.state == 'cancel':
            state = 'Purchase Order ' + self.name + ' has been cancelled.'
        message = ' *Dear%20' + self.partner_id.name + '* ' + ',' + ' %0a' + '*Your%20' + state + \
                  '* %0a%0a%20%20%20' + ' *Order Date:* ' + datetime.strptime(
            str(self.date_order), '%Y-%m-%d %H:%M:%S').strftime("%d-%m-%Y %H:%M:%S") + ',%0a%20%20%20'
        if self.date_planned:
            message = message + ' *Scheduled Date:* ' + datetime.strptime(str(self.date_planned),
                                                                          '%Y-%m-%d %H:%M:%S').strftime(
                "%d-%m-%Y %H:%M:%S") + ',%0a%20%20%20'
        if self.date_approve:
            message = message + ' *Approval Date:* ' + datetime.strptime(str(self.date_approve),
                                                                         '%Y-%m-%d %H:%M:%S').strftime(
                "%d-%m-%Y %H:%M:%S") + ',%0a%20%20%20'
        message = message + ' *Amount Untaxed:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_untaxed) + ',%0a%20%20%20' + ' *Taxes:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_tax) + ',%0a%20%20%20' + '*Amount Total:* ' + str(self.currency_id.symbol) + '%20' + str(
            self.amount_total) + '%0a%0a _Thanks and Regards_,%20%0a%20*' + self.user_id.name + '* ,%0a%20*' + self.company_id.name + '* '
        message_string = ''
        message = message.split(' ')
        for msg in message:
            message_string = message_string + msg + '%20'
        message_string = message_string[:(len(message_string) - 3)]
        mobile = self.partner_id.mobile
        if mobile:
            mobile_num = self.partner_id.mobile.replace(" ", "").replace("+", "").replace("-", "").replace("(",
                                                                                                           "").replace(
                ")", "")
            return {
                'type': 'ir.actions.act_url',
                'url': "https://web.whatsapp.com/send?phone=" + mobile_num + "&text=" + message_string,
                'target': '_blank',
                'res_id': self.id,
            }
        else:
            raise UserError(_('Please Configure Whatsapp Number with country code to Vendor.'))
