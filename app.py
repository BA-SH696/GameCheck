from flask import Flask, render_template, request

app = Flask(__name__)


# ============================================================
# CPU DATABASE
# Higher score = stronger CPU
# ============================================================

CPUS = {
    # Intel Core i3
    "Intel Core i3-3220": 20,
    "Intel Core i3-4130": 24,
    "Intel Core i3-6100": 28,
    "Intel Core i3-7100": 31,
    "Intel Core i3-8100": 40,
    "Intel Core i3-9100F": 46,
    "Intel Core i3-10100": 54,
    "Intel Core i3-12100F": 78,
    "Intel Core i3-13100F": 84,
    "Intel Core i3-14100F": 88,

    # Intel Core i5
    "Intel Core i5-4200U": 30,
    "Intel Core i5-4460": 38,
    "Intel Core i5-4590": 41,
    "Intel Core i5-6500": 45,
    "Intel Core i5-6600K": 50,
    "Intel Core i5-7400": 50,
    "Intel Core i5-7600K": 56,
    "Intel Core i5-8400": 65,
    "Intel Core i5-8600K": 70,
    "Intel Core i5-9400F": 68,
    "Intel Core i5-9600K": 73,
    "Intel Core i5-10400F": 72,
    "Intel Core i5-10600K": 80,
    "Intel Core i5-11400F": 82,
    "Intel Core i5-11600K": 88,
    "Intel Core i5-12400F": 94,
    "Intel Core i5-12600K": 105,
    "Intel Core i5-13400F": 105,
    "Intel Core i5-13600K": 120,
    "Intel Core i5-14400F": 112,
    "Intel Core i5-14600K": 125,

    # Intel Core i7
    "Intel Core i7-3770": 42,
    "Intel Core i7-4790": 50,
    "Intel Core i7-6700": 55,
    "Intel Core i7-7700": 60,
    "Intel Core i7-8700": 78,
    "Intel Core i7-9700K": 88,
    "Intel Core i7-10700K": 95,
    "Intel Core i7-11700K": 100,
    "Intel Core i7-12700K": 120,
    "Intel Core i7-13700K": 135,
    "Intel Core i7-14700K": 145,

    # Intel Core i9
    "Intel Core i9-9900K": 95,
    "Intel Core i9-10900K": 110,
    "Intel Core i9-11900K": 108,
    "Intel Core i9-12900K": 135,
    "Intel Core i9-13900K": 155,
    "Intel Core i9-14900K": 165,

    # AMD Ryzen 3
    "AMD Ryzen 3 1200": 25,
    "AMD Ryzen 3 2200G": 30,
    "AMD Ryzen 3 3100": 43,
    "AMD Ryzen 3 4100": 48,
    "AMD Ryzen 3 5300G": 58,
    "AMD Ryzen 3 7300X": 72,

    # AMD Ryzen 5
    "AMD Ryzen 5 1600": 45,
    "AMD Ryzen 5 2600": 52,
    "AMD Ryzen 5 3600": 70,
    "AMD Ryzen 5 4500": 65,
    "AMD Ryzen 5 5500": 72,
    "AMD Ryzen 5 5600": 82,
    "AMD Ryzen 5 5600X": 86,
    "AMD Ryzen 5 7600": 105,
    "AMD Ryzen 5 7600X": 110,
    "AMD Ryzen 5 8600G": 100,
    "AMD Ryzen 5 9600X": 120,

    # AMD Ryzen 7
    "AMD Ryzen 7 1700": 55,
    "AMD Ryzen 7 2700X": 65,
    "AMD Ryzen 7 3700X": 78,
    "AMD Ryzen 7 5700X": 90,
    "AMD Ryzen 7 5800X": 95,
    "AMD Ryzen 7 5800X3D": 115,
    "AMD Ryzen 7 7700": 105,
    "AMD Ryzen 7 7800X3D": 135,
    "AMD Ryzen 7 8700G": 108,
    "AMD Ryzen 7 9700X": 125,

    # AMD Ryzen 9
    "AMD Ryzen 9 3900X": 90,
    "AMD Ryzen 9 5900X": 110,
    "AMD Ryzen 9 5950X": 120,
    "AMD Ryzen 9 7900X": 130,
    "AMD Ryzen 9 7950X": 145,
    "AMD Ryzen 9 7950X3D": 155,
    # Additional desktop and mobile CPU coverage
    'Intel Core i3-6100T': 29,
    'Intel Core i3-8100T': 38,
    'Intel Core i3-10100T': 50,
    'Intel Core i3-10320': 57,
    'Intel Core i3-11100B': 61,
    'Intel Core i3-12100': 80,
    'Intel Core i3-12300': 83,
    'Intel Core i3-13100': 86,
    'Intel Core i3-14100': 90,
    'Intel Core i5-4300U': 28,
    'Intel Core i5-5200U': 32,
    'Intel Core i5-6200U': 35,
    'Intel Core i5-6300U': 38,
    'Intel Core i5-7200U': 39,
    'Intel Core i5-7300HQ': 43,
    'Intel Core i5-8250U': 47,
    'Intel Core i5-8265U': 50,
    'Intel Core i5-8300H': 55,
    'Intel Core i5-9300H': 59,
    'Intel Core i5-10300H': 63,
    'Intel Core i5-1135G7': 65,
    'Intel Core i5-11400H': 75,
    'Intel Core i5-1235U': 75,
    'Intel Core i5-1240P': 80,
    'Intel Core i5-12500H': 90,
    'Intel Core i5-1335U': 80,
    'Intel Core i5-13420H': 88,
    'Intel Core i5-13500H': 100,
    'Intel Core i5-14500': 115,
    'Intel Core i5-14500HX': 120,
    'Intel Core i5-2500K': 32,
    'Intel Core i5-3470': 33,
    'Intel Core i5-3570K': 36,
    'Intel Core i5-4690K': 44,
    'Intel Core i5-5675C': 47,
    'Intel Core i5-7500': 52,
    'Intel Core i5-8500': 64,
    'Intel Core i5-9500': 69,
    'Intel Core i5-10500': 75,
    'Intel Core i5-11500': 83,
    'Intel Core i5-12400': 95,
    'Intel Core i5-12600': 100,
    'Intel Core i5-13500': 108,
    'Intel Core i5-13600': 115,
    'Intel Core i5-14600': 120,
    'Intel Core i7-2600K': 32,
    'Intel Core i7-3770K': 44,
    'Intel Core i7-4770': 47,
    'Intel Core i7-4770K': 49,
    'Intel Core i7-6700K': 58,
    'Intel Core i7-7700K': 63,
    'Intel Core i7-8750H': 66,
    'Intel Core i7-9750H': 72,
    'Intel Core i7-10750H': 78,
    'Intel Core i7-10870H': 85,
    'Intel Core i7-11800H': 96,
    'Intel Core i7-12700H': 112,
    'Intel Core i7-13620H': 115,
    'Intel Core i7-13700H': 125,
    'Intel Core i7-14700HX': 150,
    'Intel Core i7-14700F': 145,
    'Intel Core i9-10980HK': 112,
    'Intel Core i9-11980HK': 115,
    'Intel Core i9-12900H': 130,
    'Intel Core i9-12900HX': 140,
    'Intel Core i9-13900H': 145,
    'Intel Core i9-13900HX': 160,
    'Intel Core i9-14900HX': 175,
    'Intel Core Ultra 5 125H': 100,
    'Intel Core Ultra 5 135H': 105,
    'Intel Core Ultra 7 155H': 120,
    'Intel Core Ultra 7 165H': 125,
    'Intel Core Ultra 9 185H': 140,
    'AMD Ryzen 3 3300X': 50,
    'AMD Ryzen 3 4300G': 50,
    'AMD Ryzen 3 5300U': 55,
    'AMD Ryzen 3 7320U': 58,
    'AMD Ryzen 3 8300G': 70,
    'AMD Ryzen 5 2400G': 38,
    'AMD Ryzen 5 3500': 55,
    'AMD Ryzen 5 3500U': 43,
    'AMD Ryzen 5 3550H': 47,
    'AMD Ryzen 5 4500U': 55,
    'AMD Ryzen 5 4600H': 62,
    'AMD Ryzen 5 4600G': 64,
    'AMD Ryzen 5 5600H': 72,
    'AMD Ryzen 5 5600U': 70,
    'AMD Ryzen 5 6600H': 82,
    'AMD Ryzen 5 6600U': 78,
    'AMD Ryzen 5 7535HS': 85,
    'AMD Ryzen 5 7640HS': 100,
    'AMD Ryzen 5 7640U': 95,
    'AMD Ryzen 5 8645HS': 105,
    'AMD Ryzen 5 8500G': 92,
    'AMD Ryzen 5 9600': 118,
    'AMD Ryzen 7 2700': 62,
    'AMD Ryzen 7 3750H': 55,
    'AMD Ryzen 7 4700U': 68,
    'AMD Ryzen 7 4800H': 78,
    'AMD Ryzen 7 4800U': 78,
    'AMD Ryzen 7 5800H': 92,
    'AMD Ryzen 7 6800H': 100,
    'AMD Ryzen 7 6800U': 95,
    'AMD Ryzen 7 7735HS': 105,
    'AMD Ryzen 7 7840HS': 120,
    'AMD Ryzen 7 7840U': 115,
    'AMD Ryzen 7 8845HS': 125,
    'AMD Ryzen 7 9800X3D': 155,
    'AMD Ryzen 9 4900H': 85,
    'AMD Ryzen 9 5900HX': 110,
    'AMD Ryzen 9 6900HX': 120,
    'AMD Ryzen 9 7940HS': 135,
    'AMD Ryzen 9 7945HX': 160,
    'AMD Ryzen 9 8945HS': 140,
    'AMD Ryzen 9 9950X': 165,
    'AMD Ryzen Threadripper 3960X': 140,
    'AMD Ryzen Threadripper 3970X': 155,
    'AMD Ryzen Threadripper 3990X': 165,
}


