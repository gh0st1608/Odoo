# -*- coding: utf-8 -*-

# from odoo import models, fields, api


from odoo import models, fields, api
from odoo.exceptions import ValidationError

###########################################################

class CategoriaIngreso(models.Model):
   _name = 'modulo1.categoria.ingreso'

   descripcion = fields.Char('Descripcion', required=True)
   activo = fields.Boolean('Activo?', default=True)

class CategoriaEgreso(models.Model):
   _name = 'modulo1.categoria.egreso'

   descripcion = fields.Char('Descripcion', required=True)
   activo = fields.Boolean('Activo?', default=True)

class Entidad(models.Model):
   _name = 'modulo1.entidad'




###########################################################

class Cliente(models.Model):
   _name = 'modulo1.cliente'

   descripcion    = fields.Char('Descripcion', required=True)
   ruc            = fields.Char('RUC', required=True)
   cel_contacto   = fields.Char('Contacto', required=True)
   #tipo_entidad   = fields.Selection([('Cliente','Proveedor')])
   activo         = fields.Boolean('Activo?',default=True)

class Proveedor(models.Model):
   _name = 'modulo1.proveedor'

   descripcion    = fields.Char('Descripcion', required=True)
   ruc            = fields.Char('RUC', required=True)
   cel_contacto   = fields.Char('Contacto', required=True)
   #tipo_entidad   = fields.Selection([('Cliente','Proveedor')])
   activo         = fields.Boolean('Activo?',default=True)

   #def filtrar_tipo_entidad(self):

###########################################################

class Ingreso(models.Model):
   _name = 'modulo1.ingreso'
   _rec_name= 'comentario'
   _description = 'Este modulo es para ingreso'
   #Quiero enlazar una entidad de tipo cliente que debo hacer para filtrar a los datos de entidad
   cliente_id               = fields.Many2one('Cliente', string='Cliente') 
   comentario               = fields.Char('Descripcion', required=True)
   fecha_provision_ingreso  = fields.Date('Fecha Ingreso')
   igv                      = fields.Boolean('Con IGV', default=True)
   monto_provision_ingreso  = fields.Float('SubTotal')
   periodo                  = fields.Selection([
                                                ('2020-08','2020-08'),
                                                ('2020-09','2020-09'),
                                                ('2020-10','2020-10')
                                             ])
   
   pago_ids = fields.One2many('modulo1.pago','ingreso_id','Pago')
   state = fields.Selection([('draft','borrador'),('paid','pagado')], string='state', default="draft")


   def change_state(self):
      self.state = 'paid'

  # def change_comentario(self): #boton de objeto son para funcionalidad dentro del mismo modelo, no se tiene 
   #   self.comentario = "Se cambio el comentario"
      
      


class Egreso(models.Model):
   _name = 'modulo1.egreso'

   proveedor_id             = fields.Many2one('Proveedor', string='Proveedor')
   comentario               = fields.Char('Descripcion', required=True)
   fecha_provision_egreso   = fields.Date('Fecha Egreso')
   igv                      = fields.Boolean('Con IGV', default=True)
   monto_provision_egreso   = fields.Float('Sub Total')
   periodo                  = fields.Selection([
                                                ('2020-08','2020-08'),
                                                ('2020-09','2020-09'),
                                                ('2020-10','2020-10')
                                             ])

   #def desembolsar(self):


###########################################################

class Pago(models.Model):
   _name = 'modulo1.pago'

   #@api.onchange('monto_pago')
   #def CalcularTotal(self):
   #   self.monto_pago_igv   =  self.monto_pago * 0.12 
   #   self.monto_pago_total =  self.monto_pago_igv + self.monto_pago
   origen_id                  = fields.Integer('Origen', readonly="1")
   comentario                 = fields.Char('Comentario', required=False)
   fecha_pago                 = fields.Date('Fecha Pago')
   metodo_pago                = fields.Selection([('Transferencia','Deposito')])
   monto_recaudo              = fields.Float('SubTotal', required=True)
   monto_recaudo_igv          = fields.Float('SubTotal IGV')
   monto_recaudo_detraccion   = fields.Float('Subtotal Detraccion')
   monto_recaudo_total        = fields.Float('Total')
   
   ingreso_id             = fields.Many2one('modulo1.ingreso', string='Ingreso')

   @api.onchange('monto_recaudo')
   def calcular_montos(self):
      self.monto_recaudo_igv = self.monto_recaudo * 0.18
      self.monto_recaudo_detraccion = (self.monto_recaudo + self.monto_recaudo_igv) * 0.12
      self.monto_recaudo_total = self.monto_recaudo + self.monto_recaudo_igv - self.monto_recaudo_detraccion

   #@api.model
   #def ingresar_recaudo(self):
   #   ingreso_id = self.env['modulo1.ingreso'].browse(self._context.get('active_id'))
   #   self.origen_id = ingreso_id


class Pago2(models.Model):
   _inherit = 'modulo1.pago'

   def ingresar_recaudo(self):
      print('asdfasdfa')
      super(Pago2,self).ingresar_recaudo()





"""
class GrupoEgreso(models.Model):
   _name = "grupo.egreso"

descripcion = fields.Char('Description', required=True)
activo = fields.Boolean('Active?', default=True)
"""

"""
class Mesa(models.Model):
   _name = "testing.mesa"

   name = fields.Char(string='Nombre')
   testing_silla_ids = fields.One2many('testing.silla', 'testing_mesa_id', string='Mesa')


class Silla(models.Model):
   _name = "testing.silla"

   name = fields.Char(string='Nombre')
   testing_mesa_id = fields.Many2one(comodel_name='testing.mesa', string='Mesa')
"""
# class modulo1(models.Model):
#     _name = 'modulo1.modulo1'
#     _description = 'modulo1.modulo1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

"""
class TodoTask2(models.Model):
    _name = 'todo.task2'
    _description = 'To-do Task2'
    
    def action_test2(self):
        raise ValidationError("Esta ventana se abrio desde con TodoTask2 y una vista diferente")


    name_2 = fields.Char('Description_2', required = True)
    is_done_2 = fields.Boolean('Done_2?') 
    active_2 = fields.Boolean('Active_2?', default=True)
"""