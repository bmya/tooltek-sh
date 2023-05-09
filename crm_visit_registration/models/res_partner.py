from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_view_related_visits(self):
        action = self.env.ref('crm_visit_registration.action_visit_list').read()[0]
        action['domain'] = [('partner_id', '=', self.id)]
        action['context'] = {'default_partner_id': self.id}
        return action