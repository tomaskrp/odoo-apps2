# -*- encoding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request

from odoo.addons.portal.controllers.portal import CustomerPortal


class CustomerPortalExtend(CustomerPortal):

    @http.route()
    def home(self, **kw):
        response = super(CustomerPortalExtend, self).home(**kw)
        portal_group = request.env.ref('base.group_portal').sudo()
        if request.env.user.id in portal_group.users.ids:
            response.qcontext['show_your_documents'] = False
        else:
            response.qcontext['show_your_documents'] = True
        return response
