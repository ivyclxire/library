from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Category Name", required=True, unique=True)
    