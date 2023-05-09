from odoo import models, fields, api


class CrmVisit(models.Model):
    _name = 'crm.visit'
    _description = 'CRM Visit Registration'

    name = fields.Char(string='Visit Name')
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    visit_date = fields.Datetime(string='Visit Date', default=fields.Datetime.now)
    has_sale = fields.Boolean(string='Sale Made')
    comments = fields.Text(string='Comments')