# ============================================================
# GPU DATABASE
# Higher score = stronger GPU
# ============================================================

GPUS = {

    # Intel
    "Intel HD Graphics 4000": 10,
    "Intel HD Graphics 4400": 13,
    "Intel HD Graphics 4600": 16,
    "Intel HD Graphics 5000": 18,
    "Intel HD Graphics 520": 20,
    "Intel HD Graphics 530": 24,
    "Intel UHD Graphics 620": 23,
    "Intel UHD Graphics 630": 28,
    "Intel Iris Xe Graphics": 42,
    "Intel Arc A380": 55,
    "Intel Arc A750": 78,
    "Intel Arc A770": 88,

    # NVIDIA GTX
    "NVIDIA GeForce GTX 750 Ti": 28,
    "NVIDIA GeForce GTX 950": 35,
    "NVIDIA GeForce GTX 960": 42,
    "NVIDIA GeForce GTX 970": 52,
    "NVIDIA GeForce GTX 980": 58,
    "NVIDIA GeForce GTX 1050": 40,
    "NVIDIA GeForce GTX 1050 Ti": 47,
    "NVIDIA GeForce GTX 1060 3GB": 55,
    "NVIDIA GeForce GTX 1060 6GB": 62,
    "NVIDIA GeForce GTX 1070": 72,
    "NVIDIA GeForce GTX 1080": 82,
    "NVIDIA GeForce GTX 1650": 52,
    "NVIDIA GeForce GTX 1650 Super": 60,
    "NVIDIA GeForce GTX 1660": 66,
    "NVIDIA GeForce GTX 1660 Super": 72,
    "NVIDIA GeForce GTX 1660 Ti": 75,

    # RTX 20
    "NVIDIA GeForce RTX 2060": 75,
    "NVIDIA GeForce RTX 2060 Super": 82,
    "NVIDIA GeForce RTX 2070": 88,
    "NVIDIA GeForce RTX 2070 Super": 94,
    "NVIDIA GeForce RTX 2080": 100,
    "NVIDIA GeForce RTX 2080 Ti": 112,

    # RTX 30
    "NVIDIA GeForce RTX 3050": 60,
    "NVIDIA GeForce RTX 3060": 78,
    "NVIDIA GeForce RTX 3060 Ti": 88,
    "NVIDIA GeForce RTX 3070": 100,
    "NVIDIA GeForce RTX 3070 Ti": 108,
    "NVIDIA GeForce RTX 3080": 120,
    "NVIDIA GeForce RTX 3080 Ti": 130,
    "NVIDIA GeForce RTX 3090": 138,
    "NVIDIA GeForce RTX 3090 Ti": 145,

    # RTX 40
    "NVIDIA GeForce RTX 4060": 82,
    "NVIDIA GeForce RTX 4060 Ti": 92,
    "NVIDIA GeForce RTX 4070": 108,
    "NVIDIA GeForce RTX 4070 Super": 118,
    "NVIDIA GeForce RTX 4070 Ti": 125,
    "NVIDIA GeForce RTX 4070 Ti Super": 132,
    "NVIDIA GeForce RTX 4080": 150,
    "NVIDIA GeForce RTX 4080 Super": 155,
    "NVIDIA GeForce RTX 4090": 180,

    # RTX 50
    "NVIDIA GeForce RTX 5070": 125,
    "NVIDIA GeForce RTX 5070 Ti": 145,
    "NVIDIA GeForce RTX 5080": 170,
    "NVIDIA GeForce RTX 5090": 210,

    # AMD Radeon
    "AMD Radeon HD 6670": 16,
    "AMD Radeon HD 7750": 20,
    "AMD Radeon HD 8670M": 18,
    "AMD Radeon R7 250": 22,
    "AMD Radeon R7 260X": 30,
    "AMD Radeon R9 270": 35,
    "AMD Radeon R9 280": 40,
    "AMD Radeon RX 460": 42,
    "AMD Radeon RX 470": 52,
    "AMD Radeon RX 480": 58,
    "AMD Radeon RX 570": 55,
    "AMD Radeon RX 580": 62,
    "AMD Radeon RX 5500 XT": 65,
    "AMD Radeon RX 5600 XT": 75,
    "AMD Radeon RX 5700 XT": 90,
    "AMD Radeon RX 6600": 78,
    "AMD Radeon RX 6600 XT": 86,
    "AMD Radeon RX 6700 XT": 100,
    "AMD Radeon RX 6800": 112,
    "AMD Radeon RX 6800 XT": 122,
    "AMD Radeon RX 6900 XT": 135,
    "AMD Radeon RX 7600": 82,
    "AMD Radeon RX 7700 XT": 105,
    "AMD Radeon RX 7800 XT": 118,
    "AMD Radeon RX 7900 XT": 140,
    "AMD Radeon RX 7900 XTX": 155,
    # Additional integrated, desktop, laptop and newer GPUs
    'Intel UHD Graphics 600': 8,
    'Intel UHD Graphics 605': 10,
    'Intel UHD Graphics 610': 12,
    'Intel UHD Graphics 730': 27,
    'Intel UHD Graphics 750': 32,
    'Intel UHD Graphics 770': 35,
    'Intel Iris Plus Graphics 655': 22,
    'Intel Iris Xe MAX': 35,
    'Intel Arc A310': 38,
    'Intel Arc A580': 68,
    'Intel Arc A770 16GB': 90,
    'Intel Arc B570': 72,
    'Intel Arc B580': 88,
    'NVIDIA GeForce GT 710': 5,
    'NVIDIA GeForce GT 730': 8,
    'NVIDIA GeForce GT 1030': 18,
    'NVIDIA GeForce GTX 650': 14,
    'NVIDIA GeForce GTX 660': 19,
    'NVIDIA GeForce GTX 670': 24,
    'NVIDIA GeForce GTX 680': 27,
    'NVIDIA GeForce GTX 760': 25,
    'NVIDIA GeForce GTX 770': 31,
    'NVIDIA GeForce GTX 780': 36,
    'NVIDIA GeForce GTX 950M': 14,
    'NVIDIA GeForce GTX 960M': 18,
    'NVIDIA GeForce GTX 965M': 22,
    'NVIDIA GeForce GTX 970M': 28,
    'NVIDIA GeForce GTX 980M': 35,
    'NVIDIA GeForce GTX 1050 Mobile': 35,
    'NVIDIA GeForce GTX 1050 Ti Mobile': 40,
    'NVIDIA GeForce GTX 1060 Mobile': 52,
    'NVIDIA GeForce GTX 1070 Mobile': 65,
    'NVIDIA GeForce GTX 1080 Mobile': 75,
    'NVIDIA GeForce GTX 1630': 30,
    'NVIDIA GeForce GTX 1650 Mobile': 48,
    'NVIDIA GeForce GTX 1650 Ti': 54,
    'NVIDIA GeForce GTX 1660 Ti Mobile': 68,
    'NVIDIA GeForce RTX 2050 Laptop GPU': 45,
    'NVIDIA GeForce RTX 2060 Mobile': 65,
    'NVIDIA GeForce RTX 2070 Mobile': 78,
    'NVIDIA GeForce RTX 2080 Mobile': 90,
    'NVIDIA GeForce RTX 3050 6GB': 58,
    'NVIDIA GeForce RTX 3050 Ti Laptop GPU': 57,
    'NVIDIA GeForce RTX 3060 Laptop GPU': 72,
    'NVIDIA GeForce RTX 3070 Laptop GPU': 92,
    'NVIDIA GeForce RTX 3080 Laptop GPU': 110,
    'NVIDIA GeForce RTX 4050 Laptop GPU': 68,
    'NVIDIA GeForce RTX 4060 Laptop GPU': 82,
    'NVIDIA GeForce RTX 4070 Laptop GPU': 100,
    'NVIDIA GeForce RTX 4080 Laptop GPU': 135,
    'NVIDIA GeForce RTX 4090 Laptop GPU': 150,
    'NVIDIA GeForce RTX 5050': 65,
    'NVIDIA GeForce RTX 5060': 90,
    'NVIDIA GeForce RTX 5060 Ti 8GB': 98,
    'NVIDIA GeForce RTX 5060 Ti 16GB': 100,
    'NVIDIA GeForce RTX 5070 Laptop GPU': 112,
    'NVIDIA GeForce RTX 5080 Laptop GPU': 150,
    'NVIDIA GeForce RTX 5090 Laptop GPU': 175,
    'AMD Radeon Vega 3': 10,
    'AMD Radeon Vega 6': 14,
    'AMD Radeon Vega 7': 18,
    'AMD Radeon Vega 8': 22,
    'AMD Radeon 610M': 15,
    'AMD Radeon 680M': 38,
    'AMD Radeon 780M': 48,
    'AMD Radeon 890M': 58,
    'AMD Radeon RX 550': 25,
    'AMD Radeon RX 560': 32,
    'AMD Radeon RX 590': 65,
    'AMD Radeon RX 6500 XT': 52,
    'AMD Radeon RX 6400': 40,
    'AMD Radeon RX 6650 XT': 90,
    'AMD Radeon RX 6750 XT': 105,
    'AMD Radeon RX 6950 XT': 145,
    'AMD Radeon RX 7600 XT': 88,
    'AMD Radeon RX 7900 GRE': 132,
    'AMD Radeon RX 9070': 145,
    'AMD Radeon RX 9070 XT': 160,
    'Apple M1 8-core GPU': 35,
    'Apple M2 10-core GPU': 43,
    'Apple M3 10-core GPU': 52,
}


