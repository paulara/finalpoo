from ejer1 import Cuenta_ahorro
class Persona(object):
    def __init__(self,nombre,dni,direccion,telefono,email):
        self.nombre=nombre
        self.dni=dni
        self.direccion=direccion
        self.telefono=telefono
        self.email=email
    def mostrar(self):
        print("nombre",self.nombre,"dni",self.dni,"direccion",self.direccion,"telefono",self.telefono)
        if self.email!='':
            print("email",self.email)
        else:
            print("no hay email")
class Cliente(Persona,Cuenta_ahorro):
    def __init__(self,saldo,contrasena,nombre,dni,direccion,telefono,email,credit):
        Cuenta_ahorro.__init__(self,saldo,contrasena)
        Persona.__init__(self, nombre, dni, direccion, telefono, email)
        self.credit=1000
    def mostrar_datos(self):
        Persona.mostrar(self)
if __name__ == '__main__':
    "ejercicio anterior"
    clase_tic=[]
    for n in range (10):
        nombre=input("Introduzca el nombre")
        dni=input("Introduzca el dni")
        direccion=input("Introduzca la direccion")
        telefono=input("introduzca el telefono")
        email=input("Introduzca el correo")
        clase_tic.append(Persona(nombre,dni,direccion,telefono,email))
    for i in range(10):
        clase_tic[i].mostrar()
    "Para ejercicio 3"
    cliente=Cliente(2500,"3210","Mariano Fuentes","45365968L","C/ de las Alpujarras 2, bajo",958776566, "mfuentes@iaa.es",1000)
    cliente.mostrar_datos(saldo,nombre,dni,direccion,telefono,email,credit)
