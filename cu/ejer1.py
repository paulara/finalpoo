"Crear clase cuenta"
class Cuenta(object):
    def __init__(self,__saldo,contrasena):
        self.__saldo=0.0
        self.contrasena=contrasena
    def ingresar (self,cantidades):
        self.__saldo=self.__saldo+cantidades
        print("saldo actual:",self.__saldo)
    def retirar (self,cantidades2):
            self.__saldo-=cantidades2
            print("saldo actual:",self.__saldo) 
    def leer_saldo(self,contrasena):  
        if self.contrasena==contrasena:
            print("saldo actual",self.__saldo)
        else:
            print("Contrasena incorrecta")
    def saldonooculto(self):
        return self.__saldo
"Crear clase cuenta de ahorro"            
class Cuenta_ahorro(Cuenta):
    def __avisar(self,cantidades2): 
        if  cantidades2>super(Cuenta_ahorro,self).saldonooculto():
            print("Numeros rojos")
        else:
            super(Cuenta_ahorro,self).retirar(cantidades2)
    def llamaravisar(self,cantidades2):
        self.__avisar(cantidades2)
"Programa principal"    
if __name__ == '__main__':
    "Todo con objetocuenta1"
    cuenta1=Cuenta(0.0,"3210")
    cantidades=[300]
    for elemento in range(1):
        print("cantidad ingresada",cantidades)
        cuenta1.ingresar(cantidades[elemento])
    cantidades2=[290,20,30]
    for elemento in range(3):
        print("cantidad retirada",cantidades2[elemento])
        cuenta1.retirar(cantidades2[elemento])
    contrasena=input("Introduzca contrasena")
    cuenta1.leer_saldo(contrasena)
    "Cuenta2"
    cuenta2=Cuenta_ahorro(0.0,"3210")
    cantidades=[300]
    for elemento in range(1):
        print("cantidad ingresada",cantidades)
        cuenta2.ingresar(cantidades[elemento])
    cantidades2=[290,20,30]
    for elemento in range(3):
        print("cantidad retirada",cantidades2[elemento])
        cuenta2.llamaravisar(cantidades2[elemento])