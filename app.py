import Menus 
import Dispensador
import Data 
import Cliente
import os
import time
from Metodos import error, enter, exito, buscar_cliente, OrdenarQS, OrdenarInsertClienteId, BuscarBinariaCleinteID, OrdenarInsertNcuenta


def limpiar_consola(): #Método para limpiar la consola
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

def autenticar_admin():#Método para que al ingresar como administrador verifique la clave de admin 
    credencial_correcta = "admin"
    intentos = 3
    while intentos > 0:
        credencial = input("Ingrese la credencial de administrador: ").strip()
        if credencial == credencial_correcta:
            return True
        else:
            error("Credencial incorrecta. Intente nuevamente.")
            intentos -= 1
    return False

while True:
    limpiar_consola()
    for index, dispensador in enumerate(Data.dispensadores, start=1):#Iniciamos seleccionando el dispesador
       print(f"ID: {index} | Nombre: {dispensador.nombre} | Ubicación: {dispensador.ubicacion}")
       print(f"")
           
    print("-" * 50)
    
    op = int(input("Ingrese el ID del dispensador que desea utilizar o para salir (0): "))
    if op == 0:
        break
    if op < 1 or op > len(Data.dispensadores):
        error("Opción no válida, por favor intente de nuevo.")
        enter()
        continue #Reinicia la seleccion del dispensador
    
    dispensadorseleccionado = Data.dispensadores[op-1]
    if(dispensadorseleccionado.estado == "inactivo"):#Verficar actividad del dispensador
        error("El dispensador no se encuntra activo en este momento. Pasar al siguiente \n")
        enter()
        continue
    
    print("Dispensador seleccionado: ", dispensadorseleccionado.nombre)
    limpiar_consola()
    print(Menus.menu_principal(), end='')
    
    opcion = input()
    if opcion == '1':
        limpiar_consola()
        
        OrdenarInsertClienteId(Data.clientes)#Primero ordenamos para que pueda buscar mejor el método BuscarBinaria
        ID = input("Ingrese su ID de usuario: ")#Ingresamos con nuestro ID de usuario 
        
        cliente = BuscarBinariaCleinteID(Data.clientes, 0, len(Data.clientes) - 1, ID)
        if cliente is not None:
        
            password = input("Ingrese su clave: ")
        
            if cliente.clave == password and cliente.estado == "activo"  :  # Verificamos contraseña de usuario y actividad
                 
                print(f"Bienvenid@ {cliente.nombre}\n")
                
                while True:
                
                    limpiar_consola()
                    print(Menus.menu_cliente(), end='')
                    opcion = input()
                 
                    if opcion=='1': # Depositar
                        
                        limpiar_consola()
                        cliente.depositar(dispensadorseleccionado)
                        enter()  
                        
                    elif opcion=='2': # Retirar
                        
                        limpiar_consola()
                        cliente.retirar(dispensadorseleccionado)
                        enter()
                          
                    elif opcion=='3': # Transferencia
                        
                        limpiar_consola()
                        OrdenarInsertNcuenta(Data.clientes)
                        cliente.transferencia(dispensadorseleccionado)
                        enter()
                             
                    elif opcion=='4': # Servicios
                        
                        limpiar_consola()
                        cliente.servicios(dispensadorseleccionado)
                        enter()
                    
                    elif opcion=='5': # Saldo
                        
                        print("Su saldo actual es:", cliente.saldo)
                        enter()
                             
                    elif opcion=='6': # Movimientos 
                        
                        cliente.movimientos()
                        enter()
                    
                    elif opcion=='7':
                        break
                 
            else:
                print("Contraseña incorrecta. Intente nuevamente.\n")
        else:
            print("Usuario no encontrado.\n")
             
       
    if opcion=='2':
        limpiar_consola()
        
        if autenticar_admin():#Nos aseguramos que ingrese la clave correctamente mediante método de autentificación        
            
            while True:    
                
                limpiar_consola()
                print(Menus.menu_operaciones_administrador(), end='')
                opcion_admin = input().strip()
                
                if opcion_admin == '1':
                
                    while True:
                        
                        limpiar_consola()
                        print(Menus.gestionar_clientes(),end='')
                        opcion_gestion_clientes = input().strip()
                        
                        if opcion_gestion_clientes == '1':#Registramos cliente
                        
                            limpiar_consola()
                            
                            ID_cliente = int(input("Ingrese el ID del cliente: ").strip())
                            nombre = input("Ingrese el nombre del cliente: ").strip()
                            user = input("Ingrese el usuario del cliente: ").strip()
                            clave = input("Ingrese la clave del cliente: ").strip()
                            ctacte = input("Ingrese la cuenta corriente del cliente: ").strip()
                            saldo = float(input("Ingrese el saldo del cliente: ").strip())
                            estado = input("Ingrese el estado del cliente: ").strip()
                            nuevo_cliente = Cliente.Cliente(ID_cliente, nombre, user, clave, ctacte, saldo, estado)
                            
                            Data.clientes.append(nuevo_cliente)
                            exito("Cliente agregado exitosamente.")
                                    
                        elif opcion_gestion_clientes == '2':#Editamos cliente
                            
                            limpiar_consola()
                            ID_cliente = int(input("Ingrese el ID del cliente a editar: ").strip())
                            cliente = buscar_cliente(ID_cliente)
                            if cliente:
                                cliente.nombre = input(f"Nombre actual ({cliente.nombre}), nuevo nombre: ").strip() or cliente.nombre
                                cliente.user = input(f"Usuario actual ({cliente.user}), nuevo usuario: ").strip() or cliente.user
                                cliente.clave = input(f"Clave actual, nueva clave: ").strip() or cliente.clave
                                cliente.ctacte = input(f"Cuenta corriente actual ({cliente.ctacte}), nueva cuenta: ").strip() or cliente.ctacte
                                cliente.saldo = float(input(f"Saldo actual ({cliente.saldo}), nuevo saldo: ").strip() or cliente.saldo)
                                cliente.estado = input(f"Estado actual ({cliente.estado}), nuevo estado: ").strip() or cliente.estado
                                exito("Cliente editado exitosamente.")
                            else:
                                error("Cliente no encontrado.")
                        
                        elif opcion_gestion_clientes == '3':#Busqueda de cliente
                            
                            ID_cliente = int(input("Ingrese el ID del cliente a buscar: ").strip())
                            cliente = buscar_cliente(ID_cliente)
                            if cliente:
                                print(f"ID: {cliente.ID_cliente}, Nombre: {cliente.nombre}, Usuario: {cliente.user}, Clave: {cliente.clave}, Cuenta: {cliente.ctacte}, Saldo: {cliente.saldo}, Estado: {cliente.estado}")
                            else:
                                error("Cliente no encontrado.")
                                
                        elif opcion_gestion_clientes == '4':#Eliminar cliente
                            
                            ID_cliente = int(input("Ingrese el ID del cliente a dar de baja: ").strip())
                            cliente = buscar_cliente(ID_cliente)
                            if cliente:
                                Data.clientes.remove(cliente)
                                exito("Cliente dado de baja exitosamente.")
                            else:
                                error("Cliente no encontrado.")

                        elif opcion_gestion_clientes == '5':#Conssultar lista de clientes e imprimirla 
                            
                            try:
                                print("{:<5} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10}".format("ID", "Nombre", "Usuario", "Clave", "Cuenta", "Saldo", "Estado"))
                                print("="*90)
                                
                                for cliente in Data.clientes:
                                    ID = cliente.ID_cliente
                                    name = cliente.nombre
                                    user = cliente.user
                                    password = cliente.clave
                                    cnta = cliente.ctacte
                                    saldo = cliente.saldo
                                    estado = cliente.estado
                                    print("{:<5} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10}".format(ID, name, user, "*"*len(password), cnta, saldo, estado))
                                
                                Deseo = input("¿Desea ordenar los clientes según campo? (SI/NO): ").upper()
                                
                                if Deseo == "SI":
                                
                                    while True:
                                        Campo = input("Ingrese el campo por el cual desea ordenar la lista (nombre, user, ctacte, saldo): ")
                                        
                                        Data.clientes[:] = OrdenarQS(Data.clientes, Campo)
        
                                        print("{:<5} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10}".format("ID", "Nombre", "Usuario", "Clave", "Cuenta", "Saldo", "Estado"))
                                        print("="*90)
        
                                        for cliente in Data.clientes:
                                            ID = cliente.ID_cliente
                                            name = cliente.nombre
                                            user = cliente.user
                                            password = cliente.clave
                                            cnta = cliente.ctacte
                                            saldo = cliente.saldo
                                            estado = cliente.estado
                                            print("{:<5} {:<20} {:<15} {:<15} {:<15} {:<10} {:<10}".format(ID, name, user, "*"*len(password), cnta, saldo, estado))
        
                                        Deseo = input("¿Desea volver a ordenarlo? (SI/NO): ").upper()#Preguntamos si desea ordenar la lista de clientes
                                        if Deseo != "SI":
                                           break
                                        
                                else:
                                   print("No se ordenará la lista.")
                                
                            except Exception as e:
                                print(e)
                                                       
                        elif opcion_gestion_clientes == '6': 
                            break
                        
                        else:
                            error("Opción no válida, intente de nuevo.")
                        
                        enter()
                        
                elif opcion_admin == '2':
                    
                        while True:
                            limpiar_consola()
                            print(Menus.gestionar_dispensador(),end='')
                            opcion_gestion_dispensador = input().strip()
                            
                            if opcion_gestion_dispensador == '1': # Agregar nuevo dispensador
                                limpiar_consola()
                                ID_dispensador = int(input("Ingrese el ID del dispensador: ").strip())
                                nombre = input("Ingrese el nombre del dispensador: ").strip()
                                ubicacion = input("Ingrese la ubicación del dispensador: ")
                                b200 = int(input("Ingrese la cantidad de billetes de 200: "))
                                b100 = int(input("Ingrese la cantidad de billetes de 100: "))
                                b50 = int(input("Ingrese la cantidad de billetes de 50: "))
                                b20 = int(input("Ingrese la cantidad de billetes de 20: "))
                                b10 = int(input("Ingrese la cantidad de billetes de 10: "))
                                estado = input("Ingrese el estado del dispensador: ")
                                nuevo_dispensador = Dispensador.Dispensador(ID_dispensador, nombre, ubicacion,{200:b200, 100:b100, 50:b50, 20:b20, 10:b10}, estado)
                                Data.dispensadores.append(nuevo_dispensador)
                                exito("Dispensador agregado exitosamente.")
                                enter()
                            
                            elif opcion_gestion_dispensador == '2': # Editar
                                limpiar_consola()
                                if dispensadorseleccionado:
                                    dispensadorseleccionado.nombre = input(f"Nombre actual ({dispensadorseleccionado.nombre}), nuevo nombre: ").strip() or dispensadorseleccionado.nombre
                                    dispensadorseleccionado.ubicacion = input(f"Ubicación actual ({dispensadorseleccionado.ubicacion}), nueva ubicación: ").strip() or dispensadorseleccionado.ubicacion
                                    for billete, cantidad in dispensadorseleccionado.listabilletes.items():
                                         nueva_cantidad = int(input(f"Ingresar nueva cantidad para {billete}: "))
                                         dispensadorseleccionado.listabilletes[billete] = nueva_cantidad
                                    dispensadorseleccionado.estado = input(f"Estado actual ({dispensadorseleccionado.estado}), nuevo estado: ").strip() or dispensadorseleccionado.estado
                                    exito("Dispensador editado exitosamente.")
                                else:
                                    error("Dispensador no encontrado.")
                                enter()
                            
                            elif opcion_gestion_dispensador == '3': # Actividad del dispensador selecionado
                                limpiar_consola()
                                dispensadorseleccionado.mostrarActividad()
                                enter()
                            
                            elif opcion_gestion_dispensador=='4': # Saldo del dispensador seleccionado
                                limpiar_consola()
                                dispensadorseleccionado.mostrarSaldo()
                                enter()
                            
                            elif opcion_gestion_dispensador=='5':
                                break
                            
                            else:
                                error("Opción no válida, intente de nuevo.")
                                enter()
                    
                elif opcion_admin == '3':
                    break
                
                else:
                    error("Opción no válida, intente de nuevo.")
                    enter()
        else:
            error("Acceso denegado. Credencial de administrador incorrecta.")
    
    elif opcion == '3':
        print("Saliendo del programa...")
        break