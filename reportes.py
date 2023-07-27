#REPORTES

from obtencion import*

def show_reportes():
    opcion=""
    while opcion!="0":
        print("""
    Seleccione una opcion:
        1: Mostrar paises
        2: Mostrar informacion de un pais
        3: Mostrar estados de un pais
        4: Mostrar datos meteorologicos de un pais
            
        0: Volver al menu principal
    """)
    opcion=input("Ingrese el numero de la opcion: ")
    if opcion=="1":
        show_countries
    elif opcion=="2":
        show_info_country
    elif opcion=="3":
        show_states_country
    elif opcion=="4":
        show_met_country
    elif opcion=="0":
        print ("Regresando al menu principal...")
    else:
        print 



#Mostrar países
def show_countries(self.location):
    for country in self.location:
        print (country)

#Mostrar información de un país
def show_info_country():
    for country in self.location:
        print (f"""
Pais: {country}
    Capital: {self.capital}
    Poblacion: {self.population}


""")

#Mostrar estados de un país


#Mostrar datos meteorológicos de un país