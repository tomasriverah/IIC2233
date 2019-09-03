
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
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

TRONCOMOVIL = {
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
VELOCIDAD_MINIMA = None

# Velocidad intencional
EFECTO_OSADO = None
EFECTO_PRECAVIDO = None

# Dificultad de control del vehículo
PESO_MEDIO = None
EQUILIBRIO_PRECAVIDO = None

# Tiempo pits
TIEMPO_MINIMO_PITS = None
VELOCIDAD_PITS = None

# Experiencia por ganar
BONIFICACION_PRECAVIDO = None
BONIFICACION_OSADO = None


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehiculos.csv",
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
