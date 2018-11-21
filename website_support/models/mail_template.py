# -*- coding: utf-8 -*-
from openerp import api, fields, models

class MailTemplateSupportTicket(models.Model):

    _inherit = "mail.template"

    built_in = fields.Boolean(string="Built in", help="Seperates email templates created by modules and ones created by users")


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.multi
    def message_subscribe_users(self, user_ids=None, subtype_ids=None):
        """ Wrapper on message_subscribe, using users. If user_ids is not
            provided, subscribe uid instead. """
        if user_ids is None:
            user_ids = [self._uid]
        return self.message_subscribe(
            self.env['res.users'].browse(user_ids).mapped('partner_id').ids,
            subtype_ids=subtype_ids)
