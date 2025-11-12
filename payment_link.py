from odoo import api, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def payment_link(self):
        self.ensure_one()
        self._portal_ensure_token()
        payment_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return f"{payment_url}/my/invoices/{self.id}?access_token={self.access_token}"
