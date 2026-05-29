import sys
import json
import os
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QPushButton, QLineEdit, QListWidget,
                             QListWidgetItem, QDialog, QLabel, QComboBox,
                             QDialogButtonBox, QMessageBox, QCheckBox, QDateEdit,
                             QTextEdit, QSpinBox, QFileDialog)
from PyQt5.QtCore import Qt, QDate, QDateTime
from PyQt5.QtGui import QFont, QColor, QIcon

class TodoApp:
    def __init__(self):
        self.todos_file = 'todos.json'
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.todos_file):
            try:
                with open(self.todos_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.todos_file, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, ensure_ascii=False, indent=2)
    
    def add_todo(self, title, description='', priority='Normal', due_date=None):
        """Add a new todo"""
        todo = {
            'id': len(self.todos) + 1,
            'title': title,
            'description': description,
            'priority': priority,
            'due_date': due_date,
            'completed': False,
            'created_at': datetime.now().isoformat(),
            'completed_at': None
        }
        self.todos.append(todo)
        self.save_todos()
        return todo
    
    def update_todo(self, todo_id, **kwargs):
        """Update a todo"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo.update(kwargs)
                self.save_todos()
                return todo
        return None
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        self.todos = [t for t in self.todos if t['id'] != todo_id]
        self.save_todos()
    
    def get_todo(self, todo_id):
        """Get a specific todo"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None
    
    def toggle_complete(self, todo_id):
        """Toggle todo completion status"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = not todo['completed']
                if todo['completed']:
                    todo['completed_at'] = datetime.now().isoformat()
                else:
                    todo['completed_at'] = None
                self.save_todos()
                return todo
        return None
    
    def get_all_todos(self):
        """Get all todos"""
        return self.todos
    
    def get_pending_todos(self):
        """Get all incomplete todos"""
        return [t for t in self.todos if not t['completed']]
    
    def get_completed_todos(self):
        """Get all completed todos"""
        return [t for t in self.todos if t['completed']]

class AddTodoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Add New Todo')
        self.setGeometry(100, 100, 500, 400)
        
        layout = QVBoxLayout()
        
        # Title
        layout.addWidget(QLabel('Title:'))
        self.title = QLineEdit()
        self.title.setPlaceholderText('Enter task title')
        layout.addWidget(self.title)
        
        # Description
        layout.addWidget(QLabel('Description:'))
        self.description = QTextEdit()
        self.description.setPlaceholderText('Enter task description (optional)')
        self.description.setMaximumHeight(100)
        layout.addWidget(self.description)
        
        # Priority
        layout.addWidget(QLabel('Priority:'))
        self.priority = QComboBox()
        self.priority.addItems(['Low', 'Normal', 'High', 'Urgent'])
        layout.addWidget(self.priority)
        
        # Due Date
        layout.addWidget(QLabel('Due Date (optional):'))
        self.due_date = QDateEdit()
        self.due_date.setDate(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        layout.addWidget(self.due_date)
        
        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        self.setLayout(layout)
    
    def get_data(self):
        due_date = self.due_date.date().toString('yyyy-MM-dd') if self.due_date.date() > QDate.currentDate() else None
        return {
            'title': self.title.text(),
            'description': self.description.toPlainText(),
            'priority': self.priority.currentText(),
            'due_date': due_date
        }

class EditTodoDialog(QDialog):
    def __init__(self, todo, parent=None):
        super().__init__(parent)
        self.todo = todo
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Edit Todo')
        self.setGeometry(100, 100, 500, 400)
        
        layout = QVBoxLayout()
        
        # Title
        layout.addWidget(QLabel('Title:'))
        self.title = QLineEdit()
        self.title.setText(self.todo['title'])
        layout.addWidget(self.title)
        
        # Description
        layout.addWidget(QLabel('Description:'))
        self.description = QTextEdit()
        self.description.setText(self.todo['description'])
        self.description.setMaximumHeight(100)
        layout.addWidget(self.description)
        
        # Priority
        layout.addWidget(QLabel('Priority:'))
        self.priority = QComboBox()
        self.priority.addItems(['Low', 'Normal', 'High', 'Urgent'])
        self.priority.setCurrentText(self.todo['priority'])
        layout.addWidget(self.priority)
        
        # Due Date
        layout.addWidget(QLabel('Due Date (optional):'))
        self.due_date = QDateEdit()
        if self.todo['due_date']:
            self.due_date.setDate(QDate.fromString(self.todo['due_date'], 'yyyy-MM-dd'))
        else:
            self.due_date.setDate(QDate.currentDate())
        self.due_date.setCalendarPopup(True)
        layout.addWidget(self.due_date)
        
        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        self.setLayout(layout)
    
    def get_data(self):
        return {
            'title': self.title.text(),
            'description': self.description.toPlainText(),
            'priority': self.priority.currentText(),
            'due_date': self.due_date.date().toString('yyyy-MM-dd')
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = TodoApp()
        self.current_filter = 'all'
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Todo List Application')
        self.setGeometry(100, 100, 900, 600)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        # Header
        header_layout = QHBoxLayout()
        title = QLabel('📝 My Tasks')
        title.setFont(QFont('Arial', 20, QFont.Bold))
        header_layout.addWidget(title)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)
        
        # Filter buttons
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel('Filter:'))
        
        btn_all = QPushButton('All')
        btn_all.clicked.connect(lambda: self.filter_todos('all'))
        filter_layout.addWidget(btn_all)
        
        btn_pending = QPushButton('Pending')
        btn_pending.clicked.connect(lambda: self.filter_todos('pending'))
        filter_layout.addWidget(btn_pending)
        
        btn_completed = QPushButton('Completed')
        btn_completed.clicked.connect(lambda: self.filter_todos('completed'))
        filter_layout.addWidget(btn_completed)
        
        filter_layout.addStretch()
        main_layout.addLayout(filter_layout)
        
        # Input section
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('Quick add: Enter task title...')
        self.input_field.returnPressed.connect(self.quick_add_todo)
        input_layout.addWidget(self.input_field)
        
        btn_add = QPushButton('+ Add Task')
        btn_add.clicked.connect(self.add_todo_dialog)
        input_layout.addWidget(btn_add)
        
        main_layout.addLayout(input_layout)
        
        # Todo list
        self.todo_list = QListWidget()
        self.todo_list.itemClicked.connect(self.on_todo_selected)
        main_layout.addWidget(self.todo_list)
        
        # Action buttons
        action_layout = QHBoxLayout()
        
        btn_complete = QPushButton('✓ Mark Complete')
        btn_complete.clicked.connect(self.toggle_todo)
        action_layout.addWidget(btn_complete)
        
        btn_edit = QPushButton('✎ Edit')
        btn_edit.clicked.connect(self.edit_todo)
        action_layout.addWidget(btn_edit)
        
        btn_delete = QPushButton('🗑 Delete')
        btn_delete.clicked.connect(self.delete_todo)
        action_layout.addWidget(btn_delete)
        
        action_layout.addStretch()
        
        btn_export = QPushButton('📥 Export')
        btn_export.clicked.connect(self.export_todos)
        action_layout.addWidget(btn_export)
        
        btn_clear_completed = QPushButton('Clear Completed')
        btn_clear_completed.clicked.connect(self.clear_completed)
        action_layout.addWidget(btn_clear_completed)
        
        main_layout.addLayout(action_layout)
        
        central_widget.setLayout(main_layout)
        
        # Load todos
        self.load_todos_display()
    
    def load_todos_display(self):
        """Load todos into the list widget"""
        self.todo_list.clear()
        
        if self.current_filter == 'all':
            todos = self.app.get_all_todos()
        elif self.current_filter == 'pending':
            todos = self.app.get_pending_todos()
        else:  # completed
            todos = self.app.get_completed_todos()
        
        for todo in todos:
            item = QListWidgetItem()
            item.setData(Qt.UserRole, todo['id'])
            
            # Format display text
            status = '✓' if todo['completed'] else '○'
            priority_emoji = {'Low': '🔵', 'Normal': '🟢', 'High': '🟠', 'Urgent': '🔴'}
            priority_icon = priority_emoji.get(todo['priority'], '🟢')
            
            text = f"{status} {priority_icon} {todo['title']}"
            if todo['due_date']:
                text += f" (Due: {todo['due_date']})"
            
            item.setText(text)
            
            # Set color based on priority and completion
            if todo['completed']:
                item.setForeground(QColor(150, 150, 150))
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)
            else:
                colors = {'Low': QColor(100, 150, 255), 'Normal': QColor(50, 150, 50),
                         'High': QColor(255, 165, 0), 'Urgent': QColor(255, 50, 50)}
                item.setForeground(colors.get(todo['priority'], QColor(0, 0, 0)))
            
            self.todo_list.addItem(item)
    
    def quick_add_todo(self):
        """Quick add todo from input field"""
        title = self.input_field.text().strip()
        if title:
            self.app.add_todo(title)
            self.input_field.clear()
            self.load_todos_display()
            QMessageBox.information(self, 'Success', 'Task added successfully!')
        else:
            QMessageBox.warning(self, 'Error', 'Please enter a task title')
    
    def add_todo_dialog(self):
        """Show add todo dialog"""
        dialog = AddTodoDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.get_data()
            if data['title'].strip():
                self.app.add_todo(**data)
                self.load_todos_display()
                QMessageBox.information(self, 'Success', 'Task added successfully!')
            else:
                QMessageBox.warning(self, 'Error', 'Please enter a task title')
    
    def on_todo_selected(self, item):
        """Handle todo selection"""
        self.selected_todo_id = item.data(Qt.UserRole)
    
    def toggle_todo(self):
        """Toggle todo completion"""
        if hasattr(self, 'selected_todo_id'):
            self.app.toggle_complete(self.selected_todo_id)
            self.load_todos_display()
        else:
            QMessageBox.warning(self, 'Error', 'Please select a task')
    
    def edit_todo(self):
        """Edit selected todo"""
        if hasattr(self, 'selected_todo_id'):
            todo = self.app.get_todo(self.selected_todo_id)
            if todo:
                dialog = EditTodoDialog(todo, self)
                if dialog.exec_() == QDialog.Accepted:
                    data = dialog.get_data()
                    self.app.update_todo(self.selected_todo_id, **data)
                    self.load_todos_display()
                    QMessageBox.information(self, 'Success', 'Task updated successfully!')
        else:
            QMessageBox.warning(self, 'Error', 'Please select a task')
    
    def delete_todo(self):
        """Delete selected todo"""
        if hasattr(self, 'selected_todo_id'):
            reply = QMessageBox.question(self, 'Confirm', 'Delete this task?', 
                                        QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.app.delete_todo(self.selected_todo_id)
                self.load_todos_display()
                QMessageBox.information(self, 'Success', 'Task deleted successfully!')
        else:
            QMessageBox.warning(self, 'Error', 'Please select a task')
    
    def filter_todos(self, filter_type):
        """Filter todos"""
        self.current_filter = filter_type
        self.load_todos_display()
    
    def clear_completed(self):
        """Clear all completed todos"""
        reply = QMessageBox.question(self, 'Confirm', 'Delete all completed tasks?', 
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            completed = self.app.get_completed_todos()
            for todo in completed:
                self.app.delete_todo(todo['id'])
            self.load_todos_display()
            QMessageBox.information(self, 'Success', 'Completed tasks cleared!')
    
    def export_todos(self):
        """Export todos to JSON file"""
        filename, _ = QFileDialog.getSaveFileName(self, 'Export Tasks', '', 'JSON Files (*.json)')
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.app.todos, f, ensure_ascii=False, indent=2)
                QMessageBox.information(self, 'Success', f'Tasks exported to {filename}')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Failed to export: {str(e)}')

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
