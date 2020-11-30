# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class WebsiteBinary(http.Controller):
    @http.route('/projects', type='http', auth="public", website=True, sitemap=True)
    def proyectos(self, **kw):
        projects = request.env['reliant.project'].sudo().search([])
        values={
            'projects':projects
        }    
        return request.render("theme_reliant.projects", values)

    @http.route(['/projects/<model("reliant.project"):project_id>'], type='http', auth="public", website=True, sitemap=False)
    def proyectos_detalle(self, project_id, **post):
        values={
            'project':project_id
        }
        return request.render("theme_reliant.projects_details", values)
        
    @http.route('/services', type='http', auth="public", website=True, sitemap=True)
    def servicios(self, **kw):
        services = request.env['reliant.service'].sudo().search([])
        values={
            'services':services
        }    
        return request.render("theme_reliant.services", values)
    
    @http.route(['/services/<model("reliant.service"):service_id>'], type='http', auth="public", website=True, sitemap=False)
    def servicios_detalle(self, service_id, **post):
        values={
            'service':service_id
        }
        return request.render("theme_reliant.services_details", values)

    @http.route('/home', type='http', auth="public", website=True, sitemap=True)
    def home(self, **kw):
        return request.render("theme_reliant.home")

    @http.route('/about', type='http', auth="public", website=True, sitemap=True)
    def about(self, **kw):
        return request.render("theme_reliant.about")

    @http.route('/sustainability', type='http', auth="public", website=True, sitemap=True)
    def sustainability(self, **kw):
        return request.render("theme_reliant.sustainability")