# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

###########################################################

class Recaudo(models.TransientModel):
  _name = 'modulo1.transient.recaudo'
  _inherit = 'modulo1.pago'

  impuestos_bln= fields.Boolean('Con Impuestos',default=True)
  #campo_one2many = fields.one2many('modulo1.pago')

  def validar_recaudo(self):
    ingreso_id = self.env['modulo1.ingreso'].browse(self._context.get('active_id'))
    monto_max = ingreso_id.monto_provision_ingreso
    if self.monto <= monto_max :
       print('Se valido que es menor a monto max')
    else: 
       raise UserError('Se ingreso un monto de pago mayor al del ingreso')

  def ingresar_recaudo(self):
    ingreso_id = self.env['modulo1.ingreso'].browse(self._context.get('active_id'))

    print('INGRESAR RECUADO')
    vals={
      'comentario':'Pago '+ingreso_id.comentario,
      'monto_recaudo':self.monto_recaudo_total,
      'ingreso_id':ingreso_id.id
    }
    obj_pago = self.env['modulo1.pago']
    obj_pago.create(vals)
    
    ingreso_id.change_state()



  #@api.model
  #def ingresar_recaudo(self):
  #ingreso_id = self.env['modulo1.ingreso'].browse(self._context.get('active_id'))
  #self.origen = ingreso_id
  #model_pago = self.env['modulo1.pago']
  #Crear el id del
  #nuevo_recaudo = recaudo.create({monto})
  #super('modulo1.pago',self).create()
  #super('modulo1.pago',self).create(vals)
  """
  monto_recaudo = fields.Float('Monto')
  monto_recaudo_igv = fields.Float('Monto IGV')
  monto_recaudo_detraccion = fields.Float('Monto Detraccion')
  monto_recaudo_total = fields.Float('Monto Total')
  """
  """
  @api.multi
  def insert_data(self):

  for record in self.env['target.table.name'].browse(self._context.get('active_ids', [])):

  #here you can access target table fields using *record* variable

  record.field_name = wizard.field_name

  return True






class Desembolso(models.TransientModel):
_name = 'modulo1.desembolso'

monto_desembolso = fields.Float('Monto')
monto_desembolso_igv = fields.Float('Monto IGV')
monto_desmtotal_total = fields.Float('Monto Total')
"""



