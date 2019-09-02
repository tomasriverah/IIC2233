
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': None,
        'MAX': None
    },
    'CARROCERIA': {
        'MIN': None,
        'MAX': None
    },
    'RUEDAS': {
        'MIN': None,
        'MAX': None
    },
    'MOTOR': {
        'MIN': None,
        'MAX': None
    },
    'ZAPATILLAS': {
        'MIN': None,
        'MAX': None
    },
    'PESO': {
        'MIN': None,
        'MAX': None
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': None,
        'EFECTO': None
    },
    'CARROCERIA': {
        'COSTO': None,
        'EFECTO': None
    },
    'RUEDAS': {
        'COSTO': None,
        'EFECTO': None
    },
    'MOTOR': {
        'COSTO': None,
        'EFECTO': None
    },
    'ZAPATILLAS': {
        'COSTO': None,
        'EFECTO': None
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
        'PERSONALIDAD': "precavido"
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
        'PERSONALIDAD': None
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
        'PERSONALIDAD': "osado"
    }
}


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
