class Cuentas():
    def __init__(self,titular, cantidad,ingresos,retirar,tarjeta,banco,estado):
        self.__titular=titular
        self.__cantidad=cantidad
        self.__ingresos=ingresos
        self.__retirar=retirar
        self.__tarjeta=tarjeta
        self.__banco=banco
        self.__estado=estado
    def set_titular(self, titular):
        self.__titular=titular
    def get_titular(self):
        return self.__titular
    def set_cantidad(self, cantidad):
        self.__cantidad=cantidad
    def get_cantidad(self):
        return self.__cantidad
    def set_ingresos(self, ingresos):
        self.__ingresos=ingresos
    def get_ingresos(self):
        return self.__ingresos
    def set_retirar(self, retirar):
        self.__retirar=retirar
    def get_retirar(self):
        return self.__retirar
    def set_tarjeta(self, tarjeta):
        self.__tarjeta=tarjeta
    def get_tarjeta(self):
        return self.__tarjeta
    def set_banco(self, banco):
        self.__banco=banco
    def get_banco(self):
        return self.__banco
    def set_estado(self, estado):
        self.__estado=estado
    def get_estado(self):
        return self.__estado
    
    estado="si"
    def alta(self):
        self.estado="si"
    def baja(self):
        if self.estado=="no":
            print ("No estas de alta")
        else:
            print ("estas de alta")
        
    
class CuentaJoven(Cuentas):
    def __init__(self,edad,titular,cantidad,ingresos,retirar,tarjeta,banco, estado):
        self.__edad=edad
        super().__init__(titular, cantidad,ingresos,retirar,tarjeta,banco,estado)
    def set_edad(self, edad):
        self.__edad=edad
    def get_edad(self):
        return self.__edad
    
    
def main():
    caracteristicascuenta=[]
    pregunta="si"
    while pregunta.lower()=="si":
        edad=int(input("¿Cuantos años tienes?:"))
        if edad < 18:
            print ("No puedes tener cuenta")
        else:
            titular=input("¿Quien es el titular?:")
            cantidad=int(input("¿Que cantidad tienes?:"))
            ingresos=input("¿Desea ingresar dinero?:")
            if ingresos== "si":
                ingresos=int(input("¿Cuanto desea ingresar?"))
            try:
                ingresos=int(input("Indique el ingreso:"))
            except ValueError:
                print("El valor introducido no es un número. Intenta de nuevo")
            t=cantidad+ingresos
            print ("El total es: ", t)
            retirar=input("¿Desea retirar dinero?:")
            if retirar == "si":
                retirar=int(input("¿Cuanto desea retirar?"))
            try:
                retirar=int(input("Indique lo que vas a retirar:"))
            except ValueError:
                print ("El valor introducido no es un número. Intenta de nuevo")   
            r=cantidad-retirar
            print ("El total es: " , r)
            tarjeta=input("¿Que numero tiene la tarjeta?:")
            banco=input("¿Cual es tu banco?:")
            edad=input("¿Cuantos años tienes?:")
            estado=input("¿Tu cuentas esta de alta?")
            cuenta=CuentaJoven(edad,titular,cantidad,ingresos,retirar,tarjeta,banco,estado)
            caracteristicascuenta.append(cuenta)
        pregunta=input("¿Quieres mas cuentas?")        
    for i in range(0,len(caracteristicascuenta)):
        print("El titular es:",caracteristicascuenta[i].get_titular())
        print("La cantidad es:",caracteristicascuenta[i].get_cantidad())
        print("Dinero ingresado:", caracteristicascuenta[i].get_ingresos())
        print("Dinero retirado:",caracteristicascuenta[i].get_retirar())
        print("Numero de tarjeta:",caracteristicascuenta[i].get_tarjeta())
        print("Tu banco es:",caracteristicascuenta[i].get_banco())
        print("La edad es:",caracteristicascuenta[i].get_edad())
        print("El estado es:",caracteristicascuenta[i].get_estado())
    
if __name__=="__main__":
    main()
        