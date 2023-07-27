#OBTENCIÓN Y REGISTRO DE DATOS

import requests

#Paises
class country:
    def __init__(self, location_name, location_capital, population,area,currency,main_language):
        self.location_name=location_name
        self.location_capital=location_capital
        self.population=population
        self.area=area
        self.currency=currency
        self.main_language=main_language

    def get_dat_country():
        response=requests.get(url_countries)
        data_countries=response.json()
        return data_countries

    #Estados
class states:
    def __init__(self, location_name, location_states):
        self.location_name=location_name
        self.location_states=location_states

    def get_data_states():
        response=requests.get(url_states)
        data_states=response.json()
        return data_states
    
class location_states(states):
    def __init__(self, location_name, location_states, state_name, state_capital, population, area):
        states.__init__(self, location_name, location_states)
        self.state_name=state_name
        self.state_capital=state_capital
        self.population=population
        self.area=area

    #Datos Meteorologicos
class met:
    def __init__(self, location_name, location_measurements):
        self.location_name=location_name
        self.location_measurements=location_measurements

    def get_data():
        response=requests.get(url_met)
        data_met=response.json()
        return data_met
    
class location_measurements(met):
    def __init__(self, location_name, location_measurements, temperature, humidity, wind_speed, date):
        met.__init__(self, location_name, location_measurements)
        self.temperature=temperature
        self.humidity=humidity
        self.wind_speed=wind_speed
        self.date=date
        

url_countries="https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json"
url_states="https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json"
url_met="https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json"
