from odoo import models, fields

class Player(models.Model):
    _name = 'player'
    _description = 'player'
    name = fields.Char(string = 'name', required = True)
    image = fields.Binary(string = 'image', attachment = True)
    country = fields.Char(string = 'Country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string = 'Gender' ,default = 'male')
    day_of_birth = fields.Datetime( string = 'Day of birth')
    position = fields.Char('Position')

    height = fields.Float(string = 'Height')
    weight = fields.Float(string = 'Weight')