# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

 
class telefono(osv.osv):
     _name = 'telefono.telefono'
     _rec_name='llamar'
     
     _columns={
        'llamar':fields.integer('Llamar a un contacto',size=20,required=True,help='Llamar a un contacto'),
        'enviar_sms':fields.char('enviar sms',size=250,required=True,help='Llamar a un contacto'),
        'agregar_contacto':fields.char('agregar contacto',help='Enviar mensaje a un contacto'),
        'enviar_email':fields.char('Enviar email',size=500,help='Enviar correo electronico'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...')
        }
        
     _defaults={
        'active':True,
        }
     
