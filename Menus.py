def menu_principal():
    numero_color = "\033[94m"  # Naranja
    reset_color = "\033[0m"   # Restablecer color por defecto
    menu = f"{numero_color}Menú principal{reset_color}"
    menu += "\n"
    menu += f"\n¿Como deseas ingresar?"
    menu += f"\n"
    menu += f"\n[{numero_color}1{reset_color}] Clientes"
    menu += f"\n[{numero_color}2{reset_color}] Administrador"
    menu += f"\n[{numero_color}3{reset_color}] Salir"
    menu += "\n\nSelecciona una opción: "
    return menu

def menu_cliente():
    numero_color = "\033[94m"  # Naranja
    reset_color = "\033[0m"   # Restablecer color por defecto
    
    menu = f"\033[93mOperaciones Cliente{reset_color}"
    menu += f"\n[{numero_color}1{reset_color}] Depositar"
    menu += f"\n[{numero_color}2{reset_color}] Retirar"
    menu += f"\n[{numero_color}3{reset_color}] Transferir"
    menu += f"\n[{numero_color}4{reset_color}] Pagar servicio"
    menu += f"\n[{numero_color}5{reset_color}] Consultar Saldo"
    menu += f"\n[{numero_color}6{reset_color}] Consultar Movimientos"
    menu += f"\n[{numero_color}7{reset_color}] Cerrar sesión"
    menu += "\n\nSelecciona una opción: "
    return menu

def menu_operaciones_administrador():
    numero_color = "\033[94m"  # Naranja
    reset_color = "\033[0m"   # Restablecer color por defecto
    
    menu = f"\033[93mOperaciones Administrador{reset_color}"
    menu += "\n"
    menu += f"\n[{numero_color}1{reset_color}] Gestionar Clientes"
    menu += f"\n[{numero_color}2{reset_color}] Gestionar Dispensador"
    menu += f"\n[{numero_color}3{reset_color}] Cerrar sesión"
    menu += "\n\nSelecciona una opción:"

    return menu

def gestionar_clientes():
    numero_color = "\033[94m"  # Naranja
    reset_color = "\033[0m"   # Restablecer color por defecto
    
    menu = f"{numero_color}Gestionar Clientes{reset_color}"
    menu += "\n"
    menu += f"\n[{numero_color}1{reset_color}] Agregar"
    menu += f"\n[{numero_color}2{reset_color}] Editar"
    menu += f"\n[{numero_color}3{reset_color}] Buscar"
    menu += f"\n[{numero_color}4{reset_color}] Eliminar"
    menu += f"\n[{numero_color}5{reset_color}] Listar"
    menu += f"\n[{numero_color}6{reset_color}] Ir al menú anterior"
    menu += "\n\nSelecciona una opción: "

    return menu

def gestionar_dispensador():
    numero_color = "\033[94m"  # Naranja
    reset_color = "\033[0m"   # Restablecer color por defecto
    
    menu = f"{numero_color}Gestionar Dispensador{reset_color}"
    menu += "\n"
    menu += f"\n[{numero_color}1{reset_color}] Agregar"
    menu += f"\n[{numero_color}2{reset_color}] Editar"
    menu += f"\n[{numero_color}3{reset_color}] Actividad de dispensador"
    menu += f"\n[{numero_color}4{reset_color}] Consultar saldo de dispensador"
    menu += f"\n[{numero_color}5{reset_color}] Ir al menú anterior"
    menu += "\n\nSelecciona una opción: "
    return menu