# ============================================================
# GAME DATABASE
# cpu/gpu are minimum-ish performance scores
# ============================================================

GAMES = {

    "GTA V": {
        "cpu": 35,
        "gpu": 40,
        "ram": 8,
        "fps": 60
    },

    "GTA V Enhanced": {
        "cpu": 65,
        "gpu": 78,
        "ram": 16,
        "fps": 60
    },

    "Fortnite": {
        "cpu": 45,
        "gpu": 45,
        "ram": 8,
        "fps": 60
    },

    "Minecraft": {
        "cpu": 30,
        "gpu": 25,
        "ram": 4,
        "fps": 60
    },

    "Minecraft RTX": {
        "cpu": 70,
        "gpu": 105,
        "ram": 16,
        "fps": 60
    },

    "Far Cry 3": {
        "cpu": 25,
        "gpu": 25,
        "ram": 4,
        "fps": 60
    },

    "Far Cry 4": {
        "cpu": 40,
        "gpu": 45,
        "ram": 8,
        "fps": 45
    },

    "Far Cry 5": {
        "cpu": 55,
        "gpu": 60,
        "ram": 8,
        "fps": 60
    },

    "Far Cry 6": {
        "cpu": 75,
        "gpu": 80,
        "ram": 16,
        "fps": 60
    },

    "Watch Dogs": {
        "cpu": 40,
        "gpu": 40,
        "ram": 6,
        "fps": 45
    },

    "Watch Dogs 2": {
        "cpu": 55,
        "gpu": 60,
        "ram": 8,
        "fps": 60
    },

    "Watch Dogs Legion": {
        "cpu": 80,
        "gpu": 90,
        "ram": 16,
        "fps": 60
    },

    "Titanfall 2": {
        "cpu": 40,
        "gpu": 45,
        "ram": 8,
        "fps": 60
    },

    "Crysis 3": {
        "cpu": 45,
        "gpu": 50,
        "ram": 8,
        "fps": 45
    },

    "Resident Evil 5": {
        "cpu": 25,
        "gpu": 25,
        "ram": 4,
        "fps": 60
    },

    "Resident Evil 7": {
        "cpu": 50,
        "gpu": 55,
        "ram": 8,
        "fps": 60
    },

    "Resident Evil 2 Remake": {
        "cpu": 60,
        "gpu": 65,
        "ram": 8,
        "fps": 60
    },

    "Resident Evil 3 Remake": {
        "cpu": 65,
        "gpu": 70,
        "ram": 8,
        "fps": 60
    },

    "Resident Evil Village": {
        "cpu": 70,
        "gpu": 75,
        "ram": 16,
        "fps": 60
    },

    "Cyberpunk 2077": {
        "cpu": 80,
        "gpu": 90,
        "ram": 16,
        "fps": 60
    },

    "Red Dead Redemption 2": {
        "cpu": 70,
        "gpu": 82,
        "ram": 12,
        "fps": 50
    },

    "Elden Ring": {
        "cpu": 70,
        "gpu": 72,
        "ram": 16,
        "fps": 60
    },

    "Forza Horizon 5": {
        "cpu": 70,
        "gpu": 82,
        "ram": 16,
        "fps": 60
    },

    "Apex Legends": {
        "cpu": 55,
        "gpu": 60,
        "ram": 8,
        "fps": 60
    },

    "Call of Duty Ghosts": {
        "cpu": 35,
        "gpu": 45,
        "ram": 6,
        "fps": 60
    },

    "Call of Duty Advanced Warfare": {
        "cpu": 45,
        "gpu": 55,
        "ram": 8,
        "fps": 60
    },

    "Call of Duty Black Ops III": {
        "cpu": 55,
        "gpu": 60,
        "ram": 8,
        "fps": 60
    },

    "Call of Duty Modern Warfare": {
        "cpu": 70,
        "gpu": 80,
        "ram": 16,
        "fps": 60
    },

    "Call of Duty Warzone": {
        "cpu": 75,
        "gpu": 85,
        "ram": 16,
        "fps": 60
    },

    "Battlefield 4": {
        "cpu": 40,
        "gpu": 45,
        "ram": 8,
        "fps": 60
    },

    "Battlefield 1": {
        "cpu": 55,
        "gpu": 60,
        "ram": 8,
        "fps": 60
    },

    "Battlefield V": {
        "cpu": 60,
        "gpu": 65,
        "ram": 12,
        "fps": 60
    },

    "The Witcher 3": {
        "cpu": 50,
        "gpu": 55,
        "ram": 8,
        "fps": 60
    },

    "Hogwarts Legacy": {
        "cpu": 75,
        "gpu": 85,
        "ram": 16,
        "fps": 60
    },

    # Expanded game library (requirements are approximate performance tiers)
    'Grand Theft Auto III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grand Theft Auto: Vice City': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grand Theft Auto: San Andreas': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grand Theft Auto IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grand Theft Auto V Legacy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grand Theft Auto Online': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Red Dead Redemption': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Bully: Scholarship Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'L.A. Noire': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sleeping Dogs': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sleeping Dogs: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Mafia': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mafia II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mafia III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mafia: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Saints Row 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Saints Row: The Third': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Saints Row IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Saints Row (2022)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Just Cause': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Just Cause 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Just Cause 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Just Cause 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Prototype': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Prototype 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'inFAMOUS Second Son': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Days Gone': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Horizon Zero Dawn': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Horizon Forbidden West': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Ghost of Tsushima Director’s Cut': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Death Stranding': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Death Stranding Director’s Cut': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Marvel’s Spider-Man Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Marvel’s Spider-Man: Miles Morales': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Marvel’s Spider-Man 2': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Batman: Arkham Asylum': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Batman: Arkham City': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Batman: Arkham Origins': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Batman: Arkham Knight': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Middle-earth: Shadow of Mordor': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Middle-earth: Shadow of War': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Assassin’s Creed': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed II': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Brotherhood': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Revelations': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed III': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed IV: Black Flag': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Rogue': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Unity': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Syndicate': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Origins': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Odyssey': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assassin’s Creed Valhalla': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Assassin’s Creed Mirage': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Far Cry 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Far Cry 3 Blood Dragon': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Far Cry Primal': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Far Cry New Dawn': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Avatar: Frontiers of Pandora': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Watch Dogs: Legion': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Ghost Recon Wildlands': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ghost Recon Breakpoint': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Division': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Division 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tom Clancy’s The Crew': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Crew 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Crew Motorfest': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Driver: San Francisco': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Red Faction Guerrilla Re-Mars-tered': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crackdown 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sunset Overdrive': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Control': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Alan Wake': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Alan Wake Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Alan Wake 2': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Quantum Break': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ryse: Son of Rome': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kingdoms of Amalur: Re-Reckoning': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon’s Dogma 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon’s Dogma: Dark Arisen': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Elder Scrolls IV: Oblivion': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Elder Scrolls V: Skyrim': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Skyrim Special Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Elder Scrolls Online': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fallout 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fallout: New Vegas': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fallout 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fallout 76': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Starfield': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'The Outer Worlds': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Outer Worlds 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'No Man’s Sky': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Subnautica': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Subnautica: Below Zero': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'ARK: Survival Evolved': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'ARK: Survival Ascended': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Rust': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'DayZ': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    '7 Days to Die': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Valheim': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Enshrouded': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Palworld': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sons of the Forest': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Forest': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Green Hell': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grounded': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Long Dark': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Project Zomboid': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Terraria': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Core Keeper': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Raft': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Astroneer': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Conan Exiles': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Once Human': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dying Light': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dying Light 2 Stay Human': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Island': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Island 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'State of Decay 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'State of Decay 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Call of Duty 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty 4: Modern Warfare': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: World at War': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Modern Warfare 2 (2009)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Modern Warfare 3 (2011)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops II': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Ghosts': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Advanced Warfare': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops III': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Infinite Warfare': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: WWII': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops 4': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Modern Warfare (2019)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops Cold War': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Vanguard': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Modern Warfare II (2022)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Modern Warfare III (2023)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops 6': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Black Ops 7': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Call of Duty: Warzone': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Battlefield 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Battlefield 3': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Battlefield Hardline': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Battlefield 2042': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Battlefield 6': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Medal of Honor (2010)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Medal of Honor: Warfighter': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Titanfall': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Overwatch': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Overwatch 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Counter-Strike 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Counter-Strike: Source': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Counter-Strike: Global Offensive': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Valorant': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Rainbow Six Siege': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Rainbow Six Extraction': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'The Finals': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'PUBG: Battlegrounds': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Escape from Tarkov': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hunt: Showdown 1896': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Insurgency: Sandstorm': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Squad': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Arma 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Arma Reforger': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hell Let Loose': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ready or Not': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Payday 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Payday 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Left 4 Dead': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Left 4 Dead 2': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Back 4 Blood': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Killing Floor 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Killing Floor 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'DOOM (1993)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'DOOM 3': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'DOOM (2016)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'DOOM Eternal': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Quake Champions': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Wolfenstein: The New Order': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Wolfenstein II: The New Colossus': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Rage': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Rage 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Borderlands': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Borderlands 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Borderlands: The Pre-Sequel': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Borderlands 3': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Tiny Tina’s Wonderlands': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Borderlands 4': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Metro 2033 Redux': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Metro: Last Light Redux': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Metro Exodus': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'S.T.A.L.K.E.R.: Shadow of Chernobyl': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'S.T.A.L.K.E.R.: Clear Sky': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'S.T.A.L.K.E.R.: Call of Pripyat': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'S.T.A.L.K.E.R. 2: Heart of Chornobyl': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crysis': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crysis Warhead': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crysis 2 Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Crysis 3 Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Spec Ops: The Line': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Bulletstorm: Full Clip Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Trepang2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'RoboCop: Rogue City': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warframe': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Destiny 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Halo: The Master Chief Collection': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Halo Infinite': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Gears 5': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Gears of War: Ultimate Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Baldur’s Gate 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Baldur’s Gate: Enhanced Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Baldur’s Gate II: Enhanced Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Divinity: Original Sin': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Divinity: Original Sin 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pathfinder: Kingmaker': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pathfinder: Wrath of the Righteous': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pillars of Eternity': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pillars of Eternity II: Deadfire': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Disco Elysium': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Witcher': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'The Witcher 2: Assassins of Kings': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'The Witcher 3: Wild Hunt': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Kingdom Come: Deliverance': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kingdom Come: Deliverance II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Age: Origins': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Age II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Age: Inquisition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Age: The Veilguard': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mass Effect Legendary Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mass Effect Andromeda': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Final Fantasy VII Remake Intergrade': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Final Fantasy VII Rebirth': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Final Fantasy XV Windows Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Final Fantasy XIV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Final Fantasy XVI': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Final Fantasy XIII': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Final Fantasy XII: The Zodiac Age': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Persona 3 Reload': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Persona 4 Golden': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Persona 5 Royal': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Metaphor: ReFantazio': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tales of Arise': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tales of Berseria': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'NieR: Automata': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'NieR Replicant ver.1.22474487139': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Monster Hunter: World': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Monster Hunter Rise': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Monster Hunter Wilds': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Dark Souls Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Dark Souls II: Scholar of the First Sin': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dark Souls III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sekiro: Shadows Die Twice': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Elden Ring: Shadow of the Erdtree': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Lies of P': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Black Myth: Wukong': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Wo Long: Fallen Dynasty': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Nioh': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Nioh 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Lords of the Fallen (2023)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The First Berserker: Khazan': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Immortals Fenyx Rising': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'GreedFall': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Outward Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'V Rising': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Diablo II: Resurrected': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Diablo III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Diablo IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Path of Exile': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Path of Exile 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Torchlight II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Torchlight III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Last Epoch': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Grim Dawn': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warhammer 40,000: Rogue Trader': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warhammer 40,000: Space Marine 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warhammer: Vermintide 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Darktide': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sea of Stars': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Chained Echoes': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Octopath Traveler': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Octopath Traveler II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ys VIII: Lacrimosa of Dana': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ys IX: Monstrum Nox': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kingdom Hearts III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Blue Protocol': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Genshin Impact': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Honkai: Star Rail': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Wuthering Waves': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Zenless Zone Zero': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Resident Evil': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 0': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 3': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 4 (2005)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 4 Remake': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Resident Evil 6': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil 7: Biohazard': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Resident Evil Requiem': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Silent Hill 2 (2024)': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Silent Hill 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Silent Hill 4: The Room': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Evil Within': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Evil Within 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Outlast': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Outlast 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Amnesia: The Dark Descent': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Amnesia: Rebirth': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Amnesia: The Bunker': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'SOMA': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Alien: Isolation': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Callisto Protocol': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Space (2008)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Space (2023)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Space 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Space 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Phasmophobia': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Lethal Company': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Content Warning': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Five Nights at Freddy’s: Security Breach': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Little Nightmares': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Little Nightmares II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Little Nightmares III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Until Dawn': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Quarry': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Dark Pictures Anthology: Man of Medan': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Dark Pictures Anthology: Little Hope': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Dark Pictures Anthology: House of Ashes': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Dark Pictures Anthology: The Devil in Me': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Layers of Fear': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Martha Is Dead': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Visage': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MADiSON': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead by Daylight': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Texas Chain Saw Massacre': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Need for Speed Underground': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Underground 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Most Wanted (2005)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Carbon': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed ProStreet': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Undercover': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Shift': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Hot Pursuit (2010)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed The Run': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Most Wanted (2012)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Rivals': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed (2015)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Payback': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Heat': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Need for Speed Unbound': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Forza Motorsport 7': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Forza Motorsport (2023)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Forza Horizon 2': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Forza Horizon 3': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Forza Horizon 4': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'The Sims 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'F1 2018': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 2020': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 2021': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 22': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 23': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 24': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'F1 25': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Assetto Corsa': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Assetto Corsa Competizione': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Automobilista 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Project CARS': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Project CARS 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Wreckfest': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'BeamNG.drive': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'CarX Drift Racing Online': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dirt Rally': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'DiRT Rally 2.0': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'DiRT 5': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'GRID Autosport': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'GRID (2019)': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'SnowRunner': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Euro Truck Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'American Truck Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Train Sim World 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MotoGP 24': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ride 5': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'EA Sports FC 24': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'EA Sports FC 25': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'EA Sports FC 26': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'FIFA 19': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'FIFA 22': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'eFootball': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'NBA 2K24': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'NBA 2K25': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'NBA 2K26': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'WWE 2K24': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'WWE 2K25': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tony Hawk’s Pro Skater 1 + 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Skater XL': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Session: Skate Sim': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Age of Empires II: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Age of Empires III: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Age of Empires IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Age of Mythology: Retold': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Civilization V': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Civilization VI': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Civilization VII': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Total War: Rome II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Total War: Warhammer III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Total War: Three Kingdoms': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crusader Kings III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Europa Universalis IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hearts of Iron IV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Stellaris': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Cities: Skylines': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Cities: Skylines II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Planet Zoo': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Planet Coaster': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Planet Coaster 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Microsoft Flight Simulator (2020)': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Microsoft Flight Simulator 2024': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'X-Plane 12': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kerbal Space Program': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kerbal Space Program 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Farming Simulator 22': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Farming Simulator 25': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'PowerWash Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'House Flipper 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'PC Building Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'PC Building Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Sims 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Cities in Motion 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Factorio': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Satisfactory': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dyson Sphere Program': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Oxygen Not Included': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'RimWorld': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dwarf Fortress': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Against the Storm': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Frostpunk': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Frostpunk 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Anno 1800': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Anno 2205': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Command & Conquer Remastered Collection': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'StarCraft II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warcraft III: Reforged': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Company of Heroes 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Company of Heroes 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Age of Wonders 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'XCOM 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Marvel’s Midnight Suns': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Into the Breach': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Slay the Spire': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Balatro': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Hades': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hades II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dead Cells': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hollow Knight': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Hollow Knight: Silksong': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Cuphead': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Celeste': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Ori and the Blind Forest': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ori and the Will of the Wisps': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Binding of Isaac: Rebirth': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Vampire Survivors': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Stardew Valley': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Don’t Starve Together': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Undertale': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Deltarune': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Dave the Diver': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dredge': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Cult of the Lamb': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Animal Well': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Talos Principle': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Talos Principle 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Portal': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Portal 2': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Half-Life 2': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Black Mesa': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Garry’s Mod': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Team Fortress 2': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Fall Guys': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Among Us': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Poppy Playtime': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Roblox': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Minecraft Dungeons': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Minecraft Legends': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'LEGO Star Wars: The Skywalker Saga': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'LEGO Marvel Super Heroes': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'It Takes Two': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'A Way Out': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Split Fiction': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Unravel Two': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Human: Fall Flat': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Gang Beasts': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Party Animals': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sea of Thieves': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Deep Rock Galactic': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Helldivers 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'War Thunder': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'World of Tanks': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'World of Warships': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crossout': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'GTA Trilogy: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'The Lord of the Rings: Return to Moria': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Lords of the Fallen': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Remnant: From the Ashes': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Remnant II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Returnal': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ratchet & Clank: Rift Apart': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sackboy: A Big Adventure': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Kena: Bridge of Spirits': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Stray': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Last of Us Part I': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'The Last of Us Part II Remastered': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'Uncharted: Legacy of Thieves Collection': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Detroit: Become Human': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Beyond: Two Souls': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Heavy Rain': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'A Plague Tale: Innocence': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'A Plague Tale: Requiem': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'The Witness': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Outer Wilds': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Firewatch': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'What Remains of Edith Finch': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Journey': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'ABZÛ': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Stanley Parable: Ultra Deluxe': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Inscryption': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Papers, Please': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'This War of Mine': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Walking Dead: The Telltale Definitive Series': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Telltale’s The Wolf Among Us': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Life is Strange': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Life is Strange: True Colors': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Life is Strange: Double Exposure': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tell Me Why': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tomb Raider (2013)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Rise of the Tomb Raider': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Shadow of the Tomb Raider': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Prince of Persia: The Lost Crown': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Prince of Persia: The Sands of Time': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sifu': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hi-Fi RUSH': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Granblue Fantasy: Relink': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Armored Core VI: Fires of Rubicon': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MechWarrior 5: Mercenaries': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'DCS World': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Warhammer 40,000: Darktide': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Palia': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Throne and Liberty': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Lost Ark': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'New World: Aeternum': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Black Desert Online': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Guild Wars 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'World of Warcraft': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'EVE Online': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Star Wars: The Old Republic': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Star Wars Jedi: Fallen Order': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Star Wars Jedi: Survivor': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Star Wars Battlefront II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'LEGO Horizon Adventures': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Indiana Jones and the Great Circle': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'DOOM: The Dark Ages': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Fable (2025)': {"cpu": 78, "gpu": 85, "ram": 16, "fps": 60},
    'South of Midnight': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Avowed': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Alters': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Clair Obscur: Expedition 33': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MindsEye': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pragmata': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Monster Hunter Stories 2: Wings of Ruin': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Trackmania': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Trackmania Turbo': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hot Wheels Unleashed': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hot Wheels Unleashed 2: Turbocharged': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Golf With Your Friends': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'PGA Tour 2K25': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fishing Planet': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'TheHunter: Call of the Wild': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hunting Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Surviving Mars': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Surviving the Aftermath': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Terra Nil': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Timberborn': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Farthest Frontier': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Banished': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Universim': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Farming Simulator 19': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MudRunner': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Spintires': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Car Mechanic Simulator 2021': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Gas Station Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Internet Cafe Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Thief Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Drug Dealer Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Long Drive': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'My Summer Car': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Teardown': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Besiege': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'People Playground': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Totally Accurate Battle Simulator': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ultimate Epic Battle Simulator 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Universe Sandbox': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Space Engineers': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Empyrion - Galactic Survival': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Elite Dangerous': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Star Citizen': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Everspace 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Chorus': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Riftbreaker': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'They Are Billions': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Age of Darkness: Final Stand': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Stronghold: Definitive Edition': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Stronghold Crusader HD': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Commandos: Origins': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Desperados III': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Shadow Tactics: Blades of the Shogun': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Door Kickers 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Jagged Alliance 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Men of War II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Gates of Hell: Ostfront': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'BattleBit Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Chivalry 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mordhau': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mount & Blade II: Bannerlord': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mount & Blade: Warband': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'For Honor': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Naruto to Boruto: Shinobi Striker': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Ball Z: Kakarot': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dragon Ball: Sparking! ZERO': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tekken 7': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Tekken 8': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Street Fighter 6': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Mortal Kombat 11': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Mortal Kombat 1': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Guilty Gear -Strive-': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Soulcalibur VI': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The King of Fighters XV': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Brawlhalla': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'MultiVersus': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Injustice 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Marvel Rivals': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Paladins': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Smite 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'League of Legends': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dota 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Teamfight Tactics': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hearthstone': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Legends of Runeterra': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Magic: The Gathering Arena': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Yu-Gi-Oh! Master Duel': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Minecraft Java Edition': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Minecraft Bedrock Edition': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Roblox Studio': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Starbound': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Vintage Story': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Eco': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Necesse': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Forager': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Moonlighter': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Graveyard Keeper': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Littlewood': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sun Haven': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fields of Mistria': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Coral Island': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Disney Dreamlight Valley': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'LEGO Fortnite': {"cpu": 48, "gpu": 52, "ram": 8, "fps": 60},
    'Rocket League': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'VRChat': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Rec Room': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Beat Saber': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Half-Life: Alyx': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Noita': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Risk of Rain 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Risk of Rain Returns': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Enter the Gungeon': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Wizard of Legend': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Children of Morta': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Brotato': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Loop Hero': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Darkest Dungeon': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Darkest Dungeon II': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Faster Than Light': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'FTL: Faster Than Light': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Owlboy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Shovel Knight: Treasure Trove': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'A Hat in Time': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Psychonauts 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crash Bandicoot N. Sane Trilogy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Crash Bandicoot 4: It’s About Time': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Spyro Reignited Trilogy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sonic Mania': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sonic Frontiers': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sonic X Shadow Generations': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Rayman Legends': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Rayman Origins': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Trine 4: The Nightmare Prince': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Trine 5: A Clockwork Conspiracy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'The Messenger': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Blasphemous': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Blasphemous 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tunic': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Death’s Door': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hyper Light Drifter': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Katana ZERO': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mark of the Ninja: Remastered': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Limbo': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Inside': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Braid: Anniversary Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Fez': {"cpu": 25, "gpu": 20, "ram": 4, "fps": 60},
    'Super Meat Boy': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Pizza Tower': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ape Out': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hotline Miami': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hotline Miami 2: Wrong Number': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Neon White': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ghostrunner': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Ghostrunner 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mirror’s Edge': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Mirror’s Edge Catalyst': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dishonored': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Dishonored 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Prey (2017)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Deathloop': {"cpu": 65, "gpu": 70, "ram": 12, "fps": 60},
    'Thief (2014)': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Deus Ex: Human Revolution': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Deus Ex: Mankind Divided': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hitman: World of Assassination': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Hitman 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sniper Elite 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sniper Elite 5': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Metal Gear Solid V: The Phantom Pain': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Metal Gear Solid Delta: Snake Eater': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Splinter Cell: Blacklist': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Sniper Ghost Warrior Contracts 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Shadow Warrior 2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Shadow Warrior 3': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Serious Sam 4': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Painkiller: Black Edition': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'L4D2': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Zombie Army 4: Dead War': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'World War Z: Aftermath': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'GTFO': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'Tom Clancy’s Breakpoint': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
    'XDefiant': {"cpu": 42, "gpu": 40, "ram": 8, "fps": 60},
}



