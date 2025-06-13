---

# 🐍 Snake Game in Python

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A simple, classic Snake game built using Python’s `turtle` module. Guide the snake using arrow keys and eat food to grow — avoid crashing into walls (extendable) or yourself.

---

## 🎮 Features

- Snake movement using arrow keys
- Food appears randomly and gets eaten when touched
- Snake grows after eating food
- Smooth animation using `tracer()` and `sleep()`
- Clean modular OOP structure

---

## 🧠 Python Concepts Used

- **Object-Oriented Programming**: `Snake`, `Food` classes
- **Turtle Graphics**: Visual movement, color, and position handling
- **Game Loop & Animation**: Manual frame updates
- **Collision Detection**: Distance-based food pickup
- **Event Handling**: Arrow key controls via `onkey()`

---

## 📁 File Structure

```

snake-game/
├── main.py        # Game loop
├── snake.py       # Snake class and movement
├── food.py        # Food class and random placement

````

---

## ▶️ How to Run

**Requirements**: Python 3.7+

```bash
git clone https://github.com/your-username/snake-game.git
cd snake-game
python main.py
````

---

## 🎮 Controls

| Direction | Key     |
| --------- | ------- |
| Up        | ↑ Arrow |
| Left      | ← Arrow |
| Right     | → Arrow |

---

## 📄 License

MIT License — free to use, modify, and share.

---
