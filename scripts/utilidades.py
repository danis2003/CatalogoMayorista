def mostrar_errores(errores):

    print("\n===================================")
    print("   ERRORES EN EL EXCEL")
    print("===================================\n")

    for error in errores:
        print(error)

    print(f"\nSe encontraron {len(errores)} errores.")
    print("No se generó productos.json.")