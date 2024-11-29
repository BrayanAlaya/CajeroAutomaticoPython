class Dispensador:
    def __init__(self,ID_dispensador,nombre,ubicacion, listabilletes, estado):
        self.ID_dispensador = ID_dispensador
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.listabilletes = listabilletes
        self.estado = estado 
        self.historial = []
        self.uso=0
    
    def mostrarActividad(self):
        print("{:<10} {:<20} {:<15} {:<10}".format("Num Op", "ID Dispensador", "ID Cliente", "Monto"))
        print("=" * 60)
    
        for actividad in self.historial:
            print("{:<10} {:<20} {:<15} {:<10}".format(
                actividad.num_op,
                actividad.ID_dispensador,
                actividad.ID_cliente,
                actividad.monto_retirado
            ))
    def mostrarSaldo(self):
        print("Mostrando billetes del cajero ", self.nombre)
        saldototal = 0 
        
        for billete, cantidad in self.listabilletes.items():
            print(f"{billete}: {cantidad} billetes")
            multp = billete * cantidad
            saldototal += multp
        print("Saldo total del dispensador: ", saldototal)
        print("\n")

    
    def DispensarDeBilletes(self, monto):#Usando el algoritmo Voraz

        billetes = list(self.listabilletes.keys())
        idx = 0
        dispensa = {}

        while monto > 1:

            count = 0
            while monto >= billetes[idx]:
                count += 1
                monto -= billetes[idx]

            if count > 0:
                dispensa[billetes[idx]] = count
                self.listabilletes[billetes[idx]] -= count

            idx += 1

        return dispensa
