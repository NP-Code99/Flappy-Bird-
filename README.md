<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,12,18&height=180&section=header&text=Flappy%20Bird&fontSize=52&fontColor=fff&animation=twinkling&fontAlignY=36&desc=Python%20Pygame%20Recreation%20with%20Custom%20Assets&descSize=16&descAlignY=58&descColor=bbf7d0" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pygame](https://img.shields.io/badge/Pygame-000000?style=for-the-badge&logo=python&logoColor=white)](https://pygame.org)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey?style=for-the-badge)]()
[![Forked](https://img.shields.io/badge/Forks-1-blue?style=for-the-badge&logo=github)]()

</div>

---

## 📌 Overview

A **Python + Pygame** recreation of the classic Flappy Bird arcade game, complete with custom sprite assets and fonts. The player controls a bird navigating through an endless series of pipes by tapping to flap — free to play, forever.

---

## 🎮 Features

- 🐦 **Smooth bird physics** — gravity and flap mechanics
- 🌿 **Procedural pipe generation** — infinite scrolling obstacles
- 🏆 **Score tracking** — counts pipes successfully passed
- 🖼️ **Custom assets** — original sprite images in `All Images/`
- 🔤 **Custom fonts** — styled score display from `All Fonts/`
- 💀 **Collision detection** — game over on pipe or ground hit

---

## 📁 Project Structure

```
Flappy-Bird-/
├── flappy_bird.py    # Main game loop — physics, rendering, collision
├── All Images/       # Bird, pipes, background, ground sprites
└── All Fonts/        # Custom fonts for score display
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|:---|:---|
| `Python` | Core game logic and physics |
| `Pygame` | Window rendering, sprite blitting, event handling |

---

## 🚀 Getting Started

### Install dependencies
```bash
pip install pygame
```

### Run the game
```bash
python flappy_bird.py
```

---

## 🕹️ Controls

| Action | Key |
|:---|:---|
| Flap / Jump | `SPACE` or Mouse Click |
| Restart after game over | `SPACE` |
| Quit | Close the window |

---

## ⚙️ Game Mechanics

```
Each frame:
  1. Apply gravity → bird falls
  2. On SPACE press → apply upward velocity (flap)
  3. Scroll pipes left at constant speed
  4. Spawn new pipe pair when previous clears screen
  5. Check collision → bird vs pipes + bird vs ground
  6. Increment score when bird clears a pipe gap
  7. Game over → show final score → wait for restart
```

---

## 🗺️ Roadmap

- [x] Gravity and flap physics
- [x] Infinite pipe generation
- [x] Collision detection
- [x] Score display with custom fonts
- [x] Custom sprite assets
- [ ] High score persistence (local file)
- [ ] Difficulty scaling (pipes speed up over time)
- [ ] Animated bird flap frames

---

<div align="center">

**Built by [Nandan Pullakandam](https://github.com/NP-Code99)**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/nandan-pullakandam)
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=flat-square&logo=github&logoColor=white)](https://github.com/NP-Code99)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=7,12,18&height=100&section=footer" width="100%"/>

</div>
