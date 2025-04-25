from odoo import models, fields, api

class CreateAuthorWizard(models.TransientModel):
    _name = 'create.author.wizard'
    _description = 'Create Author Wizard'

    name = fields.Char(required=True)
    nationality = fields.Char()
    biography = fields.Text()

    def create_author(self):
        self.env['res.partner'].create({
            'name': self.name,
            'nationality': self.nationality,
            'biography': self.biography,
            'is_author': True,
        })
