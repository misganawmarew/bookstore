from odoo import models, fields, api
from datetime import date

class BookDetails(models.Model):
    _name = 'book.details'
    _description = 'Book Details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    title = fields.Char(required=True, tracking=True)
    author_id = fields.Many2one('res.partner', domain=[('is_author', '=', True)], string="Author", tracking=True)
    publisher = fields.Char(required=True)
    published_date = fields.Date(required=True)
    book_age = fields.Integer(compute='_compute_book_age', store=True)
    isbn = fields.Char(required=True, unique=True)
    is_archived = fields.Boolean(default=False)
    stock_qty = fields.Float()
    price = fields.Monetary(currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', default=lambda self: self.env.company.currency_id)

    @api.depends('published_date')
    def _compute_book_age(self):
        today = date.today()
        for record in self:
            if record.published_date:
                record.book_age = (today - record.published_date).days // 365
            else:
                record.book_age = 0

    @api.constrains('stock_qty', 'price')
    def _check_positive_values(self):
        for record in self:
            if record.stock_qty < 0 or record.price < 0:
                raise ValueError('Stock quantity and price cannot be negative.')
