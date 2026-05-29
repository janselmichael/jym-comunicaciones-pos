# 📝 Todo List Application

A modern, feature-rich to-do list application with local storage functionality.

## ✨ Features

✅ **Add Tasks** - Quick add or detailed add with description
✅ **Task Management** - Edit, complete, and delete tasks
✅ **Priority Levels** - Low, Normal, High, Urgent with color coding
✅ **Due Dates** - Set deadlines for your tasks
✅ **Task Filtering** - View All, Pending, or Completed tasks
✅ **Local Storage** - All data stored in JSON file (todos.json)
✅ **Export Tasks** - Export your tasks to JSON format
✅ **Modern UI** - Clean and intuitive interface with emojis
✅ **Auto-save** - Changes are saved automatically

## 🚀 Installation & Usage

### Option 1: Run from Executable
```bash
# Download TodoList_App.exe from dist/
# Double-click to run
```

### Option 2: Run from Python
```bash
# Install dependencies
pip install PyQt5

# Run the app
python todo_app.py
```

## 📋 How to Use

### Adding Tasks
1. **Quick Add**: Type in the input field and press Enter
2. **Detailed Add**: Click "+ Add Task" to add description, priority, and due date

### Managing Tasks
- **Mark Complete**: Select task and click "✓ Mark Complete"
- **Edit**: Select task and click "✎ Edit"
- **Delete**: Select task and click "🗑 Delete"

### Filtering
- **All**: View all tasks
- **Pending**: View incomplete tasks only
- **Completed**: View completed tasks only

### Features
- **Color Coding**: 
  - 🔵 Low Priority (Blue)
  - 🟢 Normal Priority (Green)
  - 🟠 High Priority (Orange)
  - 🔴 Urgent Priority (Red)

- **Export**: Save all tasks to JSON file
- **Clear Completed**: Remove all completed tasks at once

## 💾 Data Storage

- Tasks are automatically saved to `todos.json`
- Each task contains:
  - Title
  - Description
  - Priority level
  - Due date
  - Completion status
  - Creation timestamp
  - Completion timestamp

## 🔧 Compile to Executable

```bash
python build_todo_exe.py
```

The executable will be created in `dist/TodoList_App.exe`

## 📁 File Structure

```
├── todo_app.py           # Main application
├── build_todo_exe.py     # Build script
├── todos.json            # Local storage (auto-created)
└── README_TODO.md        # This file
```

## ⚙️ System Requirements

- **Windows 7+** (for executable)
- **Python 3.7+** (for source code)
- **Minimum 10 MB** disk space

## 🎨 User Interface

- Modern tabbed interface
- Emoji icons for visual feedback
- Color-coded priority levels
- Strikethrough for completed tasks
- Real-time updates

## 📝 Example Tasks

- Buy groceries (Normal priority)
- Fix bug in code (Urgent priority)
- Call dentist (High priority, with due date)
- Read book chapter (Low priority)

## 🤝 Contributing

Feel free to customize and extend the application!

## 📄 License

Free to use and modify.

---

**Version:** 1.0
**Last Updated:** 2026
**Made with ❤️**
