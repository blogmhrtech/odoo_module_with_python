# -*- coding: utf-8 -*-

# MELQUIADES HDEZ REYES - MODULE IN ODOO

from odoo import models, fields, api

# Creating the tables

"""
IMPORTANT NOTE:  In Python, objects are created from
each class, these objects are handled by odoo.
"""

class catagory_library(models.Model):
    _name = "my_library.catagory"  # private field that are in all odoo classes

    # --- Table fields --- #

    # Important field (name): for searches, relations between objects, ...
    name = fields.Char(String="Name",required=True,help="Enter the name of the category")

    # Other fields
    description = fields.Text(string="Description",help="Enter the description of the category")

    # --- Object relationships | A category has many books --- #
    books = fields.One2many("my_library.book_library","category",string="Books")

class book_library(models.Model):
    _name = "my_library.book_library"  # private field that are in all odoo classes

    # --- Table fields --- #

    # Important field (name): for searches, relations between objects, ...
    name = fields.Char(string="Title",required=True)

    # Other fields
    price = fields.Float(string="Price")
    copies = fields.Integer(string="Copies")
    date= fields.Date(string="Date")
    secondhand = fields.Boolean(string="Second hand")
    state = fields.Selection([('0','Good'),('1','Regular'),('2','Bad')],string="State",default="0")

    # --- Object relationships | Many books have a category --- #
    category = fields.Many2one("my_library.catagory",string="Category",required=True,ondelete="cascade")

    # --- Calculated fields -- #
    total = fields.Float(string="Amount", compute="_total",store=True)

    @api.depends('copies','price') # Notation: When should I call the method
    def _total(self):               # when you change the copies or the price
        for t in self:
            t.total = t.copies*t.price
