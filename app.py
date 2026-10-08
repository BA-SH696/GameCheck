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
    }
}


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
                    f"at approximately {fps} FPS."
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
                    f"lower graphics settings. Estimated FPS: {fps}."
                )

            else:

                result_type = "danger"
                title = "🔴 CANNOT RUN WELL"

                message = (
                    f"Your PC is below the recommended performance "
                    f"for {game}. Estimated FPS: {fps}."
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

                "fps": fps,
                "settings": settings,

                "upgrades": upgrades
            }

    return render_template(
        "index.html",
        result=result,
        cpus=CPUS,
        gpus=GPUS,
        games=GAMES
    )


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":
    app.run(debug=True)