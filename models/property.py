from odoo import models, fields , api
from odoo.odoo.exceptions import ValidationError


class Property (models.Model):
    _name= 'property'
    name = fields.Char(required=True, default='new', size=15)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability= fields.Date()
    expected_price = fields.Float()
    selling_price= fields.Float(digits =(0,3))
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area= fields.Integer()
    garden_orientation= fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
        ]
    )
    _sql_constraints = [('unique_name','unique(name)','This name is taken')]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_than_zero(self):
        for rec in self:
            if self.bedrooms==0:
                print('Invalid bedrooms number')
                raise ValidationError('please enter a valid number of bedrooms')

    @api.model_create_multi
    def create(self,vals):
        res= super(Property , self).create(vals)
        print("Added successfully")
        return res

    @api.model
    def _search(self,domain , offset=0, limit=None , order = None):
        res= super (Property, self)._search(domain , offset=0, limit=None , order = None)
        print("search function")
        return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        print("updated successfully")
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("deleted successfully")
        return res