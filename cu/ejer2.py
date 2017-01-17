class Persona(object):
    nombre=''
    dni=''
    direccion=''
    telefono=''
    email=''
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
    def nombrar(self,):
        print(self.nombre)
persona1=Persona('John',77139012,'granada',987654321,'nono')
persona2=Persona('Lara',603458060,'finlandia',958439773,'lala')
persona3=Persona('Lolo',77136980,'Granada',987654321,'lolailo@gmail.com')
persona4=Persona('Paula',77139013,'Atarfe',958172252,'paulara99@gmail.com')
persona1.mostrar()
persona2.mostrar()
persona3.mostrar()
persona4.mostrar()
print('Nombre alumnos')
persona1.nombrar()
persona2.nombrar()
persona3.nombrar()
persona4.nombrar()
