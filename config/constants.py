# Lista de tarifas base por nivel de servicio
LEVEL_OF_SERVICE_BASE_RATES = {
    "AMB": 30,   # Ambulatorio
    "WCH": 45,   # Silla de ruedas
    "STR": 150,  # Camilla
    "STC": 300,  # Camilla especial
    "BWCH": 120, # Silla de ruedas bariatrica
    "BSTR": 300, # Camilla bariatrica
    "BLS": 450   # Soporte vital básico
}

# Incrementos por milla por nivel de servicio
LEVEL_OF_SERVICE_INCREMENTS = {
    "AMB": 1.8,
    "WCH": 2,
    "STR": 3.5,
    "STC": 3.5,
    "BWCH": 3,
    "BSTR": 4,
    "BLS": 6
}

# Configuración de geolocalización
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds
ROAD_DISTANCE_FACTOR = 1.3  # Factor para estimar distancia por carretera