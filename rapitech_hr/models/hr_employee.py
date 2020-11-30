# -- coding: utf-8 --
from odoo import models, fields, api
from datetime import datetime


def year_now():
    return datetime.now().year

YEAR_SELECTION = [(str(year), year) for year in range(1935, year_now()+1)]



class hr_bond_family(models.Model): 
    _name = 'hr.bond.family'
    _description = 'table bond family'

    name = fields.Char('Vinculo Familiar')
    _description = 'table vinculo familiar'

class hr_type_payment(models.Model):
    _name = 'hr.type.payment'
    _description = 'table type payment'

    name= fields.Char(string='Tipo de Pago')

class hr_reason_termination(models.Model):
    _name = 'hr.reason.termination'
    _description = 'table reason termination'

    name = fields.Char('Motivo de Cese')

class hr_special_situation(models.Model): 
    _name = 'hr.special.situation'
    _description = 'Situación Especial'

    name = fields.Char(string='Situacion Especial')


class hr_type_employee(models.Model):
    _name = 'hr.type.employee'
    _description = 'Tipo de Trabajador'

    name = fields.Char(string='Tipo de Trabajador')

class hr_pension_fund(models.Model):
    _name = 'hr.pension.fund'
    _description = 'Fondo de Pensiones'

    name = fields.Char(string='Fondo de Pensiones')
    percentage_incoming_required = fields.Float('% de aporte obligatorio')
    commission_on_flow = fields.Float('Comisión sobre flujo')
    commission_on_flow_mix = fields.Float('Comisión sobre flujo - Mixta')
    sure_prime = fields.Float('Prima de Seguros')
    maximum_insurable_remuneration = fields.Float('Remuneración máxima asegurable')

class hr_period(models.Model):
    _name = 'hr.period'
    _description = 'Periodo'

    month_period = fields.Selection(
        string="Mes",
        selection=[
            ('ene', 'Enero'),
            ('feb', 'Febrero'),
            ('mar', 'Marzo'),
            ('abr', 'Abril'),
            ('may', 'Mayo'),
            ('jun', 'Junio'),
            ('jul', 'Julio'),
            ('ago', 'Agosto'),
            ('sep', 'Septiembre'),
            ('oct', 'Octubre'),
            ('nov', 'Noviembre'),
            ('dic', 'Diciembre'),
        ]
    )
    year_period = fields.Selection(selection=YEAR_SELECTION,
                                    string='Año')
    def name_get(self):
        result = []
        for line in self:
            name = line.month_period + '-' + line.year_period[2:4] 
            result.append((line.id, name))
        return result


class hr_family(models.Model):
    _name = 'hr.family'
    _description = 'Familiares del Trabajador'

    #Datos Familiares
    hr_employee_id = fields.Many2one('hr.employee', string='Empleado')
    names_surnames_family = fields.Char('Nombres y Apellidos')
    bond_family = fields.Many2one('hr.bond.family', string='Vinculo Familiar')
    birthdate_family = fields.Date(string='Fecha de Nacimiento')
    type_document_id = fields.Many2one('hr.document.type',
        string="Tipo Documento Identificacion")
    doc_number = fields.Char('Numero de Documento')


class hr_other_income(models.Model):
    _name = 'hr.other.income'
    _description = 'table other income'
    #Ext_ingreso
    hr_employee_id = fields.Many2one('hr.employee', string='Empleado')
    period = fields.Many2one('hr.period',string='Periodo Afecta')
    total_received = fields.Float('Total Percibido')
    total_withheld = fields.Float('Total Retenido') 
    
    
class HRDocumentType(models.Model):
    _name = 'hr.document.type'
    _description = 'Tipo de Documento de Trabajador'

    name = fields.Char('Tipo de Documento', required=True)

class employee(models.Model):
    _inherit = "hr.employee"

    code = fields.Char('Codigo')
    last_name = fields.Char('Apellido Paterno')
    mother_last_name = fields.Char('Apellido Materno')
    names = fields.Char('Nombres')

    #Datos Personales
    type_document_id = fields.Many2one('hr.document.type',
        string="Tipo Documento Identificacion")
    document_number = fields.Char('Numero Documento')
    
    pension_fund = fields.Many2one('hr.pension.fund', string='Fondo de Pensiones')
    code_cussp = fields.Char('Codigo CUSSP')
    date_enrollment_afp = fields.Date('Fecha de Inscripcion AFP')
    commission_scheme = fields.Selection(
        string="Esquema de Comision",
        selection=[
            ('mixta', 'Mixta'),
            ('flujo', 'Flujo'),
        ], default="mixta"
    )
    detailed_address = fields.Char('Domicilio Detallado')

    #Adicional
    not_consider_calculation = fields.Boolean('No considerar en el Calculo', default=False)
    no_declarar_al_pdt = fields.Boolean('No declarar al PDT', default=False)
    no_affection_fifth = fields.Boolean('No afecto a Quinta', default=False)

    #Datos Laborales

    date_entry = fields.Date('Fecha de Ingreso')
    type_employee = fields.Many2one(string='Tipo Trabajador', comodel_name='hr.type.employee')
    affiliate_eps= fields.Boolean('Afiliado a EPS?', default=False)
    date_termination = fields.Date('Fecha de Cese')
    reason_termination = fields.Many2one(string='Motivo de Cese', comodel_name='hr.reason.termination')
    assignment_family = fields.Boolean('Asignacion Familiar?', default=False)
    bank_account_of_assets = fields.Char('Cuenta Bancaria de Haberes')
    bank_id = fields.Many2one(string='Banco', comodel_name='res.bank') 
    account_cts = fields.Char('Numero de Cuenta CTS')
    bank_cts_id = fields.Many2one(string='Banco CTS', comodel_name='res.bank')


    #Datos Complementarios
    special_situation = fields.Many2one(string='Situacion Especial', comodel_name='hr.special.situation')
    type_payment = fields.Many2one(string='Tipo de Pago', comodel_name='hr.type.payment')

    #Datos Familiares
    family_ids = fields.One2many('hr.family','hr_employee_id',string="Familia")

    #Otros ingresos de quinta Categoria
    other_income_ids = fields.One2many('hr.other.income','hr_employee_id', string="Otros ingresos ")

    def name_get(self):
        result = []
        for line in self:
            l_name = line.name
            if line.last_name:
                l_name+=' '+line.last_name
            if line.mother_last_name:
                l_name+=' '+line.mother_last_name
            name = l_name
            result.append((line.id, name))
        return result