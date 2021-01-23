# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json

class WebsiteBinary(http.Controller):
    @http.route('/projects', type='http', auth="public", website=True, sitemap=True)
    def proyectos(self, **kw):
        projects = request.env['reliant.project'].sudo().search([])

        list_proj_countries = []
        list_proj_countries_unique = []
        
        print('Llenar la lista de paises')
        for proj in projects:
            if proj.location_country.id not in list_proj_countries:
                list_proj_countries.append(proj.location_country.id)

        print('Llenar la lista de paises unicos')
        

        values={
            'projects':projects,
            'countries': request.env['res.country'].sudo().search([('id','in',list_proj_countries)])
        }
        print(values)
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
        allprojects = request.env['reliant.project'].sudo().search([],limit=3)
        

        values={
            'services':services,
            'allprojects':allprojects
        }    
        return request.render("theme_reliant.services", values)

    @http.route(['/ajaxtocontroller'], type='json', methods=['POST'], auth="public", website=True)
    def changeServicios(self, service):
        print(service) #2
        list_serv = []
        cont = 1
        cont_proj = 0
        #list_data = []
        list_serv.append(service)
        #print(list_serv) #['2']
        select_service = request.env['reliant.service'].sudo().search([('id', '=', service)])
        #print(select_service.name_service)
        allprojects = request.env['reliant.project'].sudo().search([('services_ids','in',list_serv)],limit=3)


        """
        for project in allprojects:
            cont_proj = cont_proj + 1


        if(cont_proj > 0):
            for project in allprojects:
                if(cont_proj == 1):
                    if (cont == 1):
                        img1 = project.image
                        name_project1 = project.name
                        #print(img1)
                    
                    img2 = project.image
                    name_project2 = project.name
                    img3 = project.image
                    name_project3 = project.name

                if(cont_proj == 2):
                    if (cont == 1):
                        img1 = project.image
                        name_project1 = project.name

                    if (cont == 2):
                        img2 = project.image
                        name_project2 = project.name

                    img3 = project.image
                    name_project3 = project.name

                if(cont_proj == 3): 
                    print('entra de 3 imagenes')  
                    if (cont == 1):
                        img1 = project.image
                        name_project1 = project.name

                    if (cont == 2):
                        img2 = project.image
                        name_project2 = project.name   
                    
                    if (cont == 3):
                        img3 = project.image
                        name_project3 = project.name

                cont = cont + 1

        """ 
        l_project = []

        cont = 1

        for project in allprojects:
            l_project.append({'imagen_project':project.image,
                'nombre_project':project.name,
                'cont_project': cont
                })
            cont += 1


        return {"titulo_service": select_service.name_service,
                "descripcion_service": select_service.description_service,
                "project": l_project
                #"imagen_project_1": img1,
                #"imagen_project_2": img2,
                #"imagen_project_3": img3,
                #"nombre_project_1": name_project1,
                #"nombre_project_2": name_project2,
                #"nombre_project_3": name_project3
                }
    """
    @http.route(['/ajaxtocontroller2'], type='json', methods=['POST'], auth="public", website=True)
    def changeProjects(self, **kw):
        list_proj_countries = []
        list_proj_countries_unique = []
        projects = request.env['reliant.project'].sudo().search([])
        
        print('Llenar la lista de paises')
        for proj in projects:
            data = {
                "pais" : proj.location_country.name
            }
            list_proj_countries.append(data)

        print('Llenar la lista de paises unicos')
        for item in list_proj_countries:
            if item not in list_proj_countries_unique:
                list_proj_countries_unique.append(item)
        
        return {"lista_countries_unicos": list_proj_countries_unique}
    """

    @http.route(['/services/<model("reliant.service"):service_id>'], type='http', auth="public", website=True, sitemap=False)
    def servicios_detalle(self, service_id, **post):
        values={
            'service':service_id
        }
        return request.render("theme_reliant.services_details", values)

    @http.route('/home', type='http', auth="public", website=True, sitemap=True)
    def home(self, **kw):
        home_to_services = request.env['reliant.service'].sudo().search([],limit=6,order="sequence")
        home_to_projects = request.env['reliant.project'].sudo().search([],limit=6)
        values={
            'home_to_services':home_to_services,
            'home_to_projects':home_to_projects
        } 

        return request.render("theme_reliant.home",values)

    @http.route('/about', type='http', auth="public", website=True, sitemap=True)
    def about(self, **kw):
        return request.render("theme_reliant.about")

    @http.route('/sustainability', type='http', auth="public", website=True, sitemap=True)
    def sustainability(self, **kw):
        return request.render("theme_reliant.sustainability")
        
    @http.route('/contacts', type='http', auth="public", website=True, sitemap=True)
    def contacts(self, **kw):
        return request.render("theme_reliant.contacts")

    @http.route(['/job_opportunities/<model("reliant.job.opportunity"):job_id>'], type='http', auth="public", website=True, sitemap=False)
    def job_detail(self, job_id, **post):
        values={
            'job':job_id
        }
        return request.render("theme_reliant.job_opportunities_detail", values)


    @http.route('/job_opportunities', type='http', auth="public", website=True, sitemap=True)
    def jobs_opportunities(self, **kw):
        opportunities = request.env['reliant.job.opportunity'].sudo().search([])

        l_country = []
        l_department = []
        l_site = []
        l_language = []
        for o in opportunities:
            if o.country.id not in l_country:
                l_country.append(o.country.id)
            if o.department.id not in l_department:
                l_department.append(o.department.id)
            if o.site.id not in l_site:
                l_site.append(o.site.id)
            if o.language.id not in l_language:
                l_language.append(o.language.id)



        values={
            'opportunities':opportunities,
            'countries':request.env['res.country'].sudo().search([('id','in',l_country)]),
            'departments':request.env['reliant.job.department'].sudo().search([('id','in',l_department)]),
            'sites':request.env['reliant.job.site'].sudo().search([('id','in',l_site)]),
            'languages_opportunity':request.env['reliant.job.language'].sudo().search([('id','in',l_language)]),
        }    
        return request.render("theme_reliant.job_opportunities", values)


    @http.route(['/change/job'], type='json', methods=['POST'], auth="public", website=True)
    def changeJob(self, country, department, site, language):
        print(country, department, site, language)

        dominio = []

        if int(country) != 0: 
            dominio.append(('country','=',int(country)))
        if int(department) != 0: 
            dominio.append(('department','=',int(department)))
        if int(site) != 0: 
            dominio.append(('site','=',int(site)))
        if int(language) != 0: 
            dominio.append(('language','=',int(language)))

        op = []

        opportunities = request.env['reliant.job.opportunity'].sudo().search(dominio)

        for o in opportunities:
            op.append({
                'id':o.id,
                'position': o.position.name,
                'location': o.location.name,
                'site': o.site.name,
                'closing_date': o.closing_date,
                'category_job_opportunity': o.category_job_opportunity.name,
                'description_job_opportunity': o.description_job_opportunity,
                })
                

        return {'opportunities':op}
