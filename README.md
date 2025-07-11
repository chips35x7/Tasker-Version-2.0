# 📝 Nigey's To-Do App

A simple desktop to-do list application built with Python and PySide6.  
Track your tasks, mark them complete, and stay organized — all with a clean and intuitive UI.

---

📷 App Screenshot
<img width="1920" height="992" alt="Tasker" src="https://github.com/user-attachments/assets/03766f44-5172-4b10-9519-db2a8a623ad9" />

## 🚀 Features

- Add new tasks
- Mark tasks as complete or incomplete
- Delete individual tasks
- Clear all tasks
- Switch between incomplete and completed task views
- Duplicate task warning
- Data saved in a local SQLite database
- Styled interface using QSS

---

## 📦 Requirements

- Python 3.7+
- PySide6

You can install dependencies with:

```bash
pip install -r requirements.txt
If requirements.txt doesn’t exist yet, create one with:
```bash

▶️ Running the App

```bash
python main.py
```bash
Make sure the following files are in the same directory:
    ---->main.py
    ---->main_ui.py (UI from Qt Designer)
    ---->database_manager.py
    ---->custom_item_list_widget.py
    ---->resources/style.qss
    ---->tasker.ico (optional app icon)

⚡ Run Without Installing Python
If you're using Windows and prefer to run the game without installing Python or Pygame, use the standalone executable included in the dist/ folder:

Navigate to the dist/ folder in this repository.
Run the file:
Tasker.v.2.0.exe
