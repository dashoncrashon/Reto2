from obtencion import*


main=""
while main!=0:
    print(f"""
Seleccione una opcion:
          
          1: Reportes
          2: Analisis de datos
          3: Filtrado de datos

          0: Salir del programa
""")
    main=input("Introduzca la opcion deseada: ")
    if main=="1":
        show_reportes():
