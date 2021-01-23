# -*- coding: utf-8 -*-
import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)

class ThemeBeauty(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_reliant_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('theme_reliant.template_header_magazine_proyect_reliant')
        self.disable_view('website.footer_custom')
        self.enable_view('theme_reliant.footer_reliant')


class reliant_project(models.Model):
    _name = 'reliant.project'
    _description = 'Proyecto Reliant'
    _rec_name = 'name'

    name = fields.Char(string='Proyecto')
    location_country = fields.Many2one(string='Pais',required=False, comodel_name='res.country')
    location_city = fields.Many2one('res.city', string='Ciudad')
    client_name = fields.Char(string='Cliente')
    commodity = fields.Char(string='Commodity')
    description = fields.Text(string='Descripción')
    image =  fields.Binary(string="Imagen")
    image_detail_1 = fields.Binary(string="Imagen Detalle 1")
    image_detail_2 = fields.Binary(string="Imagen Detalle 2")
    image_detail_3 = fields.Binary(string="Imagen Detalle 3")
    services_ids = fields.Many2many('reliant.service',
        'reliant_project_reliant_service_rel',
        string='Services')

    #fieldmany2many = fields.Many2Many('model.name','your_many2many_table_name','colum1','colum2',string="my many2many field")




class reliant_service(models.Model):
    _name = 'reliant.service'
    _description = 'Servicio Reliant'
    _rec_name = 'name_service'

    name_service = fields.Char(string='Servicio')
    description_service = fields.Text(string='Descripción')
    sequence = fields.Integer(string="Sequence")
    


class reliant_job_department(models.Model):
    _name = 'reliant.job.department'
    _description = 'Departamento Oportunidad Trabajo Reliant'

    name = fields.Char(string='Departamento')

class reliant_job_site(models.Model):
    _name = 'reliant.job.site'
    _description = 'Sitio Oportunidad Trabajo Reliant'

    name = fields.Char(string='Sitio')

class reliant_job_language(models.Model):
    _name = 'reliant.job.language'
    _description = 'Lenguaje Oportunidad Trabajo Reliant'

    name = fields.Char(string='Lenguaje')

class reliant_job_position(models.Model):
    _name = 'reliant.job.position'
    _description = 'Posición Oportunidad Trabajo Reliant'


    name = fields.Char(string='Posición')
class reliant_job_location(models.Model):
    _name = 'reliant.job.location'
    _description = 'Locación Oportunidad Trabajo Reliant'

    name = fields.Char(string='Ubicación')

class reliant_job_category(models.Model):
    _name = 'reliant.job.category'
    _description = 'Categoría Cierre Oportunidad Trabajo Reliant'

    name = fields.Char(string='Categoría')



class reliant_job_opportunity(models.Model):
    _name = 'reliant.job.opportunity'
    _description = 'Oportunidad de Trabajo Reliant'
    _rec_name = 'description_job_opportunity'

    country = fields.Many2one(comodel_name='res.country', string='Pais')
    department = fields.Many2one('reliant.job.department', string='Departamento')
    site = fields.Many2one('reliant.job.site', string='Sitio')
    language = fields.Many2one('reliant.job.language', string='Lenguaje')
    position = fields.Many2one('reliant.job.position', string='Posición')
    location = fields.Many2one('reliant.job.location', string='Ubicación')
    closing_date = fields.Date(string='Fecha de cierre')
    description_job_opportunity = fields.Text(string='Descripción Oportunidad de Trabajo')
    category_job_opportunity = fields.Many2one('reliant.job.category', string='Categoría Oportunidad de Trabajo')
    state = fields.Selection(
        string="Estado",
        selection=[
            ('cancel', 'Cancelado'),
            ('confirm', 'Confirmado'),
            ('draft', 'Borrador'),
        ], default="confirm"
    )   
    