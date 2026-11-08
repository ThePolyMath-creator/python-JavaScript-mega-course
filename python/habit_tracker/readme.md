# 🌱 Habit Tracker – Python

<p align="center">

  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
  ![Status](https://img.shields.io/badge/Status-In%20Development-orange)
  ![Storage](https://img.shields.io/badge/Storage-JSON-yellow)
  ![License](https://img.shields.io/badge/License-MIT-green)

</p>

A simple yet powerful **Habit Tracker** built with Python to help users develop positive habits, monitor daily progress, and maintain consistency.

🚀 The goal of this project is to build **three different applications** using the same core logic:

- 💻 Command-Line Interface (CLI)
- 🖥️ Desktop Application (Tkinter)
- 🌐 Web Application (Flask)

---

## 📌 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [✨ Features](#-features)
- [🛠️ Technologies](#️-technologies)
- [🗺️ Development Roadmap](#️-development-roadmap)
- [📂 Project Structure](#-project-structure)
- [🚀 Getting Started](#-getting-started)
- [💻 CLI Application](#-cli-application)
- [📚 What I'm Learning](#-what-im-learning)
- [🔮 Future Improvements](#-future-improvements)

---

## 🎯 Project Overview

The Habit Tracker allows users to create and manage daily habits while tracking their completion progress.

Example habits:

- 📖 Read for 20 minutes
- 🏋️ Exercise
- 💧 Drink 2L of water
- 🐍 Study Python

The project will evolve from a simple terminal application into a desktop application and finally a web application.

**Main Goal:** Build three working applications that share the same habit-tracking system.

---

## ✨ Features

### 📋 Core Features

| Feature | Description |
|---|---|
| ➕ Add Habits | Create new habits |
| 🗑️ Delete Habits | Remove existing habits |
| ✅ Complete Habits | Track daily completion |
| 🔥 Streaks | Count consecutive days |
| 📊 Statistics | View daily and weekly progress |
| 📅 History | View previous records |
| 💾 Data Persistence | Save progress permanently |

### 🧩 Application Features

| Application | Technology | Status |
|---|---|---|
| 💻 CLI | Python | 🟡 In Development |
| 🖥️ Desktop | Tkinter | ⏳ Planned |
| 🌐 Web | Flask, HTML, CSS, JavaScript | ⏳ Planned |

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 📄 JSON | Initial data storage |
| 🖥️ Tkinter | Desktop GUI |
| 🌐 Flask | Web backend |
| 🎨 HTML & CSS | Web interface |
| ⚡ JavaScript | Web interactivity |
| 🗄️ SQLite | Potential future database |

---

## 🗺️ Development Roadmap

### 💻 Phase 1 – CLI Habit Tracker

<details open>
<summary><b>Version 1.0 – Command Line Application</b></summary>

- [x] Create project structure
- [x] Display interactive menu
- [x] Accept user input
- [x] Implement `while` loops
- [x] Implement `if / elif / else`
- [x] Create Add Habit functionality
- [x] Create View Habits functionality
- [ ] Implement Complete Habit
- [ ] Implement Delete Habit
- [ ] Implement Statistics
- [ ] Save data using JSON
- [ ] Load saved data when starting the application
- [ ] Implement completion streaks

</details>

### 🖥️ Phase 2 – Desktop Habit Tracker

<details>
<summary><b>Version 2.0 – Tkinter Application</b></summary>

- [ ] Create desktop window
- [ ] Design dashboard
- [ ] Add habit creation form
- [ ] Add completion buttons
- [ ] Display habit progress
- [ ] Add statistics dashboard
- [ ] Integrate shared core logic

</details>

### 🌐 Phase 3 – Web Habit Tracker

<details>
<summary><b>Version 3.0 – Flask Application</b></summary>

- [ ] Set up Flask application
- [ ] Create HTML templates
- [ ] Design responsive interface
- [ ] Add CSS styling
- [ ] Implement JavaScript interactions
- [ ] Connect backend with shared core logic
- [ ] Display progress and statistics

</details>

---

## 📂 Project Structure

The planned project structure:

```text
habit_tracker/
│
├── core/
│   ├── habit.py
│   ├── tracker.py
│   └── storage.py
│
├── cli/
│   └── main.py
│
├── desktop/
│   └── main.py
│
├── web/
│   ├── app.py
│   ├── templates/
│   └── static/
│
├── data/
│   └── habits.json
│
└── README.md
```

**📌 Architecture:**

- `core/` – Shared habit-tracking logic.
- `cli/` – Command-line interface.
- `desktop/` – Tkinter desktop application.
- `web/` – Flask web application.
- `data/` – JSON data storage.

The core logic will be shared across all three applications to avoid rewriting the same functionality.

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have:

- Python installed.
- Visual Studio Code (or another Python editor).
- Basic knowledge of Python.

### 2️⃣ Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 3️⃣ Navigate to the Project

```bash
cd habit_tracker
```

### 4️⃣ Run the CLI Application

```bash
python main.py
```

Alternatively, on Windows:

```bash
py main.py
```

---

## 💻 CLI Application

The first version uses a simple interactive terminal menu.

### 📋 Main Menu

```text
================================
         HABIT TRACKER
================================

1. Add a habit
2. View all habits
3. Complete a habit
4. Delete a habit
5. View statistics
6. Exit

Choose an option:
```

### 🧪 Current Implementation

The project currently supports:

- Interactive menu navigation.
- Adding new habits.
- Displaying existing habits.
- Basic input validation.

### 📝 Example Data Structure

Habits are initially stored using Python lists and dictionaries.

```python
habits = [
    {"name": "Reading", "completed": False},
    {"name": "Exercise", "completed": False}
]
```

---

## 📚 What I'm Learning

Throughout this project, I'm practicing:

- 🐍 Python fundamentals
- 🔄 Loops and conditional statements
- 📦 Lists and dictionaries
- 🧩 Functions and modular programming
- 💾 File handling and JSON
- 🖥️ GUI development with Tkinter
- 🌐 Backend development with Flask
- 🎨 Frontend development with HTML, CSS, and JavaScript
- 🏗️ Software architecture and code reuse

---

## 🔮 Future Improvements

Potential improvements after completing the three applications:

- 📈 Advanced progress charts
- 🔔 Daily reminders
- 🎯 Weekly and monthly goals
- 🏆 Achievement system
- 📊 More detailed analytics
- 👤 Multiple user accounts
- ☁️ Cloud-based data synchronization

---

## 🤝 Contributing

Suggestions and improvements are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a Pull Request.

---

## 📜 License

This project is intended as a learning project. An MIT License can be added when the project is ready for distribution.

---

## ⭐ Support

If you find this project interesting, consider giving it a ⭐ on GitHub!

**Built with ❤️ and Python 🐍**

*One habit at a time. One step closer to a better version of yourself.* 🌱