# Typical/reference VRAM values (GB). Integrated graphics use shared system memory,
# so their actual available graphics memory depends on the computer configuration.
def get_vram(gpu_name):
    name = gpu_name.lower()
    if "5090" in name: return "32 GB"
    if "5080" in name: return "16 GB"
    if "5070 ti" in name: return "16 GB"
    if "5070" in name: return "12 GB"
    if "5060 ti 16gb" in name or "arc a770 16gb" in name: return "16 GB"
    if "5060 ti" in name or "5060" in name: return "8 GB (typical; verify exact model)"
    if "4090" in name: return "24 GB"
    if "4080" in name: return "16 GB"
    if "4070 ti super" in name: return "16 GB"
    if "4070" in name: return "12 GB (some variants differ)"
    if "4060 ti" in name: return "8 or 16 GB, depending on model"
    if "4060" in name or "3060" in name: return "8 or 12 GB, depending on model"
    if "3090" in name: return "24 GB"
    if "3080 ti" in name: return "12 GB"
    if "3080" in name: return "10 or 12 GB, depending on model"
    if "3070 ti" in name: return "8 GB"
    if "3070" in name: return "8 GB"
    if "3050 6gb" in name: return "6 GB"
    if "3050" in name: return "6 or 8 GB, depending on model"
    if "2060 super" in name: return "8 GB"
    if "2060" in name: return "6 GB (some variants differ)"
    if "2080 ti" in name: return "11 GB"
    if "2080" in name: return "8 GB"
    if "2070" in name: return "8 GB"
    if "1060 3gb" in name: return "3 GB"
    if "1060" in name: return "6 GB"
    if "1050 ti" in name: return "4 GB"
    if "1050" in name: return "2 or 3 GB, depending on model"
    if "1650" in name: return "4 GB (typical)"
    if "1660" in name: return "6 GB (typical)"
    if "1080" in name: return "8 GB"
    if "1070" in name: return "8 GB"
    if "970" in name: return "4 GB"
    if "980" in name: return "4 GB"
    if "rx 9070 xt" in name: return "16 GB"
    if "rx 9070" in name: return "16 GB"
    if "7900 xtx" in name: return "24 GB"
    if "7900 xt" in name: return "20 GB"
    if "7900 gre" in name: return "16 GB"
    if "7800 xt" in name: return "16 GB"
    if "7700 xt" in name: return "12 GB"
    if "7600 xt" in name: return "16 GB"
    if "7600" in name: return "8 GB"
    if "6800 xt" in name: return "16 GB"
    if "6800" in name: return "16 GB"
    if "6700 xt" in name or "6750 xt" in name: return "12 GB"
    if "6600" in name or "6650 xt" in name: return "8 GB"
    if "580" in name: return "4 or 8 GB, depending on model"
    if "570" in name: return "4 or 8 GB, depending on model"
    if "arc a770" in name: return "8 or 16 GB, depending on model"
    if "arc b580" in name: return "12 GB"
    if "arc b570" in name: return "10 GB"
    if "arc a750" in name: return "8 GB"
    if "arc a580" in name: return "8 GB"
    if "arc a380" in name: return "6 GB"
    if any(x in name for x in ["intel hd", "intel uhd", "iris", "vega", "radeon 610m", "radeon 680m", "radeon 780m", "radeon 890m", "apple m1", "apple m2", "apple m3"]):
        return "Shared system memory (not dedicated VRAM)"
    if "8670m" in name: return "1–2 GB, depending on model"
    if "rx 550" in name: return "2 or 4 GB, depending on model"
    if "rx 560" in name: return "2 or 4 GB, depending on model"
    if "rx 460" in name: return "2 or 4 GB, depending on model"
    if "rx 470" in name or "rx 480" in name: return "4 or 8 GB, depending on model"
    if "gt 1030" in name: return "2 GB (GDDR5 or slower DDR4 variants)"
    if "gt 710" in name or "gt 730" in name: return "1–2 GB, depending on model"
    if "rtx 2050" in name: return "4 GB"
    if "laptop" in name: return "Varies by laptop GPU configuration"
    return "Varies by exact model; check manufacturer specifications"


