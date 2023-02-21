class Cuentas():
    def __init__(self,titular, cantidad, tarjeta,banco):
        self.__titular=titular
        self.__cantidad=cantidad
        self.__tarjeta=tarjeta
        self.__banco=banco
    def set_titular(self, titular):
        self._titular=titular
    def get_titular(self):
        return self.__titular
    def set_cantidad(self, cantidad):
        self._cantidad=cantidad
    def get_cantidad(self):
        return self.__cantidad
    def set_tarjeta(self, tarjeta):
        self._tarjeta=tarjeta
    def get_tarjeta(self):
        return self.__tarjeta
    def set_banco(self, banco):
        self._banco=banco
    def get_banco(self):
        return self._banco
    
class CuentaJoven(Cuentas):
    def __init__(self,edad,titular, cantidad, tarjeta,banco):
        self.__edad=edad
        super().__init__(titular, cantidad, tarjeta,banco)
    def set_edad(self, edad):
        self._edad=edad
    def get_edad(self):
        return self._edad
    
    
def main():
    caracteristicascuenta=[]
    pregunta=input("¿Tienes cuenta?:")
    while pregunta.lower()=="si":
        titular=input("¿Quien es el titular?:")
        cantidad=input("¿Cual es tu cantidad?:")
        tarjeta=input("¿Que numero tiene la tarjeta?:")
        banco=input("¿Cual es tu banco?:")
        edad=input("¿Cuantos años tienes?:")
        if edad>18:
            print ("Puedes tener cuenta")
        else:
           print ("No puedes tener cuenta")
        
        Cuentas=CuentaJoven(edad,titular, cantidad, tarjeta,banco)
        caracteristicascuenta.appened(Cuentas)
        pregunta=input("¿Tienes mas cuentas?")
        
           
    for x in range(0,len(caracteristicascuenta)):
        print(caracteristicascuenta[x].getTitular())
        print(caracteristicascuenta[x].getCantidad())
        print(caracteristicascuenta[x].getTarjeta())
        print(caracteristicascuenta[x].getBanco())
        print(caracteristicascuenta[x].getEdad())

if __name__=="__main__":
    main()
        
    

    
    
    
    
    