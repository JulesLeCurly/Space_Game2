# 🌌 Space Game 2

A procedural 3D space simulator built with Python and **Pygame**, created completely from scratch without external 3D engines. The universe is infinitely generated through deterministic 3D chunks, featuring a software-based 3D perspective projection engine computed using pure CPU trigonometry.

---

## 📝 Background & Context

This project is a personal creation originally built for practice, learning, and above all, the joy of coding.

The 3D engine was designed and developed using only the mathematical foundation available at the time: **classic trigonometry**. For this reason, the game does not aim for cutting-edge performance or modern GPU acceleration pipelines, but rather relies on elementary mathematical equations calculated directly by the CPU. The core intention was simply to explore the challenge of building an immersive, procedural 3D universe from scratch using basic tools.

---

## 🚀 Features

* **Software 3D Engine "from scratch"** : Custom 3D rendering engine without OpenGL, computing trigonometric rotations and perspective projection directly on the CPU.
* **Infinite Universe via 3D Chunks** : Deterministic procedural generation powered by SHA-256 hashes (fully reproducible given a specific seed).
* **Rich Stellar & Planetary Systems** :
  * Stars with spectral classification, apparent magnitude, solar mass, and chemical composition.
  * Planets with mass, radius, surface temperature, atmospheric composition, and probability of harboring life (microorganisms, plant life, animal life, or intelligent civilizations with technological tiers).
* **6-DOF Space Flight** : Free camera orientation using mouse tracking, adjustable thruster power, and faster-than-light cruising (*Warp* factor).
* **Dynamic Audio System** : Randomized ambient space music playlist with automatic track chaining.
* **Save System** : Coordinate and seed persistence powered by NumPy.

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.10 or higher
* `pip`

### 1. Clone the repository
```bash
git clone https://github.com/your-username/space_game2.git
cd space_game2
```

### 2. Install dependencies
On Windows, you can double-click `Download.bat` or run:
```bash
pip install -r requirements.txt
```

---

## 🎮 How to Play

To launch the simulator:
```bash
python Main.py
```

> [!TIP]
> **Screen Resolution** : By default, the game window is set to an ultra-wide display (`3440 x 1440`). If you are using a standard monitor (e.g. Full HD `1920 x 1080`), open `Variable.py` and adjust the first two lines:
> ```python
> display_x, display_y = 1920, 1080
> ```

---

## 🕹️ Controls

| Key / Input | Action |
| :--- | :--- |
| **Mouse (Click & Drag)** | Look around / Rotate camera (pitch and yaw) |
| **Z** | Move forward (towards camera direction) |
| **S** | Move backward |
| **Q** | Strafe left |
| **D** | Strafe right |
| **Left Ctrl** | Ascend (+Y altitude) |
| **Left Shift** | Descend (-Y altitude) |
| **A** | Increase thruster power / speed |
| **E** | Decrease thruster power / speed |
| **R** | Increase Warp factor (faster rotation / speed scaling) |
| **F** | Decrease Warp factor |
| **W** | **Save** current position and seed (saved in `Save/` folder) |
| **X** | **Load** the latest save |
| **O** | Print current coordinates and chunk info to console |

---

## ⚙️ Configuration (`Variable.py`)

You can tweak simulator parameters in `Variable.py`:

* `display_x, display_y` : Window width and height in pixels.
* `Nombre_etoile_chunk` : Number of stars generated per chunk (default: `2_000`). Higher values create denser starfields but require more CPU processing.
* `Taille_chunk` : Size of each cubic chunk in space coordinates (default: `10_000`).
* `seed` : Universe generation seed (can be a number or a string).
* `Show_info` : Toggle HUD display for FPS counter and coordinates.

---

## 📂 Project Structure

```text
space_game2/
├── GameData/
│   ├── Audio/               # Music playback and duration handling
│   ├── Autopilot/           # Navigation and cruise algorithms
│   ├── Generate/            # Procedural star and planet generation
│   ├── inputs_and_coordonne/# Player movement vectors & mouse tracker
│   ├── Render/              # Software 3D renderer & text display
│   └── Save/                # Data persistence module
├── Pack/
│   └── default/             # Textures and ambient music tracks
├── Save/                    # Save directory (git-ignored, kept via .gitkeep)
├── CREDITS.md               # Legal music attributions (CC-BY 3.0)
├── Download.bat             # Quick install script for Windows
├── Main.py                  # Main entry point and game loop
├── requirements.txt         # Required Python packages
├── Variable.py              # Main configuration file (resolution, seed...)
└── Variable_space_render.py # Rendering engine tuners (FOV, brightness...)
```

---

## 🎵 Music & Credits

Ambient in-game music was composed by **Kevin MacLeod** ([incompetech.com](https://incompetech.com)) and licensed under **Creative Commons: By Attribution 3.0 (CC-BY)**.  
Please see [CREDITS.md](CREDITS.md) for full attribution notices and track titles.
