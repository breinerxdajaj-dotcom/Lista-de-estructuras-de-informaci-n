from usuario1 import Usuario
from carro1 import Carro
from estacionamiento import Estacionamiento

nombre = input ("ingrese nombre del cliente: ")
cedula = int(input("ingrese cedula del cliente: "))
tipo_cliente = ("ingrese tipo de cliente: ")
obj_cliente = (nombre,cedula,tipo_cliente)

placa = input ("ingrese placa del carro: ")
marca = input ("ingrese la marca del carro: ")
color = input ("ingrese color del carro: ")
obj_carro = Carro(placa,marca,color)

obj_estacionamiento = Estacionamiento()

puesto = int(input("ingrese el numero de puesto: "))
obj_estacionamiento.set_puesto = (puesto)
obj_estacionamiento.registrar_Entrada(obj_cliente,obj_carro)
obj_estacionamiento.guardar()

obj_estacionamiento.mostrar_info()


registrar_salida = input("¿Desea ingresar la salida de un carro? [si/no] ")

if registrar_salida.lower() == "si":
    
    placa = input("ingrese la placa del carro para dar salida: ")
    
    obj_estacionamiento.registrar_salida(placa)
    obj_estacionamiento.guardar()

obj_estacionamiento.mostrar_info()