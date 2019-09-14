
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMÓVIL = {
    'CHASIS': {
        'MIN': 1,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 1,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 1,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 1,
        'MAX': 10
    }
}

TRONCOMÓVIL = {
    'CHASIS': {
        'MIN': 1,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 1,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 1,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 1,
        'MAX': 10
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 1,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 1,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 1,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 1,
        'MAX': 10
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 1,
        'MAX': 10
    },
    'CARROCERIA': {
        'MIN': 1,
        'MAX': 10
    },
    'RUEDAS': {
        'MIN': 1,
        'MAX': 10
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 1,
        'MAX': 10
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 10,
        'EFECTO': 5
    },
    'CARROCERIA': {
        'COSTO': 10,
        'EFECTO': 5
    },
    'RUEDAS': {
        'COSTO': 10,
        'EFECTO': 5
    },
    'MOTOR': {
        'COSTO': 10,
        'EFECTO': 5
    },
    'ZAPATILLAS': {
        'COSTO': 10,
        'EFECTO': 5
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': "PRECAVIDO"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 34
        },
        'PERSONALIDAD': "HALF"
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': "OSADO"
    }
}


NUMEROEQUIPO = {"1": "TAREOS", "2": "DOCENCIOS","3": "HIBRIDOS",}

# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 10
EFECTO_PRECAVIDO = 5

# Dificultad de control del vehículo
PESO_MEDIO = 10
EQUILIBRIO_PRECAVIDO = 10

# Tiempo pits
TIEMPO_MINIMO_PITS = 5
VELOCIDAD_PITS = 1

# Experiencia por ganar
BONIFICACION_PRECAVIDO = 10
BONIFICACION_OSADO = 10


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehículos.csv",
    'COMPRA' : "compra_vehículos.csv"
}

POND_EFECT_HIELO = 1
POND_EFECT_ROCAS = 1

POND_EFECT_DIFICULTAD = 1




# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None



