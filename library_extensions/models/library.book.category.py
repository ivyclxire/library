from odoo import models, fields

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Book Category"
    _order = "name"

    name = fields.Char(string="Category Name", required=True, unique=True)
    
class LibraryBook(models.Model):
    _inherit = "library.book"

    category_id = fields.Many2many('library.book.category', string="Categories")

