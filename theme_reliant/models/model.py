# -*- coding: utf-8 -*-
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class ThemeBeauty(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_reliant_post_copy(self, mod):
        self.disable_view('website.template_header_default')

        self.enable_view('theme_reliant.template_header_magazine_proyect_reliant')
        self.enable_view('website.footer_custom')

class reliant_project(models.Model):
    _name = 'reliant.project'
    _description = 'Proyecto Reliant'
    _rec_name = 'name'

    name = fields.Char(string='Proyecto')
    location_country = fields.Many2one(string='Pais',required=False, comodel_name='res.country')
    location_city = fields.Many2one('res.city', string='Ciudad')
    description = fields.Text(string='Descripción')
    image =  fields.Binary(string="Imagen")


class reliant_service(models.Model):
    _name = 'reliant.service'
    _description = 'Servicio Reliant'
    _rec_name = 'name_service'

    name_service = fields.Char(string='Servicio')
    description_service = fields.Text(string='Descripción')
    image_service =  fields.Binary(string="Imagen")
    
