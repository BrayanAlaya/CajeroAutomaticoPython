import Data

def BuscarClienteCtateRec(lista, inicio, final, valorBuscado):#Método para buscar cliente por Número de cuenta busqueda binaria recursivo
    if inicio <= final:
        mitad = (inicio + final) // 2
        if lista[mitad].ctacte == valorBuscado:
            return mitad
        elif lista[mitad].ctacte > valorBuscado:
            return BuscarClienteCtateRec(lista, inicio, mitad - 1, valorBuscado)
        else:
            return BuscarClienteCtateRec(lista, mitad + 1, final, valorBuscado)
    else:
        return None

def buscar_cliente(ID_cliente):#busqueda secuancial para clientes por ID
    for cliente in Data.clientes:
        if cliente.ID_cliente == ID_cliente:
            return cliente
    return None

def consultar_movimientos(ID_cliente):

    cliente = buscar_cliente(ID_cliente)
    if cliente is not None:
        print("Movimientos de la cuenta:\n")
        print("{:<10} {:<15} {:<15} {:<10} {:<20} {:<30}".format("Num Op", "Dispensador", "Operación", "Monto", "Fecha", "Referencia"))
        print("=" * 100)
        for operacion in cliente.listaOperaciones:
            print("{:<10} {:<15} {:<15} {:<10} {:<20} {:<30}".format(
                operacion.num_op,
                operacion.ID_dispensador,
                operacion.operacion,
                operacion.monto,
                operacion.fecha,
                operacion.referencia
            ))
    else:
        print("Cliente no encontrado.")
        
def exito(mensaje):#Método para cambiar de color para un mensaje de exito
    verde = "\033[92m"  
    reset = "\033[0m"   
    print(f"\n{verde}{mensaje}{reset}")
    
def error(mensaje):#Método para cambiar de color para un mensaje de error
    rojo = "\033[91m" 
    reset = "\033[0m"   
    print(f"\n{rojo}{mensaje}{reset}")
    
def enter():#Método para tecla enter
    azul = "\033[94m"
    reset = "\033[0m"
    input(f"\n{azul}Presiona Enter para seguir... {reset} \n")

def OrdenarQS(lista, indicacion): #Método para Ordenar quicksort 
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[len(lista) // 2]
        left = []
        middle = []
        right = []
        
        for x in lista:
            if getattr(x, indicacion) > getattr(pivot, indicacion):
                left.append(x)
            elif getattr(x, indicacion) == getattr(pivot, indicacion):
                middle.append(x)
            else:
                right.append(x)
        
        return OrdenarQS(left, indicacion) + middle + OrdenarQS(right, indicacion)

def OrdenarInsertNcuenta(lista): #Método para ordenar por incercion por número de cuenta antes de buscar por método recursivo
    for i in range(1, len(lista)):
        aux = lista[i]
        k = i - 1
        while k >= 0 and lista[k].ctacte > aux.ctacte:
            lista[k + 1] = lista[k]
            k -= 1
        lista[k + 1] = aux

def BuscarBinariaCleinteID(lista, inicio, final, ID_cliente): #Busqueda binaria segun ID 
    while inicio <= final:
        mitad = (inicio + final) // 2
        cliente = lista[mitad]
        if cliente.ID_cliente == int(ID_cliente): 
            return cliente
        elif cliente.ID_cliente > int(ID_cliente):
            final = mitad - 1
        else:
            inicio = mitad + 1
    return None

def OrdenarInsertClienteId(lista): #Método ordenar insert segun Id
    for i in range(1, len(lista)):
        aux = lista[i]
        k = i - 1
        while k >= 0 and lista[k].ID_cliente > aux.ID_cliente:
            lista[k + 1] = lista[k]
            k -= 1
        lista[k + 1] = aux
        
