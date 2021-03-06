
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMÓVIL = {
    'CHASIS': {
        'MIN': 60,
        'MAX': 80
    },
    'CARROCERIA': {
        'MIN': 20,
        'MAX': 40
    },
    'RUEDAS': {
        'MIN': 25,
        'MAX': 50
    },
    'MOTOR': {
        'MIN': 70,
        'MAX': 80
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 90,
        'MAX': 120
    }
}

TRONCOMÓVIL = {
    'CHASIS': {
        'MIN': 20,
        'MAX': 60
    },
    'CARROCERIA': {
        'MIN': 30,
        'MAX': 45
    },
    'RUEDAS': {
        'MIN': 40,
        'MAX': 70
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 60,
        'MAX': 90
    },
    'PESO': {
        'MIN': 60,
        'MAX': 70
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': 30,
        'MAX': 50
    },
    'CARROCERIA': {
        'MIN': 40,
        'MAX': 60
    },
    'RUEDAS': {
        'MIN': 60,
        'MAX': 70
    },
    'MOTOR': {
        'MIN': 67,
        'MAX': 125
    },
    'ZAPATILLAS': {
        'MIN': 1,
        'MAX': 10
    },
    'PESO': {
        'MIN': 20,
        'MAX': 30
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': 30,
        'MAX': 40
    },
    'CARROCERIA': {
        'MIN': 30,
        'MAX': 40
    },
    'RUEDAS': {
        'MIN': 80,
        'MAX': 100
    },
    'MOTOR': {
        'MIN': 1,
        'MAX': 10
    },
    'ZAPATILLAS': {
        'MIN': 60,
        'MAX': 70
    },
    'PESO': {
        'MIN': 5,
        'MAX': 25
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
    'MOTOR/ZAPATILLAS': {
        'COSTO': 10,
        'EFECTO': 5
    },

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


NUMEROEQUIPO = {"1": "Tareos", "2": "Docencios","3": "Hibridos",}

# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = 10

# Velocidad intencional
EFECTO_OSADO = 1.3
EFECTO_PRECAVIDO = 1.1

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

POND_EFECT_HIELO = 0.02
POND_EFECT_ROCAS = 0.02

POND_EFECT_DIFICULTAD = 0.02




# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None



