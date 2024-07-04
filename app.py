import funciones as f

pedido = []

while True:
    print("1._ Registrar pedido ")
    print("2._ Lista de pedidos ")
    print("3._ Inmprimir Hoja de ruta ")
    print("4._ Buscar pedido por ID ")
    print("Salir del programa ")

    opc = input("Sececiones la opcion que desea : ")

    if opc == "1":
        f.registrar_usuario(pedido)
        
    elif opc == "2":
        f.listar_pedidos()
    elif opc == "3":
        f.imprimir_hoja()
    elif opc == "4":
        f.buscar_pedido_ID()
    elif opc == "5":
        print()
    else:
        print()