# ============================================================
# FPS ESTIMATION
# ============================================================

def estimate_fps(cpu_score, gpu_score, required_cpu, required_gpu, ram, required_ram, target_fps):

    cpu_ratio = cpu_score / required_cpu
    gpu_ratio = gpu_score / required_gpu

    performance = min(cpu_ratio, gpu_ratio)

    if ram < required_ram:
        performance *= 0.65

    # Approximate FPS
    fps = int(target_fps * performance)

    # Keep results realistic
    fps = max(5, min(fps, 240))

    return fps


def get_settings(fps):

    if fps >= 100:
        return "Ultra / Very High"

    if fps >= 70:
        return "High"

    if fps >= 50:
        return "Medium-High"

    if fps >= 30:
        return "Medium / Low"

    if fps >= 20:
        return "Low"

    return "Very Low"


# ============================================================
# MAIN ROUTE
# ============================================================

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        cpu = request.form.get("cpu")
        gpu = request.form.get("gpu")
        ram_text = request.form.get("ram")
        game = request.form.get("game")

        try:
            ram = int(ram_text)
        except (ValueError, TypeError):
            ram = 0

        if cpu not in CPUS or gpu not in GPUS or game not in GAMES:

            result = {
                "type": "danger",
                "title": "🔴 INVALID INPUT",
                "message": "Please select a valid CPU, GPU, RAM and game."
            }

        else:

            cpu_score = CPUS[cpu]
            gpu_score = GPUS[gpu]

            requirements = GAMES[game]

            required_cpu = requirements["cpu"]
            required_gpu = requirements["gpu"]
            required_ram = requirements["ram"]

            cpu_ok = cpu_score >= required_cpu
            gpu_ok = gpu_score >= required_gpu
            ram_ok = ram >= required_ram

            fps = estimate_fps(
                cpu_score,
                gpu_score,
                required_cpu,
                required_gpu,
                ram,
                required_ram,
                requirements["fps"]
            )

            settings = get_settings(fps)

            # --------------------------------------------
            # RESULT LEVEL
            # --------------------------------------------

            if cpu_ok and gpu_ok and ram_ok:

                result_type = "success"
                title = "🟢 CAN RUN"

                message = (
                    f"Your PC should be able to run {game} "
                    f"at an estimated {fps} FPS. Actual performance varies by resolution, settings, drivers, and cooling."
                )

            elif (
                cpu_score >= required_cpu * 0.75
                and gpu_score >= required_gpu * 0.75
                and ram >= required_ram * 0.75
            ):

                result_type = "warning"
                title = "🟡 MAY RUN"

                message = (
                    f"Your PC may run {game}, but you may need "
                    f"lower graphics settings. Estimated FPS: {fps}; real results can vary by system and settings."
                )

            else:

                result_type = "danger"
                title = "🔴 CANNOT RUN WELL"

                message = (
                    f"Your PC is below the recommended performance "
                    f"for {game}. Estimated FPS: {fps}; this is a rough estimate, not a benchmark guarantee."
                )

            # --------------------------------------------
            # UPGRADE ADVICE
            # --------------------------------------------

            upgrades = []

            if not gpu_ok:
                upgrades.append("🎨 A stronger GPU would help the most.")

            if not cpu_ok:
                upgrades.append("🧠 A stronger CPU would improve performance.")

            if not ram_ok:
                upgrades.append(
                    f"💾 Consider at least {required_ram} GB of RAM."
                )

            if not upgrades:
                upgrades.append("🔥 No major upgrade is required.")

            result = {
                "type": result_type,
                "title": title,
                "message": message,

                "cpu": cpu,
                "gpu": gpu,
                "ram": ram,

                "required_cpu": required_cpu,
                "required_gpu": required_gpu,
                "required_ram": required_ram,

                "cpu_score": cpu_score,
                "gpu_score": gpu_score,
                "vram": get_vram(gpu),

                "fps": fps,
                "settings": settings,

                "upgrades": upgrades
            }

    return render_template(
        "index.html",
        result=result,
        cpus=CPUS,
        gpus=GPUS,
        games=GAMES,
        cpu_count=len(CPUS),
        gpu_count=len(GPUS),
        game_count=len(GAMES)
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)
