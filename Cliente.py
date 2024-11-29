from Operacion import Operacion
from Actividad import Actividad
import Dispensador
import datetime
from Metodos import error, exito, enter
import Metodos
import Data

class Cliente:
    def __init__(self, ID_cliente, nombre, user, clave, ctacte, saldo, estado):
        self.ID_cliente = ID_cliente
        self.nombre = nombre
        self.user = user
        self.clave = clave
        self.ctacte = ctacte
        self.saldo = saldo
        self.estado = estado
        self.listaOperaciones = []  
        
    def depositar(self, dispensador):
        monto = float(input("Ingrese el monto a depositar: "))
        self.saldo += monto
        print("Depósito exitoso. Su nuevo saldo es:", self.saldo)
        fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")#Registramos opercion en la lista de operaciones del cliente actual
        
        nueva_operacion = Operacion(len(self.listaOperaciones) + 1, dispensador.nombre, self.ID_cliente, "Deposito", monto, fecha_hora_actual, "N/A")
        self.listaOperaciones.append(nueva_operacion) #Registramos operacion en el cliente que la realizo
        
        nuevaActividad = Actividad(len(dispensador.historial) + 1, dispensador.ID_dispensador , self.ID_cliente, monto)
        dispensador.historial.append(nuevaActividad) #Registramos actividad en el dispensador seleccionado

    def retirar(self, dispensador):
        monto = 0
        
        while True:
            
            monto = 0
            try:
                monto = int(input("Ingrese el monto a retirar: \n"))

                if monto % 10 == 0:#Verificamos que sea multiplo de 10, ya que si no lo es no permitira dispensar los billetes
                    break
                else:
                    print("Intente ingresar nuevamente el monto, debe ser multiplo de 10:")

            except ValueError:
                error("Entrada inválida. Ingrese un número válido.")

        resultado = dispensador.DispensarDeBilletes(monto)#Utilizamos el método del dispensador para los billetes

        print("-"*50)
        print("Desglose de billetes para :", monto, "\n")

        for denominacion, cantidad in resultado.items():#Imprimimos la cantidad de billetes dispensada
            print(f"{cantidad} billetes de {denominacion}")
            # enter()

        fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #Registramos operacion en el cliente actual
        nueva_operacion = Operacion(len(self.listaOperaciones) + 1, dispensador.nombre , self.ID_cliente , "Retiro", monto, fecha_hora_actual, "N/A")
        self.listaOperaciones.append(nueva_operacion) #Registramos operacion en el cliente que la realizo

        dispensador.uso+1
        nuevaActividad = Actividad(len(dispensador.historial) + 1, dispensador.ID_dispensador , self.ID_cliente, monto)
        dispensador.historial.append(nuevaActividad) #Registramos actividad en el dispensador seleccionado
            
        if dispensador.uso==20:# Si el uso del dispensador sobrepasa los 20 usos entra en inactividad
            dispensador.estado=="inactivo"

        self.saldo -= monto
        
    def transferencia(self, dispensador):
        
        cuenta_destino = input("Ingrese la cuenta de destino: ")
        monto = float(input("Ingrese el monto a transferir: "))
        
        if self.ctacte != cuenta_destino: 
            
            if monto <= self.saldo:
                
                indice_destino = Metodos.BuscarClienteCtateRec(Data.clientes, 0, len(Data.clientes)-1, cuenta_destino)#Buscamos que el cliente de destino exista
                print("Índice encontrado:", indice_destino) 
               
                if indice_destino is not None:
                   
                    cliente_destino = Data.clientes[indice_destino]
                    self.saldo -= monto
                    cliente_destino.saldo += monto
                    exito(f"Transferencia exitosa. Su nuevo saldo es: {self.saldo}" )
                    print("Transferencia realizada a número de cuenta", cliente_destino.ctacte)
                    fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    nueva_operacion = Operacion(len(self.listaOperaciones) + 1, dispensador.nombre, self.ID_cliente, "Transferencia", monto, fecha_hora_actual, "N/A")
                    self.listaOperaciones.append(nueva_operacion) #Registramos operacion en el cliente que la realizo
                    
                    nuevaActividad = Actividad(len(dispensador.historial) + 1, dispensador.ID_dispensador , self.ID_cliente, monto)
                    dispensador.historial.append(nuevaActividad)
                    
                else:
                    error("Cuenta de destino no encontrada.")
            else:
                error("Saldo insuficiente.")
        else:
            error("No puede transferir a su propia cuenta.")

    def servicios(self, dispensador):
        servicio = input("Ingrese el servicio a pagar: ")
        monto = float(input("Ingrese el monto del servicio: "))
        
        if monto <= self.saldo:
            
            self.saldo -= monto
            exito(f"Pago de servicio exitoso. Su nuevo saldo es: {self.saldo}")
            fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            nueva_operacion = Operacion(len(self.listaOperaciones) + 1, dispensador.nombre, self.ID_cliente, "Servicios", monto, fecha_hora_actual, servicio)
            self.listaOperaciones.append(nueva_operacion) #Registramos operacion en el cliente que la realizo
                    
            nuevaActividad = Actividad(len(dispensador.historial) + 1, dispensador.ID_dispensador , self.ID_cliente, monto)
            dispensador.historial.append(nuevaActividad)
            
    def movimientos(self): 
        
        Metodos.consultar_movimientos(self.ID_cliente)
            
            


