class Cuenta(object):
    saldo= 0.0
    def __init__(self, saldo):
        self.saldo= saldo
    def ingresar (self,cantidades):
        self.saldo=self.saldo+cantidades
        print(self.saldo)
    def retirar (self,cantidades2):
        if cantidades2<self.saldo:
            self.saldo-=cantidades2
        else:
            print("Su saldo no es suficiente")
        print(self.saldo)
cuenta1=Cuenta(0.0)
cantidades=[125.23,503.4,50.0]
for elemento in range(3):
    cuenta1.ingresar(cantidades[elemento])
print("cantidad ingresada",cantidades)
cantidades2=[333.34]
for elemento in range(1):
    cuenta1.retirar(cantidades2[elemento])
print("cantidad retirada",cantidades2)