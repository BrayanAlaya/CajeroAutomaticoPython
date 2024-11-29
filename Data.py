from Cliente import Cliente 
from Dispensador import Dispensador 

dispensadores = [
    Dispensador(1, "Quinde", "Centro", listabilletes = { 200:30, 100:20, 50:10, 20:10, 10:20 }, estado="activo"),
    Dispensador(2, "Plaza De Armas", "Norte",  listabilletes = { 200:30, 100:20, 50:10, 20:10, 10:20 }, estado= "activo"),
    Dispensador(3, "Aereopuerto", "Este",  listabilletes = { 200:30, 100:20, 50:10, 20:10, 10:20 }, estado="activo"),
    Dispensador(4, "Real Plaza", "Sur",  listabilletes = { 200:30, 100:20, 50:10, 20:10, 10:20 }, estado="activo"),
]

#(ID_cliente , nombre, nombre_usuario, clave, numero_banco, saldo, estado)
clientes = [
    Cliente(1, "Carla Mendoza", "CarlaM", "1234", "001", 1000.0, "inactivo"),
    Cliente(2, "Pedro Sánchez", "PedroS", "1234", "002", 4000.0, "activo"),
    Cliente(3, "Lucía Fernández", "LuciaF", "1234", "003", 1200.0, "activo"),
    Cliente(4, "Felipe Ramírez", "FelipeR", "1234", "004", 1500.0, "inactivo"),
    Cliente(5, "Sofía Gómez", "SofiaG", "1234", "005", 2500.0, "activo"),
    Cliente(6, "Andrés López", "AndresL", "1234", "006", 3200.0, "activo"),
    Cliente(7, "Elena Morales", "ElenaM", "1234", "007", 1600.0, "inactivo"),
    Cliente(8, "Ricardo Domínguez", "RicardoD", "1234", "008", 1500.0, "activo"),
    Cliente(9, "Valeria Vega", "ValeriaV", "1234", "009", 1800.0, "activo"),
]